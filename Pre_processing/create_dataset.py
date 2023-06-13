import os
import pandas as pd

data = "dados"
directory = "livros_filosofia"  # Diretório dos arquivos

dict_df = {"autor": [], "titulo": [], "texto": []}

for i, filename in enumerate(os.listdir(directory)):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename), "r") as file:
            texto = file.read()
            autor, titulo = filename.split("-")[0], filename.split("-")[1].split(".txt")[0]

            texto_split = texto.split("*** START")[1].split("*** END")[0]
            texto = texto_split[30:]

            dict_df["autor"].append(autor)
            dict_df["titulo"].append(titulo)
            dict_df["texto"].append(texto)

df = pd.DataFrame(dict_df)

df.to_csv(os.path.join(data, "livros_filosofia.csv"), index=False)
