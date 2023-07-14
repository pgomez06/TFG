import pandas as pd
class Municipio:
    def __init__(self, nombre):
        self.id = nombre
        self.votos = 0
        self.psoe = 0
        self.pp = 0
        self.cs = 0
        self.podemos = 0
        self.vox = 0
        self.mas_madrid = 0
        self.derecha = 0
        self.izquierda = 0
        self.precio_m2 = 0
        self.limite = None
        self.poligono = None
        self.pertenece_a = None
        self.codigo_ine = None
        self.wifis = {"trilat":[],"trilong":[],"ssid":[],"qos":[],"transid":[],"firsttime":[],"lasttime":[],
        "lastupdt":[],"netid":[],"name":[],"type":[],"comment":[],"wep":[],"bcninterval":[],"freenet":[],"dhcp":[],
        "paynet":[],"userfound":[],"channel":[],"encryption":[],"country":[],"region":[],"city":[],"housenumber":[],
        "road":[],"postalcode":[]}

    def porcentaje_votos(self,votos_partido,votos_totales):
        porcentaje = votos_partido / votos_totales
        return porcentaje
    def porcentaje_votos_partido(self,partido):
        if partido.lower() == "pp":
            return self.porcentaje_votos_pp()
        if partido.lower() == "psoe":
            return self.porcentaje_votos_psoe()
        if partido.lower() == "podemos":
            return self.porcentaje_votos_podemos()
        if partido.lower() == "cs":
            return self.porcentaje_votos_cs()
        if partido.lower() == "vox":
            return self.porcentaje_votos_vox()
        if partido.lower() == "más madrid":
            return self.porcentaje_votos_mas_madrid()
    def votos_partido(self,partido):
        if partido.lower() == "pp":
            return self.pp
        if partido.lower() == "psoe":
            return self.psoe
        if partido.lower() == "podemos":
            return self.podemos
        if partido.lower() == "cs":
            return self.cs
        if partido.lower() == "vox":
            return self.vox
        if partido.lower() == "más madrid":
            return self.mas_madrid

    def porcentaje_votos_pp(self):
        porcentaje = self.pp / self.votos
        return porcentaje
    def porcentaje_votos_psoe(self):
        porcentaje = self.psoe / self.votos
        return porcentaje
    def porcentaje_votos_podemos(self):
        porcentaje = self.podemos / self.votos
        return porcentaje
    def porcentaje_votos_cs(self):
        porcentaje = self.cs / self.votos
        return porcentaje
    def porcentaje_votos_vox(self):
        porcentaje = self.vox / self.votos
        return porcentaje
    def porcentaje_votos_mas_madrid(self):
        porcentaje = self.mas_madrid / self.votos
        return porcentaje
    def porcentaje_votos_izq(self):
        porcentaje = self.izquierda / self.votos
        return porcentaje
    def porcentaje_votos_derecha(self):
        porcentaje = self.derecha / self.votos
        return porcentaje
    def lado_ganador(self):
        if self.derecha > self.izquierda:
            return "DERECHA"
        if self.izquierda > self.derecha:
            return "IZQUIERDA"
        if self.izquierda == self.derecha:
            return "NINGUNO"
class Provincia:
    def __init__(self, nombre):
        self.id = nombre
        self.votos = 0
        self.psoe = 0
        self.pp = 0
        self.cs = 0
        self.podemos = 0
        self.vox = 0
        self.mas_madrid = 0
        self.derecha = 0
        self.izquierda = 0
        self.precio_m2 = 0
        self.municipios = []

    def porcentaje_votos(self, votos_partido, votos_totales):
        porcentaje = votos_partido / votos_totales
        return porcentaje
    def porcentaje_votos_pp(self):
        porcentaje = self.pp / self.votos
        return porcentaje
    def porcentaje_votos_psoe(self):
        porcentaje = self.psoe / self.votos
        return porcentaje
    def porcentaje_votos_podemos(self):
        porcentaje = self.podemos / self.votos
        return porcentaje
    def porcentaje_votos_cs(self):
        porcentaje = self.cs / self.votos
        return porcentaje
    def porcentaje_votos_vox(self):
        porcentaje = self.vox / self.votos
        return porcentaje
    def porcentaje_votos_mas_madrid(self):
        porcentaje = self.mas_madrid / self.votos
        return porcentaje
    def precio_m2_media(self):
        for municipio in self.municipios:
            self.precio_m2 += municipio.precio_m2
        self.precio_m2 /= len(self.municipios)
    def porcentaje_votos_izq(self):
        porcentaje = self.izquierda / self.votos
        return porcentaje
    def porcentaje_votos_derecha(self):
        porcentaje = self.derecha / self.votos
        return porcentaje
    def lado_ganador(self):
        if self.derecha > self.izquierda:
            return "DERECHA"
        if self.izquierda > self.derecha:
            return "IZQUIERDA"
        if self.izquierda == self.derecha:
            return "NINGUNO"
    def buscar_municipio(self, municipio):
        for i in self.municipios:
            if i.id == municipio:
                return i
    """def analizar_coste_ciudad(self):
        for i in self.municipios:
            """

class Pais:
    def __init__(self,nombre):
        self.id = nombre
        self.ciudades = []
        ciu_mun_csv = pd.read_csv("MUNICIPIOS.csv", encoding='windows-1252', delimiter=';')
        for i in range(len(ciu_mun_csv)):
            prov = ciu_mun_csv["PROVINCIA"][i]
            mun = ciu_mun_csv["NOMBRE_ACTUAL"][i]
            municipio = Municipio(mun)
            municipio.pertenece_a = prov
            municipio.codigo_ine = str(ciu_mun_csv["COD_INE"][i])[:5]
            if len(self.ciudades) == 0:
                self.ciudades.append(Provincia(prov))
                self.ciudades[0].municipios.append(municipio)
            else:
                ciu_repe = False
                mun_repe = False
                for j in self.ciudades:
                    if j.id == prov:
                        ciu_repe = True
                        for m in j.municipios:
                            if mun == m.id:
                                mun_repe = True
                                break
                        if not mun_repe:
                            j.municipios.append(municipio)
                        break
                if not ciu_repe:
                    self.ciudades.append(Provincia(prov))
                    self.ciudades[-1].municipios.append(municipio)

    def buscar_ciudad(self,ciudad):
        for i in self.ciudades:
            if i.id == ciudad:
                return i
