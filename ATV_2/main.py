import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1. CARREGAR DADOS
df = pd.read_csv("vendas.csv")

print("Dados carregados:")
print(df.head())

#2. TRATAMENTO DE DATAS
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df["mes"] = df["data"].dt.month

#3. EVOLUÇÃO DO FATURAMENTO
faturamento_mes = df.groupby("mes")["total_venda"].sum().sort_index()
print("\nFaturamento por mês:")
print(faturamento_mes)

#4. GRÁFICO DE LINHA
plt.figure()
plt.plot(faturamento_mes.index, faturamento_mes.values, marker='o')
plt.title("Evolução do Faturamento Mensal")
plt.xlabel("Mês")
plt.ylabel("Faturamento Total")
plt.grid()

plt.show()

#5. TICKET MÉDIO POR VENDEDOR
ticket_medio = df.groupby("vendedor")["total_venda"].mean()

vendedor_top = ticket_medio.idxmax()
valor_top = ticket_medio.max()

print("\nVendedor com maior ticket médio:")
print(f"{vendedor_top} - R$ {valor_top:.2f}")

#6. VENDAS DE ALTO VALOR (maior que 200)
df_alto_valor = df[df["total_venda"] > 200]

categorias_top = df_alto_valor["categoria"].value_counts()

print("\nCategorias que dominam vendas > 200:")
print(categorias_top)

#7. ADICIONAR VALORES NULOS
linhas_nulas = pd.DataFrame({
    "data": [None]*5,
    "vendedor": [None]*5,
    "categoria": [None]*5,
    "total_venda": [None]*5
})

df = pd.concat([df, linhas_nulas], ignore_index=True)

#8. IDENTIFICAR NULOS
print("\nValores nulos por coluna:")
print(df.isnull().sum())

#9. TRATAMENTO DE NULOS
df_limpo = df.dropna()

print("\nDataset após remoção de nulos:")
print(df_limpo.shape)

print("\nDataset após preenchimento de nulos:")
print(df_fill.head())