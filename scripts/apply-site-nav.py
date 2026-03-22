#!/usr/bin/env python3
"""Aplica o menu com submenus (PDF) em todas as páginas HTML exceto index."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADER_INNER = r'''    <header class="sticky top-0 z-50 bg-white/90 backdrop-blur border-b border-gray-100">
        <nav class="max-w-7xl mx-auto px-6 lg:px-12 py-3 flex flex-wrap items-center justify-between gap-2" aria-label="Principal">
            <a href="index.html"><img src="assets/logo.png" alt="Logo Clube de Mães Marista" class="h-12"></a>
            <div class="hidden lg:flex flex-wrap items-center justify-end gap-x-0.5 gap-y-1 text-[12px] max-w-5xl xl:max-w-none">
                <a href="index.html" class="font-medium text-gray-700 hover:text-brand-blue px-2 py-1.5 rounded-full">Início</a>
                <div class="site-nav-dropdown">
                    <button type="button" class="site-nav-dropdown__btn inline-flex items-center gap-1 text-[12px] font-medium text-gray-700 hover:text-brand-blue px-2 py-1.5 rounded-full" aria-haspopup="true">O Clube <i class="fa-solid fa-chevron-down text-[9px] opacity-70" aria-hidden="true"></i></button>
                    <div class="site-nav-dropdown__panel" role="menu">
                        <div class="site-nav-dropdown__panel-inner rounded-xl">
                            <a href="quem-somos.html" role="menuitem">Quem somos</a>
                            <a href="quem-somos.html#diretoria" role="menuitem">Diretoria</a>
                            <a href="regulamento.html" role="menuitem">Regulamento</a>
                            <a href="midia-kit.html" role="menuitem">Mídia Kit</a>
                        </div>
                    </div>
                </div>
                <a href="quem-pode-participar.html" class="font-medium text-gray-700 hover:text-brand-blue px-2 py-1.5 rounded-full" title="Quem pode se inscrever">Participação</a>
                <div class="site-nav-dropdown">
                    <button type="button" class="site-nav-dropdown__btn inline-flex items-center gap-1 text-[12px] font-medium text-gray-700 hover:text-brand-blue px-2 py-1.5 rounded-full" aria-haspopup="true">Beach Tennis <i class="fa-solid fa-chevron-down text-[9px] opacity-70" aria-hidden="true"></i></button>
                    <div class="site-nav-dropdown__panel" role="menu">
                        <div class="site-nav-dropdown__panel-inner rounded-xl">
                            <a href="beach-tennis.html" role="menuitem">Visão geral</a>
                            <a href="beach-tennis.html#estrutura" role="menuitem">Estrutura</a>
                            <a href="beach-tennis.html#horarios" role="menuitem">Horários</a>
                            <a href="beach-tennis.html#aulas" role="menuitem">Aulas de beach</a>
                            <a href="beach-tennis.html#eventos" role="menuitem">Eventos nas quadras</a>
                            <a href="beach-tennis.html#campeonatos" role="menuitem">Campeonatos</a>
                            <a href="eventos.html" role="menuitem">Agenda do clube</a>
                        </div>
                    </div>
                </div>
                <div class="site-nav-dropdown">
                    <button type="button" class="site-nav-dropdown__btn inline-flex items-center gap-1 text-[12px] font-medium text-gray-700 hover:text-brand-blue px-2 py-1.5 rounded-full" aria-haspopup="true">Notícias <i class="fa-solid fa-chevron-down text-[9px] opacity-70" aria-hidden="true"></i></button>
                    <div class="site-nav-dropdown__panel" role="menu">
                        <div class="site-nav-dropdown__panel-inner rounded-xl">
                            <a href="noticias.html" role="menuitem">Todas as notícias</a>
                            <a href="noticias.html#imprensa" role="menuitem">Imprensa</a>
                            <a href="noticias.html#blog" role="menuitem">Blog</a>
                            <a href="noticias.html#galeria" role="menuitem">Galeria de imagens</a>
                        </div>
                    </div>
                </div>
                <div class="site-nav-dropdown">
                    <button type="button" class="site-nav-dropdown__btn inline-flex items-center gap-1 text-[12px] font-medium text-gray-700 hover:text-brand-blue px-2 py-1.5 rounded-full" aria-haspopup="true">Apoio <i class="fa-solid fa-chevron-down text-[9px] opacity-70" aria-hidden="true"></i></button>
                    <div class="site-nav-dropdown__panel" role="menu">
                        <div class="site-nav-dropdown__panel-inner rounded-xl">
                            <a href="patrocinadores.html" role="menuitem">Patrocinadores</a>
                            <a href="parceiros.html" role="menuitem">Parceiros</a>
                            <a href="loja-virtual.html" role="menuitem">Loja virtual</a>
                        </div>
                    </div>
                </div>
                <a href="contato.html" class="font-medium text-gray-700 hover:text-brand-blue px-2 py-1.5 rounded-full">Contato</a>
                <a href="index.html#lead-popup" class="ml-1 bg-brand-blue text-white px-4 py-2 rounded-full text-xs font-bold hover:bg-brand-black transition">Inscreva-se</a>
            </div>
            <button type="button" id="site-nav-toggle" class="lg:hidden p-2 rounded-lg text-gray-700 hover:bg-gray-100" aria-label="Abrir menu" aria-expanded="false" aria-controls="site-nav-drawer">
                <i class="fa-solid fa-bars text-xl" aria-hidden="true"></i>
            </button>
        </nav>
    </header>

    <div id="site-nav-drawer" class="fixed inset-0 z-[70] lg:hidden bg-black/40" aria-hidden="true">
        <div id="site-nav-drawer-panel" class="absolute right-0 top-0 bottom-0 w-[min(100%,20rem)] bg-white shadow-2xl overflow-y-auto p-6 pt-5 flex flex-col">
            <div class="flex justify-between items-center mb-5">
                <span class="font-bold text-brand-blue text-lg" style="font-family: Outfit, system-ui, sans-serif">Menu</span>
                <button type="button" id="site-nav-close" class="p-2 rounded-lg hover:bg-gray-100 text-gray-600" aria-label="Fechar menu">
                    <i class="fa-solid fa-xmark text-xl" aria-hidden="true"></i>
                </button>
            </div>
            <nav class="flex flex-col gap-0.5 text-[13px]" aria-label="Menu mobile">
                <a href="index.html" class="py-2.5 px-2 rounded-lg hover:bg-slate-50 font-medium text-gray-800">Início</a>
                <details class="site-nav-details border-b border-gray-100 py-1">
                    <summary class="py-2 px-2 cursor-pointer font-medium text-gray-800 flex justify-between items-center list-none">O Clube <i class="fa-solid fa-chevron-down text-xs opacity-60"></i></summary>
                    <div class="pl-3 pb-3 pt-1 space-y-1 border-l-2 border-brand-blue/20 ml-2 text-gray-600">
                        <a href="quem-somos.html" class="block py-1">Quem somos</a>
                        <a href="quem-somos.html#diretoria" class="block py-1">Diretoria</a>
                        <a href="regulamento.html" class="block py-1">Regulamento</a>
                        <a href="midia-kit.html" class="block py-1">Mídia Kit</a>
                    </div>
                </details>
                <a href="quem-pode-participar.html" class="py-2.5 px-2 rounded-lg hover:bg-slate-50 font-medium text-gray-800 border-b border-gray-100">Participação</a>
                <details class="site-nav-details border-b border-gray-100 py-1">
                    <summary class="py-2 px-2 cursor-pointer font-medium text-gray-800 flex justify-between items-center list-none">Beach Tennis <i class="fa-solid fa-chevron-down text-xs opacity-60"></i></summary>
                    <div class="pl-3 pb-3 pt-1 space-y-1 border-l-2 border-brand-blue/20 ml-2 text-gray-600">
                        <a href="beach-tennis.html" class="block py-1">Visão geral</a>
                        <a href="beach-tennis.html#estrutura" class="block py-1">Estrutura</a>
                        <a href="beach-tennis.html#horarios" class="block py-1">Horários</a>
                        <a href="beach-tennis.html#aulas" class="block py-1">Aulas de beach</a>
                        <a href="beach-tennis.html#eventos" class="block py-1">Eventos nas quadras</a>
                        <a href="beach-tennis.html#campeonatos" class="block py-1">Campeonatos</a>
                        <a href="eventos.html" class="block py-1">Agenda do clube</a>
                    </div>
                </details>
                <details class="site-nav-details border-b border-gray-100 py-1">
                    <summary class="py-2 px-2 cursor-pointer font-medium text-gray-800 flex justify-between items-center list-none">Notícias <i class="fa-solid fa-chevron-down text-xs opacity-60"></i></summary>
                    <div class="pl-3 pb-3 pt-1 space-y-1 border-l-2 border-brand-blue/20 ml-2 text-gray-600">
                        <a href="noticias.html" class="block py-1">Todas as notícias</a>
                        <a href="noticias.html#imprensa" class="block py-1">Imprensa</a>
                        <a href="noticias.html#blog" class="block py-1">Blog</a>
                        <a href="noticias.html#galeria" class="block py-1">Galeria de imagens</a>
                    </div>
                </details>
                <details class="site-nav-details border-b border-gray-100 py-1">
                    <summary class="py-2 px-2 cursor-pointer font-medium text-gray-800 flex justify-between items-center list-none">Apoio <i class="fa-solid fa-chevron-down text-xs opacity-60"></i></summary>
                    <div class="pl-3 pb-3 pt-1 space-y-1 border-l-2 border-brand-blue/20 ml-2 text-gray-600">
                        <a href="patrocinadores.html" class="block py-1">Patrocinadores</a>
                        <a href="parceiros.html" class="block py-1">Parceiros</a>
                        <a href="loja-virtual.html" class="block py-1">Loja virtual</a>
                    </div>
                </details>
                <a href="contato.html" class="py-2.5 px-2 rounded-lg hover:bg-slate-50 font-medium text-gray-800">Contato</a>
                <a href="index.html#lead-popup" class="mt-4 text-center w-full bg-brand-blue text-white px-4 py-3 rounded-full text-sm font-semibold hover:bg-brand-black transition">Inscreva-se</a>
            </nav>
        </div>
    </div>
'''

CSS_LINK = '<link rel="stylesheet" href="assets/site-nav.css">'
SCRIPT_TAG = '<script src="assets/site-nav.js" defer></script>'


def main():
    for path in sorted(ROOT.glob("*.html")):
        if path.name == "index.html":
            continue
        text = path.read_text(encoding="utf-8")
        if "site-nav.css" not in text:
            # insert after font-awesome link
            m = re.search(
                r'(<link[^>]*font-awesome[^>]*>)',
                text,
                re.IGNORECASE,
            )
            if m:
                text = text[: m.end()] + "\n    " + CSS_LINK + text[m.end() :]
            else:
                text = text.replace("</head>", f"    {CSS_LINK}\n</head>", 1)

        new_block, n = re.subn(
            r"<header\b[^>]*>.*?</header>",
            HEADER_INNER.strip(),
            text,
            count=1,
            flags=re.DOTALL | re.IGNORECASE,
        )
        if n == 0:
            print(f"SKIP (no header): {path.name}")
            continue
        text = new_block

        if SCRIPT_TAG not in text:
            text = text.replace("</body>", f"    {SCRIPT_TAG}\n</body>", 1)

        path.write_text(text, encoding="utf-8")
        print(f"OK: {path.name}")


if __name__ == "__main__":
    main()
