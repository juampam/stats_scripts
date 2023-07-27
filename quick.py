import numpy as np
import matplotlib.pyplot as plt

# Los datos que proporcionaste
data = [
    13.2, 18, 16.9, 21.1, 21.1, 16.4, 18, 23, 18.8, 18, 20, 15.2, 15.6, 15.5, 16.5, 20, 27, 23, 20, 18, 16,
    16, 13.2, 14, 16, 20, 16, 19.8, 13.2, 18, 10, 13.2, 15.9, 15.4, 15.5, 21, 16, 20, 10.6, 12.4, 15.9, 11.9,
    17, 11.9, 13.7, 11.9, 17.2, 22.5, 18.5, 20.6, 18.4, 20, 13.2, 14.5, 15.5, 19.6, 20, 14.5, 18.5, 11.1, 18,
    13.2, 19, 13.2, 15.9, 20, 18.5, 15.2, 16.5, 20, 18, 15.9, 13.2, 15.2, 15.5, 16.5, 18, 18, 12.8, 9.2, 15.9,
    15.9, 10.6, 11.9, 15.9, 18.5, 19.8, 12.4, 21.1, 18.5, 18.5, 15.8, 19.3
]

# Crear un gráfico de densidad (kernel density estimation) para visualizar la distribución
plt.figure(figsize=(8, 5))
plt.title("Distribución de Fuel Tank Capacity")
plt.xlabel("Fuel Tank Capacity")
plt.ylabel("Densidad")
plt.hist(data, bins=15, density=True, alpha=0.6, color='b')
plt.show()

