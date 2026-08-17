<div align="center">

  <img src="img/logos/sinf.png" alt="Logo Club de Debate UMU" width="120" height="120" />

  # Club de Debate UMU — Portal Web & Suite de Herramientas

  [![GitHub Pages](https://img.shields.io/badge/Despliegue-GitHub%20Pages-brightgreen?style=flat-square&logo=github)](https://josefervg.github.io/Debate_UMU/)
  [![Universidad de Murcia](https://img.shields.io/badge/Instituci%C3%B3n-Universidad%20de%20Murcia-blue?style=flat-square)](https://www.um.es)
  [![Cumplimiento Legal](https://img.shields.io/badge/Legal-RGPD%20%7C%20LSSI--CE-orange?style=flat-square)](https://josefervg.github.io/Debate_UMU/legal/)
  [![Licencia](https://img.shields.io/badge/Licencia-Educativa%20UMU-informational?style=flat-square)](#licencia)

  <p align="center">
    Plataforma digital institucional y suite de utilidades <i>Client-Side</i> de alto rendimiento para la práctica, organización y competición en el formato de debate Parlamentario Británico (BP) y oratoria universitaria.
  </p>

  [**🌐 Visitar Sitio Web en Producción**](https://josefervg.github.io/Debate_UMU/)

</div>

---

## 📑 Tabla de Contenidos
- [Descripción General](#-descripción-general)
- [Suite de Herramientas](#-suite-de-herramientas)
- [Arquitectura de Software y Seguridad](#-arquitectura-de-software-y-seguridad)
- [Estructura del Repositorio](#-estructura-del-repositorio)
- [Guía de Instalación y Ejecución Local](#-guía-de-instalación-y-ejecución-local)
- [Auditoría SEO, GEO y Analítica](#-auditoría-seo-geo-y-analítica)
- [Marco de Cumplimiento Legal (RGPD / LSSI-CE)](#-marco-de-cumplimiento-legal-rgpd--lssi-ce)
- [Guía de Contribución](#-guía-de-contribución)
- [Licencia](#-licencia)

---

## 📖 Descripción General

El portal del **Club de Debate UMU** (Universidad de Murcia) centraliza la captación de nuevos miembros, difusión de eventos competitivos (como el torneo nacional **BP Murcia**) y pone a disposición de la comunidad hispanohablante de debate un conjunto de aplicaciones web especializadas que funcionan **completamente en el navegador del usuario**.

---

## 🛠️ Suite de Herramientas

| Módulo | Ruta | Descripción Técnica |
| :--- | :--- | :--- |
| 🔍 **Mocionero BP** | [`/mocionero/`](https://josefervg.github.io/Debate_UMU/mocionero/) | Buscador reactivo y clasificador temático de cientos de mociones oficiales de debate parlamentario extraídas mediante APIs de Tabbycat. |
| ⌛ **Timer de Debate BP** | [`/timer/`](https://josefervg.github.io/Debate_UMU/timer/) | Cronómetro configurable para discursos competitivos (7 minutos) con avisos acústicos de tiempo protegido, modo oscuro y atajos de teclado. |
| 🔥 **Preptime 15'** | [`/timer/preptime.html`](https://josefervg.github.io/Debate_UMU/timer/preptime.html) | Temporizador visual estructurado para la fase de preparación de 15 minutos en debate BP, con recomendaciones estratégicas por fases. |
| ⏱️ **Timer Pomodoro** | [`/pomodoro.html`](https://josefervg.github.io/Debate_UMU/pomodoro.html) | Temporizador de productividad y estudio con soporte de ventana flotante *Picture-in-Picture* (PiP) y personalización de intervalos. |
| 🎓 **Acreditaciones** | [`/acreditaciones/`](https://josefervg.github.io/Debate_UMU/acreditaciones/) | Diseñador e impresor por lotes de diplomas y credenciales mediante procesamiento de hojas CSV renderizadas con HTML5 Canvas y `jsPDF`. |
| ⚖️ **Justificantes** | [`/autorizaciones/`](https://josefervg.github.io/Debate_UMU/autorizaciones/) | Generador masivo de autorizaciones y justificantes de asistencia a torneos a partir de plantillas Word (`.docx`) mediante `docxtemplater` y `JSZip`. |
| 🌐 **Dossier del Club** | [`/pagpubli/`](https://josefervg.github.io/Debate_UMU/pagpubli/) | Landing page informativa con galería de actividades, fotografías de torneos y recursos de captación. |

---

## 🏗️ Arquitectura de Software y Seguridad

- **Client-Side Computing (Zero-Backend Privacy):** Las herramientas que procesan datos identificativos (listas de participantes, nombres y DNIs para justificantes) ejecutan los algoritmos íntegramente en la memoria volátil del navegador mediante Web APIs y librerías cliente. Ningún dato viaja a servidores externos.
- **Micro-Frontends Estáticos:** Cada herramienta está encapsulada en su propio directorio con estilos Tailwind CSS y Google Fonts optimizadas.
- **Accesibilidad & Responsive Design:** Cumplimiento de pautas W3C / WCAG 2.1 con diseño adaptable a dispositivos móviles, tablets y monitores ultrawide.

---

## 📂 Estructura del Repositorio

```text
Debate_UMU/
├── .gitignore                          # Exclusiones de Git (logs, temporales, pycache)
├── README.md                           # Documentación técnica del proyecto
├── robots.txt                          # Directivas para spiders y motores de búsqueda
├── sitemap.xml                         # Mapa de indexación XML para Search Console
├── google8a7197bbf5fdece6.html         # Verificación de Google Search Console
│
├── index.html                          # Landing page institucional del Club de Debate
├── pomodoro.html                       # Temporizador Pomodoro PiP
│
├── acreditaciones/                     # Generador de acreditaciones y credenciales
│   └── index.html
│
├── autorizaciones/                     # Generador de justificantes (.docx + CSV)
│   ├── index.html
│   ├── tutorial.html
│   └── modelo por defecto...docx
│
├── mocionero/                          # Buscador y generador de mociones
│   ├── index.html
│   ├── motions.json                    # Dataset de mociones
│   └── crearArchivoDebate.py           # Script ETL de extracción de Tabbycat
│
├── timer/                              # Cronómetros de competición
│   ├── index.html                      # Timer 7 min BP
│   ├── preptime.html                   # Preptime 15 min
│   └── audio/                          # Señales acústicas (campanas y avisos)
│
├── pagpubli/                           # Dossier informativo y recursos visuales
│   ├── index.html
│   └── canvaInfo.html
│
├── legal/                              # Portal normativo y de transparencia
│   ├── index.html                      # Centro Legal
│   ├── aviso-legal.html                # LSSI-CE Art. 10
│   ├── privacidad.html                 # RGPD / LOPDGDD
│   ├── cookies.html                    # Política de cookies y localStorage
│   ├── terminos.html                   # Términos de uso y disclaimers
│   └── banner.js                       # Banner de consentimiento
│
└── img/                                # Recursos gráficos y multimedia
    ├── logos/                          # Logotipos vectoriales y PNG
    ├── fondosCrono/                    # Texturas y fondos
    └── imagenesInfo/                   # Fotografías y capturas
```

---

## 🚀 Guía de Instalación y Ejecución Local

Dado que el proyecto es 100% estático, no requiere compilación previa ni bases de datos.

### 1. Clonar el repositorio
```bash
git clone https://github.com/JoseFerVG/Debate_UMU.git
cd Debate_UMU
```

### 2. Levantar un servidor local
Puedes utilizar cualquiera de las siguientes opciones:

#### Con Python:
```bash
# Python 3
python -m http.server 8000
```
Abre en tu navegador: `http://localhost:8000`

#### Con Node.js / npx:
```bash
npx serve .
```

#### Con la extensión Live Server (VS Code):
Haz clic derecho en `index.html` y selecciona **"Open with Live Server"**.

---

## 🎯 Auditoría SEO, GEO y Analítica

El portal está optimizado para su indexación en buscadores y motores de Inteligencia Artificial (GEO):
- **Local SEO & Geo-Targeting:** Metadatos geográficos con coordenadas del Campus de Espinardo / La Merced (`38.0163, -1.1685`, `ES-MU`, Murcia, España).
- **Datos Estructurados Schema.org:**
  - `EducationalOrganization` y `SportsOrganization`
  - `Event` (BP Murcia 2026)
  - `FAQPage` con respuestas directas para Google Rich Snippets y LLMs (ChatGPT, Perplexity, Gemini).
  - `WebApplication` en cada herramienta específica.
- **Sitemap & Robots:** Cobertura de todas las URLs con frecuencias y prioridades de rastreo.

---

## 🛡️ Marco de Cumplimiento Legal (RGPD / LSSI-CE)

El proyecto incluye un centro de cumplimiento normativo conforme a la legislación española y europea:
- **Aviso Legal (Art. 10 LSSI-CE):** Identificación institucional del Club de Debate UMU y régimen universitario sin ánimo de lucro.
- **Política de Privacidad (RGPD UE 2016/679 & LOPDGDD 3/2018):** Certificación de privacidad por diseño en el procesamiento de documentos personales y ejercicio de derechos ARCO-POL ante la AEPD.
- **Política de Cookies & LocalStorage (Art. 22.2 LSSI-CE):** Detalle de variables locales técnicas (`jfk-settings`, `jfk-theme`, `debate_umu_legal_banner`).
- **Cláusulas de Neutralidad y Validez:** Exención de responsabilidad sobre el contenido de las mociones de debate y aviso de validez académica requerida para justificantes.

---

## 🤝 Guía de Contribución

1. Haz un **Fork** del proyecto.
2. Crea una rama descriptiva para tu funcionalidad:
   ```bash
   git checkout -b feature/nueva-herramienta
   ```
3. Realiza tus cambios asegurando la semántica HTML5 y el diseño responsive.
4. Haz commit de tus modificaciones:
   ```bash
   git commit -m "feat: añadir filtro por idioma en mocionero"
   ```
5. Envía un **Pull Request** detallando las mejoras realizadas.

---

## ⚖️ Licencia

Desarrollado para y por la comunidad universitaria del **Club de Debate UMU** (Universidad de Murcia).  
Los materiales didácticos y herramientas son de libre uso para fines educativos y no comerciales.
