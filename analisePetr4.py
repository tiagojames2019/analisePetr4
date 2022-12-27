# ANALISE MEDIA ANUAL PETR4
import pandas as pd

arquivo = pd.read_csv('PETR4.csv')

df = pd.DataFrame(arquivo)

#Convertendo Colunas em Float
for i in range(1,6):
    a = df.columns[i]
    df[a] = df[a].str.replace(',', '.').astype(float)


print(60* '')
print(10* '--','ANALISE DE MEDIAS PETR4', 10* '--')
print(60* '')

print('PETR4 -- MEDIA ABERTURA = {:.2f}'.format(df['ABERTURA'].mean()))
print('PETR4 -- MEDIA FECHAMENTO = {:.2f}'.format(df['FECHAMENTO'].mean()))
print('PETR4 -- MEDIA MINIMO = {:.2f}'.format(df['MÍNIMO'].mean()))
print('PETR4 -- MEDIA MAXIMO = {:.2f}'.format(df['MÁXIMO'].mean()))

print(60* '')
print(60* '')