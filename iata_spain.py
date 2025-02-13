import csv

iata_spain = [
    ["code", "location", "name"],
    ["PEK", "Beijing", "Beijing Capital International Airport"],
    ["LAX", "Los Angeles", "Los Angeles International Airport"],
    ["DXB", "Dubai", "Dubai International Airport"],
    ["HND", "Tokyo", "Tokyo Haneda Airport"],
    ["ORD", "Chicago", "O'Hare International Airport"],
    ["LHR", "London", "London Heathrow Airport"],
    ["CDG", "Paris", "Charles de Gaulle Airport"],
    ["DFW", "Dallas", "Dallas/Fort Worth International Airport"],
    ["JFK", "New York", "John F. Kennedy International Airport"],
    ["SIN", "Singapore", "Singapore Changi Airport"],
    ["AMS", "Amsterdam", "Amsterdam Airport Schiphol"],
    ["HKG", "Hong Kong", "Hong Kong International Airport"],
    ["FRA", "Frankfurt", "Frankfurt Airport"],
    ["IST", "Istanbul", "Istanbul Airport"],
    ["PVG", "Shanghai", "Shanghai Pudong International Airport"],
    ["ICN", "Seoul", "Incheon International Airport"],
    ["MUC", "Munich", "Munich Airport"],
    ["BKK", "Bangkok", "Suvarnabhumi Airport"],
    ["SFO", "San Francisco", "San Francisco International Airport"],
    ["GRU", "São Paulo", "São Paulo-Guarulhos International Airport"],
    ["YYZ", "Toronto", "Toronto Pearson International Airport"],
    ["DEL", "New Delhi", "Indira Gandhi International Airport"],
    ["BCN", "Barcelona", "Barcelona-El Prat Airport"],
    ["MAD", "Madrid", "Adolfo Suárez Madrid-Barajas Airport"],
    ["SYD", "Sydney", "Sydney Kingsford Smith Airport"],
    ["MEX", "Mexico City", "Mexico City International Airport"],
    ["JNB", "Johannesburg", "O.R. Tambo International Airport"],
    ["SVO", "Moscow", "Sheremetyevo International Airport"],
    ["ZRH", "Zurich", "Zurich Airport"],
    ["CUE", "Cuenca", "Aeropuerto Internacional Mariscal Lamar"],
    ["EZE", "Buenos Aires", "Aeropuerto Internacional de Ezeiza"],
    ["GYE", "Guayaquil", "Aeropuerto Internacional José Joaquín de Olmedo"],
    ["CLO", "Cali", "Aeropuerto Internacional Bonilla Aragon"],
    ["BOG", "Bogota", "Aeropuerto Internacional El Dorado"],
    ["UIO", "Quito", "Aeropuerto Internacional Mariscal Sucre"]
]

with open(r'C:\Users\USUARIO\Desktop\GRAFO EJEMPLO\iata_spain.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(iata_spain)
