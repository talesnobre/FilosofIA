import streamlit as st
import pandas as pd
import numpy as np
from mtranslate import translate
import torch
import joblib
import torch.nn as nn
from sklearn.preprocessing import LabelEncoder

def load_model():
    pass

def main() -> None:
    # importar o modelo ja treinado

    # st.title('FilosofIA')
    st.markdown("<h1 style='text-align: center;'>FilosofIA</h1>", unsafe_allow_html=True)

    
    st.markdown("<h2 style='text-align: left;'>Objetivo</h2>", unsafe_allow_html=True)
    st.write('''
        O trabalho tem por objetivo criar um modelo de Processamento de Linguagem Natural, 
        baseado no uso de redes neurais, que seja capaz de identificar o filósofo que falaria
        uma determinada frase. Para isso, foi utilizado um dataset com frases de 
        5 filósofos (Aristóteles, Nietzsche, Platão, Schopenhauer e São Tomás de Aquino)
        e treinado um modelo de classificação.
    ''')
        
    # st.header('Digite a sua frase')
    # Texto de entrada

    text = st.text_area("**Escreva sua frase abaixo e clique Ctrl + Enter**")
    # trad = translate(text, 'en', 'pt')
    # model = load_model()
        
    # st.header("Resultado do modelo")
    # Verificando se o texto foi inserido
    if text:
        # Resultado do modelo
        # response = trad.model(text)
        # result = model(text)
        trad = translate(text, 'en', 'pt')

        # Exibindo o resultado
        st.markdown(f"O Filósofo que falaria essa frase é:  **{trad}**" )

if __name__ == "__main__":
    main()
