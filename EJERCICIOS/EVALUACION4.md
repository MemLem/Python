# Práctica 4. 6 puntos
## Tipos de colección de datos.
### 4.1 Ejercicio 1(1.2 puntos)
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su
cuadrado y su cubo.
Respuesta:

    import random

    lista = []

    for indice in range(1,11):
      lista.append(random.randint(1,10))

    for numero in lista:
      print(numero," ",numero ** 2," ",numero ** 3)

### 4.2 Ejercicio 2 (1.2 puntos)
Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia
los elementos de la lista en otra lista pero en orden inverso, y muestra sus
elementos por la pantalla.

    lista_nombres = []
    lista_nombres_inv = [] 

    for indice in range(1,6):
      lista_nombres.append(input("Ingresa un nombre: "))

    lista_nombres_inv = lista_nombres[::-1]

    for nombre in lista_nombres_inv:
      print(nombre)

### 4.3 Ejercicio 3 (1.2 puntos)
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas,
la nota media, la nota más alta que ha sacado y la menor.

    notas = []
    contador = 1

    while contador < 6:
        nota =(int(input('Ingresa una calificación: ')))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            contador = contador + 1
        else:
            print('Ingresa una nota entre 0 y 10')


    promedio = sum(notas) / len(notas)

    max_nota = max(notas)

    min_nota = min(notas)


    print(f'''Las notas del alumnos son: {notas}
          Promedio de {promedio}
          Su nota más alta es: {max_nota}
          Su nota más baja es: {min_nota}''')

### 4.4 Ejercicio 4 (1.2 puntos)
Codifica un programa en python que nos permita guardar los nombres de los
alumnos de una clase y las notas que han obtenido. Cada alumno puede tener
distinta cantidad de notas. Guarda la información en un diccionario cuya claves
serán los nombres de los alumnos y los valores serán listados con las notas de
cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su
nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al
final el programa nos mostrará la lista de alumnos y la nota media obtenida por
cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el
programa nos dará un error.


### 4.5 Ejercicio 5 (1.2 puntos)
Crea una tupla con los meses del año, pide números al usuario, si el número está
entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
muestra un mensaje de error. El programa termina cuando el usuario introduce un
cero.


    meses = ("enero", "eebrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
    "noviembre", "dicimbre")

    n_mes = int(input('Ingresa un número entre 1 y 12: '))

    while n_mes != 0:
        if n_mes >= 1 and n_mes <= len(meses):
            print(meses[n_mes - 1])
            n_mes = int(input('Ingresa un número: '))
        else:
            print('Introduce un valor entre 1 y 12')
            n_mes = int(input('Ingresa un número: '))
    else:
        print('fin')



# TRATA DE RESOLVER Y AVANZAR LO MÁS POSIBLE EN LOS EJERICICIOS, EL MARTES HABILITO "AYUDAS" EN CADA EJERCICIO
