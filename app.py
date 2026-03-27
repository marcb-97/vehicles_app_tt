# Importar librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado 
st.header('Visualizaciones de datos de vehiculos')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Boton histograma
hist_button = st.button('Construir histograma')
# Iniciar botón
if hist_button:
    st.write('Histograma del odómetro')
    # Crear histograma
    fig_hist = px.histogram(car_data, x='odometer')
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)
# Botón gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
# Iniciar botón
if scatter_button:
    st.write('Relación entre el año del modelo y el precio')
    # Crear diagrama de dispersión
    fig_scatter = px.scatter(car_data, x='model_year', y='price', title='Precio - Año del modelo')
    # Mostrar un grafico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
