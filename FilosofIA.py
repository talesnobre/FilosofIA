import streamlit as st
import pandas as pd
import numpy as np
import torch
import joblib
import torch.nn as nn
from sklearn.preprocessing import LabelEncoder

from mtranslate import translate

def preprocess_text(text, vectorizer):
    # Aplicar a mesma transformação utilizada no conjunto de treinamento
    text_transformed = vectorizer.transform([text])
    tensor = torch.Tensor(text_transformed.toarray())
    return tensor

def load_model(len_in, len_out=5):

    len_entrada = len_in
    len_saida = len_out


    class NeuralNetwork(nn.Module):
        def __init__(self):
            super().__init__()
            self.flatten = nn.Flatten()

            self.linear_relu_stack = nn.Sequential(
                nn.Linear(len_entrada, 80),
                nn.ReLU(),
                nn.Linear(80, 80),
                nn.ReLU(),
                nn.Linear(80, len_saida)
            )

        def forward(self, x):
            x = self.flatten(x)
            logits = self.linear_relu_stack(x)
            return logits


    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    # Carregar o modelo
    loaded_model = NeuralNetwork().to(device)
    loaded_model.load_state_dict(torch.load(f"./modelos/modelo_{len_entrada}.pth"))
    loaded_model.eval()

    return loaded_model

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
    text = translate(text, 'en', 'pt')

    len_entrada = 25659
    len_saida = 5

    model = load_model(len_in=len_entrada, len_out=len_saida)
    # Carregar o vetorizador
    loaded_vectorizer = joblib.load(f"./modelos/vetorizador_{len_entrada}.pkl")

    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    
    input_text = text
    # Utilizar o modelo carregado para fazer previsões
    preprocessed_text = preprocess_text(input_text, loaded_vectorizer)
    preprocessed_text = preprocessed_text.to(device)
    
    with torch.no_grad():
        model.eval()
        prediction = model(preprocessed_text)
        predicted_class = prediction.argmax().item()

    le = LabelEncoder()
    le.fit_transform(
        ["ARISTOTLE",
        "NIETZSCHE",
        "PLATO",
        "SCHOPENHAUER",
        "THOMAS AQUINAS"]
    )
    predicted_class_label = le.inverse_transform([predicted_class])[0]

    print("Classe prevista:", predicted_class_label)

    if text:

        result = predicted_class_label
        # Exibindo o resultado
        st.markdown(f"O Filósofo que falaria essa frase é:  **{result}**" )

if __name__ == "__main__":
    main()