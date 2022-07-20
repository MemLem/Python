"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
import random # Instrucción para importar el modulo nombrado "random"; el cual contiene a su vez métodos para generar números aleatorios.
import string # Instrucción para importar el modulo nombrado "string", el cual contiene funciones para la manipulación de cadenas de texto.
from palabras import palabras # Instrucción para llamar el modulo nombrado como "palabras.py", el cual es a su vez está importando especificamente la lista llamada "palabras".
from ahorcado_diagramas import vidas_diccionario_visual # Instrucción para llamar el modulo nombrado como "ahorcado_diagramas.py", el cual es a su vez está importando especificamente el diccionario llamado "vidas_diccionario_visual".


def obtener_palabra_válida(palabras): # Creación de la función llamada "obtener_palabra_válida", la cual contiene el argumento "palabras"
    palabra = random.choice(palabras) # El argumento "palabra" almacena un elemento seleccionado aleatoriamente desde la lista "palabras" (la cual fue importada con anterioridad). El método .choice() es parte del modulo "random", el cual también fue importado lineas arriba.


    while '-' in palabra or ' ' in palabra: # Intrucción que inicia un bucle de n veces. Siempre y cuando, la cadena de tetxo seleccionada desde la lista "palabras" contenga un guión "-" O un espacio en blanco " ". En caso de cumplir una u otra condición se realizará la instrucción siguiente.
        palabra = random.choice(palabras) # En caso de cumplir las condiciones del while anterior, esta variable volverá a almacenar un elemento aleatorio desde la lista "palabras" (la cual fue importada con anterioridad)

    return palabra.upper() # Instrucción que devuelve la palabra selecionada, pero en mayúsculas.


def ahorcado(): # Se crea una nueva función, llamada "ahorcado"

    print("=======================================") # Instrucción que imprimirá en consola la cadena: =======================================
    print(" ¡Bienvenido(a) al juego del Ahorcado! ") # Instrucción que imprimirá en consola la cadena: ¡Bienvenido(a) al juego del Ahorcado!
    print("=======================================") # Instrucción que imprimirá en consola la cadena: =======================================

    palabra = obtener_palabra_válida(palabras) # variable que almacena la cadena/palabra seleccionada anteriormente desde la función "obtener_palabra_válida"
    letras_por_adivinar = set(palabra) # variable que almacenará una por una las letras unicas que contenga la palabra seleccionada aleatoriamente. Con la función set() se eliminan letras repetidas, es decir, contempla un conjunto de elementos unicos.
    abecedario = set(string.ascii_uppercase) # variable que contendrá el conjunto total de letras del abecedario en mayusculas. El método "ascii_uppercase" es usado para los caracteres considerados como mayuculas, pero cuyo valor NO depende de la zona regional que tiene configurado el sistema.
    letras_adivinadas = set() # variable que almacenará un conjunto de elementos/letras sin repetirse.

    vidas = 7 # Variable nombrada "vidas" de tipo numerica, la cual indicará el número de oportunidades a jugar.


    while len(letras_por_adivinar) > 0 and vidas > 0: # ciclo que se repetira n veces, siempre y cuando la longitud de la palabra seleccionada sea mayor que 0 elementos Y vidas sea mayor a cero, es decir, cuando el jugador tenga cero letras por adivinar y cero vidas se detendra el programa.

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

      
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) 
        print(f"Palabra: {' '.join(palabra_lista)}") 

     
        letra_usuario = input('Escoge una letra: ').upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
       
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
         
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

   
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


    ahorcado()
