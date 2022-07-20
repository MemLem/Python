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


    while '-' in palabra or ' ' in palabra: 
        palabra = random.choice(palabras) # En caso de cumplir las condiciones del while anterior, esta variable almacenará un elemento seleccionado aleatoriamente desde la lista "palabras" (la cual fue importada con anterioridad)

    return palabra.upper() # Instrucción que devuelve la palabra selecionada, pero en mayúsculas.


def ahorcado():

    print("=======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)
    letras_por_adivinar = set(palabra)  
    abecedario = set(string.ascii_uppercase) 
    letras_adivinadas = set()  

    vidas = 7


    while len(letras_por_adivinar) > 0 and vidas > 0:

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
