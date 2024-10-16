import os

os.system('cls')

import pandas as pd 

filmes = {
    'Título': ['DeadPool', 'Logan', 'Repetente', 'TriploX'],
    'Gênero': ['Ação', 'Ação', 'Drama', 'Policial'],
    'Ano': [2020, 2022, 2023, 2000]
    }

df = pd.DataFrame(filmes)
serie_titulo = pd.Series(df['Título'])
serie_genero = pd.Series(df['Gênero'])
serie_ano = pd.Series(df['Ano'])

print('DATAFRAME')
print(df)
print(20 * '=')
print()

print('APLICANDO FILTRO')
print(df[df['Gênero'] == 'Ação']) # aplicando filtro
print(20 * '=')
print()

print('ACESSANDO POR ÍNDICE')
print(serie_titulo.iloc[2]) # acessando por índice
print(20 * '=')
print()

print('ACESSANDO POR POSIÇÃO')
print(serie_genero.index[0]) # acessando por posição
