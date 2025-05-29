import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('acidentes_brasil_2019.csv')

# Gráfico 2: Linha temporal por mês
df['data'] = pd.to_datetime(df['data'])
df['mes'] = df['data'].dt.month
df_mensal = df.groupby('mes').size()
plt.figure(figsize=(10, 5))
plt.plot(df_mensal.index, df_mensal.values, marker='o')
plt.title('Acidentes por Mês - 2019')
plt.xlabel('Mês')
plt.ylabel('Número de Acidentes')
plt.grid(True)
plt.show()