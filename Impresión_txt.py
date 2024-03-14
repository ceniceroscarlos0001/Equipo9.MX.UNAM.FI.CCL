def Impresion_txt(resultado, nombre_archivo_salida):
    try:
        with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            for pareja in resultado:
                archivo_salida.write(f"{pareja[0]} -> {pareja[1]}\n\n")
        return "Archivo generado con éxito."
    except Exception as e:
        return f"Error al escribir el archivo: {e}"
