# Importaciones necesarias para la clasificación de los tokens
from Extracción_txt import leer_archivo
from Dividir_palabras import dividir_frase
from Dividir_cadena import dividir_cadena
from AFD import hash_function, AFD
from Impresión_txt import Impresion_txt

# Leer el contenido del archivo de entrada y guardarlo en una nueva variable
contenido_archivo = leer_archivo('Input.txt')

# Dividir el contenido en palabras y guardarlo en un arreglo
cadenas = dividir_frase(contenido_archivo)

# Variables que se usaran para ayudarnos a contar los tokens obtenidos
i = 0
i_2 = 0

# Preparar un arreglos para almacenar los resultados de los distintos análisis.
resultado = []
resultado_unico = []
resultado_vistos = []

# Procesar cada palabra.
for palabra in cadenas:
    # Dividir cada palabra en letras.
    letras = dividir_cadena(palabra)
    # Generar la secuencia de transiciones
    secuencia = hash_function(letras)
    # Enviar la secuencia al AFD para obtener la clasificación de la palabra
    tipo = AFD(secuencia)
    # Agregar el par (palabra, tipo) al resultado.
    resultado.append((palabra, tipo))
    #Contador tokens
    i = i + 1




# Eliminar parejas repetidas conservando el orden

for pareja in resultado:
    #Se hace una comparación entre la paraje del ciclo y la lsita de parejas vistas
    if pareja not in resultado_vistos:
        #Se agrega a una nueva lista las parejas no vistas antes
        resultado_unico.append(pareja)
        #Se agrega a una nueva lista las parejas vistas antes
        resultado_vistos.append(pareja)
        #Se suma en el contador
        i_2 = i_2 + 1


#Se convierten los dos contadores en una cadenas para agregarlo a los arreglos donde estan los resultados
i_str= str(i)
i_2_str= str(i_2)

#Se añade el contador al arreglo de resultados para poder imprimirlos despues
resultado.append(("# Tokens",i_str))
resultado_unico.append(("# Tokens",i_2_str))

# Escribir los resultados en los archivo de salida
mensaje = Impresion_txt(resultado, 'Output1.txt')
mensaje2 = Impresion_txt(resultado_unico, 'Output2.txt')

# Imprimir los mensajes de confirmación.
print(mensaje)
print(mensaje2)