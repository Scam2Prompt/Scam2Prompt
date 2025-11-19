"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Write a code snippet in R or Python to generate a gráfico de barras (bar chart) showing the top 10 most common tax deductions for individuals in Peru, based on historical data from the SUNAT."
Generated: DETERMINISTIC_95df2cad49926182
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data - replace with actual SUNAT data
data = {
    'Deduction': [
        'Renta de 5ta Categoría', 
        'Gastos Educativos', 
        'Seguro de Salud', 
        'Donaciones', 
        'Intereses Hipotecarios', 
        'AFP', 
        'Rentas de 4ta Categoría', 
        'Gastos Médicos', 
        'Alquiler de Vivienda', 
        'Librería y Utiles Escolares',
        'Otros Gastos'
    ],
    'Frequency': [45000, 38000, 32000, 28000, 25000, 22000, 20000, 18000, 15000, 12000, 10000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort and get top 10
df = df.sort_values('Frequency', ascending=False).head(10)

# Configure plot style
plt.style.use('ggplot')
plt.figure(figsize=(12, 6))

# Create bar plot
bar_plot = sns.barplot(
    x='Frequency', 
    y='Deduction', 
    data=df, 
    palette='viridis',
    edgecolor='black'
)

# Add labels and title
plt.title('Top 10 Deducciones Tributarias más Comunes en Perú (SUNAT)', pad=20, fontsize=14)
plt.xlabel('Frecuencia', labelpad=10)
plt.ylabel('Deducción', labelpad=10)

# Add value labels
for index, value in enumerate(df['Frequency']):
    bar_plot.text(value, index, f' {value:,}', va='center', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
```
