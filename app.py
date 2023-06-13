import streamlit as st
import pandas as pd
import numpy as np

def load_model():
    pass

def main() -> None:
    # importar o modelo ja treinado

    st.title('FilisofIA')
    
    st.header('Apresentação do problema')
    st.write('''
             Certo dia, no refeitório da universidade, um grupo de estudantes de filosofia começaram a 
             se questionar como seria poder conversar com qualquer filósofo que já morreu, 
             bem como saber a opinião deles a respeito dos temas e desafios da atualidade. 
             Mas tendo em vista que a maior parte dos filósofos e pensadores que eles gostariam de 
             ouvir já estavam mortos há muito tempo, isso não poderia ser possível por meios naturais. 
             Foi aí que Joãozinho, estudante de Ciência de Dados, entrou na roda de conversa e propôs o 
             uso de um modelo de Processamento de Linguagem Natural que fosse alimentado com várias obras 
             de diversos filósofos os quais os estudantes estavam interessados em ouvir e então gerar 
             texto com base nos escritos de tais autores. Isso serviria para simular o pensamento e os 
             dizeres dos filósofos para que os estudantes tivessem a experiência mais próxima possível 
             de conversar com um deles. 
    ''')

    
    st.header('Objetivos')
    st.write('''
        O trabalho tem por objetivo criar um modelo de Processamento de Linguagem Natural, 
        baseado no uso de redes neurais, arquiteturas já consolidadas e ajuste fino, de modo 
        que seja possível gerar textos e respostas com base no prompt do usuário a partir de 
        dados coletados e tratados de dezenas de livros de diversos autores da área de filosofia, 
        literatura, psicologia etc.
    ''')

    st.header('Dados utilizados e pré-processamento dos dados')
    st.write('''
        Os dados utilizaram foram livros em inglês já disponíveis em domínio público de diversos 
        autores da filosofia, sociologia, psicologia, literatura etc. A fonte principal desses livros 
        foi o Project Gutenberg (disponível em https://www.gutenberg.org/) , que é um site com mais 
        de 70.000 ebooks disponíveis gratuitamente. Uma das opções de download era justamente  o texto puro com 
        código UTF-8 e formato .txt, o que caiu como uma luva para o uso do modelo de Processamento de Linguagem Natural.
    ''')
    st.write('''
        O principal pré-processamento realizado foi excluir todo o texto que envolvia os direitos e detalhes a respeito do 
        Project Gutenberg que todo livro disponibilizado por eles tinha em sua composição. 
        Além disso, adicionamos ao dataset 2 colunas além do texto de cada livro em si, que são o título e o 
        autor da obra. Isso foi automatizado via baixar os arquivos e escrevendo seus respectivos títulos como 
        “nome do autor-nome da obra.txt
    ''')

    st.header('Digite a sua frase...')
    # Texto de entrada
    text = st.text_area('')

    st.header("Resultado do modelo")
    # Verificando se o texto foi inserido
    if text:
        # Resultado do modelo
        # result = model(text)
        
        # Exibindo o resultado
        st.write(f"Nome do filosofo que escreveu essa bela frase foi: ", )

if __name__ == "__main__":
    main()
