# Fecha: 01/11/2022
# Autor: Roxanyffer Velasco Contreras
# Computación Paralela y Distribuida

# Se presenta un Programa Python para verificar si hay un triplete pitagórico en 
# una matriz dada
 
# Devuelve verdadero si hay pitagórico
# triplete en ar[0..n-1]
 
def isTriplet(ar, n):
    j = 0
     
    for i in range(n - 2):
        for j in range(i + 1, n):
            for k in range(j + 1, n - 1):
                # Calcular el cuadrado de los elementos de la matriz
                x = ar[i]*ar[i]
                y = ar[j]*ar[j]
                z = ar[k]*ar[k]
                if (x == y + z or y == x + z or z == x + y):
                    return 1
     
    # Si se llega a este punto es porque no se encontró ningún triplete.
    return 0
 
 
"""
# Programa de controlador para probar la función anterior
ar = [3, 1, 4, 6, 5]
ar_size = len(ar)
 
if(isTriplet(ar, ar_size)):
    print("\nLa función Si es un Triplete")
else:
    print("\nLa función No es un Triplete")

"""