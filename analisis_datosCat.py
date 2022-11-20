#---------------------------- TABLAS DE CONTINGENCIA: ---------------------------------------------------
#----------FUNCIONES REQUERIDAS PARA ANÁLISIS DE CLASIFICACIÓN DE UNO, DOS O MÁS VÍAS --------------------

#--------------- Amélie Bernès, Noviembre del 2022.

#- Librerías ----------------------

import numpy as np
from numpy import array
import ast
from scipy.stats import chi2

#- Funciones -----------------------

def gran_total(celdas_observadas,r):
    GT=0 #gran total; inicializamos la suma.
    for j in range(r):
        GT=GT+sum(celdas_observadas[j])
    return GT

def calculo_probabilidades_filas(r, celdas_observadas, GT):
    probab_pj=np.array([])
    for j in range(r):
        probab_pj=np.append(probab_pj, sum(celdas_observadas[j])/GT)
    return probab_pj

def calculo_probabilidades_columnas(r, c, celdas_observadas, GT):
    probab_pi=np.array([])
    for i in range(c):
        suma=0
        for j in range(r):
            suma+=celdas_observadas[j][i]
        probab_pi=np.append(probab_pi, suma/GT)
    return probab_pi

def tabla_esperanzas(r, c, celdas_observadas, GT, probab_pj, probab_pi):
    celdas_esperadas={} #inicializamos el diccionario
    for j in range(r):
        #llenamos el vector fila de las esperanzas:
        esperanza_fila=np.array([])
        for i in range(c):
            esperanza_fila=np.append(esperanza_fila, probab_pj[j]*probab_pi[i]*GT)
        #y luego lo agregamos al diccionario celdas_esperadas
        celdas_esperadas[j]=esperanza_fila
    return celdas_esperadas


def estadistico(r, c, celdas_observadas, celdas_esperadas):
    chi=0 #inicializamos el estadístico
    for j in range(r):
        for i in range(c):
            chi= chi+ (celdas_observadas[j][i]-celdas_esperadas[j][i])**2/celdas_esperadas[j][i]
    return chi

def estadistico1(c, celdas_observadas, celdas_esperadas):
    chi=0 #inicializamos el estadístico
    for i in range(c):
        chi+=(celdas_observadas[i]-celdas_esperadas[i])**2/celdas_esperadas[i]
    return chi
