import pandas as pd

#1. Carregamento dos dados
df = pd.read_csv('livros.csv', sep=';')

#visualização inicial
print("Primeiras linhas do dataset:")
print(df.head())

print("\nInformações gerais:")
print(df.info())

#2. Limpeza de dados
#remove valores nulos
df = df.dropna()

#converter tipos
df['paginas'] = pd.to_numeric(df['paginas'], errors='coerce')
df['ano'] = pd.to_numeric(df['ano'], errors='coerce')

#3. Análises
print("\nTotal de livros:", len(df))

media_paginas = df['paginas'].mean()
print("\nMédia de páginas:", media_paginas)

livro_max = df.loc[df['paginas'].idxmax()]
print("\nLivro com mais páginas:")
print(livro_max)

autor_top = df['autor'].value_counts().idxmax()
qtd_autor_top = df['autor'].value_counts().max()

print("\nAutor com mais livros:")
print(f"{autor_top} ({qtd_autor_top} livros)")

livros_por_ano = df['ano'].value_counts().sort_index()
print("\nQuantidade de livros por ano:")
print(livros_por_ano)

top10 = df.sort_values(by='paginas', ascending=False).head(10)
print("\nTop 10 livros com mais páginas:")
print(top10[['titulo', 'autor', 'paginas']])