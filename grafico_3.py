import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('acidentes_brasil_2019.csv')

# Gráfico 3: Dispersão (vítimas x tipo de via)
sns.scatterplot(data=df, x='tipo_via', y='num_vitimas', alpha=0.6)
plt.title('Correlação entre Tipo de Via e Número de Vítimas')
plt.xlabel('Tipo de Via')
plt.ylabel('Número de Vítimas')
plt.show()
