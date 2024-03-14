def is_letras(caracter):
    letras_latinas = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if caracter in ['i', 'I']:
        return 2
    elif caracter in ['n', 'N']:
        return 3
    elif caracter in ['t', 'T']:
        return 4
    elif caracter in letras_latinas:
        return 1
    else:
        return 0

def is_numeros(caracter):
    numeros = '0123456789'
    if caracter in numeros:
        return 5
    else:
        return 0

def is_puntuacion(caracter):
    signos_puntuacion = '(){};,'
    if caracter in signos_puntuacion:
        return 6
    else:
        return 0

def is_operador(caracter):
    operador = '+*=/><'
    if caracter in operador:
        return 7
    else:
        return 0

def hash_function(arreglo):
    resultados = []
    for elemento in arreglo:
        elemento_str = str(elemento)
        resultado = is_letras(elemento_str) or is_numeros(elemento_str) or is_puntuacion(elemento_str) or is_operador(elemento_str)
        resultados.append(resultado)
    return resultados

def AFD(arreglo):
    estado = 1
    tabla_estados = [
    [99, 1,  2,  3,  4,  5,  6,  7],
    [1,  5,  2,  5,  5,  6,  7,  8],
    [2,  5,  5,  3,  5,  0,  0,  0],
    [3,  5,  5,  5,  4,  0,  0,  0],
    [4,  5,  5,  5,  5,  0,  0,  0],
    [5,  5,  5,  5,  5,  0,  0,  0],
    [6,  0,  0,  0,  0,  6,  0,  0],
    [7,  0,  0,  0,  0,  0,  0,  0],
    [8,  0,  0,  0,  0,  0,  0,  0]
    ]
    
    for elemento in arreglo:
        if elemento == 0:
            return "La cadena contiene un caracter no definido en el alfabeto"
    
    for elemento in arreglo:
        estado = tabla_estados[estado][elemento]
        if estado == 0:
            return "Cadena no valida"

    if      estado == 4:
        return "Palabra reservada"
    
    elif    estado == 2 or 3 or 5:
        return "Identificador"
    
    elif    estado == 6:
        return "Numeros"
    
    elif    estado == 7:
        return "Signo puntuación"
    
    elif    estado == 8:
        return "Operador"
    
    else:
        return "Cadena no valida"
