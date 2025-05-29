import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('acidentes_brasil_2019.csv')

# Gráfico 1: Barras por estado
df_estado = df['estado'].value_counts().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
df_estado.plot(kind='bar', color='skyblue')
plt.title('Acidentes por Estado - 2019')
plt.xlabel('Estado')
plt.ylabel('Número de Acidentes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()