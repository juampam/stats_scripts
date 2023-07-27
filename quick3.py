import matplotlib.pyplot as plt

def plot_miles_per_gallon(data):
    # Separar los datos por tipo de carro
    car_types = {}
    for car, miles_per_gallon in data:
        if car in car_types:
            car_types[car].append(miles_per_gallon)
        else:
            car_types[car] = [miles_per_gallon]

    # Crear un gráfico de caja y bigotes para cada tipo de carro
    plt.figure(figsize=(10, 6))
    plt.boxplot(car_types.values(), labels=car_types.keys())
    plt.xlabel('Tipo de Carro')
    plt.ylabel('Millas por Galón en Ciudad')
    plt.title('Distribución de Millas por Galón en Ciudad por Tipo de Carro')
    plt.grid(True)
    plt.show()

# Datos de millas por galón en ciudad por tipo de carro
data = [
    ('Small', 25), ('Midsize', 18), ('Compact', 20), ('Midsize', 19), ('Midsize', 22), ('Midsize', 22), 
    # Resto de los datos...
    ('Compact', 21), ('Sporty', 18), ('Compact', 21), ('Midsize', 20)
]

# Llamar a la función para graficar los datos
plot_miles_per_gallon(data)

