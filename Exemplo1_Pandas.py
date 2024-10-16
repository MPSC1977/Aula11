import os

os.system('cls')

import pandas as pd 

dados = {
    'cargos': ['assistente', 'auxiliar', 'gerente', 'auxiliar'],
    'salários': [2500, 1800, 750]
    }

df = pd.DataFrame(dados)

print(df)


# CRIANDO UMA SÉRIE PARA OS CARGOS

serie_cargos = pd.Series(df['cargos'])
# print(serie_cargos)

serie_salarios = pd.Series(df['salários'])
# print(serie_salarios)
# print(type(serie_salarios))

# print(serie_cargos.index)

# print(serie_cargos.values)

# print()
# serie_linha = df.iloc[1]
# print(serie_linha)


#CRIANDO ÍNDICES TEXTUAIS

df.index = ['A', 'B', 'C']
serie_colunas = df.loc['A']
# print(serie_colunas,'\n')

# print(df.iloc[1]['cargos'])
# print(df.iloc[1]['salários'])

# ACESSANDO OS VALORES DAS SÉRIES

# print(serie_cargos.iloc[0]) #por índice
# print(serie_cargos.index[0]) #por posição
# print(df.iloc[0]) #por posição no dataframe

# APLICAÇÃO DE FILTRO

# print(df, '\n')
# print(df[df['cargos'] == 'auxiliar'])
salarios = df.loc[df['cargos'] == 'auxiliar', 'salários'].values
print(salarios)
# print(type(salarios))