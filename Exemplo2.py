import os

os.system('cls')

import pandas as pd

try:
    df = pd.read_csv('ClassicDisco.csv', sep=',', encoding='utf-8')
    # print(df)
    # print(df.to_string())
    # print(df.head(15))
    # print(df.tail())
    # print(df.info())
    # print(df.describe())
    # pd.set_option('display.min_rows', 10)
    # popularidade = df[df['Popularity'] > 20]
    # print(popularidade[["Track", "Popularity"]])
    # michael_jackson = df[df['Artist'] == 'Michael Jackson']
    # print(michael_jackson[["Album", "Track", "Artist"]])

    # df.to_csv('ClassicDisco_modificado.csv', index=False, sep=',', encoding='utf-8')

    df.to_excel('ClassicDisco_modificado.xls', index=False, engine='openpyxl')

except Exception as e:

    print(f'Erro {e}')
    exit()