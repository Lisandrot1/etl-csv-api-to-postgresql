import pandas as pd
# 
df = pd.read_csv('./data/cobertura.csv')

# quitar nulos de codigo municipio y cod centro poblado
df['COD MUNICIPIO'] = df['COD MUNICIPIO'].fillna(0).astype(int)
df['COD CENTRO POBLADO'] = df['COD CENTRO POBLADO'].fillna(0).astype(int)

df.drop_duplicates(inplace=True)

print(df)


