#-------------------- TABLAS DE CONTINGENCIA: CLASIFICACIÓN DE UNA SOLA VÍA --------------------
#--------------- Amélie Bernès, Noviembre del 2022.

#- Librerías ----------------------

import numpy as np
from numpy import array
from tabulate import tabulate
import ast
from scipy.stats import chi2
import analisis_datosCat as analisis_ame

np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
def extraccion_data_tipo1(nombre):
    """
    TODO: Deberías cambiar el orden de los elementos, para que sea compatible con el abordaje hecho para el caso en el que se tenga más de una sola fila.
    Input es un archivo .txt (guardado en la misma carpeta que este script) llamado nombre.
    La primera fila contiene los datos fila a analizar,
    la segunda fila contiene las probabilidades, y 
    la tercera fila contiene el valor alpha.
    Esta función regresa un array donde estos datos se almacenan en dos np.array y float, respectivamente.
    """
    informacion=[]
    p=nombre
    with open(p, "r") as f:
        for i in f.readlines():
            informacion.append(ast.literal_eval(i.strip()))
    informacion=array(informacion)
    #cambiamos el tipo de los primeros dos elementos de 'informacion'
    informacion[0]=np.asarray(informacion[0])
    informacion[1]=np.asarray(informacion[1])
    return informacion

def accion1_noInteractivo(informacion):
    print('Iniciando el análisis estadístico...')
    c=len(informacion[0])
    alpha=informacion[2]
    df=c-1 #grados de libertad
    celdas_observadas=informacion[0]
    vector_probab=informacion[1]
    GT=sum(celdas_observadas)
    celdas_esperadas=GT*vector_probab
    chi=analisis_ame.estadistico1(c, celdas_observadas, celdas_esperadas)
    print('Los datos introducidos son: ')
    print(celdas_observadas)
    print('Los datos esperados son: ')
    print(celdas_esperadas)
    print('El valor del estadístico es: ')
    print(chi)
    print('Valor P= ')
    print(chi2.sf(chi, df))
    valor_critico=1-chi2.cdf(alpha, df)

informacion=extraccion_data_tipo1('data.txt')
accion1_noInteractivo(informacion)
