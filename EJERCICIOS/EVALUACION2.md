## Práctica 2. 6 puntos
2 Práctica 2. Números enteros y reales.

Realiza los ejercicios de acuerdo a las indicaciones

2.1 Ejercicio 1 (1.5 puntos)

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius.

    g_fahrenheit = float(input('¿Cuál es la temperatura en grados fahrenheit? '))

    g_celsius = (g_fahrenheit - 32) / 1.8

    print(f'La temperatura {g_fahrenheit} en grados fahrenheit a grados celsius es: {g_celsius}°')

2.2 Ejercicio 2 (1.5 puntos)

Dados dos números, mostrar la suma, resta, división y multiplicación de
ambos.

    num1 = int(input('Ingresa un valor superior a cero: '))
    num2 = int(input('Ingresa un segundo valor superior a cero: '))

    suma = num1 + num2
    resta = num1 - num2
    division = num1 / num2
    multiplicacion = num1 * num2

    print(f'''El resultado de operar aritmeticamente los números {num1} y {num2} es:
    Suma: {suma}
    Resta: {resta}
    División: {division}
    Multiplicación: {multiplicacion}''')

2.3 Ejercicio 3 (1.5 puntos)

Calcular el perímetro y área de un rectángulo dada su base y su altura.
Respuesta:

    base = float(input('Ingresa el valor de la base del rectángulo: '))
    altura = float(input('Ingresa el valor de la altura del rectángulo: '))

    perimetro = (base * 2) + (altura * 2)

    area = base * altura

    print(f'Un rectángulo con una base de {base}cm y una altura de {altura}cm tiene un perimetro de {perimetro}cm y una área de {area}cm2')

