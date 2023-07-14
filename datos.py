from pygle import network
import math
import json
import pandas as pd
from shapely.geometry import Polygon, Point,MultiPolygon, shape
from dateutil import parser
import os
import requests

"""lista_wifi = {"trilat":[],"trilong":[],"ssid":[],"qos":[],"transid":[],"firsttime":[],"lasttime":[],
"lastupdt":[],"netid":[],"name":[],"type":[],"comment":[],"wep":[],"bcninterval":[],"freenet":[],"dhcp":[],
"paynet":[],"userfound":[],"channel":[],"encryption":[],"country":[],"region":[],"city":[],"housenumber":[],
"road":[],"postalcode":[]}
lista_json = []"""
limite_diario_wifis = 500

with open("Municipios_IGN.geojson", encoding='utf-8') as file:
    archivo_limite_muns = json.load(file)
OBJECTID = []
NAMEUNIT = []
CODIGOINE = []
for i in range(len(archivo_limite_muns["features"])):
    OBJECTID.append(archivo_limite_muns["features"][i]["properties"]["OBJECTID"])
    NAMEUNIT.append(archivo_limite_muns["features"][i]["properties"]["NAMEUNIT"])
    CODIGOINE.append(archivo_limite_muns["features"][i]["properties"]["CODIGOINE"])
data_muns_geojson = pd.DataFrame({"OBJECTID":OBJECTID,"NAMEUNIT":NAMEUNIT,"CODIGOINE":CODIGOINE})
data_muns_geojson["color"] = 10

def tratar_datos(archivo, ciudad):
    """Guarda los resultados electorales en cada clase municipio """
    columnas = archivo.columns
    columnas = columnas.tolist()
    for columna in range(len(columnas)):
        columnas[columna] = columnas[columna].lower()
    valores = archivo.values
    for i in range(len(valores) - 1):
        index_mun = None
        for j in range(len(valores)):
            if j == columnas.index("municipio"):
                for m in range(len(ciudad.municipios)):
                    if ciudad.municipios[m].id == valores[i][j]:
                        index_mun = m
            """if j == columnas.index("votos validos"):
                ciudad.municipios[index_mun].votos += valores[i][j]
                ciudad.votos += valores[i][j]"""
            if index_mun is not None:
                if j == columnas.index("votos_total"):
                    ciudad.municipios[index_mun].votos += valores[i][j]
                    ciudad.votos += valores[i][j]

                if j == columnas.index("cs"):
                    ciudad.municipios[index_mun].cs += valores[i][j]
                    ciudad.municipios[index_mun].derecha += valores[i][j]
                    ciudad.cs += valores[i][j]
                    ciudad.derecha += valores[i][j]
                if j == columnas.index("pp"):
                    ciudad.municipios[index_mun].pp += valores[i][j]
                    ciudad.municipios[index_mun].derecha += valores[i][j]
                    ciudad.pp += valores[i][j]
                    ciudad.derecha += valores[i][j]
                if j == columnas.index("psoe"):
                    ciudad.municipios[index_mun].psoe += valores[i][j]
                    ciudad.municipios[index_mun].izquierda += valores[i][j]
                    ciudad.psoe += valores[i][j]
                    ciudad.izquierda += valores[i][j]
                if j == columnas.index("podemos-iu"):
                    ciudad.municipios[index_mun].podemos += valores[i][j]
                    ciudad.municipios[index_mun].izquierda += valores[i][j]
                    ciudad.podemos += valores[i][j]
                    ciudad.izquierda += valores[i][j]
                if j == columnas.index("vox"):
                    ciudad.municipios[index_mun].vox += valores[i][j]
                    ciudad.municipios[index_mun].derecha += valores[i][j]
                    ciudad.vox += valores[i][j]
                    ciudad.derecha += valores[i][j]
                if j == columnas.index("más madrid"):
                    ciudad.municipios[index_mun].mas_madrid += valores[i][j]
                    ciudad.municipios[index_mun].izquierda += valores[i][j]
                    ciudad.mas_madrid += valores[i][j]
                    ciudad.izquierda += valores[i][j]

def analizar_wifis_municipio_ant(municipio):
    """Version antigua del analisis del municipio, menos eficiente y mucho mas compleja"""
    ubicacion = network.geocode(municipio.id)
    municipio.limite = ubicacion["results"][0]["boundingbox"]
    cont_wifis = 0
    loc_wifis = network.search(latrange1=municipio.limite[0], latrange2=municipio.limite[1], longrange1=municipio.limite[2], longrange2=municipio.limite[3])
    total_wifis = loc_wifis["totalResults"]
    if total_wifis <= 100:
        cont_wifis += total_wifis
    else:
        filas = 0
        columnas = 0
        min_casillas = math.ceil(total_wifis / 100)
        while (filas * columnas) <= min_casillas:
            filas += 1
            columnas += 1
        #la diferencia del eje x e y por cuadrado
        dif_lat = (municipio.limite[1] - municipio.limite[0]) / filas
        dif_long = (municipio.limite[3] - municipio.limite[2]) / columnas
        print("municipio recorrido", filas * columnas)
        print("en total hay que analizar", total_wifis)
        for fila in range(filas):
            #la formula es para dividir la zona en cuadrados
            for columna in range (columnas):
                if cont_wifis == total_wifis:
                    break
                else:
                    lat1 = municipio.limite[1] - dif_lat * (fila + 1)
                    lat2 = municipio.limite[1] - dif_lat * (fila)
                    long1 = municipio.limite[2] + dif_long * (columna)
                    long2 = municipio.limite[2] + dif_long * (columna + 1)
                    coordenadas = [lat1,lat2,long1,long2]
                    print("fila", fila, "columna", columna)
                    print("coordenadas", coordenadas)
                    recursividad_zonas(coordenadas)


def recursividad_zonas(coordenadas):
    """Funcion auxiliar de la anterior para la recursividad,no es eficiente"""
    if cont_wifis == total_wifis:
                    return
    buscar_wifis = network.search(latrange1=coordenadas[0], latrange2=coordenadas[1], longrange1=coordenadas[2], longrange2=coordenadas[3])
    print("coordenadas del bucle", coordenadas)
    print("llevamos analizadas",cont_wifis)
    if buscar_wifis["totalResults"] <= 100:
        #zona que entra en ese area
        cont_wifis += buscar_wifis["totalResults"]
        print("zona analizada, hay ",buscar_wifis["totalResults"])
        print("ahora hay analizadas", cont_wifis)

    else:
        print("zona SIN analizar, hay ", buscar_wifis["totalResults"])
        dif_lat = calcular_diferencia(coordenadas[1],coordenadas[0])
        dif_long = calcular_diferencia(coordenadas[3], coordenadas[2])
        """
        4 zonas
        #cuadrado izq_arriba
        c1 = [(coordenadas[0])+dif_lat,coordenadas[1],coordenadas[2],coordenadas[3]-dif_long]
        self.recursividad_zonas(c1)
        # cuadrado izq_abajo
        c2 = [coordenadas[0], coordenadas[1]- dif_lat, coordenadas[2], coordenadas[3]-dif_long]
        self.recursividad_zonas(c2)
        # cuadrado drcho_arriba
        c3 = [coordenadas[0]+dif_lat, coordenadas[1], coordenadas[2]+dif_long, coordenadas[3]]
        self.recursividad_zonas(c3)
        # cuadrado drcho_abajo
        c4 = [coordenadas[0], coordenadas[1]-dif_lat, coordenadas[2]+dif_long, coordenadas[3]]
        self.recursividad_zonas(c4)"""
        #2 zonas
        # cuadrado izq
        c1 = [(coordenadas[0]), coordenadas[1], coordenadas[2], coordenadas[3] - dif_long]
        recursividad_zonas(c1)
        # cuadrado drcho
        c2 = [coordenadas[0], coordenadas[1], coordenadas[2] + dif_long, coordenadas[3]]
        recursividad_zonas(c2)

def calcular_diferencia(coor1,coor2):
    return (coor1 - coor2)/2


def analizar_wifis_municipio(municipio):
    """Analiza las wifis de cada municipio y las guarda en un csv"""
    lista_wifi = {"trilat": [], "trilong": [], "ssid": [], "qos": [], "transid": [], "firsttime": [], "lasttime": [],
                  "lastupdt": [], "netid": [], "name": [], "type": [], "comment": [], "wep": [], "bcninterval": [],
                  "freenet": [], "dhcp": [],
                  "paynet": [], "userfound": [], "channel": [], "encryption": [], "country": [], "region": [],
                  "city": [], "housenumber": [],
                  "road": [], "postalcode": []}
    lista_json = []
    cont = 0
    municipio.poligono = poligono_municipio(municipio.id)
    municipio.limite = coordenadas_limite_municipio(municipio.poligono)
    wifis = 0
    if not isinstance(municipio.poligono, bool):
        loc_wifis = network.search(latrange1=municipio.limite[0], latrange2=municipio.limite[1], longrange1=municipio.limite[2], longrange2=municipio.limite[3])
        print(loc_wifis)
        cont+=1
        print(cont)
        cont_datos = loc_wifis["resultCount"]
        total_wifis = loc_wifis["totalResults"]
        if total_wifis <= 100:
            for data in range(cont_datos):
                trilat = loc_wifis["results"][data]["trilat"]
                trilong = loc_wifis["results"][data]["trilong"]
                coor_wifi = [trilong,trilat]
                coor_valida = coordenada_valida(coor_wifi, municipio)
                if coor_valida:
                    if loc_wifis["results"][data]["city"] == municipio.id or loc_wifis["results"][data]["city"] is None:
                        guardar_datos_dict(loc_wifis, data,lista_wifi)
                        lista_json.append(loc_wifis["results"][data])
                        wifis += 1
                        print("Wifi valida numero", wifis)
                else:
                    pass

            guardar_datos_wifis_csv(municipio,lista_wifi)
            guardar_datos_wifis_json(municipio,lista_json)
        else:
            search_after = loc_wifis["search_after"]
            n = math.ceil((total_wifis - 100) / 100)
            for i in range(n):
                try:
                    loc_wifis = network.search(latrange1=municipio.limite[0], latrange2=municipio.limite[1], longrange1=municipio.limite[2], longrange2=municipio.limite[3], searchAfter=search_after)
                except requests.exceptions.HTTPError:
                    print("Todavia no se ha analizado todo el municipio, quedan", n+1 - cont, "ejecuciones")
                    guardar_datos_wifis_csv(municipio,lista_wifi)
                    guardar_datos_wifis_json(municipio,lista_json)
                    dict_datos = [
                        {"Municipio": municipio.id, "Ejecuciones Totales": n + 1, "Ejecuciones actuales": cont,
                         "Ejecuciones restantes": n + 1 - cont,"Ejecuciones realizadas hoy": cont,
                         "SearchAfter": search_after, "Dia": 1}]
                    nombre_archivo_wifi = f"{municipio.id}_ejecuciones_restantes.json"
                    with open(nombre_archivo_wifi, "w", encoding="windows-1252") as archivo_wifi:
                        json.dump(dict_datos, archivo_wifi)
                    print(dict_datos)
                    return dict_datos
                cont_datos = loc_wifis["resultCount"]
                for data in range(cont_datos):
                    trilat = loc_wifis["results"][data]["trilat"]
                    trilong = loc_wifis["results"][data]["trilong"]
                    coor_wifi = [trilong,trilat]
                    coor_valida = coordenada_valida(coor_wifi, municipio)
                    if coor_valida:
                        if loc_wifis["results"][data]["city"] == municipio.id or loc_wifis["results"][data]["city"] is None :
                            guardar_datos_dict(loc_wifis, data,lista_wifi)
                            lista_json.append(loc_wifis["results"][data])
                            wifis += 1
                            print("Wifi valida numero", wifis)
                    else:
                        pass
                search_after = loc_wifis["search_after"]
                print(loc_wifis)
                cont += 1
                print(cont)

            guardar_datos_wifis_csv(municipio,lista_wifi)
            guardar_datos_wifis_json(municipio,lista_json)

def analizar_wifis_municipio_aftersearch(municipio):
    """Esta funcion es igual que la anterior pero adaptada para analizar los municipios que lleven mas de 1 dia
    analizarlos. IMPORTANTE, la 1 vez que se ejecute un municipio se utiliza la funcion anterior, a partir de esa ejecucion
     se utiliza esta. Sobreescribe los datos que ya habia en el csv"""
    lista_wifi = {"trilat": [], "trilong": [], "ssid": [], "qos": [], "transid": [], "firsttime": [], "lasttime": [],
                  "lastupdt": [], "netid": [], "name": [], "type": [], "comment": [], "wep": [], "bcninterval": [],
                  "freenet": [], "dhcp": [],
                  "paynet": [], "userfound": [], "channel": [], "encryption": [], "country": [], "region": [],
                  "city": [], "housenumber": [],
                  "road": [], "postalcode": []}
    lista_json = []
    cont = 0
    municipio.poligono = poligono_municipio(municipio.id)
    municipio.limite = coordenadas_limite_municipio(municipio.poligono)
    wifis = 0
    nombre_archivo_wifi = f"{municipio.id}_ejecuciones_restantes.json"
    with open(nombre_archivo_wifi, encoding="windows-1252") as archivo_wifi:
        ant = json.load(archivo_wifi)
    ejecuciones_restantes = ant[-1]["Ejecuciones restantes"]
    SearchAfter = ant[-1]["SearchAfter"]
    loc_wifis = network.search(latrange1=municipio.limite[0], latrange2=municipio.limite[1],longrange1=municipio.limite[2], longrange2=municipio.limite[3], searchAfter=SearchAfter)
    cont_datos = loc_wifis["resultCount"]
    for data in range(cont_datos):
        trilat = loc_wifis["results"][data]["trilat"]
        trilong = loc_wifis["results"][data]["trilong"]
        coor_wifi = [trilong, trilat]
        coor_valida = coordenada_valida(coor_wifi, municipio)
        if coor_valida:
            if loc_wifis["results"][data]["city"] == municipio.id or loc_wifis["results"][data]["city"] is None:
                guardar_datos_dict(loc_wifis, data,lista_wifi)
                lista_json.append(loc_wifis["results"][data])
                wifis += 1
                print("Wifi valida numero", wifis)
        else:
            pass
    SearchAfter = loc_wifis["search_after"]
    print(loc_wifis)
    cont += 1
    print(cont)

    total_wifis = loc_wifis["totalResults"]
    n = math.ceil((total_wifis) / 100)
    ejecuciones_totales = ant[-1]["Ejecuciones Totales"]
    ejecuciones_restantes -= 1
    ejecuciones_actuales = ant[-1]["Ejecuciones actuales"]
    print(f"Se llevan realizadas {ejecuciones_actuales} actualmente")
    print(f"Las ejecuciones totales son {ejecuciones_totales}")
    print(f"Quedan por ejecutar {ejecuciones_restantes}")
    if n > ejecuciones_totales:
        ejecuciones_totales = n
        ejecuciones_restantes = ejecuciones_totales - (ejecuciones_actuales + 1)
        print(f"Se han cambiado las ejecuciones totales a {ejecuciones_totales}")
        print(f"Se han cambiado las ejecuciones restantes a {ejecuciones_restantes}")
    for i in range(ejecuciones_restantes):
        try:
            loc_wifis = network.search(latrange1=municipio.limite[0], latrange2=municipio.limite[1], longrange1=municipio.limite[2], longrange2=municipio.limite[3],searchAfter=SearchAfter)
        except requests.exceptions.HTTPError:
            print("Todavia no se ha analizado todo el municipio, quedan", ejecuciones_restantes - cont + 1, "ejecuciones")
            guardar_datos_wifis_csv_search_after(municipio,lista_wifi)
            guardar_datos_wifis_json_search_after(municipio,lista_json)
            ejecuciones_actuales += cont
            dict_datos = {"Municipio": municipio.id, "Ejecuciones Totales": ejecuciones_totales,
                          "Ejecuciones actuales": ejecuciones_actuales,
                          "Ejecuciones restantes": ejecuciones_totales - ejecuciones_actuales,"Ejecuciones realizadas hoy": cont,
                          "SearchAfter": SearchAfter, "Dia": len(ant) + 1}
            ant.append(dict_datos)
            with open(nombre_archivo_wifi, "w", encoding="windows-1252") as archivo_wifi:
                json.dump(ant, archivo_wifi)
            print(dict_datos)
            return dict_datos
        cont_datos = loc_wifis["resultCount"]
        for data in range(cont_datos):
            trilat = loc_wifis["results"][data]["trilat"]
            trilong = loc_wifis["results"][data]["trilong"]
            coor_wifi = [trilong, trilat]
            coor_valida = coordenada_valida(coor_wifi, municipio)
            if coor_valida:
                if loc_wifis["results"][data]["city"] == municipio.id or loc_wifis["results"][data]["city"] is None:
                    guardar_datos_dict(loc_wifis, data,lista_wifi)
                    lista_json.append(loc_wifis["results"][data])
                    wifis += 1
                    print("Wifi valida numero", wifis)
            else:
                pass
        SearchAfter = loc_wifis["search_after"]
        print(loc_wifis)
        cont+=1
        print(cont)

    guardar_datos_wifis_csv_search_after(municipio,lista_wifi)
def coordenada_valida(coor,municipio):
    """Sirve para ver si el punto que se analiza esta dentro del area del municipio o no"""
    lista_poligs = []
    for i in municipio.poligono:
        for m in i:
            lista_poligs.append(Polygon(m))
    poligono_mun = MultiPolygon(lista_poligs)
    punto = Point(coor[0],coor[1])
    valida = poligono_mun.contains(punto)
    if valida:
        print("El punto ",coor,"se encuentra dentro del municipio:")
    else:
        print("El punto ",coor,"no se encuentra dentro del municipio:")
    return valida
def guardar_datos_dict(loc_wifis,data,lista_wifi):
    """Se guardan en el diccionario los atributos de cada wifi"""
    trilat = loc_wifis["results"][data]["trilat"]
    trilong = loc_wifis["results"][data]["trilong"]
    ssid = loc_wifis["results"][data]["ssid"]
    qos = loc_wifis["results"][data]["qos"]
    transid = loc_wifis["results"][data]["transid"]
    firsttime = loc_wifis["results"][data]["firsttime"]
    lasttime = loc_wifis["results"][data]["lasttime"]
    lastupdt = loc_wifis["results"][data]["lastupdt"]
    netid = loc_wifis["results"][data]["netid"]
    name = loc_wifis["results"][data]["name"]
    type = loc_wifis["results"][data]["type"]
    comment = loc_wifis["results"][data]["comment"]
    wep = loc_wifis["results"][data]["wep"]
    bcninterval = loc_wifis["results"][data]["bcninterval"]
    freenet = loc_wifis["results"][data]["freenet"]
    dhcp = loc_wifis["results"][data]["dhcp"]
    paynet = loc_wifis["results"][data]["paynet"]
    userfound = loc_wifis["results"][data]["userfound"]
    channel = loc_wifis["results"][data]["channel"]
    encryption = loc_wifis["results"][data]["encryption"]
    country = loc_wifis["results"][data]["country"]
    region = loc_wifis["results"][data]["region"]
    city = loc_wifis["results"][data]["city"]
    housenumber = loc_wifis["results"][data]["housenumber"]
    road = loc_wifis["results"][data]["road"]
    postalcode = loc_wifis["results"][data]["postalcode"]
    lista_wifi["trilat"].append(trilat)
    lista_wifi["trilong"].append(trilong)
    lista_wifi["ssid"].append(ssid)
    lista_wifi["qos"].append(qos)
    lista_wifi["transid"].append(transid)
    lista_wifi["firsttime"].append(firsttime)
    lista_wifi["lasttime"].append(lasttime)
    lista_wifi["lastupdt"].append(lastupdt)
    lista_wifi["netid"].append(netid)
    lista_wifi["name"].append(name)
    lista_wifi["type"].append(type)
    lista_wifi["comment"].append(comment)
    lista_wifi["wep"].append(wep)
    lista_wifi["bcninterval"].append(bcninterval)
    lista_wifi["freenet"].append(freenet)
    lista_wifi["dhcp"].append(dhcp)
    lista_wifi["paynet"].append(paynet)
    lista_wifi["userfound"].append(userfound)
    lista_wifi["channel"].append(channel)
    lista_wifi["encryption"].append(encryption)
    lista_wifi["country"].append(country)
    lista_wifi["region"].append(region)
    lista_wifi["city"].append(city)
    lista_wifi["housenumber"].append(housenumber)
    lista_wifi["road"].append(road)
    lista_wifi["postalcode"].append(postalcode)

def crear_directorio(directorio):
    try:
        os.mkdir(directorio)
    except OSError:
        print(f"La carpeta {directorio} ya existe")
    return directorio

def guardar_datos_wifis_csv(municipio,lista_wifi):
    directorio = f"{municipio.pertenece_a}"
    crear_directorio(directorio)
    nombre_directorio_or = f"{directorio}/original"
    crear_directorio(nombre_directorio_or)
    nombre_directorio = f"{nombre_directorio_or}/csv"
    crear_directorio(nombre_directorio)
    nombre_archivo_wifi = f"{nombre_directorio}/{municipio.id}_wifi.csv"
    archivo_wifi = pd.DataFrame(lista_wifi, columns= ["trilat","trilong","ssid","qos","transid","firsttime","lasttime",
    "lastupdt","netid","name","type","comment","wep","bcninterval","freenet","dhcp","paynet","userfound","channel",
    "encryption","country","region","city","housenumber","road","postalcode"])
    archivo_wifi.to_csv(nombre_archivo_wifi,index=False)
    return archivo_wifi

def guardar_datos_wifis_csv_search_after(municipio,lista_wifi):
    nombre_directorio_or = f"{municipio.pertenece_a}/original"
    nombre_directorio = f"{nombre_directorio_or}/csv"
    nombre_archivo_wifi = f"{nombre_directorio}/{municipio.id}_wifi.csv"
    archivo_wifi = pd.read_csv(nombre_archivo_wifi)
    datos_nuevos = pd.DataFrame(lista_wifi,columns=["trilat", "trilong", "ssid", "qos", "transid", "firsttime", "lasttime",
    "lastupdt", "netid", "name", "type", "comment", "wep", "bcninterval","freenet", "dhcp", "paynet", "userfound","channel",
    "encryption", "country", "region", "city", "housenumber", "road","postalcode"])
    archivo = pd.concat([archivo_wifi,datos_nuevos],ignore_index=True)
    archivo.to_csv(nombre_archivo_wifi,index=False)

def guardar_datos_wifis_json(municipio,lista_json):
    directorio = f"{municipio.pertenece_a}"
    crear_directorio(directorio)
    nombre_directorio_or = f"{directorio}/original"
    crear_directorio(nombre_directorio_or)
    nombre_directorio = f"{nombre_directorio_or}/json"
    crear_directorio(nombre_directorio)
    nombre_archivo_wifi = f"{nombre_directorio}/{municipio.id}_wifi.json"
    with open(nombre_archivo_wifi,"w",encoding="windows-1252") as archivo_wifi:
        json.dump(lista_json,archivo_wifi)

    return archivo_wifi

def guardar_datos_wifis_json_search_after(municipio,lista_json):
    nombre_directorio_or = f"{municipio.pertenece_a}/original"
    nombre_directorio = f"{nombre_directorio_or}/json"
    crear_directorio(nombre_directorio)
    nombre_archivo_wifi = f"{nombre_directorio}/{municipio.id}_wifi.json"
    with open(nombre_archivo_wifi,encoding="windows-1252") as archivo_wifi:
        ant = json.load(archivo_wifi)
    for dicc in lista_json:
        ant.append(dicc)
    with open(nombre_archivo_wifi,"w", encoding="windows-1252") as archivo_wifi:
        json.dump(ant, archivo_wifi)

    return archivo_wifi

def comprobar_archivo(municipio_id,archivo1):
    archivo = pd.read_excel("Coordenadas-mun-todas.xlsx")
    if municipio_id in archivo.poblacion.values and municipio_id in archivo1.Municipio.values:
        return True
    else:
        return False
def limite_municipio(municipio_id):
    archivo = pd.read_excel("Coordenadas-mun-todas.xlsx")
    archivo1 = pd.read_excel("elecciones_madrid - copia.xls",sheet_name="Municipios")
    comprobar_mun = comprobar_archivo(municipio_id,archivo1)
    if comprobar_mun:
        poblacion = archivo.index[archivo["poblacion"] == municipio_id].tolist()
        limite = archivo["coordinates"].values[poblacion[0]]
        lista_limite = []
        antes = 0
        numero = ''
        cont = 0

        for i in limite:
            if (antes == ',' and i == '0') or i == "#":
                pass
            elif i == ',':
                if cont % 2 == 0:
                    lista_limite.append([])
                lista_limite[-1].append(float(numero))
                numero = ''
                cont += 1
                antes = i
            else:
                numero += i
                antes = i
        return lista_limite
    else:
        return comprobar_mun
def poligono_municipio(municipio_id):
    index_mun = False
    for i in range(len(archivo_limite_muns["features"])):
        if archivo_limite_muns["features"][i]["properties"]["NAMEUNIT"].lower() == municipio_id.lower():
            index_mun = i
            break
    if index_mun is not False:
        mun = archivo_limite_muns["features"][index_mun]["geometry"]["coordinates"]
        return mun
    else:
        return index_mun
def coordenadas_limite_municipio(lista_limite):
    """Devuelve una lista con los puntos extremos de cada eje de coordenadas"""
    lat1 = 10000000000
    lat2 = -1000000000
    long1 = 1000000000
    long2 = -1000000000
    for i in lista_limite:
        for m in i:
            for j in m:
                if j[0] > long2:
                    long2 = j[0]
                if j[0] < long1:
                    long1 = j[0]
                if j[1] > lat2:
                    lat2 = j[1]
                if j[1] < lat1:
                    lat1 = j[1]
    lista_coor = [lat1,lat2,long1,long2]
    return lista_coor

def analizar_coste_ciudad(ciudad):
    """Esta funcion devuelve un archivo csv con el tiempo estimado, ejecuciones de la api y el numero de wifis totales
    de cada municipio de la ciudad"""
    crear_directorio("analisis_coste_ciudades")
    cont = 0
    dias = 0
    wifis_totales = 0
    lista_mun = []
    limite_api = 500
    dic = {"Municipio":[],"Dias":[],"Ejecuciones":[],"Wifis":[]}
    for i in ciudad.municipios:
        lista_limite = poligono_municipio(i.id)
        if not isinstance(lista_limite,bool):
            coor = coordenadas_limite_municipio(lista_limite)
            loc_wifis = network.search(latrange1=coor[0], latrange2=coor[1],
                                       longrange1=coor[2], longrange2=coor[3])
            print(loc_wifis)
            #cont_wifis
            wifis = loc_wifis["totalResults"]
            wifis_totales += wifis
            #ejecuciones
            ejecuciones = math.ceil(wifis / 100)
            cont += ejecuciones

            #dias
            dias_mun = ejecuciones / limite_api
            dias += dias_mun
            #dict
            dic["Municipio"].append(i.id)
            dic["Dias"].append(dias_mun)
            dic["Ejecuciones"].append(ejecuciones)
            dic["Wifis"].append(wifis)

            dic_mun = {f"{i.id}": {"Dias": dias_mun,"Ejecuciones":ejecuciones,"Wifis":wifis}}
            print(dic_mun)
            lista_mun.append(dic_mun)
            print("Dias Totales",dias,"Ejecuciones Totales",cont,"Wifis Totales",wifis_totales)
        else:
            pass
    dic["Municipio"].append("Total")
    dic["Dias"].append(dias)
    dic["Ejecuciones"].append(cont)
    dic["Wifis"].append(wifis_totales)
    dic_mun = {"Total": {"Dias":dias, "Ejecuciones":cont, "Wifis":wifis_totales}}
    lista_mun.append(dic_mun)

    directorio = "analisis_coste_ciudades"
    crear_directorio(directorio)
    directorio_csv = f"{directorio}/csv"
    crear_directorio(directorio_csv)
    directorio_json = f"{directorio}/json"
    crear_directorio(directorio_json)
    archivo = f"{directorio_json}/analisis_coste_{ciudad.id}.json"
    with open(archivo,"w",encoding="windows-1252") as archivo_wifi:
        json.dump(lista_mun,archivo_wifi)
    csv = f"{directorio_csv}/analisis_coste_{ciudad.id}.csv"
    archivo1 = pd.DataFrame(dic,columns=["Municipio","Dias","Ejecuciones","Wifis"])
    archivo1.to_csv(csv,index=False)

def sanitizar_mun(municipio,lista_datos = ["transid","name","type","comment","wep","bcninterval","userfound","housenumber"]):
    """Funcion que elimina aquellas wifis repetidas, o que tengan el ssid vacio"""
    existe = True
    nombre_directorio_or = f"{municipio.pertenece_a}/original"
    nombre_directorio = f"{nombre_directorio_or}/csv"
    nombre_archivo_wifi = f"{nombre_directorio}/{municipio.id}_wifi.csv"
    try:
        archivo = pd.read_csv(nombre_archivo_wifi)
    except OSError:
        existe = False
        print(f"No se ha analizado el municipio de {municipio.id} todavia")
    if existe:
        archivo = archivo.drop(lista_datos,axis = 1)
        ssid_null = archivo.ssid.isnull()
        anterior = None
        long = len(archivo)
        eliminados = []
        for i in range(long):
            if ssid_null[i]:
                eliminados.append(i)
            if isinstance(archivo.ssid[i],str):
                eliminado = False
                if anterior == archivo.ssid[i]:
                    eliminados.append(i)
                    eliminado = True

                if "5g" in archivo.ssid[i].lower() and anterior is not None and not eliminado:
                    if anterior in archivo.ssid[i]:
                        eliminados.append(i)
                        eliminado = True

                if "_plus" in archivo.ssid[i].lower() and not eliminado:
                    char = "_plus"
                    string = archivo.ssid[i].lower()
                    string = string.replace(char,"")
                    if string == anterior.lower():
                        eliminados.append(i)
                        eliminado = True

                if "-plus" in archivo.ssid[i].lower() and not eliminado:
                    char = "-plus"
                    string = archivo.ssid[i].lower()
                    string = string.replace(char,"")
                    if string == anterior.lower():
                        eliminados.append(i)
                        eliminado = True

                if i > 0 and anterior is not None:
                    if "_plus" in anterior.lower() and not eliminado:
                        char = "_plus" #hay que tener en cuenta -plus
                        string = anterior.lower()
                        string = string.replace(char,"")
                        if string == archivo.ssid[i].lower():
                            eliminados.append(i-1)
                            eliminado = True

                    if "-plus" in anterior.lower() and not eliminado:
                        char = "-plus" #hay que tener en cuenta -plus
                        string = anterior.lower()
                        string = string.replace(char,"")
                        if string == archivo.ssid[i].lower():
                            eliminados.append(i-1)
                            eliminado = True

                anterior = archivo.ssid[i]

        archivo.drop(index=eliminados,inplace=True)
        archivo.reset_index(drop=True,inplace=True)
        nombre_directorio_or = f"{municipio.pertenece_a}/sanitizada"
        crear_directorio(nombre_directorio_or)
        nombre_directorio = f"{nombre_directorio_or}/csv"
        crear_directorio(nombre_directorio)
        nombre_archivo_sanitizada = f"{nombre_directorio}/{municipio.id}_wifi.csv"
        archivo.to_csv(nombre_archivo_sanitizada,index= False)

def sanitizar_ciudad(ciudad):
    """Funcion que sanitiza toda la ciudad"""
    for i in ciudad.municipios:
        print("Se va a sanitizar",i.id)
        sanitizar_mun(i)
        print(f"{i.id} sanitizado")

def clasificador_wifis(mun):
    csv = f"{mun.pertenece_a}/sanitizada/csv/{mun.id}_wifi.csv"
    archivo = pd.read_csv(csv)
    Movistar = []
    Orange = []
    Vodafone = []
    Digi = []
    for i in range(len(archivo)):
        if isinstance(archivo["ssid"][i],str):
            if "movistar" in archivo["ssid"][i].lower():
                Movistar.append([archivo["ssid"][i],archivo["trilong"],archivo["trilat"]])
                print("La red",archivo["ssid"][i],"pertenece a Movistar")
            if "orange" in archivo["ssid"][i].lower():
                Orange.append([archivo["ssid"][i],archivo["trilong"],archivo["trilat"]])
                print("La red",archivo["ssid"][i],"pertenece a Orange")
            if "vodafone" in archivo["ssid"][i].lower() or "mifibra" in archivo["ssid"][i].lower():
                Vodafone.append([archivo["ssid"][i],archivo["trilong"],archivo["trilat"]])
                print("La red",archivo["ssid"][i],"pertenece a Vodafone")
            if "digi" in archivo["ssid"][i].lower():
                Digi.append([archivo["ssid"][i],archivo["trilong"],archivo["trilat"]])
                print("La red",archivo["ssid"][i],"pertenece a Digi")
    dic = {"Movistar":len(Movistar),"Orange":len(Orange),"Vodafone":len(Vodafone),"Digi":len(Digi)}
    return dic

def elegir_muns_wifis(ciudad):
    """Funcion para elegir los municipios que se hayan analizado"""
    muns_validos = []
    for i in ciudad.municipios:
        existe = True
        try:
            archivo = pd.read_csv(f"{ciudad.id}/sanitizada/csv/{i.id}_wifi.csv")
        except OSError:
            existe = False
        if existe:
            muns_validos.append(i.id)
    return muns_validos

def elegir_muns_votos(ciudad):
    "Funcion para elegir los municipios con mas de 1000 votos"
    min_votos = 1000
    muns_validos = []
    for i in ciudad.municipios:
        if i.votos >= min_votos:
            muns_validos.append(i.id)
    return muns_validos

def elegir_muns(ciudad):
    """Funcion final que tiene todos los municipios validos"""
    muns_wifis = elegir_muns_wifis(ciudad)
    muns_votos = elegir_muns_votos(ciudad)
    muns_elegidos = []
    for i in muns_wifis:
        if i in muns_votos:
            muns_elegidos.append(i)
    return muns_elegidos

def guardar_datos_clasificador(dic_wifis,archivo,i,operador,municipio,tipo,dispositivo):
    """Guarda los datos de cada wifi en el diccionario"""
    dic_wifis["ssid"].append(archivo["ssid"][i])
    dic_wifis["netid"].append(archivo["netid"][i])
    dic_wifis["municipio"].append(municipio.id)
    dic_wifis["operador"].append(operador)
    dic_wifis["tipo"].append(tipo)
    dic_wifis["dispositivo"].append(dispositivo)

def clasificador_mun_todo_agrupando(municipio,inicio,fin,mes_fin,dic_wifis,mes_inicio):
    """Funcion final en la que se agrupan todas las wifis del municipio"""
    nombre_directorio_or = f"{municipio.pertenece_a}/sanitizada"
    nombre_directorio = f"{nombre_directorio_or}/csv"
    nombre_archivo_wifi = f"{nombre_directorio}/{municipio.id}_wifi.csv"
    existe = True
    try:
        archivo_wifi = pd.read_csv(nombre_archivo_wifi)
    except OSError:
        existe = False
        print(f"No se ha analizado el municipio de {municipio.id} todavia")
        return dic_wifis
    if existe:
        archivo = wifis_rango(municipio,mes_inicio,mes_fin,inicio,fin)
        index_archivo = archivo.index
        min_wifis = 100
        if len(index_archivo) < min_wifis:
            return dic_wifis
        else:
            lista_coche = ["coche","audi","alsa","renault","sanlorenzo"]
            lista_moviles = ["android","iphone","samsung","huawei","xiaomi","oneplus","sony","oppo","motorola","realme","poco","galaxy"]
            lista_impresoras = ["canon","epson","brother","envy","direct","print"]
            datos_ssid = pd.read_excel("Router passwords.xlsx")
            Movistar = []
            Orange = []
            Vodafone = []
            Digi = []
            MasMovil = []
            dudas = []
            desconocido = []
            dispositivo = []
            for i in index_archivo:
                asignado = False
                operador = False
                netid = archivo["netid"][i][0:8]
                filtro = datos_ssid[datos_ssid["BSSID"].str.contains(netid,na=False)]
                operadoras = filtro["ISP"].unique().tolist()
                for j in range(len(operadoras)):
                    operadoras[j] = operadoras[j].lower()
                if isinstance(archivo["ssid"][i], str):
                    for coche in lista_coche:
                        if coche in archivo["ssid"][i].lower():
                            dispositivo.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                            guardar_datos_clasificador(dic_wifis, archivo, i, "DESCONOCIDO", municipio,"DISPOSITIVO","COCHE")
                            asignado = True
                            break
                    for imprenta in lista_impresoras:
                        if imprenta in archivo["ssid"][i].lower():
                            dispositivo.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                            guardar_datos_clasificador(dic_wifis, archivo, i, "DESCONOCIDO", municipio,"DISPOSITIVO","IMPRESORA")
                            asignado = True
                            break

                    for movil in lista_moviles:
                        if movil in archivo["ssid"][i].lower():
                            dispositivo.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                            guardar_datos_clasificador(dic_wifis, archivo, i, "DESCONOCIDO", municipio,"DISPOSITIVO","MOVIL")
                            asignado = True
                            break
                    if "eduroam" in archivo["ssid"][i].lower():
                        dispositivo.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                        guardar_datos_clasificador(dic_wifis, archivo, i, "DESCONOCIDO", municipio, "DISPOSITIVO","EDUROAM")
                        asignado = True
                    if len(archivo["ssid"][i].lower()) >= 3:
                        if "chromecast" in archivo["ssid"][i].lower() or ".v" in archivo["ssid"][i][-3:].lower() or ".o" in archivo["ssid"][i][-3:].lower() \
                                or ".m" in archivo["ssid"][i][-3:].lower() or ".b" in archivo["ssid"][i][-3:].lower() or ".k" in archivo["ssid"][i][-3:].lower():
                            dispositivo.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                            guardar_datos_clasificador(dic_wifis, archivo, i, "DESCONOCIDO", municipio, "DISPOSITIVO","CHROMECAST")
                            asignado = True
                    if not asignado:
                        if "movistar" in archivo["ssid"][i].lower() or "wlan" in archivo["ssid"][i].lower():
                            guardar_datos_clasificador(dic_wifis, archivo, i, "MOVISTAR", municipio,"OPERADOR","NINGUNO")
                            Movistar.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                            asignado = True
                        if "orange" in archivo["ssid"][i].lower() or "jazztel" in archivo["ssid"][i].lower():
                            guardar_datos_clasificador(dic_wifis, archivo, i, "ORANGE", municipio,"OPERADOR","NINGUNO")
                            Orange.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                            asignado = True
                        if "vodafone" in archivo["ssid"][i].lower() or "ono" in archivo["ssid"][i].lower() or "lowi" in archivo["ssid"][i].lower():
                            guardar_datos_clasificador(dic_wifis, archivo, i, "VODAFONE", municipio,"OPERADOR","NINGUNO")
                            Vodafone.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                            asignado = True
                        if "digi" in archivo["ssid"][i].lower():
                            guardar_datos_clasificador(dic_wifis, archivo, i, "DIGI", municipio,"OPERADOR","NINGUNO")
                            Digi.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                            asignado = True
                        if "masmovil" in archivo["ssid"][i].lower() or "yoigo" in archivo["ssid"][i].lower() or "pepephone" in archivo["ssid"][i].lower() :
                            guardar_datos_clasificador(dic_wifis, archivo, i, "MASMOVIL", municipio,"OPERADOR","NINGUNO")
                            MasMovil.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                            asignado = True
                        if not asignado:
                            if len(operadoras) == 1 and "movistar" in operadoras:
                                guardar_datos_clasificador(dic_wifis, archivo, i, "MOVISTAR", municipio, "OPERADOR","NINGUNO")
                                Movistar.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                                operador = True
                            if (len(operadoras) == 1 and "orange" in operadoras) or (len(operadoras) == 1 and "jazztel" in operadoras) or \
                                ("mifibra" in archivo["ssid"][i].lower() or "livebox" in archivo["ssid"][i].lower() \
                                or "flybox" in archivo["ssid"][i].lower()):
                                guardar_datos_clasificador(dic_wifis, archivo, i, "ORANGE", municipio,"OPERADOR","NINGUNO")
                                Orange.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                                operador = True
                            if (len(operadoras) == 1 and "vodafone" in operadoras) or (len(operadoras) == 1 and "ono" in operadoras) or \
                                (len(operadoras) == 1 and "lowi" in operadoras):
                                guardar_datos_clasificador(dic_wifis, archivo, i, "VODAFONE", municipio,"OPERADOR","NINGUNO")
                                Vodafone.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                                operador = True
                            if (len(operadoras) == 1 and "digi" in operadoras):
                                guardar_datos_clasificador(dic_wifis, archivo, i, "DIGI", municipio,"OPERADOR","NINGUNO")
                                Digi.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                                operador = True
                            if (len(operadoras) == 1 and "masmovil" in operadoras) or (len(operadoras) == 1 and "yoigo" in operadoras) or \
                                    (len(operadoras) == 1 and "pepephone" in operadoras):
                                guardar_datos_clasificador(dic_wifis, archivo, i, "MASMOVIL", municipio,"OPERADOR","NINGUNO")
                                MasMovil.append([archivo["ssid"][i], archivo["trilong"], archivo["trilat"]])
                                operador = True
                            if not operador:
                                if "miwifi" in archivo["ssid"][i].lower():
                                    operadoras = ["masmovil","orange"]
                                if len(operadoras) == 0:
                                    guardar_datos_clasificador(dic_wifis,archivo,i,"DESCONOCIDO",municipio,"DESCONOCIDO","NINGUNO")
                                    desconocido.append([archivo["ssid"][i],archivo["trilong"],archivo["trilat"]])

                                if len(operadoras) > 1:
                                    dic_dudas = {"Operador posible":operadoras,"Wifi":archivo["ssid"][i]}
                                    guardar_datos_clasificador(dic_wifis,archivo,i,"DUDA",municipio,"DUDA","NINGUNO")
                                    dudas.append(dic_dudas)
            dic = {"Movistar":len(Movistar),"Orange":len(Orange),"Vodafone":len(Vodafone),"Digi":len(Digi),
            "MasMovil":len(MasMovil),"Dispositivos":len(dispositivo),"Dudas":len(dudas),"Desconocido":len(desconocido)}
            #QUEDA GUARDAR ESTO COMO DATAFRAME
            print(dic)
            return dic_wifis

def clasificador_ciudad_elegidos_todo_agrupando(ciudad,inicio,fin,mes_fin = 4,mes_inicio = 1):
    dic_wifis = {"ssid":[],"netid":[],"municipio":[],"tipo":[],"operador":[],"dispositivo":[]}
    lista = elegir_muns(ciudad)
    for i in lista:
        print("Voy a clasificar las wifis de",i)
        municipio = ciudad.buscar_municipio(i)
        clasif_mun = clasificador_mun_todo_agrupando(municipio,inicio,fin,mes_fin,dic_wifis,mes_inicio)
        dic_wifis = clasif_mun
        print(f"{municipio.id} clasificado")
    dir = f"{ciudad.id}/clasificador"
    crear_directorio(dir)
    archivo1 = pd.DataFrame(dic_wifis,columns=["ssid","netid","municipio","tipo","operador","dispositivo"])
    nombre_archivo_clasif = f"{dir}/{ciudad.id}_clasificador_elegidos_todo_agrupando{mes_inicio}-{inicio}_{mes_fin}-{fin}.csv"
    archivo1.to_csv(nombre_archivo_clasif,index=False)
    return nombre_archivo_clasif
def columna_to_datetime(municipio):
    """Convierte el valor de las columnas de fecha en datetime para poder operar"""
    nombre_archivo = f"{municipio.pertenece_a}/sanitizada/csv/{municipio.id}_wifi.csv"
    archivo = pd.read_csv(nombre_archivo)
    modificado = False
    for i in range(len(archivo)):
        if isinstance(archivo.firsttime[i],str) and ("T" and "Z" in archivo.firsttime[i]):
            archivo.firsttime[i] = parser.parse(archivo.firsttime[i][:-2])
            modificado = True
        if isinstance(archivo.lasttime[i],str) and ("T" and "Z" in archivo.lasttime[i]):
            archivo.lasttime[i] = parser.parse(archivo.lasttime[i][:-2])
            modificado = True
        if isinstance(archivo.lastupdt[i],str) and ("T" and "Z" in archivo.lastupdt[i]):
            archivo.lastupdt[i] = parser.parse(archivo.lastupdt[i][:-2])
            modificado = True
    if modificado:
        archivo.to_csv(nombre_archivo,index=False)

def wifis_rango(municipio,mes_inicio,mes_fin,inicio=2001,fin=2023):
    """Agrupa las wifis del municipio en un rango de tiempo"""
    columna_to_datetime(municipio)
    nombre_archivo = f"{municipio.pertenece_a}/sanitizada/csv/{municipio.id}_wifi.csv"
    archivo = pd.read_csv(nombre_archivo)
    if mes_fin == 12:
        filtrado = archivo.loc[((archivo["lasttime"] >= f"{fin+1}-01-01") | (archivo["lasttime"] == archivo["lastupdt"])) & (archivo["firsttime"] < f"{fin+1}-01-01") & (archivo["firsttime"] >= f"{inicio}-{mes_inicio}-00")]
    else:
        filtrado = archivo.loc[((archivo["lasttime"] >= f"{fin}-{mes_fin+1}-01") | (archivo["lasttime"] == archivo["lastupdt"])) & (archivo["firsttime"] < f"{fin}-{mes_fin+1}-01") & (archivo["firsttime"] >= f"{inicio}-{mes_inicio}-00")]

    return filtrado

def clasificador_renta(archivo_nombre,ciudad):
    """Añade al clasificador la renta neta media de cada municipio"""
    archivo = pd.read_csv(archivo_nombre)
    renta_media = pd.read_excel("renta_media_madrid_2019.xlsx")
    lista_renta = []
    for i in range(len(archivo)):
        mun = archivo.municipio[i]
        municipio = ciudad.buscar_municipio(mun)
        filtro = renta_media[renta_media["Municipios"].str.contains(municipio.codigo_ine)]
        lista_renta.append(filtro["Total"].values[0])
    archivo = archivo.assign(renta=lista_renta)
    print(archivo)
    archivo.to_csv(archivo_nombre, index=False)

def clasificador_elecciones(archivo_nombre,ciudad,year):
    """Añade al clasificador los resultados electorales de cada municipio"""
    archivo = pd.read_csv(archivo_nombre)
    if year == 2019:
        datos_electoral_ciudad = pd.read_excel("elecciones_madrid_2019.xlsx")
    if year == 2023:
        datos_electoral_ciudad = pd.read_excel("elecciones_madrid_2023.xlsx")
    tratar_datos(datos_electoral_ciudad,ciudad)
    lista_elecciones = []
    for i in range(len(archivo)):
        mun = archivo.municipio[i]
        municipio = ciudad.buscar_municipio(mun)
        result = municipio.lado_ganador()
        lista_elecciones.append(result)
    archivo = archivo.assign(partido_ganador=lista_elecciones)
    print(archivo)
    archivo.to_csv(archivo_nombre,index=False)














