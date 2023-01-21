import streamlit as st

st.title("Aplicación Neuronas")

from PIL import Image
image = Image.open('neurona.png')

st.image(image, caption='Visualizacion de Neurona')

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas"])

with tab1:
  st.header("Primera entrada")
  number00 = st.slider("Peso w0", 0.0,5.0, key = "slider0")
  valor00 = st.number_input("Entrada x0: ", 0,100, key = "val0")

  boton = st.button("Calcular la salida", key="boton0")
  if boton:

    resultado = number00*valor00

    st.write(f"La salida es:{resultado}")

with tab2:
  col1, col2= st.columns(2)
  with col1:
    st.header("Entrada1")
    number01 = st.slider("Peso w0", 0.0,5.0,key ="slider1")
    valor01 = st.number_input("Entrada x0: ", 0,100,key ="val1")
  with col2:
    st.header("Entrada2")
    number02 = st.slider("Peso w1", 0.0,5.0,key ="slider2")
    valor02 = st.number_input("Entrada x1: ", 0,100,key ="val2")

  boton = st.button("Calcular la salida",key ="boton1")
  if boton:
    resultado = number01*valor01 + number02*valor02

    st.write(f"La salida es:{resultado}")

with tab3:
  col1, col2,col3= st.columns(3)
  with col1:
    st.header("Entrada1")
    number03 = st.slider("Peso w0", 0.0,5.0,key ="slider3")
    valor03 = st.number_input("Entrada x0: ", 0,100,key ="val3")
  with col2:
    st.header("Entrada2")
    number04 = st.slider("Peso w1", 0.0,5.0,key ="slider4")
    valor04 = st.number_input("Entrada x1: ", 0,100,key ="val4")
  with col3:
    st.header("Entrada3")
    number05 = st.slider("Peso w2", 0.0,5.0,key ="slider5")
    valor05 = st.number_input("Entrada x2: ", 0,100,key ="val5")

  sesgo = st.number_input("Introduzca el valor del sesgo: ")

  boton = st.button("Calcular la salida",key ="boton2")
  if boton:
    resultado = number03*valor03 + number04*valor04 + number05*valor05 + sesgo

    st.write(f"La salida es:{resultado}")
  
