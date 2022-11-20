#-------------------- TABLAS DE CONTINGENCIA: CLASIFICACIÓN DE DOS O MÁS VÍAS --------------------
#--------------- Amélie Bernès, Noviembre del 2022.

#- Librerías ----------------------

import numpy as np
from numpy import array
from tabulate import tabulate
import ast
from scipy.stats import chi2
import analisis_datosCat as analisis_ame

np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
def extraccion_data_tipo2(nombre):
    """
    Input es un archivo .txt (guardado en la misma carpeta que este script) llamado nombre.
    La primera fila contiene el valor alpha,
    las siguientes filas contienen los datos a analizar; pueden introducirse más de una fila.
    Se regresa un vector, TODO: actualizar. cuya primera entrada es r=cantidad de filas, la segunda es c= cantidad de columnas, y la tercera es un diccionario que contiene las filas; la llave de una fila es su número.
    """
    informacion=[]
    p=nombre
    r=-1 #inicializamos el contador de filas en -1, pues la primera fila del archivo de texto es la del valor alpha
    with open(p, "r") as f:
        for i in f.readlines():
            informacion.append(ast.literal_eval(i.strip()))
            r+=1
    alpha=informacion[0]
    c=len(informacion[1]) #c es la cantidad de columnas.
    celdas_observadas=[]
    for i in range(1,r+1):
        celdas_observadas.append(np.asarray(informacion[i]))
    return (r, c, alpha, celdas_observadas)

#TODO: intentar poner la etiqueta de filas al inicio de cada fila.

def accion2_noInteractivo(informacion):
    print('Iniciando el análisis estadístico...')
    #Extraemos los datos contenidos en el vector información.
    r=informacion[0]
    c=informacion[1]
    alpha=informacion[2]
    celdas_observadas=informacion[3]
    df=(c-1)*(r-1) #grados de libertad
    GT=analisis_ame.gran_total(celdas_observadas, r)
    probab_pj=analisis_ame.calculo_probabilidades_filas(r, celdas_observadas, GT)
    probab_pi=analisis_ame.calculo_probabilidades_columnas(r,c, celdas_observadas, GT)
    celdas_esperadas=analisis_ame.tabla_esperanzas(r,c,celdas_observadas, GT, probab_pj, probab_pi)
    chi=analisis_ame.estadistico(r, c, celdas_observadas, celdas_esperadas)
    print('Los datos introducidos son: ')
    print(tabulate(celdas_observadas))
    print('Los datos esperados son: ')
    print(tabulate(celdas_esperadas))
    print('El valor del estadístico es: ')
    print(chi)
    print('Valor P= ')
    print(chi2.sf(chi, df))
    #valor_critico=1-chi2.cdf(alpha, df)


informacion=extraccion_data_tipo2('data3.txt')
accion2_noInteractivo(informacion)
