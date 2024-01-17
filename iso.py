import random

# Lista de preguntas y respuestas

preguntas = [
    (
        "¿Cómo obtienes el día de la semana con el comando date, mostrando solo las tres primeras letras?",
        [
            "a) date +%a",
            "b) date +%A",
            "c) date +%d",
            "d) date +%D",
        ],
        "a"
    ),
    (
        "¿Cuál es la opción para obtener el día de la semana con todas las letras?",
        [
            "a) date +%a",
            "b) date +%A",
            "c) date +%d",
            "d) date +%D",
        ],
        "b"
    ),
    (
        "¿Cómo obtienes el mes con el comando date, mostrando solo las tres primeras letras?",
        [
            "a) date +%b",
            "b) date +%B",
            "c) date +%m",
            "d) date +%M",
        ],
        "a"
    ),
    (
        "¿Cuál es la opción para obtener el mes con todas las letras?",
        [
            "a) date +%b",
            "b) date +%B",
            "c) date +%m",
            "d) date +%M",
        ],
        "b"
    ),
    (
        "¿Cuál es la opción para obtener la fecha y hora completa con el comando date?",
        [
            "a) date +%c",
            "b) date +%F",
            "c) date +%T",
            "d) date +%dt",
        ],
        "a"
    ),
    (
        "¿Cómo obtienes el día del mes con dos dígitos?",
        [
            "a) date +%d",
            "b) date +%D",
            "c) date +%F",
            "d) date +%y",
        ],
        "a"
    ),
    (
        "¿Cómo obtienes la fecha en formato mm/dd/aa?",
        [
            "a) date +%d",
            "b) date +%D",
            "c) date +%F",
            "d) date +%y",
        ],
        "b"
    ),
    (
        "¿Cómo obtienes la fecha en formato aaaa/mm/dd?",
        [
            "a) date +%d",
            "b) date +%D",
            "c) date +%F",
            "d) date +%b",
        ],
        "c"
    ),
    (
        "¿Cómo obtienes el año en dos dígitos según el calendario de la semana?",
        [
            "a) date +%g",
            "b) date +%G",
            "c) date +%y",
            "d) date +%Y",
        ],
        "a"
    ),
    (
        "¿Cómo obtienes el año en cuatro dígitos según el calendario de la semana?",
        [
            "a) date +%g",
            "b) date +%G",
            "c) date +%y",
            "d) date +%Y",
        ],
        "b"
    ),
    (
        "¿Cómo obtienes la hora en formato HH:MM:SS?",
        [
            "a) date +%H",
            "b) date +%I",
            "c) date +%T",
            "d) date +%S",
        ],
        "c"
    ),
    (
        "¿Cómo obtienes el día de la semana en número (0 para Domingo)?",
        [
            "a) date +%w",
            "b) date +%W",
            "c) date +%S",
            "d) date +%D",
        ],
        "a"
    ),
    (
        "¿Cómo obtienes el número de la semana del año?",
        [
            "a) date +%w",
            "b) date +%W",
            "c) date +%m",
            "d) date +%wn",
        ],
        "b"
    ),
    (
        "Si quieres combinar texto con formatos de fecha y hora, ¿cuál sería el comando adecuado?",
        [
            'd) date +"Año:%G-Hora:%T"',
            'b) date +%D',
            'c) date +%c',
            'a) date +%F',
        ],
        "d"
    ),
    (
        "¿Cómo obtienes el mes en número?",
        [
            "a) date +%b",
            "b) date +%B",
            "d) date +%m",
            "c) date +%M",
        ],
        "d"
    ),
    (
        "¿Cómo obtienes los minutos?",
        [
            "a) date +%h",
            "d) date +%M",
            "c) date +%T",
            "b) date +%m",
        ],
        "d"
    ),
]




#######################################################################################

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)

# Función para calcular la equivalencia de la puntuación en una nota sobre 10
def calcular_equivalencia_puntuacion(puntuacion, total_preguntas):
    escala_maxima = 10.0
    equivalencia = (puntuacion / total_preguntas) * escala_maxima
    return equivalencia

# Función para realizar el test
def realizar_test():
    puntaje = 0
    total_preguntas = len(preguntas)

    for i, (pregunta, opciones, respuesta) in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta}")
        random.shuffle(opciones)
        for opcion in opciones:
            print(opcion)
        respuesta_usuario = input("\nTu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta:
            print("-------------------------")
            print("¡Respuesta correcta! ✔✔✔✔✔✔✔✔✔")
            print("-------------------------\n")
            puntaje += 1
        else:
            print("-------------------------")
            print(f"✖✖✖✖✖✖✖ Respuesta incorrecta. La opción correcta es: {respuesta}\n")
            print("-------------------------\n")
    
    equivalencia = calcular_equivalencia_puntuacion(puntaje, total_preguntas)
    
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"  Has completado el test, {nombre_usuario}. Puntuación final: {puntaje}/{total_preguntas}")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("                                                  ==========")
    print(f"Tu equivalencia de nota sobre 10 es ━━━━━━━━━━━━❯✷ {equivalencia:.2f}/10 ✷❮━━━━━━━━━━━━")
    print("                                                  ==========")

# Solicitar el nombre del usuario
nombre_usuario = input("Bienvenido al test de Fundamentos. Por favor, introduce tu nombre: ")

# Solicitar el número de preguntas
num_preguntas = int(input("¿Cuántas preguntas deseas en el test? "))
while num_preguntas > len(preguntas):
    print(f"Lo siento, solo hay {len(preguntas)} preguntas disponibles.")
    num_preguntas = int(input("Por favor, elige un número igual o menor: "))

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)
preguntas = preguntas[:num_preguntas]

# Ejecutar el test
print(f"Muy bien, {nombre_usuario}! Comencemos con tu test de Fundamentos con {num_preguntas} preguntas.")
realizar_test()