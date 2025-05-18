import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Agrícola", layout="wide")

st.title("Dashboard de Sensores Agrícolas")

uploaded_file = st.file_uploader("📂 Envie o arquivo Excel com os dados dos sensores", type=["xlsx"])

if uploaded_file:
    # Carregando as planilhas
    xls = pd.ExcelFile(uploaded_file)
    
    try:
        df_ph = pd.read_excel(xls, sheet_name="SENSOR_PH")
        df_fosforo = pd.read_excel(xls, sheet_name="SENSOR_FOSFORO")
        df_potassio = pd.read_excel(xls, sheet_name="SENSOR_POTASSIO")
    except Exception as e:
        st.error(f"Erro ao ler as abas: {e}")
    else:
        # Conversão da coluna data_hora (garante formato datetime)
        for df in [df_ph, df_fosforo, df_potassio]:
            if 'data_hora' in df.columns:
                df['data_hora'] = pd.to_datetime(df['data_hora'])

        # Abas do dashboard
        tab1, tab2, tab3 = st.tabs(["PH", "Fósforo", "Potássio"])

        with tab1:
            st.subheader("Níveis de PH")
            st.dataframe(df_ph)
            fig_ph = px.line(df_ph, x='data_hora', y='PH_registrado', color='loc_sensor', markers=True,
                             title="Variação do PH por Localização")
            st.plotly_chart(fig_ph, use_container_width=True)

        with tab2:
            st.subheader("Níveis de Fósforo")
            st.dataframe(df_fosforo)
            fig_umid = px.line(df_fosforo, x='data_hora', y='Fosforo_registrado', color='loc_sensor', markers=True,
                               title="Variação do Fósforo por Localização")
            st.plotly_chart(fig_umid, use_container_width=True)

        with tab3:
            st.subheader("Níveis de Potássio")
            st.dataframe(df_potassio)
            fig_p = px.line(df_potassio, x='data_hora', y='Potassio_registrado', color='loc_sensor', markers=True,
                            title="Variação do Potássio por Localização")
            st.plotly_chart(fig_p, use_container_width=True)

else:
    st.warning("Faça o upload de um arquivo `.xlsx` com abas: ph, umidade, nutrientes, bomba.")
