from geopy.distance import distance

longitud_1 = float(input("Ingrese la longitud del primer punto: "))
latitud_1 = float(input("Ingrese la latitud del primer punto: "))

punto1 = (latitud_1, longitud_1)

longitud_2 = float(input("Ingrese la longitud del segundo punto: "))
latitud_2 = float(input("Ingrese la latitud del segundo punto: "))

punto2 = (latitud_2, longitud_2)

distancia = distance(punto1, punto2).kilometers

print(f"La distancia entre las coordenadas es de {distancia:2f} km")