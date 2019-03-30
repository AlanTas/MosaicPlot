from statsmodels.graphics.mosaicplot import mosaic
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


# Carrega o arquivo excel em um dataframe
data = pd.read_excel('data3.xlsx', index_col=None)

# Define a cor dos bloquins pela acurácia, tira isso aqui pq n serve de nada
def props(key):
    if '1.0' in key:
        return {'color': (56/255, 142/255, 60/255, 1)}
    if '0.5' in key:
        return {'color': (255/255, 238/255, 88/255, 1)}
    if '0.0' in key:
        return {'color': (198/255, 40/255, 40/255, 1)}


# Define as dimensões do plot
N, M = 3.7, 3.9
fig, ax = plt.subplots(figsize=(N, M))
# Faz o mosaico passando o dataframe, as colunas que tu quer, o eixo, o espaço entre os quadradins e as propriedades
mosaic(data, ['Test', 'Scenario', 'Question', 'Acuracy'], ax=ax, gap=0.02, properties=props)
#amostra
plt.show()
