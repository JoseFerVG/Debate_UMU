(function() {
  const STORAGE_KEY = 'debate_umu_legal_banner';
  if (localStorage.getItem(STORAGE_KEY)) return;

  function initBanner() {
    // Determinar la ruta relativa a la carpeta legal
    const isSubdir = window.location.pathname.includes('/acreditaciones/') ||
                     window.location.pathname.includes('/autorizaciones/') ||
                     window.location.pathname.includes('/mocionero/') ||
                     window.location.pathname.includes('/timer/') ||
                     window.location.pathname.includes('/pagpubli/') ||
                     window.location.pathname.includes('/herramientas/') ||
                     window.location.pathname.includes('/logos-bpmurcia/') ||
                     window.location.pathname.includes('/legal/');
    
    const basePath = isSubdir ? '../legal/' : './legal/';

    const banner = document.createElement('div');
    banner.id = 'debate-legal-banner';
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-label', 'Aviso de privacidad y almacenamiento local');
    banner.style.cssText = 'position:fixed;bottom:0.75rem;left:0.75rem;right:0.75rem;max-width:46rem;margin:0 auto;z-index:9999;background:rgba(255,255,255,0.96);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(226,232,240,0.9);box-shadow:0 20px 35px -10px rgba(0,0,0,0.15);border-radius:1.25rem;padding:0.75rem 1rem;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:0.75rem;font-family:Inter,system-ui,-apple-system,sans-serif;color:#1e293b;font-size:0.8125rem;transition:all 0.3s ease;animation:fadeInBanner 0.4s ease;';

    banner.innerHTML = `
      <style>
        @keyframes fadeInBanner {
          from { opacity: 0; transform: translateY(12px); }
          to { opacity: 1; transform: translateY(0); }
        }
        @media (min-width: 640px) {
          #debate-legal-banner {
            bottom: 1.25rem !important;
            left: 1.25rem !important;
            right: 1.25rem !important;
            padding: 1rem 1.25rem !important;
          }
        }
      </style>
      <div style="flex:1;min-width:180px;line-height:1.4;">
        <span style="font-weight:700;display:inline-flex;align-items:center;gap:0.4rem;color:#0f172a;">
          <svg style="width:14px;height:14px;color:#16a34a;flex-shrink:0;" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"/>
          </svg>
          Privacidad y Almacenamiento Técnico
        </span>
        <p style="margin:0.25rem 0 0 0;color:#64748b;font-size:0.75rem;">
          Este sitio web utiliza almacenamiento local técnico (sin cookies comerciales ni rastreo publicitario) y procesa tus documentos 100% en tu navegador.
          <a href="${basePath}privacidad.html" style="color:#ea580c;text-decoration:underline;margin-left:0.25rem;" target="_blank">Privacidad</a> · 
          <a href="${basePath}cookies.html" style="color:#ea580c;text-decoration:underline;" target="_blank">Cookies</a>
        </p>
      </div>
      <div style="display:flex;align-items:center;gap:0.5rem;">
        <a href="${basePath}index.html" style="padding:0.4rem 0.8rem;border-radius:9999px;background:#f1f5f9;color:#475569;font-weight:600;font-size:0.75rem;text-decoration:none;transition:background 0.2s;">
          Saber más
        </a>
        <button id="btn-accept-legal-banner" style="cursor:pointer;padding:0.4rem 0.9rem;border-radius:9999px;border:none;background:#0f172a;color:#ffffff;font-weight:700;font-size:0.75rem;transition:opacity 0.2s;">
          Entendido
        </button>
      </div>
    `;

    document.body.appendChild(banner);

    const btn = document.getElementById('btn-accept-legal-banner');
    if (btn) {
      btn.addEventListener('click', function() {
        localStorage.setItem(STORAGE_KEY, 'true');
        banner.style.opacity = '0';
        banner.style.transform = 'translateY(12px)';
        setTimeout(() => banner.remove(), 300);
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBanner);
  } else {
    initBanner();
  }
})();
