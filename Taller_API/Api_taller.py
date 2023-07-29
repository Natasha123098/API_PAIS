
import requests

def listar_nombre_paises(url):
    paises = requests. get(url)
    paises = paises.json()
    lista_marea = []
    lista_mpoblacion = []
    lista_countries = []
    lista_total_pob = []

    for pais in paises:
        pais = pais['translations']['spa']['official']
        print(f"\nEl Nombre del pais es: {pais}")

        area_pais = pais['area']
        print(f"\nEl área del pais es de: {area_pais}")

        poblacion_pais = pais['population']
        print (f"\nLa población del pais es: {poblacion_pais}")

        lista_countries.append(pais)
        lista_marea.append(area_pais)
        lista_mpoblacion.append(poblacion_pais)
    lista_total_pob.append(lista_countries)
    lista_total_pob.append(lista_mpoblacion)

    def mayor_p(lista):
        return max(lista)

    def Total_poblacion(lista):
        return sum(lista)

    #def media(lista):
     #   return sum(lista)/len(lista)

    def calcular_media(lista):
        if len(lista) == 0:
            return 0  # Manejo de lista vacía para evitar división por cero
        else:
            return sum(lista) / len(lista)

    def calcular_median(lista):
        data = sorted(lista)
        index = len(data) // 2

        # If the dataset is odd
        if len(lista) % 2 != 0:
            return data[index]

        # If the dataset is even
        return (data[index - 1] + data[index]) / 2

    def calcular_moda(lista):
        frecuencia = {}
        for value in lista:
            frecuencia[value] = frecuencia.get(value, 0) + 1
        mayor_frecuencia = max(frecuencia.values())
        modas = [key for key, value in frecuencia.items()
                 if value == mayor_frecuencia]

        return modas

    print("\nESTADISTICA")
    print(f"El pais con mayor poblacion es: {mayor_p(lista_mpoblacion)}")
    print(f"El pais con mayor area: {mayor_p(lista_marea)}")
    print(f"La poblacion total es: {Total_poblacion(lista_mpoblacion)}")
    print(f"La media de la poblacion es: {calcular_media(lista_mpoblacion)}")
    print(f"La Mediana de la poblacion es: {calcular_median(lista_mpoblacion)}")
    print(f"La Moda de la poblacion es: {calcular_moda(lista_mpoblacion)}")

url = 'https://restcountries.com/v3.1/all=translations, area, population'
listar_nombre_paises(url)





'''
population = [55197, 105697, 226915, 27691019, 11555997, 4829764, 9749763, 3278292, 34813867,
           1160164, 45741000, 7132530, 26545864, 67391582, 8278737, 1265740, 18100, 18092, 29136808, 56,
           98462, 9890400, 9398861, 6871287, 1411, 4047200, 109581085, 2837743, 273523621, 69799978, 1901548,
           17643060, 53771300, 5057677, 30237, 33938, 1380004385, 1701583, 19129955, 366425, 437483, 254541,
           198410, 3714000, 25987, 0, 8947027, 31072945, 40218234, 509414, 896444, 51780579, 23503349, 10698896,
           6624554, 10305564, 19116209, 2416664, 397621, 540542, 307150, 32365998, 97928, 83992953, 119446,
           378243, 164689383, 2663234, 128932753, 1331057, 5106622, 329484123, 38137, 393248, 12123198, 1775378,
           11792, 48865, 65720, 102334403, 10110116, 25687041, 85032, 4994724, 287371, 6486201, 16858333, 125836021,
           97338583, 57557, 2794700, 183629, 7500700, 32866268, 31255435, 2351625, 83240525, 17500657, 2617820, 6069,
           62999, 11750, 37950802, 1399491, 3000, 59194, 8917205, 2724900.0, 106766, 59308690, 586634, 63903, 4922,
           26378275, 4649660, 7976985, 13132792, 280904, 220892331, 300, 2142252, 16743930, 9537642, 8654622, 5352000,
           400, 100800, 16718971, 110947, 40812, 451, 3473727, 510713, 555988, 59554023, 62215293, 649342, 786559,
           5379475, 271960, 11193729, 20903278, 400132, 6825442, 53192, 4270563, 30, 54409794, 9216900, 6031187,
           10715549, 39244, 28435943, 5657000, 57351567, 2302, 71991, 11818618, 84339067, 50882884, 869595, 686878,
           4255, 34232050, 4803269, 1000, 11326616, 2225728, 6591600, 115021, 103553442, 38659, 5458827, 108407721,
           621718, 33691, 15893219, 21919000,1207361, 7275556, 36910558, 1318442, 29825968, 2563, 1402985, 44700000,
           18383956, 6908224, 77265, 219161, 988002, 6927288, 106290, 45376763, 206139587, 12952209, 38005238, 25778815,
           29458, 2077132, 16655799, 24206636, 5685807, 16425859, 1470, 1967998, 10834, 14862927, 1402112000, 2072,
           394034, 114963583, 112519, 5530719, 38718, 11890781, 168783, 1203140, 20250834, 44134693, 840974, 2562, 544,
           59734213, 2881060, 212559409, 43849269, 19286123, 13452, 40222503, 771612, 9904608, 2540916, 2100126,
           11402533, 3280815, 56367, 2961161, 525285, 11673029
           ]
'''




