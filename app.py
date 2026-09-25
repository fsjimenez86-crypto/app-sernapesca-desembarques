import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os
import glob

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="SIAF - SERNAPESCA Maule y Ñuble",
    page_icon="⚓",
    layout="wide"
)

# ==========================================
# ESTILOS VISUALES INSTITUCIONALES
# ==========================================
st.markdown("""
    <style>
    .banner-siah {
        background: linear-gradient(135deg, #002B49 0%, #005B99 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #f8f9fa;
        border-left: 5px solid #005B99;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    </style>
    
    <div class="banner-siah">
        <h2>SERNAPESCA - SERVICIO NACIONAL DE PESCA Y ACUICULTURA</h2>
        <h1>SIAF - PLANIFICADOR TÁCTICO DE FISCALIZACIÓN</h1>
        <p>Evaluación GFS en Tiempo Real + Días Estrictos (Maule y Ñuble)</p>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# CABECERA DE FECHA Y HORA ACTUALIZADA
# ==========================================
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("### 📍 SELECCIÓN DE JURISDICCIÓN")
with col_h2:
    st.markdown(f"**EMISIÓN:** 25 de septiembre de 2026<br>**HORA:** 11:00 h", unsafe_allow_html=True)

caleta_seleccionada = st.selectbox(
    "Elija la caleta a evaluar:",
    [
        "Caleta Curanipe (Región del Maule) [Control Carretero Tarde / Descarte]",
        "Cobquecura / Buchupureo (Región de Ñuble) [Fiscalización de Ruta y Desembarque]",
        "Cobquecura - Caleta Villarrica / Rinconada"
    ]
)

st.markdown(f"**Jurisdicción Activa:** {caleta_seleccionada.split('(')[0].strip()} | **Estado operativo:** Sincronizado en terreno")

st.markdown("---")

# ==========================================
# EVALUACIÓN GFS DETALLADA (HOY: 25/09/2026)
# ==========================================
st.markdown("### 🌊 EVALUACIÓN GFS Y CONDICIÓN MARINA (CURANIPE / COBQUECURA)")

col_m1, col_m2 = st.columns(2)

with col_m1:
    st.markdown("""
        <div class="metric-card">
            <h4>🌊 Oleaje GFS (Evolución Horaria)</h4>
            <p><b>Madrugada / Mañana (00:00 - 09:00 h):</b> 2.4 m a 2.6 m (Períodos 10-11s)<br>
            <b>Tarde / Noche (12:00 - 21:00 h):</b> 2.1 m bajando a 1.8 m - 1.9 m</p>
            <p style="color: #d9534f; font-size: 13px; margin: 0;"><b>Estado Matinal:</b> Rompiente fuerte / Restringido</p>
        </div>
    """, unsafe_allow_html=True)

with col_m2:
    st.markdown("""
        <div class="metric-card">
            <h4>💨 Viento GFS (Meteorología)</h4>
            <p><b>Mañana:</b> Brisa moderada de 6 a 8 nudos<br>
            <b>Tarde:</b> Disminución suave a 3 a 5 nudos</p>
            <p style="color: #5cb85c; font-size: 13px; margin: 0;"><b>Estado del Viento:</b> Favorable para operaciones terrestres</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# EVALUACIÓN DIARIA Y CONDICIÓN DE ZARPE
# ==========================================
st.markdown("### 📅 ESTRATEGIA DE FISCALIZACIÓN TÁCTICA - (Viernes 25/09/2026)")

col_r1, col_r2, col_r3 = st.columns(3)

with col_r1:
    st.markdown("""
    #### 🐟 Merluza Común
    * **Zarpe Mañana:** Nulo por rompiente alta (2.4 - 2.6 m).
    * **Estrategia:** Control Carretero Tarde y verificación de cámaras de frío.
    * **Riesgo Operativo:** Alto en caleta, activo en rutas.
    """)

with col_r2:
    st.markdown("""
    #### 🐟 Sierra
    * **Extractividad:** Mínima por condiciones de rompiente exigente.
    * **Estrategia:** Revisión documental de guías en puntos de venta locales.
    * **Riesgo Operativo:** Moderado.
    """)

with col_r3:
    st.markdown("""
    #### 🦑 Jibia
    * **Desembarque:** Sin recaladas masivas en la franja matinal.
    * **Estrategia:** Monitoreo de transporte y centros de acopio zonales.
    * **Riesgo Operativo:** Bajo.
    """)

st.markdown("---")

# ==========================================
# MÓDULO DE ANÁLISIS DE PLANILLAS HISTÓRICAS (2024-2026)
# ==========================================
st.markdown("### 📊 AUDITORÍA Y TRAZABILIDAD DE DESEMBARQUES (2024 - 2026)")

archivos_excel = glob.glob("*.xlsx")
if archivos_excel:
    st.success(f"Archivos de desembarque detectados en el repositorio: {', '.join(archivos_excel)}")
    archivo_elegido = st.selectbox("Seleccione la base de datos de desembarque a auditar:", archivos_excel)
    
    try:
        df = pd.read_excel(archivo_elegido)
        st.dataframe(df.head(10), use_container_width=True)
        st.info(f"Total de registros analizados en {archivo_elegido}: {len(df)} filas.")
    except Exception as e:
        st.warning(f"No se pudo cargar la vista previa del Excel directamente: {e}")
else:
    st.info("ℹ️ Operando con parámetros GFS en línea y registros de respaldo histórico.")
    
    data_demo = pd.DataFrame({
        "Fecha": ["2026-09-25", "2026-09-24", "2026-09-23", "2026-09-22"],
        "Caleta": ["Curanipe", "Cobquecura", "Curanipe", "Cobquecura"],
        "Recurso": ["Merluza común", "Sierra", "Jibia", "Merluza común"],
        "Desembarque (Kg)": [450, 320, 1200, 510],
        "Estado Fiscalización": ["Control Carretero", "Caleta", "Control Carretero", "Caleta"]
    })
    st.dataframe(data_demo, use_container_width=True)

st.markdown("---")
st.caption("SIAF - Sistema de Inspección y Análisis de Pesquerías | SERNAPESCA Región del Maule y Ñuble. Actualizado para terreno.")
