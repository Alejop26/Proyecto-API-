from api import api_gov_data_covid as api
from ui import user_interface as ui
from comprobacion_datos import comprobacion_datos as cd

print("Proyecto Fundamentos Básicos de Python\n\n")

#se toman y se comprueban los datos de una sola vez
nombre_departamento = cd.comprobar_input_departamentos()
limite =  cd.comprobar_input_limite_datos()

#se filtran e imprimen los datos extraidos
libreria_datos_extraidos = api.extraccion_datos_api(nombre_departamento, limite)
ui.impresion_datos_extraidos(libreria_datos_extraidos)