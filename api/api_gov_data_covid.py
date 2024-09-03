import pandas as pd
from sodapy import Socrata


def extraccion_datos_api (nombre_departamento, limite_registros):
    # Unauthenticated client only works with public data sets . Note 'None '
    # in place of application token , and no username or password :
    client = Socrata("www.datos.gov.co", None)

    results = client.get("gt2j-8ykr", limit=limite_registros, departamento_nom=nombre_departamento )
    lista_datos_requeridos = ["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio", "estado", "unidad_medida"]

    # convierte a biblioteca y lo devuelve
    return pd.DataFrame.from_records(results)[lista_datos_requeridos]