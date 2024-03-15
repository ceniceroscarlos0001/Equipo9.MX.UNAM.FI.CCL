# Equipo9.MX.UNAM.FI.CCL
## Especificación de Requerimientos de Software
- Proyecto 1 Analizador Léxico
- Fecha: 14/03/2024
- Versión Final
### 1. Introducción
#### Propósito
En este documento especificaremos el alcance de los requisitos y objetivos que tendra este proyecto de software
#### Alcance del proyecto
La finalidad de este proyecto es el de generar un programa que sea capaz procesar tokens para su posterior clasificación
#### Definiciones, acrónimos y abreviaturas
Autómata de estados finitos -> AFD
### 2. Descripción general
#### Perspectiva del producto
Dentro de los compiladores el analizador léxico es el primer gran paso por ello su desarrollo correcto es escencial para proyectos futuros
#### Funciones del producto
Este proyecto en su funcionalidad minima es clasificar distintos tipos de tokens. Apuntando a más funcionalidades sería el de recibir los tokens dentro de un archivo externo y posteriormente imprimirlos en otro archivo externo
La clasificacion de tokens se hara mediante la aplicación de los conceptos de los AFD
#### Características de los usuarios
El usuario debera poseer conocimientos basicos de programación para hacer un mejor uso del mismo, ya que en caso de desearlo necesitara modificar los archivos de entreda o la definicion del alfabeto para ajustarlo a sus necesidades
#### Restricciones
Al ser un programa muy simple no posee restricciones ni a nivel software ni hardware, lo unico necesario sería un editor de programas que sea capaz de correr programas en python
#### Particionamiento del sistema
El sistema se dividio en 5 modulos
- Extracción_txt.py
- Dividir_palabras.py
- Dividir_cadena.py
- AFD.py
- Impresión_txt.py
Además de contar con una función main que importa las funciones necesarias para obtener el funcionamiento completo del proyecto
### 3. Requerimientos específicos
#### Requerimientos de interfaz
El proyecto interactura con un programa que ejecute python por lo tanto las interacciones con el hardware dependeran del mismo
#### Rendimiento
Debido a la simplicidad del programa los tiempos de respuesta son en cuestion de fracciones de segundo
#### Requerimientos de software del sistema
Mientras posea un programa que sea capaz de correr python debe de funcionar de manera exitosa
#### Requerimientos de comunicación
El proyecto debe de ser capaz de leer el archivo adjunto y crear un nuevo por lo que tiene que poseer permisos para hacerlo
#### Restricciones de diseño
El proyecto se apego a los requerimientos del mismo dados por el profesor
