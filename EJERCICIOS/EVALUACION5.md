# 5 Práctica 5. Operadores relacionales. (6 puntos) 
### 5.1 Ejercicio 1 (2 puntos)
Programa que imprima si el número es positivo o negativo, el número debe ser ingresado por consola.

    numero = int(input('Ingresa un número positivo o negativo: '))

    if numero == 0:
        print('El número es neutro')
    elif numero > 0:
        print('El número ingresado es positivo')
    else:
        print('El número ingresado es negativo')

### 5.2 Ejercicio 2 (2 puntos)
Programa que imprima si el número ingresado esta en el rango de 1 a 7, el número se solicita por consola.

    numero = int(input('Ingresa un número: '))

    if numero >= 1 and numero <= 7:
        print('El número ingresado está en el rando de 1 a 7')
    else:
        print('El número ingresado está fuera del rando de 1 a 7')

### 5.3 Ejercicio 3 (2 puntos)
Programa que solicite un monto y que solicite el interés mensual, si el interés es mayor al 30% nos imprimirá que es incorrecto, si es menor realizará el cálculo e imprimira el monto con su interés adicionado.

    monto = int(input('Ingresa un monto: '))

    interes_mensual = float(input('Ingresa un interes mensual menor al 30%: '))

    if interes_mensual > 30:
        print('El interes ingresado es incorrecto')
    else:
        total = monto + (monto * (interes_mensual / 100))
        print(f'''
        Por un monto de ${monto} 
        Con una tasa de interes mensual del {interes_mensual}% 
        El total a pagar es de ${total}''')
