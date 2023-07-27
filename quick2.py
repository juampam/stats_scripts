# Datos de millas por galón en ciudad por tipo de carro
data = [
    ('Small', 25), ('Midsize', 18), ('Compact', 20), ('Midsize', 19), ('Midsize', 22), ('Midsize', 22), 
    ('Large', 19), ('Large', 16), ('Midsize', 19), ('Large', 16), ('Midsize', 16), ('Compact', 25), 
    ('Compact', 25), ('Sporty', 19), ('Midsize', 21), ('Van', 18), ('Van', 15), ('Large', 17), 
    ('Sporty', 17), ('Large', 20), ('Compact', 23), ('Large', 20), ('Small', 29), ('Small', 23), 
    ('Compact', 22), ('Van', 17), ('Midsize', 21), ('Sporty', 18), ('Small', 29), ('Large', 20), 
    ('Small', 31), ('Small', 23), ('Compact', 22), ('Sporty', 22), ('Sporty', 24), ('Van', 15), 
    ('Midsize', 21), ('Large', 18), ('Small', 46), ('Sporty', 30), ('Sporty', 24), ('Small', 42), 
    ('Compact', 24), ('Small', 29), ('Small', 22), ('Sporty', 26), ('Midsize', 20), ('Midsize', 17), 
    ('Midsize', 18), ('Midsize', 18), ('Midsize', 17), ('Large', 18), ('Small', 29), ('Small', 28), 
    ('Compact', 26), ('Van', 18), ('Sporty', 17), ('Compact', 20), ('Midsize', 19), ('Sporty', 23), 
    ('Midsize', 19), ('Small', 29), ('Midsize', 18), ('Small', 29), ('Compact', 24), ('Van', 17), 
    ('Midsize', 21), ('Compact', 24), ('Midsize', 23), ('Van', 18), ('Large', 19), ('Sporty', 23), 
    ('Small', 31), ('Compact', 23), ('Sporty', 19), ('Midsize', 19), ('Large', 19), ('Compact', 20), 
    ('Small', 28), ('Small', 33), ('Small', 25), ('Compact', 23), ('Small', 39), ('Small', 32), 
    ('Sporty', 25), ('Midsize', 22), ('Van', 18), ('Small', 25), ('Van', 17), ('Compact', 21), 
    ('Sporty', 18), ('Compact', 21), ('Midsize', 20)
]

# Separar los datos por tipo de carro
car_types = {}
for car, miles_per_gallon in data:
    if car in car_types:
        car_types[car].append(miles_per_gallon)
    else:
        car_types[car] = [miles_per_gallon]

# Calcular las medidas de centro y dispersión para cada tipo de carro
statistics = {}
for car, miles_per_gallon in car_types.items():
    statistics[car] = {
        'Media': sum(miles_per_gallon) / len(miles_per_gallon),
        'Mediana': sorted(miles_per_gallon)[len(miles_per_gallon) // 2],
        'Rango': max(miles_per_gallon) - min(miles_per_gallon),
        'Desviacion_Estandar': (sum((x - (sum(miles_per_gallon) / len(miles_per_gallon))) ** 2 for x in miles_per_gallon) / len(miles_per_gallon)) ** 0.5
    }

# Imprimir resultados
for car, stats in statistics.items():
    print(f"Tipo de carro: {car}")
    print(f"Media: {stats['Media']:.2f}")
    print(f"Mediana: {stats['Mediana']}")
    print(f"Rango: {stats['Rango']}")
    print(f"Desviacion Estándar: {stats['Desviacion_Estandar']:.2f}")
    print()

