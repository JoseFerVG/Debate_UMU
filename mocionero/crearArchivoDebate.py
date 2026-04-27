import os
import re
import json
import glob
import argparse
import requests
from urllib.parse import urlparse, urljoin

def clean_html(raw_html: str) -> str:
    """Limpia etiquetas HTML y convierte saltos de línea a texto plano."""
    if not raw_html:
        return ""
    text = re.sub(r'<br\s*/?>|</p>', '\n', raw_html)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'&nbsp;', ' ', text)
    return text.strip()

def extract_motions():
    parser = argparse.ArgumentParser(description="Extractor de Mociones Automático para Tabbycat")
    parser.add_argument("--url", type=str, help="URL completa del torneo")
    parser.add_argument("--nombre", type=str, help="Nombre personalizado del torneo")
    parser.add_argument("--anio", type=str, help="Año del torneo")
    parser.add_argument("--edicion", type=str, help="Edición del torneo (ej. 1ra). Pon -1 si no tiene edición.")
    args = parser.parse_args()

    raw_url = args.url or input("Pega la URL completa del torneo (ej. https://calico.tabbycat.com/slug-torneo/): ").strip()
    torneo_nombre = args.nombre or input("Nombre personalizado del torneo: ").strip()
    anio = args.anio or input("Año del torneo: ").strip()
    edicion = args.edicion or input("Edición del torneo (pon -1 si no tiene): ").strip()

    parsed_url = urlparse(raw_url)
    if not parsed_url.scheme or not parsed_url.netloc:
        print("[!] Error: Formato de URL inválido. Asegúrate de incluir https://")
        return

    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    path_parts = [p for p in parsed_url.path.split('/') if p]
    
    if not path_parts:
        print("[!] Error: La URL no contiene la ruta del torneo (slug).")
        return
        
    slug = path_parts[0]
    print(f"[*] Dominio detectado: {base_url} | Slug detectado: {slug}")

    headers = {'Accept': 'application/json'}
    
    try:
        motions_url = urljoin(base_url, f"/api/v1/tournaments/{slug}/motions")
        print(f"[*] Extrayendo mociones desde: {motions_url}")
        response = requests.get(motions_url, headers=headers)
        response.raise_for_status()
        motions_data = response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"[!] Error crítico de conexión. ¿Está expuesta la API en este torneo? Detalle: {e}")
        return

    # Eliminar mociones duplicadas (a veces la API devuelve la misma moción múltiples veces)
    unique_motions = []
    seen_keys = set()
    for m in motions_data:
        key = (m.get('reference', '').strip(), m.get('text', '').strip())
        if key not in seen_keys:
            seen_keys.add(key)
            unique_motions.append(m)
            
    motions_data = unique_motions

    # Enumeración de rondas por orden de llegada (la API no envía info de ronda)
    total_mociones = len(motions_data)
    
    def nombre_ronda(indice, total):
        """Asigna nombre a la ronda: las 2 últimas son Semifinal y Final."""
        if total >= 2 and indice == total - 1:
            return "Final"
        elif total >= 2 and indice == total - 2:
            return "Semifinal"
        else:
            return f"Ronda {indice + 1}"

    edicion_str = "" if edicion == "-1" else edicion
    
    sufijo_dir = f"_{anio}"
    if edicion_str:
        sufijo_dir += f"_{edicion_str}"
        
    output_dir = f"mociones_{slug}{sufijo_dir}"
    os.makedirs(output_dir, exist_ok=True)

    for i, motion in enumerate(motions_data):
        ronda_nombre = nombre_ronda(i, total_mociones)
        
        datos_limpios = {
            "torneo": torneo_nombre,
            "año": anio,
            "edicion": edicion_str,
            "ronda": ronda_nombre,
            "titulo": motion.get('reference', ''),
            "infoslide": clean_html(motion.get('info_slide', '')),
            "mocion": clean_html(motion.get('text', '')),
            "Tematica": "Sin clasificar",
            "Tipo de Mocion": "Sin clasificar"
        }
        
        nombre_base = f"{torneo_nombre}-{ronda_nombre}-{anio}"
        if edicion_str:
            nombre_base += f"-{edicion_str}"
        nombre_archivo = f"{nombre_base}.json".replace(" ", "").lower()
        ruta_archivo = os.path.join(output_dir, nombre_archivo)
        
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos_limpios, f, ensure_ascii=False, indent=4)
        
    print(f"[+] Extracción finalizada. {total_mociones} archivos JSON individuales generados.")
    consolidar_jsons()

def consolidar_jsons():
    """Busca todas las mociones guardadas en carpetas y genera el motions.json central."""
    todas_las_mociones = []
    # Buscar en directorios que empiecen con "mociones" (como "mociones_slug_2026" o la carpeta "mociones")
    rutas = glob.glob("mociones*/*.json")
    for archivo in rutas:
        with open(archivo, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if isinstance(data, dict):
                    todas_las_mociones.append(data)
                elif isinstance(data, list):
                    todas_las_mociones.extend(data)
            except Exception as e:
                print(f"[!] Error leyendo {archivo}: {e}")
                pass
                
    if todas_las_mociones:
        with open("motions.json", "w", encoding="utf-8") as out:
            json.dump(todas_las_mociones, out, ensure_ascii=False, indent=4)
        print(f"[*] motions.json ha sido actualizado con éxito. Contiene {len(todas_las_mociones)} mociones en total.")
    else:
        print("[!] No se encontraron mociones para consolidar en motions.json.")

if __name__ == "__main__":
    extract_motions()
