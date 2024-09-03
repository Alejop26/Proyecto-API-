from tabulate import tabulate

#solo admite bibliotecas
def impresion_datos_extraidos (results_df):

    print(tabulate(results_df, tablefmt="github", headers=["Número de registro", "Ciudad de ubicación","Departamento", "Edad", "Tipo", "Estado", "País de procedencia"]))