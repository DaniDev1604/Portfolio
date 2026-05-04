import streamlit as st

st.set_page_config(
    page_title="Portafolio · Interfaces Multimodales",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── Inject custom CSS ───────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>
/* ── CSS variables ── */
:root {
    --bg:       #0E0812;
    --bg-card:  #160D20;
    --border:   #2A1840;
    --rose:     #FF4D7E;
    --lavender: #BF85FF;
    --peach:    #FFB3C6;
    --mint:     #7EECD6;
    --text:     #F5EDF8;
    --muted:    #7A6890;
    --dimmer:   #3D2A52;
}

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"],
[data-testid="stMain"], [data-testid="stVerticalBlock"] {
    background: var(--bg) !important;
}

[data-testid="stAppViewContainer"] { background: var(--bg) !important; }
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { right: 1rem; }
section[data-testid="stSidebar"] { display: none; }

/* hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* ── Typography ── */
body { font-family: 'DM Sans', sans-serif; color: var(--text); }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--rose); border-radius: 2px; }

/* ── Layout container ── */
.port-wrap {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem 6rem;
}

/* ── Gradient orbs in background ── */
.noise {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background:
        radial-gradient(ellipse 600px 400px at 10% 20%, rgba(191,133,255,.07) 0%, transparent 70%),
        radial-gradient(ellipse 500px 350px at 90% 70%, rgba(255,77,126,.06) 0%, transparent 70%),
        radial-gradient(ellipse 400px 300px at 50% 100%, rgba(126,236,214,.04) 0%, transparent 70%);
}

/* ── Hero ── */
.hero {
    position: relative;
    padding: 7rem 0 4rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 4rem;
}

.hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: .72rem;
    letter-spacing: .22em;
    text-transform: uppercase;
    color: var(--rose);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: .75rem;
}

.hero-eyebrow::after {
    content: '';
    display: inline-block;
    height: 1px;
    width: 48px;
    background: linear-gradient(90deg, var(--rose), var(--lavender));
}

.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: clamp(3.5rem, 8vw, 6.5rem);
    line-height: .92;
    letter-spacing: -.01em;
    color: var(--text);
    margin-bottom: 1.2rem;
}

.hero-title em {
    font-style: italic;
    background: linear-gradient(135deg, var(--rose) 0%, var(--lavender) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    font-size: 1.05rem;
    color: var(--muted);
    max-width: 500px;
    line-height: 1.7;
    margin-bottom: 2.5rem;
}

.hero-meta {
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
}

.hero-meta-item {
    display: flex;
    flex-direction: column;
    gap: .2rem;
}

.hero-meta-label {
    font-family: 'DM Mono', monospace;
    font-size: .65rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    color: var(--dimmer);
}

.hero-meta-value {
    font-size: .9rem;
    color: #D4C5E0;
    font-weight: 400;
}

.hero-deco {
    position: absolute;
    top: 5rem;
    right: 0;
    left: 0;
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3rem, 7vw, 5.5rem);
    font-weight: 300;
    color: transparent;
    -webkit-text-stroke: 1px rgba(191,133,255,.12);
    line-height: 1;
    pointer-events: none;
    user-select: none;
    letter-spacing: .05em;
    white-space: nowrap;
    overflow: hidden;
}

/* ── Section header ── */
.section-header {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 2.5rem;
    padding-top: .5rem;
}

.section-number {
    font-family: 'DM Mono', monospace;
    font-size: .7rem;
    color: var(--lavender);
    letter-spacing: .1em;
}

.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2rem;
    font-weight: 400;
    color: var(--text);
    letter-spacing: -.01em;
}

.section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border) 0%, transparent 100%);
}

.section-count {
    font-family: 'DM Mono', monospace;
    font-size: .65rem;
    color: var(--dimmer);
    letter-spacing: .08em;
}

/* ── Project grid ── */
.proj-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
    gap: 1.25rem;
    margin-bottom: 4rem;
}

/* ── Project card ── */
.proj-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.75rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    transition: border-color .25s ease, transform .25s ease, box-shadow .25s ease;
    position: relative;
    overflow: hidden;
}

.proj-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,77,126,.05) 0%, rgba(191,133,255,.04) 100%);
    opacity: 0;
    transition: opacity .3s;
    border-radius: 10px;
    pointer-events: none;
}

.proj-card:hover {
    border-color: var(--rose);
    transform: translateY(-4px);
    box-shadow: 0 16px 48px rgba(255,77,126,.18), 0 0 0 1px rgba(255,77,126,.2);
}

.proj-card:hover::before { opacity: 1; }

.proj-card-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.proj-icon {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(255,77,126,.15), rgba(191,133,255,.15));
    border: 1px solid rgba(255,77,126,.25);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
}

.proj-index {
    font-family: 'DM Mono', monospace;
    font-size: .6rem;
    color: var(--dimmer);
    letter-spacing: .1em;
    padding-top: .25rem;
}

.proj-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.35rem;
    font-weight: 400;
    color: var(--text);
    line-height: 1.2;
    letter-spacing: -.01em;
}

.proj-desc {
    font-size: .82rem;
    color: var(--muted);
    line-height: 1.65;
    font-weight: 300;
    flex: 1;
}

.proj-tags {
    display: flex;
    flex-wrap: wrap;
    gap: .4rem;
}

.proj-tag {
    font-family: 'DM Mono', monospace;
    font-size: .6rem;
    letter-spacing: .08em;
    padding: .2rem .6rem;
    border-radius: 20px;
    text-transform: uppercase;
}

.proj-tag:nth-child(3n+1) {
    background: rgba(255,77,126,.12);
    color: #FF8AAF;
    border: 1px solid rgba(255,77,126,.25);
}
.proj-tag:nth-child(3n+2) {
    background: rgba(191,133,255,.12);
    color: #C99CFF;
    border: 1px solid rgba(191,133,255,.25);
}
.proj-tag:nth-child(3n) {
    background: rgba(126,236,214,.1);
    color: #7EECD6;
    border: 1px solid rgba(126,236,214,.2);
}

.proj-link {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    font-size: .78rem;
    font-weight: 500;
    color: var(--rose);
    text-decoration: none;
    letter-spacing: .04em;
    padding: .55rem 1rem;
    border: 1px solid rgba(255,77,126,.3);
    border-radius: 20px;
    background: rgba(255,77,126,.08);
    transition: all .25s;
    width: fit-content;
    margin-top: auto;
}

.proj-link:hover {
    background: rgba(255,77,126,.18);
    border-color: var(--rose);
    color: var(--peach);
    box-shadow: 0 0 16px rgba(255,77,126,.2);
}

.proj-link svg {
    width: 12px;
    height: 12px;
    transition: transform .2s;
}

.proj-link:hover svg {
    transform: translate(2px, -2px);
}

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(191,133,255,.2) 30%, rgba(255,77,126,.2) 70%, transparent);
    margin: 1rem 0 3.5rem;
}

/* ── Footer ── */
.foot {
    border-top: 1px solid var(--border);
    padding-top: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.foot-left {
    font-family: 'DM Mono', monospace;
    font-size: .65rem;
    color: var(--dimmer);
    letter-spacing: .1em;
    text-transform: uppercase;
}

.foot-right {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1rem;
    font-style: italic;
    color: var(--dimmer);
}
</style>
""", unsafe_allow_html=True)

# ─── Data ────────────────────────────────────────────────────────────────────
BATCH_1 = [
    {
        "name": "Copia de Interfaces",
        "desc": "Reproducción de interfaces interactivas con Streamlit como primer acercamiento al desarrollo de aplicaciones web multimodales.",
        "icon": "⊡",
        "tags": ["streamlit", "ui", "python"],
        "url": "https://copyinterfaces6-fcpqkkfc3hjacik46gku8h.streamlit.app/"
    },
    {
        "name": "Interfaces Multimodales I",
        "desc": "Primera exploración de interfaces que integran múltiples canales de entrada y salida: texto, imagen y audio en un solo entorno.",
        "icon": "◈",
        "tags": ["multimodal", "python", "streamlit"],
        "url": "https://interfaces-multimodales-3m2xhesmsue8uhkqvyu7mw.streamlit.app/"
    },
    {
        "name": "Proyecto Exploratorio",
        "desc": "Experimento de interfaz interactiva con combinación de componentes visuales y de entrada de datos para explorar las capacidades de Streamlit.",
        "icon": "○",
        "tags": ["exploración", "streamlit"],
        "url": "https://vvynpk4wvvqomwcjxvwwtd.streamlit.app/"
    },
    {
        "name": "OCR + Audio",
        "desc": "Herramienta que combina reconocimiento óptico de caracteres (OCR) con procesamiento de audio, permitiendo extraer texto de imágenes y convertirlo a voz.",
        "icon": "◎",
        "tags": ["ocr", "audio", "visión", "tts"],
        "url": "https://ocr-audio-ro7wctihn2pxo5wrf5dprk.streamlit.app/"
    },
    {
        "name": "Análisis de Sentimientos",
        "desc": "Clasificador de sentimientos en texto usando NLP. Permite introducir frases y obtener una evaluación de la polaridad emocional del mensaje.",
        "icon": "◐",
        "tags": ["nlp", "sentimientos", "texto"],
        "url": "https://sentimenta-2pwabnaknu7h9kqfahejet.streamlit.app/"
    },
    {
        "name": "TF-IDF en Español",
        "desc": "Implementación de TF-IDF para analizar la importancia relativa de términos en documentos en español, con visualización interactiva de resultados.",
        "icon": "≡",
        "tags": ["tf-idf", "nlp", "español"],
        "url": "https://tdfesp-kvcwqxqf4nmdruxtwz8jyz.streamlit.app/"
    },
    {
        "name": "Interfaz Generativa",
        "desc": "Aplicación interactiva de generación de contenido mediante parámetros configurables por el usuario en tiempo real.",
        "icon": "◇",
        "tags": ["generativo", "interactivo"],
        "url": "https://fuhxeoifcpmwamxowlzepj.streamlit.app/"
    },
    {
        "name": "Aplicación Interactiva",
        "desc": "Exploración de patrones de interacción multimodal con componentes de entrada personalizada y retroalimentación visual inmediata.",
        "icon": "▷",
        "tags": ["interacción", "ui", "streamlit"],
        "url": "https://aybssvusi3hgvwi7hcdv8k.streamlit.app/"
    },
    {
        "name": "Interfaces Multimodales II",
        "desc": "Versión extendida del proyecto de interfaces multimodales con mayor integración de modelos de lenguaje y capacidades de procesamiento.",
        "icon": "◈",
        "tags": ["multimodal", "llm", "nlp"],
        "url": "https://interfaces-multimodales-6kbnlmaukplcydn76ffhad.streamlit.app/"
    },
    {
        "name": "Nube de Palabras",
        "desc": "Generador dinámico de word clouds a partir de texto ingresado por el usuario, con personalización de colores, fuentes y filtros de frecuencia.",
        "icon": "⌘",
        "tags": ["wordcloud", "visualización", "nlp"],
        "url": "https://wordcloud-469qvyuqczclk5xgsmok4k.streamlit.app/"
    },
    {
        "name": "Detección YOLOv5",
        "desc": "Inferencia en tiempo real con el modelo YOLOv5 para detección y clasificación de objetos en imágenes cargadas por el usuario.",
        "icon": "⊕",
        "tags": ["yolov5", "detección", "cv", "deep learning"],
        "url": "https://yolov5-hifubagmkds4jeu9qcxzxk.streamlit.app/"
    },
]

BATCH_2 = [
    {
        "name": "Vision App",
        "desc": "Aplicación de visión por computadora que analiza imágenes en tiempo real identificando elementos visuales con modelos de clasificación avanzados.",
        "icon": "⊙",
        "tags": ["visión", "cv", "clasificación", "deep learning"],
        "url": "https://visionapp-6mtwzmxexfqpwp4e4h86uy.streamlit.app"
    },
    {
        "name": "Reconocimiento de Dibujos",
        "desc": "Canvas interactivo donde el usuario dibuja a mano libre y un modelo de ML reconoce en tiempo real la figura dibujada.",
        "icon": "✦",
        "tags": ["canvas", "ml", "reconocimiento", "dibujo"],
        "url": "https://drawrecog-ev278lzajp34t2rkxc7cvg.streamlit.app/"
    },
    {
        "name": "Own Canva",
        "desc": "Editor de diseño gráfico simplificado construido en Streamlit: capas, formas, texto y exportación de imágenes, todo desde el navegador.",
        "icon": "▣",
        "tags": ["diseño", "canvas", "editor", "gráficos"],
        "url": "https://owncanva-tezvddy5zdc7hqhm9q5wxz.streamlit.app/"
    },
    {
        "name": "Control por Voz",
        "desc": "Interfaz controlada completamente por comandos de voz. Transcripción en tiempo real para navegar y ejecutar acciones sin teclado ni mouse.",
        "icon": "◉",
        "tags": ["voz", "asr", "accesibilidad", "audio"],
        "url": "https://ctrlvoice-6wdfc89zj4tdvz6qleumd8.streamlit.app/"
    },
]

ARROW_SVG = """<svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M3 13L13 3M13 3H6M13 3V10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

def card(proj, idx):
    return f"""
<div class="proj-card">
  <div class="proj-card-top">
    <div class="proj-icon">{proj['icon']}</div>
    <span class="proj-index">/{str(idx).zfill(2)}</span>
  </div>
  <div class="proj-name">{proj['name']}</div>
  <div class="proj-desc">{proj['desc']}</div>
  <div class="proj-tags">
    {''.join(f'<span class="proj-tag">{t}</span>' for t in proj['tags'])}
  </div>
  <a href="{proj['url']}" target="_blank" class="proj-link">
    Abrir proyecto {ARROW_SVG}
  </a>
</div>"""

def section_header(number, title, count):
    return f"""
<div class="section-header">
  <span class="section-number">{number}</span>
  <span class="section-title">{title}</span>
  <div class="section-line"></div>
  <span class="section-count">{count} proyectos</span>
</div>"""

# ─── Render ──────────────────────────────────────────────────────────────────
st.markdown('<div class="noise"></div>', unsafe_allow_html=True)

st.markdown('<div class="port-wrap">', unsafe_allow_html=True)

# Hero
st.markdown(f"""
<div class="hero">
  <div class="hero-deco">Daniela Gomez Ospina</div>
  <div class="hero-eyebrow">Portafolio académico</div>
  <h1 class="hero-title">Interfaces<br><em>Multimodales</em></h1>
  <p class="hero-sub">
    Colección de proyectos desarrollados durante el curso de Interfaces Multimodales —
    explorando la intersección entre visión, lenguaje, audio y diseño de interacción.
  </p>
  <div class="hero-meta">
    <div class="hero-meta-item">
      <span class="hero-meta-label">Curso</span>
      <span class="hero-meta-value">Interfaces Multimodales</span>
    </div>
    <div class="hero-meta-item">
      <span class="hero-meta-label">Total proyectos</span>
      <span class="hero-meta-value">{len(BATCH_1) + len(BATCH_2)}</span>
    </div>
    <div class="hero-meta-item">
      <span class="hero-meta-label">Tecnologías</span>
      <span class="hero-meta-value">Python · Streamlit · CV · NLP</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Batch 1
st.markdown(section_header("01 —", "Primera Entrega", len(BATCH_1)), unsafe_allow_html=True)
cards_html_1 = '<div class="proj-grid">' + "".join(card(p, i+1) for i, p in enumerate(BATCH_1)) + '</div>'
st.markdown(cards_html_1, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Batch 2
st.markdown(section_header("02 —", "Portafolio Actualizado", len(BATCH_2)), unsafe_allow_html=True)
cards_html_2 = '<div class="proj-grid">' + "".join(card(p, i+1) for i, p in enumerate(BATCH_2)) + '</div>'
st.markdown(cards_html_2, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="foot">
  <span class="foot-left">◈ Portafolio · Interfaces Multimodales</span>
  <span class="foot-right">construido con Streamlit</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
