from pygle import network
from datos_municipio import *
from datos import *
import pandas as pd
"""datos_madrid = pd.read_excel("elecciones_madrid - copia.xls",sheet_name="Municipios")
lista = []
Madrid = Provincia("Madrid")

datos.tratar_datos(datos_madrid,Madrid)
print("votos la acebeda",Madrid.municipios[0].id,Madrid.municipios[0].votos,Madrid.cs,Madrid.votos)
"""

spain = Pais("spain")
"""ciudad = spain.buscar_ciudad("Málaga")
analizar_coste_ciudad(ciudad)"""
#ciudad = spain.buscar_ciudad("Barcelona")
#ciudad = spain.buscar_ciudad("Cádiz")
"""ciudad = spain.buscar_ciudad("Sevilla")
analizar_coste_ciudad(ciudad)"""
"""ciudad = spain.buscar_ciudad("Granada")
analizar_coste_ciudad(ciudad)"""
"""ciudad = spain.buscar_ciudad("Córdoba")
analizar_coste_ciudad(ciudad)"""
#ciudad = spain.buscar_ciudad("Valladolid")
ciudad = spain.buscar_ciudad("Madrid")
"""municipio = ciudad.buscar_municipio("Robledo de Chavela")
analizar_wifis_municipio(municipio)"""
"""datos_electoral_ciudad = pd.read_excel("elecciones_madrid_2019.xlsx")
tratar_datos(datos_electoral_ciudad,ciudad)"""
#lista = ["Brunete","Bustarviejo","Campo Real"]
#lista = ["Canencia","Casarrubuelos","Cercedilla","Chinchón","Collado Mediano","Colmenar Viejo","Colmenarejo"]
#QUEDA VILLALBILLA Y VILLANUEVA
"""lista=["Daganzo de Arriba","El Boalo","El Molar","Fuente el Saz de Jarama","Fuentidueña de Tajo","Griñón","Humanes de Madrid"
,"Los Molinos","Los Santos de la Humosa","Manzanares el Real","Meco","Mejorada del Campo","Miraflores de la Sierra","Moraleja de Enmedio"
,"Moralzarzal","Navacerrada","Rivas-Vaciamadrid","San Agustín del Guadalix","San Lorenzo de El Escorial","San Martín de la Vega"
,"Soto del Real","Talamanca de Jarama","Tielmes","Torrejón de Velasco","Torrejón de la Calzada","Torrelaguna","Torres de la Alameda"
,"Valdemorillo","Villalbilla","Villanueva del Pardillo"]"""
#lista = ["Collado Villalba","Majadahonda","Pinto","Galapagar"]
"""lista = ["Valdemoro","Pozuelo de Alarcón","Móstoles"]
for i in lista:
    municipio = ciudad.buscar_municipio(i)
    analizar_wifis_municipio(municipio)"""
"""municipio = ciudad.buscar_municipio("Móstoles")
analizar_wifis_municipio_aftersearch(municipio)"""
"""municipio = ciudad.buscar_municipio("Galapagar")
analizar_wifis_municipio_aftersearch(municipio)"""
"""municipio = ciudad.buscar_municipio("Móstoles")
analizar_wifis_municipio(municipio)"""
"""municipio = ciudad.buscar_municipio("Villalbilla")
analizar_wifis_municipio_aftersearch(municipio)
municipio = ciudad.buscar_municipio("Villanueva del Pardillo")
analizar_wifis_municipio(municipio)"""
"""municipio = ciudad.buscar_municipio("Colmenar Viejo")
analizar_wifis_municipio_aftersearch(municipio)
municipio = ciudad.buscar_municipio("Colmenarejo")
analizar_wifis_municipio(municipio)"""
"""ciudad = spain.buscar_ciudad("Córdoba")
municipio = ciudad.buscar_municipio("Montoro")
analizar_wifis_municipio(municipio)"""
#municipio = ciudad.buscar_municipio("Ajalvir")
"""municipio = ciudad.buscar_municipio("Alameda del Valle")
analizar_wifis_municipio(municipio)"""
#sanitizar_ciudad(ciudad)
"""clasificador_ciudad(ciudad,2001,2018)
clasificador_ciudad(ciudad,2017,2019)"""
#clasificador_ciudad(ciudad,2001,2023)
"""clasificador_ciudad_elegidos(ciudad,2001,2018)
clasificador_ciudad_elegidos(ciudad,2001,2023)
clasificador_ciudad_elegidos_todo(ciudad,2001,2018)
clasificador_ciudad_elegidos_todo(ciudad,2001,2023)"""
"""clasificador_ciudad_elegidos_todo(ciudad,2001,2018)
clasif_2018_todo=clasificador_ciudad_elegidos_todo(ciudad,2001,2023)
#clasif_2018=clasificador_ciudad_elegidos(ciudad,2001,2018)
#clasificador_ciudad_elegidos(ciudad,2001,2023)
#clasificador_renta(clasif_2018,ciudad)
clasificador_renta(clasif_2018_todo,ciudad)
#clasificador_elecciones(clasif_2018,ciudad)
clasificador_elecciones(clasif_2018_todo,ciudad)
"""
"""clasificador_ciudad_elegidos_todo_agrupando(ciudad,2000,2019)
clasificador_ciudad_elegidos_todo_agrupando(ciudad,2019,2023,mes_fin=1,mes_inicio=6)"""
clasificador_renta("Madrid/clasificador/Madrid_clasificador_elegidos_todo_agrupando1-2000_4-2019.csv",ciudad)
clasificador_elecciones("Madrid/clasificador/Madrid_clasificador_elegidos_todo_agrupando1-2000_4-2019.csv",ciudad,2019)
clasificador_elecciones("Madrid/clasificador/Madrid_clasificador_elegidos_todo_agrupando6-2019_1-2023.csv",ciudad,2023)
#clasif_2018_todo_agrupando=clasificador_ciudad_elegidos_todo_agrupando(ciudad,2001,2018)
"""clasif_2018_agrupando=clasificador_ciudad_elegidos_agrupando(ciudad,2001,2018)
clasif_2023_agrupando=clasificador_ciudad_elegidos_agrupando(ciudad,2001,2023)
#clasif_2023_todo_agrupando=clasificador_ciudad_elegidos_todo_agrupando(ciudad,2001,2023)
#clasif_2018=clasificador_ciudad_elegidos(ciudad,2001,2018)
#clasificador_ciudad_elegidos(ciudad,2001,2023)
#clasificador_renta(clasif_2018,ciudad)
#clasificador_renta(clasif_2018_todo_agrupando,ciudad)
#clasificador_elecciones(clasif_2018,ciudad)
#clasificador_elecciones(clasif_2018_todo_agrupando,ciudad)

clasificador_renta(clasif_2018_agrupando,ciudad)
#clasificador_elecciones(clasif_2018,ciudad)
clasificador_elecciones(clasif_2018_agrupando,ciudad)"""

"""clasif_2018_agrupando=clasificador_ciudad_elegidos_agrupando(ciudad,2018,2018)
clasif_2018_todo_agrupando=clasificador_ciudad_elegidos_todo_agrupando(ciudad,2018,2018)
clasif_2018=clasificador_ciudad_elegidos(ciudad,2018,2018)
clasif_2018_t=clasificador_ciudad_elegidos_todo(ciudad,2018,2018)


clasificador_renta(clasif_2018_agrupando,ciudad)
clasificador_elecciones(clasif_2018_agrupando,ciudad)

clasificador_renta(clasif_2018_todo_agrupando,ciudad)
clasificador_elecciones(clasif_2018_todo_agrupando,ciudad)

clasificador_renta(clasif_2018,ciudad)
clasificador_elecciones(clasif_2018,ciudad)

clasificador_renta(clasif_2018_t,ciudad)
clasificador_elecciones(clasif_2018_t,ciudad)"""

"""clasif_2019_2023_agrupando=clasificador_ciudad_elegidos_agrupando(ciudad,2019,2023)


clasif_2019_2023_todo_agrupando=clasificador_ciudad_elegidos_todo_agrupando(ciudad,2019,2023)"""

"""clasificador_ciudad_todo(ciudad,2001,2018)
clasificador_ciudad_todo(ciudad,2001,2023)"""
#clasificador_ciudad(ciudad,2017,2019)
#clasificador_ciudad_todo(ciudad,2001,2023)
#mun = ciudad.buscar_municipio("Boadilla del Monte")
#municipio = ciudad.buscar_municipio("San Sebastián de los Reyes")
#municipio = ciudad.buscar_municipio("Villaviciosa de Odón")
#municipio = ciudad.buscar_municipio("San Sebastián de los Reyes")
#municipio = ciudad.buscar_municipio("Alcobendas")
#municipio = ciudad.buscar_municipio("Ajalvir")
#municipio = ciudad.buscar_municipio("Colmenar Viejo")
#municipio = ciudad.buscar_municipio("Torrejón de Ardoz")
#municipio = ciudad.buscar_municipio("Venturada")
#municipio = ciudad.buscar_municipio("Cobeña") FALTA POR ANALIZAR
#municipio = ciudad.buscar_municipio("Pozuelo de Alarcón")
#municipio = ciudad.buscar_municipio("Villanueva de la Cañada")
#municipio = ciudad.buscar_municipio("Valdemoro")
"""wifis = clasificador_wifis(municipio)
print(wifis)"""
"""municipio = ciudad.buscar_municipio("Pinto")
analizar_wifis_municipio(municipio)

municipio = ciudad.buscar_municipio("Majadahonda")
analizar_wifis_municipio(municipio)

municipio = ciudad.buscar_municipio("Galapagar")
analizar_wifis_municipio(municipio)

municipio = ciudad.buscar_municipio("Collado Villalba")
analizar_wifis_municipio(municipio)

municipio = ciudad.buscar_municipio("Ciempozuelos")
analizar_wifis_municipio(municipio)"""

#DESDE AQUI HA PETADO, SALE EN EL CODIGO POSTAL ARGANDA DEL REY NO SE POR QUE
"""municipio = ciudad.buscar_municipio("Arganda del Rey")
analizar_wifis_municipio(municipio)"""

"""municipio = ciudad.buscar_municipio("Parla")
analizar_wifis_municipio(municipio)"""

"""municipio = ciudad.buscar_municipio("Coslada")
analizar_wifis_municipio(municipio)"""

"""municipio = ciudad.buscar_municipio("El Escorial")
analizar_wifis_municipio(municipio)"""

"""municipio = ciudad.buscar_municipio("Paracuellos de Jarama")
analizar_wifis_municipio(municipio)"""
#COMPLETADO NAVALCARNERO BIEN
"""municipio = ciudad.buscar_municipio("Navalcarnero")
analizar_wifis_municipio(municipio)"""
#HASTA AQUI SALE LO DE ARGANDA DEL REY
"""municipio = ciudad.buscar_municipio("Hoyo de Manzanares")
analizar_wifis_municipio(municipio)"""
"""municipio = ciudad.buscar_municipio("Guadarrama")
analizar_wifis_municipio(municipio)"""
"""municipio = ciudad.buscar_municipio("San Fernando de Henares")
analizar_wifis_municipio(municipio)
analizar_wifis_municipio_aftersearch(municipio,256040847824761,53,2)
analizar_wifis_municipio_aftersearch(municipio,279590252152906,1,2)"""
#COMPLETADO FUENLA
"""municipio = ciudad.buscar_municipio("Fuenlabrada")
#analizar_wifis_municipio(municipio)
analizar_wifis_municipio_aftersearch(municipio)"""
#COMPLETADO MOSTO
"""municipio = ciudad.buscar_municipio("Móstoles")
#analizar_wifis_municipio(municipio)
analizar_wifis_municipio_aftersearch(municipio)"""
#COMPLETADO GETAFE
"""municipio = ciudad.buscar_municipio("Getafe")
#analizar_wifis_municipio(municipio)
analizar_wifis_municipio_aftersearch(municipio)"""
#ultimo searchafter: 280374907824108
#COMPLETADO ALCORCON
"""municipio = ciudad.buscar_municipio("Alcorcón")
#analizar_wifis_municipio(municipio)
analizar_wifis_municipio_aftersearch(municipio)"""
#LEGANES COMPLETADO
"""municipio = ciudad.buscar_municipio("Leganés")
#analizar_wifis_municipio(municipio)
#analizar_wifis_municipio_aftersearch(municipio,110827916889492,793,1)
analizar_wifis_municipio_aftersearch(municipio)"""
#EJECUTADO ALCALA
"""municipio = ciudad.buscar_municipio("Alcalá de Henares")
#analizar_wifis_municipio(municipio)
analizar_wifis_municipio_aftersearch(municipio)"""
#lista_muns = elegir_muns(ciudad)
"""vendedor = vendedor_router(municipio)"""
"""clasificador_mun = clasificador_wifis(municipio)
print(clasificador_mun)"""
#analizar_coste_ciudad(ciudad)
"""muns_madrid_wifis = elegir_muns_wifis(ciudad)
muns_madrid = elegir_muns_votos(ciudad,muns_madrid_wifis)
print(muns_madrid_wifis)
print(muns_madrid)"""
#pa buscar
"""opciones distintas para la geolocalizacion
# import module
from geopy.geocoders import Nominatim
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
place = "Boring road patna"
location = geolocator.geocode(place)
print(location)
data = location.raw
print(data)
en el bounding box de data vienen las latitudes y longitudes. data es un diccionario
"""

"""b = network.geocode("Hoyo de Manzanares")
c = Madrid.buscar_municipio("Hoyo de Manzanares")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
d1.analizar_wifis_municipio(c)
"""
"""search_after = 0
for i in range(6):
    if i == 0:
        wifis = network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3])
        search_after = wifis["search_after"]
    else:
        wifis = network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3],searchAfter= search_after)
        search_after = wifis["search_after"]

    print("busqueda", wifis)

print("busqueda",wifis)"""




"""b = network.geocode("Torrelodones")
c = Madrid.buscar_municipio("Torrelodones")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
d1.analizar_wifis_municipio(c)"""

"""
b = network.geocode("La Acebeda")
c = Madrid.buscar_municipio("La Acebeda")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
#print(network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3]))
d1.analizar_wifis_municipio(c)"""


"""b = network.geocode("Ajalvir")
c = Madrid.buscar_municipio("Ajalvir")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
#print(network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3]))
d1.analizar_wifis_municipio(c)"""

"""
b = network.geocode("Alameda del Valle")
c = Madrid.buscar_municipio("Alameda del Valle")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
#print(network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3]))
d1.analizar_wifis_municipio(c)

b = network.geocode("El Álamo")
c = Madrid.buscar_municipio("El Álamo")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
#print(network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3]))
d1.analizar_wifis_municipio(c)"""

"""b = network.geocode("Alcalá de Henares")
c = Madrid.buscar_municipio("Alcalá de Henares")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
#print(network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3]))
d1.analizar_wifis_municipio(c)"""

"""b = network.geocode("Ambite")
c = Madrid.buscar_municipio("Ambite")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
#print(network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3]))
d1.analizar_wifis_municipio(c)"""

"""b = network.geocode("Anchuelo")
c = Madrid.buscar_municipio("Anchuelo")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
#print(network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3]))
d1.analizar_wifis_municipio(c)"""

"""b = network.geocode("Getafe")
c = Madrid.buscar_municipio("Getafe")
print("coordenadas del municipio",b["results"][0]["boundingbox"],c.id)
coordenadas = b["results"][0]["boundingbox"]
#print(network.search(latrange1=coordenadas[0],latrange2=coordenadas[1],longrange1=coordenadas[2],longrange2=coordenadas[3]))
d1.analizar_wifis_municipio(c)"""


"""df = pd.read_csv("Hoyo de Manzanares_wifi_n.csv")
df.to_excel("Hoyo de Manzanares_wifi.xlsx",index= None,header = True)"""
"""import geocoder
loc = geocoder.google("Las Rozas de Madrid,Madrid,Spain")
print(loc)"""
#network.search()
#supuestamente pones el nombre de la ciudad y te devuelve las coordenadas , muy util para crear una base de datos

"""#limites de municipio
municipio = Madrid.buscar_municipio("Hoyo de Manzanares")
limite_mun = d1.limite_municipio(municipio.id)
print(limite_mun)"""
"""#calculo de planificacion de tiempo
municipio = Madrid.buscar_municipio("Torrelodones")
limite_mun = d1.limite_municipio(municipio.id)
print(limite_mun)
lat1 = 10000000000
lat2 = 0
long1 = 1000000000
long2 = -1000000000
for i in limite_mun:
    if i[0] > long2:
        long2 = i[0]
    if i[0] < long1:
        long1 = i[0]
    if i[1] > lat2:
        lat2 = i[1]
    if i[1] < lat1:
        lat1 = i[1]
#print("puntos extremos mun:",lat1,lat2,long1,long2)
#print(network.search(latrange1= lat1,latrange2=lat2,longrange1=long1,longrange2=long2))
#%%
municipio.coordenadas = [lat1,lat2,long1,long2]
d1.analizar_wifis_municipio(municipio)"""
#tiempo ejecucion
"""d1.analizar_coste_ciudad(Madrid)"""
#municipio = Madrid.buscar_municipio("Torrelodones")
#municipio = Madrid.buscar_municipio("Las Rozas de Madrid")
#municipio = Madrid.buscar_municipio("Tres Cantos")
#municipio = Madrid.buscar_municipio("Alcobendas")
#municipio = Madrid.buscar_municipio("Algete")
#municipio = Madrid.buscar_municipio("Hoyo de Manzanares")
#municipio = Madrid.buscar_municipio("Alpedrete")
#municipio = Madrid.buscar_municipio("Ambite")
#municipio = Madrid.buscar_municipio("Anchuelo")
#municipio = Madrid.buscar_municipio("Aranjuez")
#municipio = Madrid.buscar_municipio("Arganda del Rey")
#municipio = Madrid.buscar_municipio("Arroyomolinos")
#municipio = Madrid.buscar_municipio("Becerril de la Sierra")

"""Madrid = spain.buscar_ciudad("Madrid")
#municipio = Madrid.buscar_municipio("Boadilla del Monte")
municipio = Madrid.buscar_municipio("Hoyo de Manzanares")
#municipio = Madrid.buscar_municipio("El Boalo")
#municipio = Madrid.buscar_municipio("Buitrago del Lozoya")
analizar_wifis_municipio(municipio)"""

"""archivo = "analisis_coste_Madrid_ant.csv"
d1.analizar_wifis_dia(archivo,Madrid,1)"""

#datos.pintar_wifis_mun("Las Rozas de Madrid")