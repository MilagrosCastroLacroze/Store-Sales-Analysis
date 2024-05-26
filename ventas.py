import pandas as pd
import numpy as np

#IMPORT DATA

# Load the CSV file
df = pd.read_csv('ventas_tienda.csv')

# Display the first rows of the DataFrame
print(df.head())

# Convert 'Fecha' column to datetime type
df['Fecha'] = pd.to_datetime(df['Fecha'])

#DATA CLEANING

# Check for null values
print(df.isnull().sum())

#ANALYZE DATA

# Add a total income column
df['Ingresos'] = df['Precio'] * df['Unidades_Vendidas']

# Group by date and add income
ingresos_diarios = df.groupby('Fecha')['Ingresos'].sum().reset_index()
print(ingresos_diarios)

# Group by category and add the units sold
unidades_por_categoria = df.groupby('Categoria')['Unidades_Vendidas'].sum().reset_index()
print(unidades_por_categoria)

# Group by product and add up the income
ingresos_por_producto = df.groupby('Producto')['Ingresos'].sum().reset_index()

# Find the product with the highest income
producto_top = ingresos_por_producto.loc[ingresos_por_producto['Ingresos'].idxmax()]
print(producto_top)

# Calculate mean and standard deviation of price
precio_medio = np.mean(df['Precio'])
precio_std = np.std(df['Precio'])

print(f"Precio medio: {precio_medio}")
print(f"Desviación estándar del precio: {precio_std}")

#VISUALIZATION DATA 

import matplotlib.pyplot as plt

# Graph daily income
plt.figure(figsize=(10,6))
plt.plot(ingresos_diarios['Fecha'], ingresos_diarios['Ingresos'], marker='o')
plt.title('Ingresos Diarios')
plt.xlabel('Fecha')
plt.ylabel('Ingresos')
plt.grid(True)
plt.show()

# Graph units sold by category
plt.figure(figsize=(10,6))
plt.bar(unidades_por_categoria['Categoria'], unidades_por_categoria['Unidades_Vendidas'], color='skyblue')
plt.title('Unidades Vendidas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Unidades Vendidas')
plt.show()




