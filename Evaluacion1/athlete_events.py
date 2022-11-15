# IMPORTANDO LIBRERIAS
import math
import pandas as pd

# LEYENDA LA DATA
df = pd.read_csv('Evaluacion1/athlete_events.csv')

# INGRESO POR TECLADO
sports = df.Sport.unique()

def validacion(texto):
    while True:
        sport = input(texto).strip()
        if sport in sports:
            return sport
        print("Ingrese un deporte valido")

sportA = validacion("Ingrese un deporte: ")
sportB = validacion("Ingrese otro deporte: ")

# AMBOS DEPORTES PRESENTES
listA = df.Year[df.Sport == sportA].unique()
listB = df.Year[df.Sport == sportB].unique()

listAB = sorted(list(set(listA) & set(listB)))

# DETERMINAR ALTURAS
for year in listAB:
    
    auxA = df.Height[(df.Year == year) & (df.Sport == sportA)].dropna()
    auxB = df.Height[(df.Year == year) & (df.Sport == sportB)].dropna()

    result = (auxA.mean() - auxB.mean()) / math.sqrt((auxA.var() / auxA.count()) + (auxB.var() / auxB.count()))

    print("Año " + str(year) + " D: " + "%.4f" % result + (" Hay diferencia significativa" if abs(result) > 1.96 else " No hay diferencia significativa"))