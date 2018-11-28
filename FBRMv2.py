
# SUBMIT BUTTON : ctl00$BBuscar #

URL = "https://www.fbrm.org/competicion-327/competiciones-fbrm.aspx"

EQUIPOS = {
    'SENIOR': {
        "__EVENTTARGET": '',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": '',
        "__VIEWSTATEGENERATOR": '',
        "__EVENTVALIDATION": '',
        "ctl00$TBBusquedaCab": '',
        "ctl00$contenedor_informacion$DDLCategorias": '',
        "ctl00$contenedor_informacion$DDLFases": '',
        "ctl00$contenedor_informacion$DDLGrupos": ''
    },
    'JUNIOR': {
        "__EVENTTARGET": '',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": '',
        "__VIEWSTATEGENERATOR": '',
        "__EVENTVALIDATION": '',
        "ctl00$TBBusquedaCab": '',
        "ctl00$contenedor_informacion$DDLCategorias": '',
        "ctl00$contenedor_informacion$DDLFases": '',
        "ctl00$contenedor_informacion$DDLGrupos": ''
    },
    'CADETE': {
        "__EVENTTARGET": '',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": '',
        "__VIEWSTATEGENERATOR": '',
        "__EVENTVALIDATION": '',
        "ctl00$TBBusquedaCab": '',
        "ctl00$contenedor_informacion$DDLCategorias": '',
        "ctl00$contenedor_informacion$DDLFases": '',
        "ctl00$contenedor_informacion$DDLGrupos": ''
    },
    'INFANTIL': {
        "__EVENTTARGET": '',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": '',
        "__VIEWSTATEGENERATOR": '',
        "__EVENTVALIDATION": '',
        "ctl00$TBBusquedaCab": '',
        "ctl00$contenedor_informacion$DDLCategorias": '',
        "ctl00$contenedor_informacion$DDLFases": '',
        "ctl00$contenedor_informacion$DDLGrupos": ''
    },
    'ALEVIN': {
        "__EVENTTARGET": '',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": '',
        "__VIEWSTATEGENERATOR": '',
        "__EVENTVALIDATION": '',
        "ctl00$TBBusquedaCab": '',
        "ctl00$contenedor_informacion$DDLCategorias": '',
        "ctl00$contenedor_informacion$DDLFases": '',
        "ctl00$contenedor_informacion$DDLGrupos": ''
    }
}


def resultados_y_proximos_partidos_HTML():
    pass


class ResultadoPartido():

    def __init__(self, equipo, jornada, equipo_local, equipo_visitante, resultado_local, resultado_visitante):
        self.equipo = equipo
        self.jornada = jornada
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.resultado_local = resultado_local
        self.resultado_visitante = resultado_visitante

    def to_html(self):
        return('<tr><td>' + self.equipo + '</td><td>' + self.jornada + '</td><td>' + self.equipo_local + '</td><td>' +
               self.resultado_local + '</td><td>' + self.resultado_visitante + '</td><td>' + self.equipo_visitante +
               '</td></tr>')


class ProximoPartido():

    def __init__(self, equipo, equipo_local, equipo_visitante, fecha_partido, lugar_partido):
        self.equipo = equipo
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha_partido = fecha_partido
        self.lugar_partido = lugar_partido

    def to_html(self):
        return ('<tr><td>' + self.equipo + '</td><td>' + self.equipo_local + '</td><td>' + self.equipo_visitante +
                '</td><td>' + self.fecha_partido + '</td><td>' + self.lugar_partido + '</td></tr>')
