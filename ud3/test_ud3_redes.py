import random

# Lista de preguntas y respuestas
preguntas = [
    ("Cuando se establece una comunicación o trasmisión, ¿a través de qué alcanza el destino la información?", [
        "a) Fibra óptica.",
        "b) Cable coaxial.",
        "c) Conector RJ-45.",
        "d) Medio de transmisión."
    ], "d"),
    ("¿Con qué nivel está relacionado el medio de transmisión?", [
        "a) Nivel de red.",
        "b) Nivel de transmisión.",
        "c) Nivel físico.",
        "d) Nivel de enlace."
    ], "c"),
    ("¿Cuál es el objetivo del nivel físico?", [
        "a) La transmisión y la recepción de bits.",
        "b) Conectar dispositivos a la red.",
        "c) Generar corriente eléctrica.",
        "d) Detectar errores en la conexión."
    ], "a"),
    ("¿Cuáles son funciones del nivel físico?", [
        "a) Definir características eléctricas, mecánicas, de procedimiento y funcionales para activar, mantener y desactivar el enlace físico entre 2 equipos.",
        "b) Definir características de los conectores y cableado y asegurar su compatibilidad.",
        "c) Determinar la codificación, voltaje de la señal eléctrica y la duración de los pulsos eléctricos.",
        "d) Todas son correctas."
    ], "d"),
    ("¿A qué nivel corresponde la amplificación de la señal mediante amplificadores?", [
        "a) Nivel de red.",
        "b) Nivel de amplificación.",
        "c) Nivel físico.",
        "d) Nivel de enlace."
    ], "c"),
    ("¿Qué deben tener en cuenta los protocolos del nivel 1 (físico) para realizar el transporte de la información?", [
        "a) La longitud del cableado y el número de dispositivos conectados a la red.",
        "b) El modo de enviar los dígitos binarios por el medio, tener en cuenta si el medio permite la transmisión en un único sentido o en ambos, la corrección de las distorsiones y perturbaciones que sufre la señal en su camino, y la posibilidad o no de enviar varias transmisiones simultáneamente.",
        "c) La longitud del cableado, el número de dispositivos conectados a la red y el voltaje de la red eléctrica.",
        "d) La longitud del cableado y la cantidad de bits por segundo que pueden ser transmitidos por el medio físico."
    ], "b"),
    ("¿Cuáles son ejemplos de especificaciones del nivel físico de la capa física de Ethernet?", [
        "a) 10BASE-T, 10BASE2, 10BASE5, 100BASE-TX, 100BASE-FX Y 100BASE-T.",
        "b) 10FASE-T, 10FASE2, 10FASE5, 100FASE-TX, 100FASE-FX, 100FASE-T.",
        "c) 10CASE-T, 10CASE2, 10CASE5, 100CASE-TX, 100CASE-CX, 100CASE-T.",
        "d) Ninguna de las anteriores."
    ], "b"),
    ("¿Dentro de qué viaja la información en la mayoría de las transmisiones?", [
        "a) De ondas.",
        "b) De un taxi.",
        "c) De trasmisores.",
        "d) De conectores."
    ], "a"),
    ("¿Qué es una onda?", [
        "a) Un ataque de Son Goku.",
        "b) Una perturbación que se desplaza en el espacio llevando energía.",
        "c) Un pulso uniforme de energía que se desplazada en el vacío.",
        "d) Un pulso uniforme de energía que se desplaza por campos electro-magnéticos."
    ], "b"),
    ("¿Por qué son producidas las ondas electromagnéticas?", [
        "a) Por el choque de ondas eléctricas en imanes de gran tamaño.",
        "b) Por el choque de ondas eléctricas en imanes, sin importar el tamaño.",
        "c) Por un pulso uniforme eléctrico en un campo magnético asociado.",
        "d) Por la oscilación de un campo eléctrico en relación con un campo magnético asociado."
    ], "d"),
    ("¿Cómo puede ser la transmisión?", [
        "a) Analógica o magnética.",
        "b) Abierta o cerrada.",
        "c) Analógica, digital o magnética.",
        "d) Analógica o digital."
    ], "d"),
    ("¿Qué valor o valores puede tomar la señal en una transmisión analógica?", [
        "a) Toma un valor fijo siempre.",
        "b) Toma valores continuos en el tiempo, tomando cualquier valor dentro de un rango determinado.",
        "c) Toma valores predefinidos por el administrador de la red.",
        "d) Toma valores discontinuos en el tiempo."
    ], "b"),
    ("La potencia de una transmisión analógica estará comprendida entre unos valores...", [
        "a) Positivo y negativo.",
        "b) Máximo y mínimo.",
        "c) Absoluto y relativo.",
        "d) Ninguna de las anteriores."
    ], "b"),
    ("La calidad de la transmisión depende...", [
        "a) Solo de la potencia recibida.",
        "b) De la potencia recibida y del ruido que lleva la señal.",
        "c) De la potencia recibida y del sonido que lleva la señal.",
        "d) Ninguna de las anteriores."
    ], "b"),    
    ("Los amplificadores empleados en la transmisión analógica...", [
        "a) Amplifican la señal, con lo cual también amplifican el ruido que llega con la misma.",
        "b) Amplifican la señal, pero no el ruido que llega con la misma.",
        "c) En las transmisiones analógicas no se usan amplificadores.",
        "d) No amplifican la señal, sino el ruido que llega con la misma."
    ], "a"),
    ("¿Cómo se llama al periodo de tiempo (por ejemplo, cada 2 mseg) a partir del cual se repite el patrón de la señal?", [
        "a) Periodo.",
        "b) Amplitud.",
        "c) Frecuencia.",
        "d) Fase."
    ], "a"),
    ("", [
        "a) .",
        "b) .",
        "c) .",
        "d) ."
    ], "a"),
    ("¿Qué indica la tasa de transferencia en el contexto de las comunicaciones?", [
    "a) La cantidad de datos que se pueden transmitir por unidad de tiempo.",
    "b) La distancia que pueden cubrir las señales de transmisión.",
    "c) La calidad de la conexión física entre dispositivos.",
    "d) La capacidad de almacenamiento de los dispositivos de red."
    ], "a"),
    ("¿Cómo se define la tasa de transferencia máxima en el contexto de las comunicaciones?", [
    "a) Como la cantidad máxima de datos que se pueden transmitir por unidad de tiempo.",
    "b) Como la velocidad mínima requerida para la transmisión de datos.",
    "c) Como la calidad de la conexión física entre dispositivos.",
    "d) Como la capacidad de almacenamiento de los dispositivos de red."
], "a"),
("¿Cuál es la tasa de transferencia máxima del estándar 802.11n, según lo discutido en temas anteriores?", [
    "a) 100 Mbps.",
    "b) 300 Mbps.",
    "c) 600 Mbps.",
    "d) 1000 Mbps."
], "c"),
("¿Qué factores afectan la tasa de transferencia máxima en una comunicación, según se menciona en el fragmento?", [
    "a) La longitud del cable y el número de dispositivos conectados a la red.",
    "b) El tipo de conector y el voltaje de la red eléctrica.",
    "c) El ancho de banda analógico, la potencia del señal, la potencia del ruido en el canal y la codificación del canal.",
    "d) La cantidad de bits por segundo que pueden ser transmitidos por el medio físico."
], "c"),
("¿Cómo se define la tasa de transferencia real en el contexto de las comunicaciones?", [
    "a) La velocidad máxima teórica del canal de transmisión.",
    "b) La velocidad mínima requerida para la transmisión de datos.",
    "c) La velocidad que percibe el usuario durante transmisiones habituales.",
    "d) La capacidad de almacenamiento de los dispositivos de red."
], "c"),
("¿Cuál es la tasa de transferencia máxima del estándar 10BASE2 (802.3a)?", [
    "a) 100 Mbps.",
    "b) 50 Mbps.",
    "c) 10 Mbps.",
    "d) 1 Gbps."
], "c"),
("¿Cuál es la tasa de transferencia máxima del estándar 10BASE5?", [
    "c) 100 Mbps.",
    "b) 50 Mbps.",
    "a) 10 Mbps.",
    "d) 1 Gbps."
], "a"),
("¿Cuál es la tasa de transferencia máxima del estándar 10BASE-T (802.3i)?", [
    "a) 100 Mbps.",
    "c) 50 Mbps.",
    "b) 10 Mbps.",
    "d) 1 Gbps."
], "b"),
("¿Cuál es la tasa de transferencia máxima del estándar 100BASE-TX (802.3u)?", [
    "a) 100 Mbps.",
    "b) 50 Mbps.",
    "c) 10 Mbps.",
    "d) 1 Gbps."
], "a"),
("¿Cuál es la tasa de transferencia máxima del estándar 100BASE-F (802.3u)?", [
    "a) 100 Mbps.",
    "b) 50 Mbps.",
    "c) 10 Mbps.",
    "d) 1 Gbps."
], "a"),
("¿Cuál es la tasa de transferencia máxima del estándar 1000BASE-T (802.3ab)?", [
    "a) 100 Mbps.",
    "b) 500 Mbps.",
    "c) 1 Gbps.",
    "d) 10 Gbps."
], "c"),
("¿Cuál es la tasa de transferencia máxima del estándar 1000BASE-F (802.3z)?", [
    "a) 100 Mbps.",
    "b) 500 Mbps.",
    "c) 1 Gbps.",
    "d) 10 Gbps."
], "c"),
("¿Cuál es la tasa de transferencia máxima del estándar 10GBASE-T (802.3an)?", [
    "a) 1 Gbps.",
    "b) 5 Gbps.",
    "c) 10 Gbps.",
    "d) 100 Gbps."
], "c"),
("¿Cómo se define la ganancia de un sistema en el contexto de señales electromagnéticas?", [
    "a) La velocidad de transmisión de datos.",
    "b) La relación entre la distancia entre el emisor y el receptor.",
    "d) La proporción entre las potencias de salida y entrada, en términos de energía por unidad de tiempo.",
    "c) La capacidad de almacenamiento de los dispositivos de red."
], "d"),
("La ganancia de un sistema puede ser positiva (amplificación) o negativa (atenuación). ¿Cómo se caracteriza una ganancia positiva y una ganancia negativa en este contexto?", [
    "a) Una ganancia positiva implica una pérdida de energía, mientras que una ganancia negativa implica una amplificación de la señal.",
    "b) Una ganancia positiva implica una amplificación de la señal, mientras que una ganancia negativa implica una pérdida de energía.",
    "c) Ambas ganancias, positiva y negativa, implican una pérdida de energía.",
    "d) Ambas ganancias, positiva y negativa, implican una amplificación de la señal."
], "b"),
("¿Cómo se expresa la ganancia?", [
    "a) En Hz.",
    "b) En dB.",
    "c) En A.",
    "d) En W."
], "b"),
("El logaritmo decimal de la relación entre la potencia de salida y entrada, conocido como Bel en honor a Graham Bell, inventor/patentador del teléfono. ¿Cuál es la unidad derivada de Bel que comúnmente se utiliza para medir la ganancia en sistemas de comunicación?", [
    "a) Hertz (Hz).",
    "b) Vatio (W).",
    "c) Decibelio (dB).",
    "d) Newton (N)."
], "c"),
("La décima parte del Bel, comúnmente utilizada para medir ganancias en sistemas de comunicación, se conoce como decibelio (dB). ¿Cómo se define el decibelio en términos de la relación entre la potencia de salida y la potencia de entrada?", [
    "a) dB = 10 · log (Potencia de salida - Potencia de entrada)",
    "b) dB = log10 (Potencia de salida / Potencia de entrada)",
    "c) dB = log2 (Potencia de salida / Potencia de entrada)",
    "d) dB = 10 · log (Potencia de salida / Potencia de entrada)"
], "d"),
("Como es sabido, el logaritmo en base 10 es la inversa de la operación matemática de potenciación. Por ejemplo, ¿cómo se expresa el logaritmo en base 10 de 1000?", [
    "a) log10(1000) = 1",
    "b) log10(1000) = 2",
    "c) log10(1000) = 3",
    "d) log10(1000) = 4"
], "c"),
("¿Cuál es la razón principal para el uso del logaritmo en el contexto de la ganancia de sistemas de comunicación?", [
    "a) Para aumentar la complejidad de los cálculos.",
    "b) Para simplificar las unidades y emplear valores menores.",
    "c) Para complicar la representación de la ganancia.",
    "d) Para cambiar la escala de los valores."
], "b"),
("¿Cuál es la razón principal para el uso del logaritmo en el contexto de la ganancia de sistemas de comunicación?", [
    "a) Para aumentar la complejidad de los cálculos.",
    "b) Para simplificar las unidades y emplear valores menores.",
    "c) Para complicar la representación de la ganancia.",
    "d) Para cambiar la escala de los valores."
], "b"),
("Si un medio no pierde ni gana potencia (Potencia Salida / Potencia Entrada = 1), ¿cómo se reflejaría esto en la expresión logarítmica y en la medida de ganancia en decibelios (dB)?", [
    "a) log(1) = 1, ganancia = 1 dB.",
    "b) log(1) = 0, ganancia = 0 dB.",
    "c) log(1) = 10, ganancia = 10 dB.",
    "d) log(1) = -1, ganancia = -1 dB."
], "b"),
("Si un amplificador amplifica la potencia de entrada en 100 veces, ¿cómo se expresaría la ganancia en decibelios (dB) según la fórmula logarítmica?", [
    "a) 5 dB.",
    "b) 10 dB.",
    "c) 20 dB.",
    "d) 100 dB."
], "c"),
("En el caso de pérdida de potencia, si la potencia de salida es la mitad de la potencia de entrada, ¿cómo se expresaría la ganancia (o pérdida) en decibelios (dB) según la fórmula logarítmica?", [
    "a) -1 dB.",
    "b) -3 dB.",
    "c) -6 dB.",
    "d) -9 dB."
], "b"),
("Supongamos que tenemos un cable que pierde 1 dB por kilómetro. Si el cable tiene 4 kilómetros de longitud, ¿cuánta pérdida de decibelios tendríamos? Luego, si tenemos un amplificador que proporciona una ganancia de 20 dB, ¿cuál sería el resultado final de la ganancia o pérdida en decibelios?", [
    "a) Pérdida de 4 dB, ganancia de 20 dB; resultado final: 16 dB.",
    "b) Pérdida de 4 dB, ganancia de 20 dB; resultado final: 24 dB.",
    "c) Pérdida de 4 dB, ganancia de 20 dB; resultado final: 4 dB.",
    "d) Pérdida de 4 dB, ganancia de 20 dB; resultado final: 20 dB."
], "a"),
("Dentro de los tipos de transmisión, ¿qué clasificación podemos hacer?", [
    "a) Secuencia dos bits, simultaneidad en la emisión-recepción, sincronismo.",
    "b) Frecuencia, amplitud, duración.",
    "c) Voltaje, resistencia, corriente.",
    "d) Longitud de onda, potencia, velocidad."
], "a"),
("Dentro de la secuencia de bits, ¿cuáles son las dos modalidades principales de transmisión?", [
    "a) Serie y paralelo.",
    "b) Sincrónica y asíncrona.",
    "c) Analógica y digital.",
    "d) Unipolar y bipolar."
], "a"),
("En la transmisión en serie, ¿cómo se envían los bits de una palabra?", [
    "a) Consecutivamente, uno tras otro, por una única línea de datos.",
    "b) Simultáneamente, todos al mismo tiempo, por diferentes líneas de datos.",
    "c) En bloques, agrupados por su valor, por diferentes líneas de datos.",
    "d) Aleatoriamente, sin un orden específico, por una única línea de datos."
], "a"),
("En la transmisión en paralelo, ¿cómo se envían los bits de una palabra?", [
    "a) Consecutivamente, uno tras otro, por una única línea de datos.",
    "b) Simultáneamente, todos al mismo tiempo, por diferentes líneas de datos.",
    "c) En bloques, agrupados por su valor, por diferentes líneas de datos.",
    "d) Aleatoriamente, sin un orden específico, por una única línea de datos."
], "b"),
("En cuanto a la simultaneidad en la emisión-recepción, ¿cuáles son las tres modalidades principales de transmisión?", [
    "a) Simplex, semi-duplex (half-duplex), dúplex (full-duplex).",
    "b) Serie, paralelo, dúplex (full-dúplex).",
    "c) Simples, semi-duplex, dúplex, full-dúplex",
    "d) Simplex (semi- dúplex), dúplex (full-dúplex)."
], "a"),
("En la modalidad de transmisión 'Simplex', ¿cómo se lleva a cabo la transmisión de datos?", [
    "a) En ambos sentidos simultáneamente.",
    "b) En un único sentido.",
    "c) En ambos sentidos, pero no simultáneamente.",
    "d) En diferentes líneas de datos."
], "b"),
("En la modalidad de transmisión 'Semi-duplex (half-duplex)', ¿cómo se realiza la transmisión de datos?", [
    "a) En ambos sentidos simultáneamente.",
    "b) En un único sentido.",
    "c) En ambos sentidos, pero no simultáneamente.",
    "d) En diferentes líneas de datos."
], "c"),
("En la modalidad de transmisión 'Dúplex (full-dúplex)', ¿cómo se lleva a cabo la transmisión de datos?", [
    "a) En ambos sentidos simultáneamente.",
    "b) En un único sentido.",
    "c) En ambos sentidos, pero no simultáneamente.",
    "d) En diferentes líneas de datos."
], "a"),
("En el contexto de la transmisión de datos, ¿cómo se define el 'Sincronismo'?", [
    "a) Es el proceso de envío de bits de manera consecutiva.",
    "b) Es el proceso de informar al receptor sobre el inicio y fin de un bloque de bits, así como la duración de cada bit.",
    "c) Es el proceso de transmitir datos en ambos sentidos simultáneamente.",
    "d) Es el proceso de agrupar bits por su valor y enviarlos en bloques."
], "b"),
("En el contexto de la sincronización en la transmisión de datos, ¿cuáles son las tres formas principales de sincronización?", [
    "a) Sincronización de frecuencia, sincronización de amplitud, sincronización de duración.",
    "b) Sincronización de bit, sincronización de palabra, sincronización de bloque.",
    "c) Sincronización de voltaje, sincronización de resistencia, sincronización de corriente.",
    "d) Sincronización de serie, sincronización de paralelo, sincronización de dúplex."
], "b"),
("¿Cómo se define la 'Sincronización de bit' en la transmisión de datos?", [
    "a) Es el reconocimiento de la frecuencia de cada bit.",
    "b) Es el reconocimiento del inicio y fin de cada bit.",
    "c) Es el reconocimiento del voltaje de cada bit.",
    "d) Es el reconocimiento del valor de cada bit."
], "b"),
("¿Cómo se define la 'Sincronización de palabra' en la transmisión de datos?", [
    "a) Es el reconocimiento de la frecuencia de cada palabra.",
    "b) Es el reconocimiento del inicio y fin de cada palabra.",
    "c) Es el reconocimiento del voltaje de cada palabra.",
    "d) Es el reconocimiento del valor de cada palabra."
], "b"),
("¿Cómo se define la 'Sincronización de bloque' en la transmisión de datos?", [
    "a) Es el reconocimiento de la frecuencia de cada bloque.",
    "b) Es el reconocimiento del inicio y fin de cada bloque.",
    "c) Es el reconocimiento del voltaje de cada bloque.",
    "d) Es el reconocimiento del valor de cada bloque."
], "b"),
("En función de cómo se establece el sincronismo, ¿cuáles son los dos tipos de transmisión que podemos distinguir?", [
    "a) Transmisión digital y transmisión analógica.",
    "b) Transmisión serie y transmisión paralelo.",
    "c) Transmisión asíncrona y transmisión síncrona.",
    "d) Transmisión unipolar y transmisión bipolar."
], "c"),
("¿Cuál fue el primer tipo de transmisión en utilizarse, y cuál es un ejemplo de su aplicación?", [
    "a) Transmisión digital, Ethernet.",
    "b) Transmisión paralelo, USB.",
    "c) Transmisión asíncrona, HDMI.",
    "d) Transmisión síncrona, RS-232."
], "c"),
("En la transmisión asíncrona, ¿cómo se produce el proceso de sincronización?", [
    "a) Para cada letra (bit) que se transmite.",
    "b) Para cada palabra (byte) que se transmite.",
    "c) Simultáneamente para todos los bits de una palabra.",
    "d) No hay sincronización en la transmisión asíncrona."
], "b"),
("En el contexto de la transmisión asíncrona, ¿qué se envía junto con los bits de la palabra para indicar el inicio y el final de la palabra?", [
    "a) Bits de paridad.",
    "b) Bits de inicio y de parada.",
    "c) Bits de control.",
    "d) Bits de sincronización."
], "b"),
("En la transmisión asíncrona, ¿qué requisitos deben cumplir el emisor y el receptor?", [
    "a) Deben trabajar a diferentes frecuencias.",
    "b) Deben tener relojes desincronizados.",
    "c) Deben trabajar a la misma frecuencia y tener los relojes sincronizados.",
    "d) No es necesario que trabajen a la misma frecuencia ni que tengan los relojes sincronizados."
], "c"),
("Si enviamos palabras de 5 bits de información junto con 1 bit de inicio y 1 bit de fin, ¿cuál sería la eficiencia del código, considerando que se transmiten 7 bits en total?", [
    "a) 50%",
    "b) 60%",
    "c) 71%",
    "d) 80%"
], "c"),
("En la transmisión síncrona, ¿cómo se envía el sincronismo con respecto a los datos?", [
    "a) Paralelamente con cada byte.",
    "b) Secuencialmente antes de cada byte.",
    "c) Paralelamente con los datos, pero NO en cada byte.",
    "d) No se envía sincronismo en la transmisión síncrona."
], "c"),
("En la transmisión síncrona, ¿cómo se indica la duración de cada uno de los bits?", [
    "a) No se indica la duración de los bits.",
    "b) Se envía una señl periódica de sincronización junto con los datos.",
    "c) Se envía un bit especial al inicio de cada palabra para indicar la duración.",
    "d) Se utiliza un código especial al final de cada byte para señalar la duración."
], "b"),
("En comparación con las transmisiones asíncronas, ¿cómo afecta el hecho de que la transmisión síncrona no emplea señales de inicio y fin en cada palabra/byte a la velocidad de transmisión?", [
    "a) Las transmisiones síncronas son más lentas.",
    "b) Las transmisiones síncronas son más rápidas.",
    "c) No hay diferencia en la velocidad entre transmisiones síncronas y asíncronas.",
    "d) Depende de la longitud de las palabras/bytes transmitidos."
], "b"),
("En la transmisión síncrona, ¿cómo se envía la señal de sincronización en relación con la señal de datos?", [
    "a) En cables diferentes.",
    "b) Por el mismo cable.",
    "c) En la misma señal.",
    "d) Depende de la distancia entre el emisor y el receptor."
], "c"),
("En la trama IEEE 802.3 de Ethernet, ¿cuál es la función de los primeros 7 bytes (56 bits) de sincronización?", [
    "a) Indican el inicio de la trama.",
    "b) Contienen información de control de flujo.",
    "c) Establecen la velocidad de transmisión.",
    "d) Todos los bits alternos 0, 1, 0, 1, ... para sincronización."
], "d"),
("¿Cómo se definen las perturbaciones en el contexto de la transmisión de datos?", [
    "a) Son acciones que mejoran la calidad del sistema de transmisión.",
    "b) Son acciones externas que no afectan al sistema de transmisión.",
    "c) Son acciones tanto externas como internas que provocan que la señal recibida no sea exactamente igual al emitido por el emisor.",
    "d) Son acciones que solo afectan al sistema de transmisión en modo síncrono."
], "c"),
("En relación con las perturbaciones y la transmisión de datos, ¿cómo afecta una perturbación que no modifica sustancialmente la señal enviada?", [
    "a) Provoca errores de transmisión.",
    "b) Garantiza una transmisión libre de errores.",
    "c) No tiene ningún efecto en la transmisión.",
    "d) Aumenta la velocidad de transmisión."
], "b"),
("¿Cuáles son algunas de las perturbaciones posibles en la transmisión de datos y cómo se define el indicador de esta perturbación?", [
    "a) Distorsión, intermodulación, ecos, diafonías, ruido, atenuación y modularización.",
    "b) Distorsión, intermodulación, ecos, atenuación y modularización.",
    "c) Distorsión, diafonías, ruido, atenuación y modularización.",
    "d) Distorsión, intermodulación, ecos, diafonías, ruido y atenuación."
], "d"),
("¿Cómo se caracteriza la distorsión en la transmisión de datos?", [
    "a) Por variaciones solo en amplitud.",
    "b) Por variaciones solo en frecuencia.",
    "c) Por variaciones tanto en amplitud como en frecuencia, generalmente causadas por el efecto del ruido.",
    "d) Por variaciones en la velocidad de transmisión."
], "c"),
("¿Cómo se define la intermodulación en la transmisión de datos?", [
    "c) Es la variación de amplitud de la seña emitido.",
    "b) Es la variación de frecuencia de la seña emitido.",
    "a) Es la llegada de otras señales a distintas frecuencias junto con la señal emitido.",
    "d) Es la variación de velocidad de transmisión de la señal."
], "a"),
("En relación con los ecos en la transmisión de datos, ¿a partir de cuándo es apreciable en el receptor?", [
    "a) A partir de los 10 ms.",
    "b) A partir de los 100 ms.",
    "c) A partir de 1 s.",
    "d) A partir de 1 ms."
], "a"),
("¿Cómo se caracteriza la diafonía en la transmisión de datos?", [
    "a) Se produce entre cables de diferentes materiales.",
    "b) Se produce en líneas de transmisión ópticas.",
    "c) Se produce en líneas metálicas homogéneas, donde acoplamientos entre dos o varios cables en el mismo conducto afectan al otro cable sumándose a la otra señal.",
    "d) Se produce solo en transmisiones inalámbricas."
], "c"),
("En términos de transmisión de datos, ¿cómo se define el ruido?", [
    "a) Es la variación de amplitud de la señal recibido.",
    "b) Es la variación de frecuencia de la señal recibido.",
    "c) Es la interferencia que recibe el medio de transmisión de distintos elementos externos, añadiendo una señal conocida y no deseada.",
    "d) Es la atenuación de la señal transmitido."
], "c"),
("¿Cómo afectará el ruido al sistema de transmisión según la potencia de la señal?", [
    "a) Ambas son correctas.",
    "b) Dependiendo de la potencia de la señal, el ruido afectará más o menos.",
    "c) Ambas son incorrectas.",
    "d) El ruido no tiene relación con la potencia de la señal."
], "b"),
("En el contexto de la transmisión de datos, ¿cómo se define el indicador de la perturbación por ruído?", [
    "a) Se mide en decibelios.",
    "b) Se representa como la variación de frecuencia entre señal y ruido.",
    "c) Se expresa como la relación de potencia entre señal y ruido, definido como PotenciaSeñal / PotenciaRuido.",
    "d) Se calcula como la variación de amplitud entre señal y ruido."
], "c"),
("En relación con la atenuación en la transmisión de datos, ¿cómo se manifiesta este fenómeno?", [
    "a) La atenuación no afecta a la potencia del sinal.",
    "b) La atenuación provoca un aumento de la potencia del sinal a medida que aumenta la distancia de transmisión.",
    "c) La atenuación implica una pérdida de potencia (amplitud) a medida que aumenta la distancia de transmisión, con un efecto proporcional a la longitud del medio de transmisión.",
    "d) La atenuación solo ocurre en transmisiones inalámbricas."
], "c"),
("¿Qué sucede a partir de cierta distancia en la atenuación de la transmisión de datos y cómo se puede abordar este problema?", [
    "a) La atenuación no tiene impacto en la transmisión a larga distancia.",
    "b) La atenuación aumenta la potencia del sinal a medida que la distancia crece.",
    "c) A partir de cierta distancia, el sinal se vuelve tan fuerte que no se necesita repetidores ni amplificadores intermedios.",
    "d) A partir de cierta distancia, el sinal se debilita y no se puede interpretar la información, requiriendo el uso de repetidores y amplificadores intermedios."
], "d"),
("En relación con la atenuación en la transmisión de datos, ¿cómo se relaciona este fenómeno con la longitud del medio de transmisión?", [
    "c) La atenuación es inversamente proporcional a la longitud del medio de transmisión.",
    "b) La atenuación no está relacionada con la longitud del medio de transmisión.",
    "a) La atenuación tiene un efecto proporcional a la longitud del medio de transmisión.",
    "d) La atenuación aumenta a medida que disminuye la longitud del medio de transmisión."
], "a"),
("En el contexto de la atenuación en la transmisión de datos, ¿por qué a partir de cierta distancia la señal se vuelve tan débil que no se puede interpretar la información?", [
    "a) La atenuación no afecta la interpretación de la información a larga distancia.",
    "b) A mayor distancia, la atenuación disminuye, fortaleciendo la señal.",
    "c) La atenuación causa interferencias en la señal a medida que la distancia aumenta.",
    "d) A medida que la distancia aumenta, la atenuación debilita la señal, requiriendo repetidores y amplificadores intermedios para interpretar la información."
], "d"),
("¿Cuál es el objetivo principal de la multiplexación en la transmisión de datos?", [
    "a) Transmitir información de una única fuente o emisor por canal.",
    "b) Transmitir información de distintas fuentes o emisores por un mismo canal.",
    "c) Evitar la transmisión de información de diferentes emisores.",
    "d) Reducir la velocidad de transmisión de datos."
], "b"),
("¿Cuál es la base fundamental para la multiplexación en las comunicaciones?", [
    "a) Utilizar la capacidad del medio al 100% en todas las comunicaciones.",
    "b) Aprovechar al máximo la capacidad del medio de transmisión.",
    "c) Limitar la cantidad de información transmitida por canal.",
    "d) Garantizar que cada comunicación tenga su propio canal dedicado."
], "b"),
("¿Cuáles son los dos tipos principales de multiplexación?", [
    "a) Multiplexación por división de espacio y Multiplexación por división de potencia.",
    "b) Multiplexación por división de tiempo y Multiplexación por división en frecuencias.",
    "c) Multiplexación por división de señal y Multiplexación por división de velocidad.",
    "d) Multiplexación por división de canales y Multiplexación por división de codificación."
], "b"),
("¿En qué situación se utiliza la Multiplexación por División de Tiempo (TDM) según la información proporcionada?", [
    "a) Cuando la velocidad del medio (canal) es igual a la velocidad de los datos a transmitir.",
    "b) Únicamente se utiliza cuando la velocidad del medio es inferior a la velocidad de los datos.",
    "c) Cuando la velocidad del medio (canal) es superior a la velocidad de los datos a ser transmitidos.",
    "d) Se aplica solo en casos de comunicaciones inalámbricas."
], "c"),

("¿Cuándo sería apropiado utilizar la Multiplexación por División de Tiempo (TDM) según la situación planteada?", [
    "a) Cuando la velocidad de los emisores y receptores es igual a la velocidad del canal.",
    "b) Únicamente se utiliza cuando la velocidad de los emisores y receptores es mayor que la velocidad del canal.",
    "c) Cuando la velocidad de los emisores y receptores es menor que la velocidad del canal.",
    "d) Se aplica solo en casos de comunicaciones con igual velocidad en todos los componentes."
], "c"),
("En el contexto de la Multiplexación por División de Tiempo (TDM), ¿cómo se asigna el tiempo del canal a cada fuente de baja velocidad?", [
    "a) Todas las fuentes comparten el tiempo del canal simultáneamente.",
    "c) Cada fuente de baja velocidad recibe su propio canal dedicado.",
    "b) A cada fuente de baja velocidad se le asigna un fragmento de tiempo del canal.",
    "d) El tiempo del canal se asigna solo a las fuentes de alta velocidad."
], "b"),
("¿Cómo funciona la Multiplexación por División en Frecuencias (FDM)?", [
    "a) Cada fuente de datos tiene su propia canal dedicada.",
    "b) La canal se divide en segmentos de tiempo asignados a cada fuente.",
    "c) La canal se divide en bandas de frecuencia y estas se asignan a cada fuente de datos.",
    "d) Todas las fuentes comparten la misma banda de frecuencia simultáneamente."
], "c"),
("¿Cuál es la necesidad en el receptor al utilizar Multiplexación por División en Frecuencias (FDM)?", [
    "a) Utilizar un filtro de tiempo para distinguir las diferentes fuentes de emisión.",
    "b) No se requiere ningún filtro en el receptor.",
    "c) Emplear un filtro de amplitud para separar las señales de las diferentes fuentes.",
    "d) Es necesario emplear un filtro de frecuencias para distinguir las diferentes fuentes de emisión."
], "d"),
("¿Cuál es un ejemplo práctico de la aplicación de la Multiplexación por División en Frecuencias (FDM)?", [
    "a) La utilización de filtros de tiempo en emisoras de radio.",
    "b) La transmisión de señales sin la necesidad de asignar frecuencias específicas a cada emisora.",
    "c) En las emisiones de radio, cada emisora ocupa una posición en el dial o rango de frecuencias diferente.",
    "d) Todas las emisoras de radio comparten la misma frecuencia simultáneamente."
], "c"),
("¿Cuáles son algunos de los equipos necesarios para transmitir datos digitales sobre líneas de comunicación?", [
    "a) Antenas y amplificadores.",
    "b) Teclados y ratones.",
    "c) Módems, tarjetas de red, codificadores, decodificadores, etc.",
    "d) Pantallas y altavoces."
], "c"),
("¿Cuándo es posible enviar una señal sin modificaciones sobre el medio de transmisión?", [
    "a) Solo si la frecuencia de la señal es igual a la frecuencia de la onda del medio de transmisión.",
    "b) Siempre es posible enviar una señal sin modificaciones.",
    "c) Solo si la longitud de onda de la señal es menor que la del medio de transmisión.",
    "d) Si la frecuencia de la señal es mayor que la frecuencia de la onda del medio de transmisión."
], "a"),
("¿Cómo se denomina a la técnica en la que la frecuencia de la señal que se quiere transmitir coincide con la frecuencia de la onda empleada por el medio de transmisión?", [
    "a) Banda ancha.",
    "b) Banda lateral.",
    "c) Banda estrecha.",
    "d) Banda base."
], "d"),
("En el contexto de transmisión de señales, ¿qué técnica se utiliza cuando las frecuencias no coinciden, y es necesario adaptar la señal para que cumpla ciertas condiciones?", [
    "a) Banda base.",
    "b) Banda lateral.",
    "c) Banda ancha.",
    "d) Banda estrecha."
], "c"),
("¿Cómo se define la técnica de transmisión en Banda Base en el contexto de las comunicaciones?", [
    "a) Transmisión de señales sin modificaciones.",
    "b) Transmisión de señales adaptadas a diferentes frecuencias.",
    "c) Técnicas de transmisión en las que las frecuencias del medio coinciden con las frecuencias del sinal a transmitir.",
    "d) Transmisión de señales con cambios en la amplitud."
], "c"),
("¿Cuál es el propósito principal de las diferentes técnicas de codificación en las comunicaciones?", [
    "a) Modificar la frecuencia de la señal para una mejor transmisión.",
    "b) Facilitar la adaptación del sinal al medio de transmisión.",
    "c) Establecer un acuerdo entre emisor y receptor para intercambiar mensajes.",
    "d) Aumentar la potencia de la señal durante la transmisión."
], "c"),
("¿Cuál es el objetivo principal de los métodos de codificación en términos de mejorar la sincronización entre el emisor y el receptor?", [
    "a) Aumentar la velocidad de transmisión.",
    "b) Reducir la potencia de la señal.",
    "c) Mejorar la sincronización y aumentar la fiabilidad de la transmisión.",
    "d) Adaptar la señal al medio de transmisión."
], "c"),
("¿Qué método de codificación utilizaba Ethernet clásica para lograr la sincronización sin depender de un reloj externo?", [
    "a) PSG y PSG diferencial.",
    "b) Manchester y Manchester Diferencial.",
    "c) Bayern y Bayern Diferencial.",
    "d) Liverpool y Liverpool Diferencial."
], "b"),
("En el método de codificación Manchester, ¿cómo se representa el '0' y el '1' en términos de transiciones de voltaje?", [
    "a) '0' tiene una transición de – a + y '1' tiene una transición de + a -.",
    "b) '0' tiene una transición de + a - y '1' tiene una transición de – a +.",
    "c) Ambos '0' y '1' tienen una transición de + a -.",
    "d) Ambos '0' y '1' tienen una transición de – a +."
], "b"),
("En el método Manchester Diferencial de codificación, ¿cómo se distingue entre '0' y '1' en términos de transiciones de voltaje?", [
    "a) '0' tiene una transición + a – tanto al principio como en la mitad del intervalo, y '1' tiene cualquier transición de voltaje pero solo en la mitad del intervalo.",
    "b) '0' tiene una transición + a – en la mitad del intervalo, y '1' tiene una transición + a – tanto al principio como en la mitad del intervalo.",
    "c) '0' tiene cualquier transición de voltaje pero solo en la mitad del intervalo, y '1' tiene una transición + a – tanto al principio como en la mitad del intervalo.",
    "d) '0' tiene cualquier transición de voltaje pero solo en la mitad del intervalo, y '1' tiene cualquier transición de voltaje pero solo en la mitad del intervalo."
], "a"),
("En la transmisión en Banda Ancha, ¿cómo se define esta técnica en relación con las frecuencias de la onda en el medio y las frecuencias de la señal que se desea transmitir?", [
    "a) Las frecuencias de la onda en el medio coinciden con las frecuencias de la señal que se desea transmitir.",
    "b) Las frecuencias de la onda en el medio no coinciden con las frecuencias de la señal que se desea transmitir.",
    "c) Las frecuencias de la onda en el medio son inversamente proporcionales a las frecuencias de la señal que se desea transmitir.",
    "d) Las frecuencias de la onda en el medio son directamente proporcionales a las frecuencias de la señal que se desea transmitir."
], "b"),
("En el contexto de la transmisión, ¿cuáles son los elementos principales involucrados?", [
    "a) Receptor y transmisor.",
    "b) Portadora y moduladora.",
    "c) Frecuencia y amplitud.",
    "d) Analógico y digital."
], "b"),
("En el proceso de transmisión, ¿cómo se define la 'portadora'?", [
    "a) Es el medio físico de transmisión.",
    "b) Es la información que se desea transmitir.",
    "c) Es el canal por el cual se envía la señal.",
    "d) Es la señal del medio que transporta la información."
], "d"),
("En el contexto de la transmisión en banda ancha, ¿cómo se define la 'moduladora' según la información proporcionada?", [
    "a) Es la señal del medio que transporta la información.",
    "b) Es la información que se desea transmitir.",
    "c) Es el canal por el cual se envía la señal.",
    "d) Es la señal que modifica algún parámetro de la portadora y contiene la información."
], "d"),
("En el contexto de la transmisión en banda ancha, ¿cómo se define la 'moduladora' según la información proporcionada?", [
    "a) Es la señal del medio que transporta la información.",
    "b) Es la información que se desea transmitir.",
    "c) Es el canal por el cual se envía la señal.",
    "d) Es la señal que modifica algún parámetro de la portadora y contiene la información."
], "d"),
("En el contexto de una portadora analógica, ¿cuáles son las dos formas comunes de modular la señal?", [
    "a) Moduladora analógica y Moduladora digital.",
    "b) Moduladora analógica y Moduladora de amplitud.",
    "c) Moduladora digital y Moduladora de frecuencia.",
    "d) Moduladora de amplitud y Moduladora de fase."
], "a"),
("En el contexto de una moduladora analógica, ¿cuáles son las posibles técnicas de modulación que puede emplear?", [
    "a) Modulación de amplitud (AM) y de frecuencia (FM).",
    "b) Modulación de frecuencia (FM) únicamente.",
    "c) Modulación de fase (AM) únicamente.",
    "d) Modulación de amplitud (AM), modulación de frecuencia (FM) y modulación de fase (PM)."
], "d"),
("En el contexto de una moduladora digital, ¿cuáles son las posibles técnicas de modulación que puede emplear?", [
    "a) Modulación por desplazamiento de amplitud (ASK) únicamente.",
    "b) Modulación por desplazamiento de frecuencia (FSK) únicamente.",
    "c) Modulación por desplazamiento de fase (PSK) únicamente.",
    "d) Modulación por desplazamiento de amplitud (ASK), modulación por desplazamiento de frecuencia (FSK) y modulación por desplazamiento de fase (PSK)."
], "d"),
("En el contexto de una portadora digital, ¿cuál de las siguientes opciones describe correctamente la relación entre la portadora digital y la modulación?", [
    "a) La portadora digital es independiente de cualquier técnica de modulación.",
    "b) La portadora digital está asociada exclusivamente con la modulación analógica.",
    "c) La portadora digital se utiliza únicamente en la modulación digital.",
    "d) La portadora digital puede estar asociada tanto con la modulación analógica como con la modulación digital."
], "d"),
("En el contexto de una portadora digital utilizada para modulación analógica, ¿cuál es su función principal?", [
    "a) Transmitir señales digitales por medios digitales.",
    "b) Transmitir señales analógicas por medios digitales.",
    "c) Transmitir señales digitales por medios analógicos.",
    "d) No tiene ninguna función específica en la modulación analógica."
], "b"),
("¿Qué tipo de señal se utiliza comúnmente para transmitir la voz en telefonía móvil digital?", [
    "a) Señal analógica.",
    "b) Señal digital.",
    "c) Señal de frecuencia modulada.",
    "d) Señal de amplitud modulada."
], "b"),
("¿Qué problema se presenta en la portadora digital y modulación analógica?", [
    "a) Que son incompatibles.",
    "b) Que se infrautiliza el canal.",
    "c) Que se pierde potencia.",
    "d) No existe ningún problema, va todo bien."
], "b"),
("¿Qué variantes exiten en la portadora digital y modulación analógica?", [
    "a) PPM (Pulsos Modulados en Frecuencia) y PDM (Pulsos Modulados en Fase).",
    "b) PDM (Pulsos Modulados en Fase) y PAM (Pulsos Modulados en Amplitude).",
    "c) PCM (Modulación por Codificación de Pulsos) y PDM (Pulsos Modulados en Fase).",
    "d) PAM (Pulsos Modulados en Amplitude), PPM (Pulsos Modulados en Frecuencia) y PDM (Pulsos Modulados en Fase)."
], "d"),
("¿Cuántas y cuáles son las variantes de la portadora digital?", [
    "a) Dos variantes: PAM y PDM.",
    "b) Tres variantes: PAM, PPM, y PDM.",
    "c) Cuatro variantes: PAM, PPM, PDM, y PCM.",
    "d) Una variante: PDM."
], "b"),
("¿Qué caracteriza a la portadora digital con modulación digital?", [
    "a) Se utiliza comúnmente en transmisiones en banda base.",
    "b) No se utiliza en ningún caso debido a su obsolescencia.",
    "c) Es una forma especializada de transmisión en banda base que no se usa frecuentemente.",
    "d) Es el estándar principal en las comunicaciones modernas."
], "c"),
("¿Cómo se define un medio de transmisión?", [
    "a) Como el proceso de enviar señales desde el emisor hasta el receptor.",
    "b) Como el soporte físico que utiliza la señal para llegar desde el emisor hasta el receptor.",
    "c) Como el espacio que separa al emisor del receptor durante la transmisión de señales.",
    "d) Como la velocidad con la que viaja la señal desde el emisor hasta el receptor."
], "b"),
("¿Qué aspectos determina la naturaleza del medio de transmisión?", [
    "a) Solo el tipo de señal transmitida.",
    "b) Únicamente la calidad de la transmisión.",
    "c) Tanto el tipo de señal transmitida como las características y calidad de la transmisión.",
    "d) La velocidad de transmisión pero no la calidad."
], "c"),
("¿Por qué la elección del medio de transmisión es probablemente la parte más permanente del diseño de la red?", [
    "a) Porque es la opción más económica.",
    "b) Debido a su fácil reemplazo en caso de cambios en la red.",
    "c) Dado que afecta la estabilidad a largo plazo de la red.",
    "d) Solo influye en la calidad momentánea de la transmisión."
], "c"),
("¿Por qué es importante realizar adecuadamente la elección del cableado en el diseño de una red?", [
    "a) Porque afecta solo temporalmente el rendimiento de la red.",
    "b) Debido a su fácil sustitución en caso de problemas.",
    "c) Dado que la elección del cableado es probablemente la parte más permanente del diseño de la red.",
    "d) Porque no hay estándares que reduzcan las posibilidades de cableado."
], "c"),
("¿Qué se debe hacer para realizar una valoración objetiva de la necesidad de un cableado?", [
    "c) Evaluar únicamente las tecnologías disponibles en el momento actual.",
    "b) Considerar solo las necesidades actuales sin mirar al futuro.",
    "a) Realizar una valoración adecuada de las tecnologías disponibles y una estimación tanto de las necesidades actuales como de las futuras.",
    "d) No considerar las tecnologías disponibles y solo centrarse en las necesidades actuales."
], "a"),
("¿Por qué es importante mantenerse informado en el campo de cableado?", [
    "a) Porque no hay cambios frecuentes en productos y sistemas en este campo.",
    "b) Para evitar la aparición de nuevos productos y sistemas.",
    "c) Dado que este es un campo muy activo con frecuentes desarrollos de productos y sistemas.",
    "d) Porque la información sobre cableado no afecta significativamente a la red."
], "c"),
("¿Cuántos grandes grupos se pueden utilizar para clasificar los medios de transmisión, según el texto?", [
    "a) 1",
    "b) 2",
    "c) 3",
    "d) 4"
], "c"),
("¿Cuántos grandes grupos se pueden utilizar para clasificar los medios de transmisión?", [
    "a) 1",
    "b) 2, sin hilos y con hilos",
    "c) 3, cables metálicos, ópticos y sin hilos",
    "d) 4, cables metálicos, ópticos, sin hilos y wifi"
], "c"),
("¿En qué situaciones el cable metálico es el medio de transmisión más empleado?", [
    "a) En distancias muy largas y tasas de transferencia bajas.",
    "b) Solo en distancias muy cortas.",
    "d) En distancias no muy largas y cuando se necesitan tasas de transferencia elevadas.",
    "c) Exclusivamente en transmisiones inalámbricas."
], "d"),
("¿Cómo se transmite la información a través del cable?", [
    "a) A través de pulsos eléctricos de baja frecuencia.",
    "c) Mediante señales de radio.",
    "b) En forma de ondas electromagnéticas: corrientes eléctricas de alta frecuencia.",
    "d) Utilizando luz visible."
], "b"),
("¿Por qué el metal utilizado en cables siempre es el cobre?", [
    "c) Porque es el metal más barato.",
    "b) Debido a su alta conductividad y resistencia a grandes corrientes eléctricas.",
    "a) Por su alta conductividad, costo razonable, ductilidad y maleabilidad.",
    "d) Por su resistencia a la deformación sin romperse."
], "a"),
("¿Cuáles son los principales problemas de los cables metálicos?", [
    "c) Atenuación e interferencias ópticas.",
    "b) Resistencia e interferencias magnéticas.",
    "a) Atenuación e interferencias electromagnéticas.",
    "d) Pérdida de información y resistencia térmica."
], "a"),
("¿Qué se utiliza comúnmente para evitar los problemas de atenuación e interferencias electromagnéticas en los cables metálicos?", [
    "a) Cableado de mayor longitud.",
    "b) Cableado sin protección adicional.",
    "c) Cables apantallados.",
    "d) Cables con mayor resistencia eléctrica."
], "c"),
("¿Cuál fue el medio de transmisión más utilizado en los primeros tiempos de las LAN?", [
    "a) Cable de fibra óptica.",
    "b) Cable de pares.",
    "c) Cable coaxial.",
    "d) Transmisión inalámbrica."
], "c"),
("¿Cuál fue el medio más empleado en las comunicaciones telefónicas a larga distancia?", [
    "a) Cable de pares.",
    "b) Transmisión inalámbrica.",
    "c) Cable coaxial.",
    "d) Fibra óptica."
], "c"),
("En la actualidad, ¿dónde sigue siendo utilizado el cable coaxial?", [
    "a) Exclusivamente en comunicaciones telefónicas.",
    "b) Como cable principal en LAN.",
    "c) Como cable de distribución de televisión y para conectar hogares con nodos zonales en la tecnología HFC (Híbrido de Fibra Óptica y Coaxial).",
    "d) En comunicaciones inalámbricas."
], "c"),
("¿Cómo se compone un cable coaxial?", [
    "a) Con un núcleo de aluminio rodeado de material aislante.",
    "b) Con un núcleo de fibra óptica rodeado de plástico.",
    "c) Con un núcleo de cobre como transmisor rodeado de material aislante (plástico).",
    "d) Con un núcleo de hierro rodeado de material conductor."
], "c"),
("¿Cómo se protege el plástico en un cable coaxial y qué propósito tiene dicha protección?", [
    "a) No se protege.",
    "c) Con una capa adicional de plástico.",
    "b) Está cubierto por una malla protectora metálica (compuesta por malla de cobre o aluminio) para aislar de interferencias electromagnéticas.",
    "d) Con una capa de fibra óptica para mayor resistencia."
], "b"),
("¿Cómo se protege el cable coaxial contra interferencias electromagnéticas?", [
    "a) Con una cubierta de plástico.",
    "b) No se toma ninguna medida de protección.",
    "c) Mediante una malla protectora metálica compuesta por cobre o aluminio.",
    "d) Con una capa adicional de fibra óptica."
], "c"),
("¿Qué proporciona la construcción y la blindaje del cable coaxial?", [
    "a) Ancho de banda bajo y resistencia al ruido pobre.",
    "b) Ancho de banda alto y excelente inmunidad frente al ruido.",
    "c) Ancho de banda variable y baja inmunidad al ruido.",
    "d) Ancho de banda alto pero vulnerable al ruido."
], "b"),
("¿Qué factores determinan el ancho de banda posible en el cable coaxial?", [
    "a) Solo la longitud del cable.",
    "b) Solo la relación señal/ruido del señal de datos.",
    "d) Tanto la longitud del cable como la relación señal/ruido del señal de datos.",
    "c) Ningún factor afecta al ancho de banda posible."
], "d"),
("¿Cuántos tipos de cable coaxial existen?", [
    "a) Uno, cable coaxial a secas.",
    "b) Dos, coaxial de banda ancha y coaxial de banda base.",
    "c) Tres, coaxial de banda ancha, coaxial de banda base y coaxial de banda Manchester.",
    "d) Cuatro, coaxial de banda ancha, coaxial de banda estrecha, coaxial de banda base y coaxial de banda masiva."
], "b"),
("¿Para qué se utiliza el cable coaxial de banda ancha en las comunicaciones telefónicas?", [
    "a) Como nivel intermedio entre cable coaxial de banda base y fibra óptica.",
    "b) Exclusivamente en redes LAN.",
    "c) Para conectar hogares con nodos zonales en la tecnología HFC.",
    "d) Para transmisiones inalámbricas."
], "a"),
("¿En qué tipo de instalaciones se utiliza también el cable coaxial de banda ancha?", [
    "a) Exclusivamente en redes de fibra óptica.",
    "b) Solo en comunicaciones telefónicas.",
    "c) En instalaciones de televisión por cable.",
    "d) En transmisiones inalámbricas."
], "c"),
("¿Cuál es la impedancia del cable coaxial de banda ancha?", [
    "a) 50 Ω",
    "b) 75 Ω",
    "c) 100 Ω",
    "d) 125 Ω"
], "b"),
("¿En qué situaciones se utiliza el cable coaxial de banda ancha en redes LAN?", [
    "a) Cuando se prefiere utilizar fibra óptica.",
    "b) Cuando se necesita poca capacidad de transmisión.",
    "c) Cuando se requiere mucha capacidad pero no se desea utilizar la fibra óptica.",
    "d) Exclusivamente en transmisiones inalámbricas."
], "c"),
("¿Cuál es el estado actual del cable coaxial de banda base?", [
    "a) En pleno uso y expansión.",
    "b) En desuso.",
    "c) Utilizado exclusivamente en comunicaciones telefónicas.",
    "d) En constante desarrollo tecnológico."
], "b"),
("¿Cuál es la impedancia del cable coaxial de banda base?", [
    "a) 25 Ω",
    "b) 50 Ω",
    "c) 75 Ω",
    "d) 100 Ω"
], "b"),
("¿Cuántos tipos de cable coaxial de banda base existen?", [
    "a) Uno, de banda base a secas.",
    "b) Dos, fino y grueso.",
    "c) Tres, de baja frecuencia, de media frecuencia y de alta frecuencia.",
    "d) Cuatro, de un hilo, de dos hilos, de tres hilos y de cuatro hilos."
], "b"),
("¿En qué redes se utiliza el cable coaxial fino?", [
    "a) En redes Ethernet 10BASE5.",
    "b) En redes 10BASE2 con una velocidad de 10Mbps.",
    "c) En redes de fibra óptica.",
    "d) Exclusivamente en transmisiones inalámbricas."
], "b"),
("¿Cómo se conoce al cable coaxial fino en las redes 10BASE2?", [
    "a) Cheapernet",
    "b) Thicknet",
    "c) FastEthernet",
    "d) Coaxnet"
], "a"),
("¿En qué redes se utiliza el cable coaxial grueso?", [
    "a) En redes Ethernet 10BASE2.",
    "b) En redes de fibra óptica.",
    "c) En redes 10BASE5.",
    "d) Exclusivamente en comunicaciones telefónicas."
], "c"),
("¿Cuáles son las características del cable coaxial grueso?", [
    "a) Grosor de 2cm y costo bajo.",
    "b) Grosor de 1cm y costo alto.",
    "c) Grosor de 0.5cm y costo medio.",
    "d) Grosor variable y costo variable."
], "b"),
("En la actualidad, ¿quién sigue utilizando ampliamente el cable coaxial en las instalaciones de red para la parte del cliente?", [
    "a) Exclusivamente las redes 10BASE5.",
    "b) Proveedores de servicios telefónicos.",
    "c) Proveedores de internet.",
    "d) Redes de fibra óptica."
], "c"),
("¿Cuál es uno de los medios de transmisión más antiguos y aún ampliamente utilizado en redes LAN y como cable telefónico?", [
    "a) Cable coaxial.",
    "b) Fibra óptica.",
    "c) Cable de par trenzado.",
    "d) Cable de red inalámbrica."
], "c"),
("¿Cómo está construido el cable de par trenzado comúnmente utilizado, consistiendo en 4 pares de 2 alambres de cobre de aproximadamente 1mm de grosor trenzados de manera helicoidal y envueltos en un plástico protector?", [
    "a) 8 pares de cables de aluminio.",
    "b) 2 pares de cables de fibra óptica.",
    "c) 4 pares de 2 alambres de cobre de aproximadamente 1mm de grosor trenzados de manera helicoidal y envueltos en un plástico protector.",
    "d) 16 pares de cables de red inalámbrica."
], "c"),
("¿Cuál es el propósito de trenzar los cables?",
 ["a) Aumentar la resistencia eléctrica.",
  "b) Evitar la formación de una antena.",
  "c) Mejorar la transmisión magnética.",
  "d) Reducir la velocidad de transmisión."],
 "b"),
("¿Qué problema se intenta evitar al trenzar los cables en lugar de dejarlos paralelos?",
 ["a) Pérdida de señal.",
  "b) Formación de una antena.",
  "c) Aumento de la velocidad de transmisión.",
  "d) Mayor resistencia eléctrica."],
 "b"),
("¿Cómo se llama el fenómeno que se quiere prevenir al trenzar los cables?",
 ["a) Interferencia magnética.",
  "b) Antena colectiva.",
  "c) Trenzado electromagnético.",
  "d) Formación de antena."],
 "d"),
("¿Cuál sería el resultado si los dos cables fueran dejados paralelos en lugar de ser trenzados?",
 ["a) Mayor velocidad de transmisión.",
  "b) Menor resistencia eléctrica.",
  "c) Formación de una antena.",
  "d) Reducción de la interferencia magnética."],
 "c"),
("¿Qué efecto tiene el trenzado en la reducción de la interferencia eléctrica entre dos pares de cables vecinos y la que podrían recibir del exterior?",
 ["a) Aumenta la interferencia eléctrica.",
  "b) No tiene impacto en la interferencia.",
  "c) Reduce la interferencia entre pares vecinos y del exterior.",
  "d) Solo afecta la interferencia del exterior."],
 "c"),
("¿Qué características destacan sobre la instalación y velocidad de transmisión de un sistema que puede alcanzar hasta 1Gbps?",
 ["a) Difícil instalación y velocidad limitada.",
  "b) Fácil instalación y velocidad limitada.",
  "c) Difícil instalación y velocidad de hasta 1Gbps.",
  "d) Fácil instalación y velocidad de hasta 1Gbps."],
 "d"),
("¿Cuál es uno de los aspectos destacados de este sistema en términos de economía y uso común en redes LAN?",
 ["a) Es costoso y raramente utilizado en redes LAN.",
  "b) Es económico y comúnmente utilizado en redes LAN.",
  "c) Es costoso y ampliamente utilizado en redes LAN.",
  "d) Es económico pero poco utilizado en redes LAN."],
 "b"),
("¿Cómo se llaman los conectores utilizados en cables de par trenzado?",
 ["a) Conectores RJ-11.",
  "b) Conectores RJ-22.",
  "c) Conectores RJ-45.",
  "d) Conectores RJ-58."],
 "c"),
("¿Cuántos tipos principales de cables de par trenzado existen según estén o no apantallados?",
 ["a) 1",
  "b) 2",
  "c) 3",
  "d) 4"],
 "b"),
("¿Cómo se conoce comúnmente al cable de par trenzado no apantallado?",
 ["a) FTP (Foiled Twisted Pair).",
  "b) STP (Shielded Twisted Pair).",
  "c) UTP (Unshielded Twisted Pair).",
  "d) NTP (Non Twisted Pair)."],
 "c"),
("¿Cuál es el cable más utilizado en las redes LAN debido a sus características?",
 ["a) Cable coaxial.",
  "b) Par trenzado apantallado.",
  "c) Fibra óptica.",
  "d) Par trenzado no apantallado (UTP)."],
 "d"),
("¿Cuáles son algunas de las características del cable de par trenzado que se destacan, como ser ligero, flexible, fácil de instalar y económico?",
 ["a) Fibra óptica.",
  "b) Cable coaxial.",
  "c) Par trenzado apantallado.",
  "d) Par trenzado no apantallado (UTP)."],
 "d"),
("¿Cómo se denomina el cable de par trenzado con pantalla individual para cada par, diseñado para reducir la interferencia eléctrica?",
 ["a) UTP (Unshielded Twisted Pair).",
  "b) FTP (Foiled Twisted Pair).",
  "c) STP (Shielded Twisted Pair).",
  "d) NTP (Non Twisted Pair)."],
 "c"),
("¿Cuál es una de las razones por las que el par trenzado blindado (STP) es menos utilizado en comparación con el par trenzado no apantallado (UTP)?",
 ["a) Menor interferencia eléctrica.",
  "b) Menor volumen y costo.",
  "c) Mayor flexibilidad.",
  "d) El par trenzado no apantallado no es menos utilizado que el UTP."],
 "b"),
("¿Cómo se conoce a la variedad de par trenzado apantallado que tiene una pantalla global para todo el conjunto?",
 ["a) UTP (Unshielded Twisted Pair) y FTP (Foiled Twisted Pair).",
  "b) FTP (Foiled Twisted Pair) y NPC (New Protocol Coaxial).",
  "c) STP (Shielded Twisted Pair) o FTT (Flex Twisted Tee).",
  "d) ScTP (Screened Twisted Pair) o FTP (Foiled Twisted Pair)."],
 "d"),
 ("¿Qué factores influyen en la frecuencia y la tasa de transferencia máxima que se pueden transmitir por un cable de par trenzado?",
 ["a) Solo el grosor del cable.",
  "b) Grosor del cable, distancia, tipo de aislamiento, densidad de vueltas del trenzado, etc.",
  "c) Solo la distancia.",
  "d) Solo el tipo de aislamiento."],
 "b"),
("Tomando como ejemplo Gigabit Ethernet, ¿cuántos megabits por segundo (Mbps) puede transmitir cada par en un cable de par trenzado, cuando se utilizan 4 pares en total y la distancia alcanza hasta 100 metros?",
 ["a) 100 Mbps por cada par.",
  "b) 250 Mbps por cada par.",
  "c) 500 Mbps por cada par.",
  "d) 1 Gbps por cada par."],
 "b"),
("En el caso de ADSL, ¿a qué velocidad puede transmitir por un solo par de cable telefónico a distancias de hasta 5 km?",
 ["a) 2 Mbps.",
  "b) 4 Mbps.",
  "c) 6 Mbps.",
  "d) 8 Mbps."],
 "d"),
("¿Cómo se clasifican los diferentes tipos de cables de par trenzado según las normativas de cableado estructurado?",
 ["a) Por su grosor y velocidad de transmisión.",
  "b) Por su color y longitud.",
  "c) Por categorías de acuerdo con sus características para la transmisión de datos, que dependen del número de vueltas por metro del trenzado y del material aislante.",
  "d) Por su flexibilidad y resistencia eléctrica."],
 "c"),
("En relación con la categoría del par trenzado, ¿cómo afecta el aumento de la categoría a la atenuación y a la propagación de las señales en el medio, así como a la tasa de transferencia?",
 ["a) Aumenta la atenuación y disminuye la propagación de las señales.",
  "b) Aumenta la atenuación y mejora la propagación de las señales.",
  "c) Disminuye la atenuación y mejora la propagación de las señales.",
  "d) Disminuye la atenuación y disminuye la propagación de las señales."],
 "c"),
("En conclusión, ¿qué representa la clasificación en categorías en términos de una instalación de par trenzado?",
 ["a) Indica el color de los cables.",
  "b) Es un indicador de la longitud máxima permitida.",
  "c) Es un indicador de la velocidad de transmisión que puede lograrse en una instalación.",
  "d) Indica el grosor del cable."],
 "c"),
("¿Cuáles son algunos de los errores comunes que pueden ocurrir si la instalación no se realiza con suficiente cuidado?",
 ["a) Usar conectores de colores incorrectos.",
  "b) No asegurar adecuadamente las bridas.",
  "c) Destrenzar excesivamente los conectores, doblar el cable en exceso, y apretar demasiado las bridas.",
  "d) No doblar el cable en absoluto."],
 "c"),
("¿Cuál es la estimación para el porcentaje de instalaciones de categoría 5 que no soportarán Gigabit Ethernet, principalmente debido a problemas relacionados con los conectores?",
 ["a) Entre un 1 y un 5%.",
  "b) Entre un 5 y un 10%.",
  "c) Entre un 10 y un 15%.",
  "d) Entre un 15 y un 20%."],
 "b"),
("En el caso de un cable de categoría 5, ¿cuál es la recomendación para la longitud de los cables destrenzados para lograr una tasa de transferencia de 100Mbps?",
 ["a) No hay restricción en la longitud de los cables destrenzados.",
  "b) Debería ser superior a los 13mm.",
  "c) Debería ser exactamente de 13mm.",
  "d) No debería superar los 13mm."],
 "d"),
("¿Cómo se transportan los señales digitales de datos en la fibra de vidrio?",
 ["a) Mediante corriente eléctrica.",
  "b) Mediante pulsos modulados de luz visible.",
  "c) Mediante ondas de sonido.",
  "d) Mediante pulsos de radiofrecuencia."],
 "b"),

("¿Cuál es una de las ventajas de la fibra de vidrio en términos de seguridad en la transmisión de datos?",
 ["a) Sensibilidad a interferencias electromagnéticas.",
  "b) Vulnerabilidad a señales eléctricas externas.",
  "c) Seguridad ante interferencias electromagnéticas externas.",
  "d) Inmunidad a la luz visible."],
 "c"),
("¿Cómo está compuesta una fibra óptica en términos de su estructura interna?",
 ["a) Núcleo de metal.",
  "b) Núcleo de plástico.",
  "c) Núcleo muy delgado de vidrio capaz de conducir un rayo óptico por su interior.",
  "d) Núcleo de madera."],
 "c"),
("¿Cómo está estructurada la composición de una fibra óptica en términos de revestimientos?",
 ["a) Núcleo de plástico, revestimiento de metal y cubierta de madera.",
  "b) Núcleo de metal, revestimiento de vidrio y cubierta de plástico.",
  "c) Núcleo de vidrio, revestimiento de plástico y cubierta protectora de madera.",
  "d) Núcleo delgado de vidrio, revestimiento de plástico (generalmente vidrio) y cubierta protectora (generalmente plástico)."],
 "d"),
("En una fibra óptica, ¿cómo se comporta el rayo de luz en términos de reflexión contra las paredes?",
 ["a) Refleja únicamente en ángulos cerrados.",
  "b) Refleja únicamente en ángulos agudos.",
  "c) Refleja en ángulos muy abiertos, prácticamente avanzando por el centro de la fibra.",
  "d) No experimenta reflexión."],
 "c"),
("¿Cuál es una de las distinciones clave entre la fibra óptica y el cable eléctrico en términos de transmisión de señales?",
 ["a) Los cables eléctricos no tienen pérdida ni atenuación.",
  "b) La fibra óptica no permite el avance de señales de luz.",
  "c) Los cables eléctricos tienen mayor alcance que la fibra óptica.",
  "d) Los señales de luz pueden avanzar sin pérdida ni atenuación a grandes distancias en la fibra óptica."],
 "d"),
("¿Cuáles son algunas de las principales ventajas de la fibra óptica?",
 ["a) Baja tasa de transferencia y alta susceptibilidad al ruido.",
  "b) Alta tasa de transferencia, inmunidad al ruido y a interferencias electromagnéticas, baja atenuación y ausencia de fugas de luz.",
  "c) Baja tasa de errores y alta atenuación.",
  "d) Alta tasa de transferencia, alta susceptibilidad al ruido y a interferencias electromagnéticas, y alta tasa de errores."],
 "b"),
("La fibra óptica tiene una baja tasa de transferencia.",
 ["v) Verdadero.",
  "f) Falso.",
],
 "f"),
("La fibra óptica es inmune al ruido y a las interferencias electromagnéticas.",
 ["v) Verdadero.",
  "f) Falso.",
],
 "v"),
("La fibra óptica tiene baja atenuación.",
 ["v) Verdadero.",
  "f) Falso.",
],
 "v"),
("La fibra óptica no tiene fugas de luz.",
 ["v) Verdadero.",
  "f) Falso.",
],
 "v"),
 ("La fibra óptica tiene bajo Bit Error Rate.",
 ["v) Verdadero.",
  "f) Falso.",
],
 "v"),
 ("La fibra óptica es gruesa y pesada.",
 ["v) Verdadero.",
  "f) Falso.",
],
 "f"),
 ("Una de las ventajas de la fibra óptica es su bajo coste.",
 ["v) Verdadero.",
  "f) Falso.",
],
 "f"),
("La fibra óptica es fácil de instalar y no requiere especialistas.",
 ["v) Verdadero.",
  "f) Falso.",
],
 "f"),
("La fibra óptica tiene facilidad para conectarse a ella (lo que indirectamente produce una vulnerabilidad en la seguridad para el robo de señal).",
 ["v) Verdadero.",
  "f) Falso.",
],
 "f"),
 ("¿En qué parte del espectro electromagnético se utilizan las frecuencias de 0.85, 1.30 y 1.55 micras (μm) para las comunicaciones con fibra óptica?",
 ["a) Espectro ultravioleta.",
  "b) Espectro visible.",
  "c) Espectro infrarrojo.",
  "d) Espectro de microondas."],
 "c"),
("¿Cuál es la pérdida por atenuación de las frecuencias de 1.30 y 1.55 micras (μm) (infrarrojos) en las comunicaciones ópticas?",
 ["a) Más del 5% por kilómetro.",
  "b) Menos del 1% por kilómetro.",
  "c) Exactamente del 5% por kilómetro.",
  "d) Menos del 5% por kilómetro."],
 "d"),
 ("Debido a la baja pérdida por atenuación, ¿a qué distancia son necesarios los repetidores en las comunicaciones con fibra ópticas?",
 ["a) A distancias inferiores a 10 km.",
  "b) A distancias de aproximadamente 50 km.",
  "c) A distancias de alrededor de 100 km.",
  "d) A distancias superiores a 200 km."],
 "c"),
("¿Cuál es el medio de transmisión más utilizado para comunicaciones a larga distancia debido a sus características?",
 ["a) Cable coaxial.",
  "b) Par trenzado no apantallado (UTP).",
  "c) Fibra óptica.",
  "d) Cable de par trenzado apantallado (STP)."],
 "c"),
("¿Por qué, en el caso de fibras de vidrio que transmiten señales en una única dirección (simplex), se requieren dos fibras para lograr una comunicación full-dúplex?",
 ["a) Porque las fibras de vidrio no permiten la transmisión full-dúplex.",
  "b) Porque las fibras de vidrio solo pueden transmitir en una dirección.",
  "c) Porque la comunicación full-dúplex solo es posible con cables de cobre.",
  "d) Porque para una comunicación full-dúplex se necesitan fibras independientes para cada sentido de transmisión."],
 "d"),
("¿Cuáles son los dos tipos de fibra óptica utilizados actualmente para la transmisión de datos?",
 ["a) Fibra óptica de un solo modo y fibra de vidrio.",
  "b) Fibra óptica monocromática y fibra multimodo.",
  "c) Fibra multimodo y fibra monomodo.",
  "d) Fibra de un solo sentido y fibra de doble sentido."],
 "c"),
("¿Cómo se utiliza la luz en las fibras multimodo para la transmisión de datos?",
 ["a) La luz se genera de forma continua.",
  "b) La luz se genera en forma de pulsos utilizando LED's y tiene varias frecuencias.",
  "c) La luz se genera mediante láser a una sola frecuencia.",
  "d) La luz se refleja en las paredes de la fibra sin pulsos."],
 "b"),
("¿Cuál es el ancho típico del núcleo en las fibras multimodo?",
 ["a) 25 o 50 µm.",
  "b) 50 o 62,5 µm.",
  "c) 75 µm.",
  "d) 125 µm."],
 "b"),
("¿Cuál es el ancho típico de la cubierta en las fibras multimodo?",
 ["a) 25 o 50 µm.",
  "b) 50 o 62,5 µm.",
  "c) 75 µm.",
  "d) 125 µm."],
 "d"),
("¿Cómo se utiliza la luz en las fibras monomodo para la transmisión de datos?",
 ["a) La luz se genera de forma continua.",
  "b) La luz se genera en forma de pulsos utilizando LED's y tiene varias frecuencias.",
  "c) La luz se genera mediante láser a una sola frecuencia.",
  "d) La luz se refleja en las paredes de la fibra sin pulsos."],
 "c"),
("¿Cuál es el ancho típico del núcleo en las fibras monomodo?",
 ["a) 25 µm.",
  "b) 50 µm.",
  "c) 75 µm.",
  "d) 9 µm."],
 "d"),
("¿Cuál es el ancho típico de la cubierta en las fibras monomodo?",
 ["a) 125 µm.",
  "b) 50 µm.",
  "c) 75 µm.",
  "d) 9 µm."],
 "a"),
("¿Cuál es la atenuación típica en fibra monomodo para la transmisión de luz infrarroja a 1500 nm?",
 ["a) 0,5 dB/km.",
  "b) 1,0 dB/km.",
  "c) 2,5 dB/km.",
  "d) 5,0 dB/km."],
 "c"),
("En la transmisión de un cable UTP-5 con una frecuencia de 62,5MHz, ¿cuál es la atenuación típica en 100 metros?",
 ["a) 5 dB.",
  "b) 10 dB.",
  "c) 17 dB.",
  "d) 20 dB."],
 "c"),
("¿Cuál es una ventaja de las fibras multimodo en comparación con las monomodo en redes LAN?",
 ["a) Las fibras multimodo son más caras que las monomodo.",
  "b) Las fibras multimodo tienen una vida media más corta que las monomodo.",
  "c) Los LED's utilizados en fibras multimodo tienen una vida media mayor que los láser de las monomodo.",
  "d) Las fibras multimodo solo permiten tasas de transferencia de hasta 1 Gbps."],
 "c"),
("En redes de área extensa, ¿por qué se prefieren las fibras monomodo sobre las multimodo?",
 ["a) Las fibras monomodo son más baratas.",
  "b) Las fibras monomodo permiten una vida media más larga de los emisores láser.",
  "c) Las fibras monomodo pueden alcanzar distancias de más de 100 km sin repetidores.",
  "d) Las fibras monomodo solo permiten tasas de transferencia de hasta 1 Gbps."],
 "c"),
("¿Qué significa la sigla FTTH en telecomunicaciones?",
 ["a) Fast Transfer to Home.",
  "b) Fiber To The Home.",
  "c) Faster Transmission Through Hubs.",
  "d) Frequency Transmission for Home."],
 "b"),
("En el diseño de la infraestructura de red, ¿qué aspectos podrían influir en la elección entre cable de par trenzado y fibra óptica?",
 ["a) La disponibilidad de conectores RJ-45.",
  "b) La distancia que se necesita cubrir sin repetidores.",
  "c) La preferencia por cables más ligeros y flexibles.",
  "d) La elección entre luz infrarroja y luz visible para la transmisión de datos."],
 "b"),
("¿En qué situaciones suele ser preferible elegir fibra óptica en comparación con el cable de par trenzado?",
 ["a) En redes locales (LAN).",
  "b) En distancias cortas dentro de un mismo edificio.",
  "c) Cuando se necesita gran seguridad y es difícil manipular las fibras ópticas.",
  "d) En conexiones entre dispositivos dentro de un mismo rack de servidores."],
 "c"),
("¿Entre qué se suele elegir como medio físico a la hora de diseñar la red?",
 ["a) Entre el UTP categoría 5e o 6 y la fibra óptica multimodo.",
  "b) Entre cable coaxial RJ-45 y fibra óptica multimodo.",
  "c) Entre cable coaxial RJ-45 y fibra óptica monomodo.",
  "d) Entre cable de part renzado y fibra óptica multimodo.."],
 "a"),
("En qué situaciones se elegiría preferentemente fibra óptica en el diseño de cableado de una red?",
 ["a) Cuando se requiere cableado para conexiones dentro de un mismo edificio.",
  "b) Siempre que sea posible, independientemente de las condiciones.",
  "c) Cuando los edificios están ubicados a distancias cortas.",
  "d) Cuando el cableado conecta edificios diferentes y hay riesgo de interferencias eléctricas, necesidad de seguridad, o exposición a ambientes corrosivos."],
 "d"),
("En qué situaciones se preferiría el uso de cable UTP en lugar de fibra óptica?",
 ["a) Siempre, independientemente de las circunstancias.",
  "b) Cuando se requiere alta seguridad en la transmisión de datos.",
  "c) Cuando el presupuesto es un factor importante y no se cumplen las condiciones específicas para la elección de fibra óptica.",
  "d) Únicamente cuando se conectan edificios diferentes."],
 "c"),
("Cuál es la práctica general en una instalación grande en cuanto al uso de fibra y UTP?",
 ["a) Se utiliza únicamente fibra para todos los componentes de la instalación.",
  "b) La fibra se emplea solo en el cableado horizontal dentro del edificio.",
  "c) Se utiliza fibra para los tendidos principales y UTP para el cableado horizontal dentro del edificio.",
  "d) UTP se utiliza exclusivamente para unir edificios diferentes."],
 "c"),
("¿En qué situación se puede utilizar UTP para el cableado vertical en instalaciones pequeñas?",
 ["a) Únicamente cuando las distancias entre armarios son grandes.",
  "b) Siempre se utiliza UTP para el cableado vertical en instalaciones pequeñas.",
  "c) Solo cuando se requiere una gran seguridad.",
  "d) Cuando las distancias entre armarios son pequeñas en instalaciones pequeñas."],
 "d"),
("¿Cómo se conoce el cableado realizado siguiendo las normas establecidas para el interior de edificios?",
 ["a) Cableado básico.",
  "b) Cableado estándar.",
  "c) Cableado estructurado.",
  "d) Cableado interno."],
 "c"),
("¿Qué permite integrar el cableado estructurado en el interior de edificios?",
 ["a) Solo datos.",
  "b) Solo telefonía.",
  "c) Voz (telefonía) y datos (red local).",
  "d) Electricidad y datos."],
 "c"),
("¿Cuáles son las normas que rigen el cableado estructurado en Estados Unidos y Europa?",
 ["a) EIA/TIA 568-A en Estados Unidos y ISO/IEC 11801 en Europa.",
  "b) ISO/IEC 11801 en Estados Unidos y EIA/TIA 568-A en Europa.",
  "c) ANSI/TIA-568-C en Estados Unidos y ISO/IEC 11801 en Europa.",
  "d) EIA/TIA 568-A en Estados Unidos y ANSI/TIA-568-C en Europa."],
 "a"),
("¿Por qué es habitual cumplir ambas normativas (EIA/TIA 568-A y ISO/IEC 11801) al diseñar un cableado?",
 ["a) Para aumentar los costos de instalación.",
  "b) Para asegurar la máxima compatibilidad con todos los fabricantes.",
  "c) Porque es una recomendación opcional.",
  "d) Para simplificar el proceso de diseño."],
 "b"),
("¿Cuál es la ventaja de seguir las normas de cableado estructurado (EIA/TIA 568-A e ISO/IEC 11801)?",
 ["a) Aumentar la complejidad de la red.",
  "b) Evitar problemas si decidimos modificar las tecnologías de nuestra red local.",
  "c) Garantizar un mayor rendimiento en la transmisión de datos.",
  "d) Reducir la compatibilidad con otros fabricantes."],
 "b"),
("¿Cuál es la longitud máxima del enlace cuando se utiliza cable de par trenzado en sistemas de cableado estructurado?",
 ["a) 50m", "b) 75m", "c) 100m", "d) 150m"],
 "c"),
("¿En general, qué se emplea para los tendidos principales en instalaciones grandes, como uniones entre edificios y cableado vertical para distribución por andares dentro del edificio?",
 ["a) Par trenzado no apantallado (UTP)", "b) Par trenzado apantallado (STP)", "c) Fibra óptica", "d) Coaxial"],
 "c"),
("¿Qué se utiliza para el cableado horizontal, hasta los despachos, en general?",
 ["a) Par trenzado no apantallado (UTP)", "b) Par trenzado apantallado (STP)", "c) Fibra óptica", "d) Coaxial"],
 "a"),

("En instalaciones pequeñas, ¿qué se emplea también para el cableado vertical junto con la fibra?",
 ["a) Par trenzado no apantallado (UTP)", "b) Par trenzado apantallado (STP)", "c) Fibra óptica", "d) Coaxial"],
 "a"),
("¿Qué es más eficiente, desde el punto de vista del mantenimiento, en el diseño de cableado?",
 ["a) Pocos armarios de cableado grandes", "b) Muchos armarios de cableado pequeños"],
 "a"),
("¿Cómo se aconseja diseñar el reparto de armarios en un edificio?",
 ["a) Con radios de 100m, ubicando un armario en cada centro", "b) Con radios de 50m, ubicando varios armarios pequeños"],
 "a"),
("Al planificar la instalación del cableado LAN, ¿cuáles son las cuatro áreas físicas que se deben considerar?",
 ["a) Área de trabajo, área de descanso, sala de servidores, área de almacenamiento.",
  "b) Área de trabajo, cuarto de comunicaciones, cableado backbone (o vertical), cableado de distribución.",
  "c) Área de descanso, cuarto de comunicaciones, cableado vertical, sala de servidores.",
  "d) Área de trabajo, sala de servidores, cableado horizontal, área de almacenamiento."],
 "b"),
("En las instalaciones de cable de par trenzado UTP, ¿cuál es la limitación de longitud total combinada para el cable que abarca las cuatro áreas (área de trabajo, cuarto de comunicaciones, cableado backbone, cableado de distribución) según el estándar?",
 ["a) 50m por canal.",
  "b) 75m por canal.",
  "c) 100m por canal.",
  "d) 150m por canal."],
 "c"),
("Según este estándar, ¿cuántos metros de latiguillo o patch cable se pueden utilizar para conectar los patch panels con los switches?",
 ["a) Hasta 1 metro.",
  "b) Hasta 2 metros.",
  "c) Hasta 3 metros.",
  "d) Hasta 5 metros."],
 "d"),
("¿Cómo se pueden utilizar los restantes 5 metros de cable desde el punto de terminación del cableado en la pared hasta el computador?",
 ["a) No se pueden utilizar.",
  "b) Solo se pueden utilizar para teléfonos.",
  "c) Pueden utilizarse para cualquier propósito.",
  "d) Solo se pueden utilizar para conectar impresoras."],
 "c"),
("¿Cuál es la recomendación del estándar EIA/TIA para la longitud máxima de los cables UTP utilizados para conectar dispositivos a las rosetas en las áreas de trabajo?",
 ["a) 2 metros.",
  "b) 3 metros.",
  "c) 5 metros.",
  "d) 8 metros."],
 "c"),
("¿Cómo se describen las áreas de trabajo en el contexto de la instalación de cableado LAN?",
 ["a) Son las ubicaciones de los servidores.",
  "b) Son las áreas de descanso de los usuarios.",
  "c) Son las ubicaciones para los dispositivos finales utilizados por los usuarios individuales.",
  "d) Son las áreas donde se almacenan los cables de red."],
 "c"),
("¿Cuál es la recomendación para la cantidad mínima de rosetas en cada área de trabajo para conectar equipos según el estándar?",
 ["a) 1 roseta.",
  "b) 2 rosetas.",
  "c) 3 rosetas.",
  "d) 4 rosetas."],
 "b"),
("¿Cómo se utilizan los latiguillos (patch cords) en el contexto de conectar dispositivos individuales a las rosetas en las áreas de trabajo?",
 ["a) No se utilizan en absoluto.",
  "b) Se utilizan para conectar dispositivos a los servidores.",
  "c) Se utilizan para conectar dispositivos individuales a las rosetas.",
  "d) Se utilizan solo para conexiones telefónicas."],
 "c"),
("Según el estándar EIA/TIA, ¿cuál es la lonxitude máxima recomendada para los cables UTP utilizados para conectar dispositivos a las rosetas en las áreas de trabajo?",
 ["a) 2 metros.",
  "b) 3 metros.",
  "c) 5 metros.",
  "d) 8 metros."],
 "c"),
("¿Cuál es la función principal del cuarto de telecomunicaciones en un sistema de cableado?",
 ["a) Almacenamiento de documentos importantes.",
  "b) Realización de conexiones con dispositivos finales.",
  "c) Conexión con dispositivos intermedios como hubs, switchs y routers.",
  "d) Almacenamiento de material de oficina."],
 "c"),
("¿Cuál es la función del cuarto de telecomunicaciones en relación con el cableado backbone y el cableado horizontal?",
 ["a) Almacenar dispositivos finales.",
  "b) Proporcionar conexión directa a Internet.",
  "c) Proporcionar transición entre el cableado backbone y el cableado horizontal.",
  "d) Almacenar cables de reserva."],
 "c"),
("¿Qué función realizan los latiguillos dentro del cuarto de telecomunicaciones?",
 ["a) Almacenar cables horizontales.",
  "b) Conectar dispositivos finales a los patch panels.",
  "c) Proporcionar conexión directa a Internet.",
  "d) Realizar conexiones entre los patch panels, donde terminan los cables horizontales, y los dispositivos intermedios."],
 "d"),
("Además de conectar dispositivos intermediarios a los patch panels, ¿qué otra función realizan los latiguillos dentro del cuarto de telecomunicaciones?",
 ["a) Almacenar cables horizontales.",
  "b) Conectar dispositivos finales a los patch panels.",
  "c) Proporcionar conexión directa a Internet.",
  "d) Conectar entre sí los dispositivos intermediarios."],
 "d"),
("Según los estándares EIA/TIA, ¿cuál es la diferencia entre el patch cable y el patch cord en el contexto de conexiones en el cuarto de telecomunicaciones?",
 ["a) No hay diferencia, ambos términos se utilizan indistintamente.",
  "b) El patch cable se utiliza para conectar dispositivos a las rosetas, mientras que el patch cord interconecta el switch o router con los patch panels.",
  "c) El patch cord se utiliza para conectar dispositivos a las rosetas, mientras que el patch cable interconecta el switch o router con los patch panels.",
  "d) Ambos términos se refieren a conexiones telefónicas en el cuarto de telecomunicaciones."],
 "b"),
("Según los estándares EIA/TIA, ¿cómo se denomina al latiguillo de UTP que interconecta el switch o router con los patch panels en el cuarto de telecomunicaciones?",
 ["a) Patch Cord.",
  "b) Patch Panel.",
  "c) Patch Cable.",
  "d) Latiguillo de Conexión."],
 "c"),
("Según los estándares EIA/TIA, ¿cómo se denomina al latiguillo de UTP utilizado para conectar dispositivos a las rosetas o puntos de terminación en la pared?",
 ["a) Patch Cord.",
  "b) Patch Panel.",
  "c) Patch Cable.",
  "d) Latiguillo de Conexión."],
 "a"),
("¿Cuál es una de las finalidades adicionales que pueden tener los cuartos de telecomunicaciones?",
 ["a) Almacenar dispositivos finales.",
  "b) Conectar directamente a Internet.",
  "c) Incluir servidores utilizados por la red.",
  "d) Proporcionar almacenamiento para documentos."],
 "c"),
("¿Cuál es la longitud máxima del cableado horizontal?",
 ["a) 50 metros.",
  "b) 75 metros.",
  "c) 90 metros.",
  "d) 100 metros."],
 "c"),
("¿Cuál es la función principal del cableado horizontal?",
 ["a) Conectar dispositivos en el mismo cuarto.",
  "b) Conectar cuartos de telecomunicaciones con áreas de trabajo.",
  "c) Conectar dispositivos a Internet.",
  "d) Conectar servidores en el centro de datos."],
 "b"),
("¿Cuál es la longitud máxima del cable desde el punto de terminación hasta el cuarto de comunicaciones según el fragmento?",
 ["a) 50 metros.",
  "b) 75 metros.",
  "c) 90 metros.",
  "d) 100 metros."],
 "c"),
("¿Por qué se denomina 'enlace permanente' al cableado horizontal según el fragmento?",
 ["a) Porque no se puede modificar una vez instalado.",
  "b) Porque está diseñado para conexiones temporales.",
  "c) Porque está instalado en la estructura del edificio.",
  "d) Porque solo se utiliza en situaciones de emergencia."],
 "c"),
("¿Cuál es el trayecto de los medios horizontales según el fragmento?",
 ["a) Desde el cuarto de telecomunicaciones hasta el área de trabajo.",
  "b) Desde la roseta de parede hasta el cuarto de comunicaciones.",
  "c) Desde el panel de parcheo hasta el área de trabajo.",
  "d) Desde el área de trabajo hasta el cuarto de telecomunicaciones."],
 "c"),
("¿Cómo se realizan las conexiones desde la roseta a los dispositivos según el fragmento?",
 ["a) Con cables coaxiales.",
  "b) Con cables de fibra óptica.",
  "c) Con patch cords.",
  "d) Con cables de par trenzado."],
 "c"),
("¿Cuál es la función principal del cableado backbone según el fragmento?",
 ["a) Conectar dispositivos en una misma área de trabajo.",
  "b) Interconectar múltiples cuartos de telecomunicaciones.",
  "c) Conectar dispositivos a la conexión WAN.",
  "d) Conectar dispositivos a un ISP."],
 "b"),
("¿Cuál es el propósito del cableado backbone según el fragmento?",
 ["a) Conectar dispositivos en una misma área de trabajo.",
  "b) Conectar dispositivos a la conexión WAN.",
  "c) Interconectar múltiples cuartos de telecomunicaciones.",
  "d) Conectar los cuartos de telecomunicaciones a las salas de equipamiento donde suelen estar los servidores."],
 "d"),
("¿Cuál es una característica del cableado backbone según el fragmento?",
 ["a) Conectar dispositivos en una misma área de trabajo.",
  "b) Interconectar múltiples cuartos de telecomunicaciones.",
  "c) Conectar dispositivos a la conexión WAN.",
  "d) Conectar dispositivos a un ISP."],
 "b"),
("¿Cuál es el destino común de los cables de backbone según el fragmento?",
 ["a) Conectar dispositivos en una misma área de trabajo.",
  "b) Interconectar múltiples cuartos de telecomunicaciones.",
  "c) Conectar dispositivos a la conexión WAN o a una conexión ofrecida por un ISP.",
  "d) Conectar dispositivos a un ISP."],
 "c"),
("¿Qué tipo de tráfico se menciona como uno de los usos comunes de los backbones según el fragmento?",
 ["a) Tráfico local dentro de un área de trabajo.",
  "b) Tráfico entre dispositivos en una misma área de trabajo.",
  "c) Tráfico de entrada o salida de Internet.",
  "d) Tráfico exclusivo de conexiones WAN."],
 "c"),
("¿Cuál es uno de los usos mencionados para los backbones según el fragmento?",
 ["a) Tráfico local dentro de un área de trabajo.",
  "b) Tráfico entre dispositivos en una misma área de trabajo.",
  "c) Tráfico de entrada o salida de Internet.",
  "d) Tráfico exclusivo de conexiones WAN."],
 "c"),
("¿Qué tipo de cables suele emplearse comúnmente para los backbones según el fragmento?",
 ["a) Cable coaxial.",
  "b) Cable de par trenzado UTP o fibra óptica.",
  "c) Cable de par trenzado STP.",
  "d) Cable de fibra óptica o STP."],
 "b"),
 ("¿Cuáles son las categorías comunes de par trenzado utilizadas para backbones según el fragmento?",
 ["a) Categoría 3 y 5.",
  "b) Categoría 5e, 6 u 6a.",
  "c) Categoría 7 y 8.",
  "d) Categoría 1 y 2."],
 "b"),
("¿Qué característica comparten los medios inalámbricos según el fragmento?",
 ["a) Requieren un tendido extenso de cables.",
  "b) Son conocidos como medios guiados.",
  "c) No necesitan tendido de cable entre el emisor y el receptor.",
  "d) Se propagan exclusivamente por ondas de agua."],
 "c"),
("¿Cómo se les denomina a los medios de transmisión que no necesitan tendido de cable entre el emisor y el receptor?",
 ["a) Medios guiados o inalámbricos.",
  "b) Medios inalámbricos o no guiados.",
  "c) Medios de radiotransmisión o no guiados.",
  "d) Medios de microondas."],
 "b"),
("¿Para qué son especialmente interesantes los medios de transmisión que no necesitan tendido de cable, según el fragmento?",
 ["a) Para conexiones de alta velocidad.",
  "b) Para áreas urbanas.",
  "c) Para usuarios móviles o zonas geográficas difícilmente accesibles.",
  "d) Para aplicaciones de fibra óptica."],
 "c"),
("¿Cómo se propagan las ondas electromagnéticas en los medios de transmisión que no necesitan tendido de cable, según el fragmento?",
 ["a) A través de cables de fibra óptica.",
  "b) Por ondas de sonido.",
  "c) Circulan por el aire y se propagan como las ondas de agua en el agua.",
  "d) Mediante radiación nuclear."],
 "c"),
("¿Cuáles son las diferentes variantes de medios inalámbricos según el tipo de radiación, según el fragmento?",
 ["a) Radiación nuclear y radiotransmisión.",
  "b) Ondas de sonido y microondas.",
  "c) Radiotransmisión, microondas e infrarrojos.",
  "d) Luz visible e ultravioleta."],
 "c"),
("¿En qué rango de frecuencias opera la radiotransmisión según el fragmento?",
 ["a) 300 MHz a 3 GHz.",
  "b) 3 GHz a 30 GHz.",
  "c) 10 KHz a 300 MHz.",
  "d) 400 THz a 600 THz."],
 "c"),
("¿Cuál es el rango de frecuencias utilizado por las microondas según el fragmento?",
 ["a) 3 GHz a 30 GHz.",
  "b) 300 MHz a 3 GHz.",
  "c) 10 KHz a 300 MHz.",
  "d) 300 MHz a 300 GHz."],
 "d"),
("¿Cuál es el rango de frecuencias utilizado por la radiación infrarroja según el fragmento?",
 ["a) 3 GHz a 30 GHz.",
  "b) 300 GHz a 3 THz.",
  "c) 300 GHz a 400 THz.",
  "d) 10 KHz a 300 MHz."],
 "c"),
("¿Por qué los enlaces sin cables son especialmente interesantes según el fragmento?",
 ["a) Para evitar interferencias eléctricas.",
  "b) Para conexiones a larga distancia.",
  "c) Para usuarios móviles o en áreas de difícil acceso.",
  "d) Para reducir la atenuación en la transmisión."],
 "c"),
("¿Cuál es la diferencia comúnmente usada al referirse a las ondas de radiofrecuencia o microondas y al infrarrojo según el fragmento?",
 ["a) En radiofrecuencia se utiliza la longitud de onda, mientras que en infrarrojo se menciona la frecuencia.",
  "b) Ambos se refieren a la frecuencia de las ondas.",
  "c) En radiofrecuencia se menciona la frecuencia, mientras que en infrarrojo se utiliza la longitud de onda.",
  "d) No hay una diferencia específica entre ambos."],
 "c"),
("¿Cuál es la relación entre la frecuencia (f), la velocidad de la luz (c) y la longitud de onda (λ) según la información proporcionada?",
 ["a) λf = c",
  "b) λf * c = λ",
  "c) f = c * λ",
  "d) No hay una relación definida entre estas magnitudes."],
 "a"),
("¿Qué factores influyen principalmente en las características de transmisión de las ondas en el aire según la información proporcionada?",
 ["a) La velocidad de propagación",
  "b) La frecuencia",
  "c) La longitud de onda",
  "d) Ambas b) y c)"],
 "d"),
("¿Cómo se describe el comportamiento de las ondas en la zona de radiofrecuencias según la información proporcionada?",
 ["a) Comportamiento muy direccional",
  "b) Comportamiento poco direccional",
  "c) Dificultad para atravesar obstáculos grandes",
  "d) Ambas a) y c)"],
 "b"),
("¿Para qué son utilizadas las emisiones en la zona de radiofrecuencias según la información proporcionada?",
 ["a) Transmisión de señales de televisión",
  "b) Comunicación mediante radio",
  "c) Transmisión de señales de microondas",
  "d) Ambas a) y b)"],
 "b"),
("¿Cómo afecta la frecuencia a la transmisión en microondas según la información proporcionada?",
 ["a) La transmisión en microondas es poco direccional",
  "b) La transmisión en microondas es más direccional y sensible a obstáculos",
  "c) A partir de los 100 MHz, la transmisión en microondas se hace en línea recta",
  "d) A partir de los 500 GHz en el infrarrojo, la transmisión es completamente direccional"],
 "b"),
("¿Cómo se comporta la transmisión en microondas en relación con la dirección y los obstáculos?",
 ["a) La transmisión en microondas es poco direccional y atraviesa obstáculos fácilmente",
  "b) La transmisión en microondas es más direccional y sensible a obstáculos",
  "c) La transmisión en microondas es independiente de la dirección y obstáculos",
  "d) A partir de los 100 MHz, la transmisión en microondas se hace en línea recta"],
 "b"),
("¿Cómo afecta la frecuencia a la transmisión en microondas?",
 ["a) La transmisión en microondas se vuelve menos direccional a medida que aumenta la frecuencia",
  "b) A partir de los 100 MHz, la transmisión en microondas se vuelve más direccional y los obstáculos afectan la comunicación",
  "c) La frecuencia no tiene impacto en la transmisión en microondas",
  "d) A mayor frecuencia, la transmisión en microondas atraviesa obstáculos más fácilmente"],
 "b"),
("¿Qué ocurre con la transmisión en microondas entre 300 MHz y 1 GHz?",
 ["a) La transmisión se vuelve más direccional",
  "b) La transmisión se vuelve menos direccional",
  "c) La lluvia absorbe parte de la potencia de transmisión",
  "d) La transmisión en microondas no se ve afectada en esta frecuencia"],
 "c"),
("¿Cómo se comporta la transmisión en la banda infrarroja (infravermello) a partir de 500 GHz?",
 ["a) La transmisión es poco direccional",
  "b) La transmisión es completamente direccional y solo es posible hacer transmisiones a corta distancia y con buenas condiciones meteorológicas.",
  "c) Se puede realizar transmisión a larga distancia",
  "d) La transmisión en infrarrojo no se ve afectada en esta frecuencia"],
 "b"),
("¿Qué característica describe la transmisión mediante radiotransmisión?",
 ["a) Las ondas viajan en línea recta",
  "b) Las ondas son absorbidas por la ionosfera",
  "c) Las ondas penetran en edificios",
  "d) La transmisión es direccionada y requiere alineación física"],
 "c"),
("¿En qué rango de frecuencias se utilizan ondas de radio en la radiotransmisión?",
 ["a) 1MHz a 100MHz",
  "b) 50KHz a 500KHz",
  "c) 10KHz a 300MHz",
  "d) 200MHz a 1GHz"],
 "c"),
("¿Qué características tienen las ondas de radio en radiotransmisión?",
 ["a) Viajan solo en línea recta",
  "b) Tienen corto alcance",
  "c) Pueden viajar largas distancias, penetrar edificios y moverse en todas las direcciones desde la fuente emisora",
  "d) Son absorbidas por la ionosfera"],
 "c"),
("¿Qué ventaja ofrece la radiotransmisión debido a que las ondas de radio van en todas las direcciones?",
 ["a) Requiere alineación precisa del emisor y receptor",
  "b) Se necesita una línea de visión clara entre el emisor y el receptor",
  "c) No es necesario que el emisor y el receptor estén alineados físicamente",
  "d) Solo puede utilizarse en espacios abiertos"],
 "c"),
("¿Quién regula las transmisiones de radiotransmisión para evitar interferencias?",
 ["a) Organización Mundial de la Salud (OMS)",
  "b) Gobiernos",
  "c) Naciones Unidas",
  "d) Unión Internacional de Telecomunicaciones (UIT)"],
 "b"),
("¿Cuál es la tasa de transferencia máxima alcanzada por la radiotransmisión?",
 ["a) 500 Kbps",
  "b) 1 Mbps",
  "c) 2 Mbps",
  "d) 5 Mbps"],
 "b"),
("¿Qué pasa con las ondas de baja frecuencia en las radiotransmisiones?",
 ["a) Penetran fácilmente en los edificios",
  "b) Son absorbidas por la Tierra",
  "c) Siguen la curvatura de la Tierra",
  "d) Son reflejadas por la ionosfera"],
 "c"),
 ("¿Por qué las ondas de alta frecuencia en las radiotransmisiones son absorbidas y rebotan en la ionosfera?",
 ["a) Porque siguen la curvatura de la Tierra",
  "b) Porque penetran fácilmente en los edificios",
  "c) Las ondas de alta frecuencia no son absorbidas, son absorbidas las de baja frecuencia, que siguen la curvatura de la Tierra",
  "d) Porque rebotan en la ionosfera"],
 "d"),
 (
    "¿Cuál es una característica de las comunicaciones por infrarrojos según el texto?",
    [
        "a) Tienen frecuencias superiores a 400 THz.",
        "b) Son omnidireccionales.",
        "c) Pueden atravesar objetos sólidos fácilmente.",
        "d) No se ven afectadas por la radiación infrarroja solar.",
    ],
    "c"
),
(
    "¿Cuál es el rango de frecuencias de las comunicaciones por infrarrojos según el texto?",
    [
        "a) Menos de 300 GHz.",
        "b) Entre 300 GHz y 400 THz.",
        "c) Más de 400 THz.",
        "d) Exactamente 400 THz.",
    ],
    "b"
),
(
    "¿Para qué se utilizan las comunicaciones por infrarrojos según el texto?",
    [
        "a) Comunicaciones a larga distancia.",
        "b) Comunicaciones de corto alcance como el control remoto de TV y algunos mandos a distancia.",
        "c) Comunicaciones exteriores.",
        "d) Comunicaciones a través de internet.",
    ],
    "b"
),
(
    "¿Cuál es una característica de las ondas infrarrojas según el texto?",
    [
        "a) Son ondas omnidireccionales.",
        "b) Son ondas que pueden atravesar objetos sólidos fácilmente.",
        "c) Son ondas que no tienen direccionalidad.",
        "d) Son ondas que no pueden atravesar objetos sólidos.",
    ],
    "d"
),
(
    "¿Por qué la comunicación por infrarrojos no debe usarse en exteriores según el texto?",
    [
        "a) Porque el sol emite radiación ultravioleta que afecta a la comunicación.",
        "b) Porque el sol emite radiación infrarroja que puede interferir con la señal enviada.",
        "c) Porque la comunicación por infrarrojos solo funciona en ambientes cerrados.",
        "d) Porque el sol afecta negativamente a la dirección de las ondas infrarrojas.",
    ],
    "b"
),
(
    "¿Cuál es una característica de la comunicación por infrarrojos según el texto?",
    [
        "a) Solo se utiliza en exteriores.",
        "b) Se usa comúnmente en comunicaciones de largo alcance.",
        "c) Se pueden encontrar puertos infrarrojos en algunos portátiles.",
        "d) La velocidad máxima de transmisión es de 100 Mbps.",
    ],
    "c"
),
(
    "¿Qué tipo de dispositivos utilizan frecuencias en la banda de las microondas según el texto?",
    [
        "a) Hornos microondas.",
        "b) Equipos de telefonía móvil.",
        "c) Redes wi-fi.",
        "d) Todos los anteriores.",
    ],
    "d"
),
(
    "¿Cuáles son las frecuencias más empleadas en comunicación de redes informáticas según el texto y a qué pertenecen?",
    [
        "a) 1 GHz a 300 GHz, a ondas wifi.",
        "b) 300 MHz a 300 GHz, a microondas.",
        "c) 30 centímetros a 1 milímetro, a infrarrojos.",
        "d) 2,45 GHz, a radiofrecuencia.",
    ],
    "b"
),
(
    "¿En qué dispositivos se utilizan las microondas según el texto?",
    [
        "a) Solo en telefonía móvil.",
        "b) Solo en comunicación por Bluetooth.",
        "c) En telefonía móvil, comunicación por Bluetooth, redes Wi-Fi en estándares 802.11, etc.",
        "d) Solo en redes Wi-Fi.",
    ],
    "c"
),
(
    "¿Cuál es la frecuencia de trabajo de las microondas según el texto?",
    [
        "a) 1 GHz.",
        "b) Entre 30 centímetros y 1 milímetro.",
        "c) 2,45 GHz.",
        "d) De 300 MHz a 300 GHz.",
    ],
    "d"
),
(
    "¿Cuál es la afirmación correcta sobre las microondas según el texto?",
    [
        "a) Se usan solo en redes informáticas.",
        "b) Tienen una frecuencia de trabajo de 1 GHz.",
        "c) Tienen una frecuencia de trabajo entre 1 GHz y 300 GHz.",
        "d) Tienen longitudes de onda de entre 30 centímetros y 1 milímetro.",
    ],
    "c"
),
(
    "¿Por qué se utilizan las microondas en los hornos microondas según el texto?",
    [
        "a) Porque tienen una frecuencia de 1 GHz.",
        "b) Porque vibran las moléculas de agua a esa frecuencia.",
        "c) Porque tienen una longitud de onda de 30 centímetros.",
        "d) Porque son eficientes para la comunicación por bluetooth.",
    ],
    "b"
),
(
    "¿En qué rango de frecuencias emiten los móviles en los que se emplean microondas?",
    [
        "a) 300 MHz - 1 GHz.",
        "b) 1-2 GHz.",
        "c) 2-300 GHz.",
        "d) 30 centímetros - 1 milímetro.",
    ],
    "b"
),
(
    "¿Qué frecuencia emplean los terminales de telefonía fija inalámbrica, dispositivos Bluetooth y alarmas inalámbricas?",
    [
        "a) 300 MHz - 1 GHz.",
        "b) 1-2 GHz.",
        "c) 2-45 GHz.",
        "d) 2,45 GHz.",
    ],
    "d"
),
(
    "En cuanto a las microondas, ¿Por qué la banda de 2,45 GHz está más saturada y puede tener mayor presencia de ruido?",
    [
        "a) Porque es una banda poco utilizada.",
        "b) Porque la frecuencia es muy baja.",
        "c) Porque muchos elementos hacen uso de esta banda.",
        "d) Porque es una banda reservada para usos especiales.",
    ],
    "c"
),
(
    "En los estándares wifi 802.11, ¿qué frecuencias utilizan los estándares 802.11b y 802.11g?",
    [
        "a) 5 GHz",
        "b) 2,4 GHz",
        "c) 1 GHz",
        "d) 300 MHz",
    ],
    "b"
),
(
    "¿Cuántos canales contiene la banda de 2,4 GHz en el contexto de las microondas?",
    [
        "a) 5 canales",
        "b) 10 canales",
        "c) 13 canales",
        "d) 20 canales",
    ],
    "c"
),
(
    "¿Cuánto es el ancho de cada canal en la banda de 2,4 GHz en el contexto de las microondas?",
    [
        "a) 10 MHz",
        "b) 15 MHz",
        "c) 20 MHz",
        "d) 22 MHz",
    ],
    "d"
),
(
    "¿Cuál es una medida recomendada para evitar interferencias entre puntos de acceso en una red wifi?",
    [
        "a) Utilizar siempre el canal 6",
        "b) Utilizar canales solapados para aumentar la capacidad",
        "c) Asignar canales no solapados a puntos de acceso cercanos",
        "d) No es necesario tener en cuenta los canales al configurar puntos de acceso",
    ],
    "c"
),
(
    "¿Por qué es importante que varios puntos de acceso emitan en canales diferentes y no solapados?",
    [
        "a) Para aumentar las interferencias y reducir la tasa de transferencia",
        "b) Para mejorar la coexistencia de puntos de acceso y reducir interferencias",
        "c) Porque no afecta a la tasa de transferencia",
        "d) Para limitar el alcance de la red wifi",
    ],
    "b"
),
(
    "¿Cuál es el efecto de las interferencias en una red?",
    [
        "a) Aumentan la tasa de transferencia",
        "b) Reducen la tasa de transferencia",
        "c) No afectan la tasa de transferencia",
        "d) Mejoran la estabilidad de la red",
    ],
    "b"
),
(
    "En una red donde coexisten clientes 802.11n y 802.11ac, ¿qué mecanismo se utiliza para evitar interferencias?",
    [
        "a) RTS/CTS",
        "b) ACK/NACK",
        "c) ARP",
        "d) DNS",
    ],
    "a"
),
(
    "En el ejemplo dado con un punto de acceso y dos clientes (802.11N y 802.11AC), ¿qué trama se utiliza para indicar el tiempo de transmisión y evitar colisiones en la red?",
    [
        "a) ACK",
        "b) RTS",
        "c) CTS",
        "d) NACK",
    ],
    "b"
),
(
    "En el estándar 802.11n, ¿qué bandas de frecuencia puede utilizar para la transmisión?",
    [
        "a) Solo 2,4 GHz",
        "b) Solo 5 GHz",
        "c) Tanto 2,4 GHz como 5 GHz",
        "d) Ninguna de las anteriores",
    ],
    "c"
),
(
    "¿Cuáles son las estrategias utilizadas por los equipos que siguen el estándar 802.11n para lograr mayores velocidades?",
    [
        "a) Sistemas S.I.S.O (Single Input Single Output)",
        "b) Sistemas M.I.M.O (Multiple Input Multiple Output) y canales de 20MHz de ancho",
        "c) Sistemas M.I.M.O (Multiple Input Multiple Output) y canales de 40MHz de ancho",
        "d) Sistemas S.I.M.O (Single Input Multiple Output) y canales de 40MHz de ancho",
    ],
    "c"
),
(
    "¿Cómo funcionan los sistemas que emplean tecnología MIMO con dispersión por separación espacial?",
    [
        "c) Tienen una única antena para emitir y recibir datos.",
        "b) Tienen múltiples antenas solo para recibir datos.",
        "a) Tienen múltiples antenas para emitir y recibir datos, permitiendo diferentes flujos de datos por antena.",
        "d) Tienen una única antena para emitir, pero múltiples antenas para recibir datos.",
    ],
    "a"
),
(
    "¿Cómo está limitado el número de flujos simultáneos que se pueden emitir en sistemas que emplean tecnología MIMO con dispersión por separación espacial?",
    [
        "a) No está limitado, ya que cada antena puede emitir su propio flujo de datos independientemente.",
        "b) Está limitado por el número total de antenas en ambos lados de la comunicación.",
        "c) Está limitado solo por el número de antenas en el lado que emite los datos.",
        "d) Está limitado solo por el número de antenas en el lado que recibe los datos.",
    ],
    "b"
),
(
    "Si el equipo emisor tiene 3 antenas y el receptor tiene 2 antenas receptoras, ¿cuántos flujos independientes (simultáneos) puede emplear la comunicación?",
    [
        "a) 1 flujo independiente.",
        "b) 2 flujos independientes.",
        "c) 3 flujos independientes.",
        "d) 5 flujos independientes.",
    ],
    "b"
),
(
    "Los sistemas deberían ser capaces de alcanzar 600 Mbps (con 4 flujos independientes, 150 Mbps por cada flujo).",
    [
        "a) Verdadero.",
        "b) Falso."
    ],
    "a"
),
(
    "En la actualidad, los sistemas que consiguen 3 flujos deberían ser capaces de llegar a 450 Mbps, aunque en los clientes no es habitual esta configuración de 3 antenas.",
    [
        "a) Verdadero.",
        "b) Falso."
    ],
    "a"
),
(
    "Como habitualmente los clientes tienen 2 antenas receptoras, el máximo real está siendo de 300 Mbps (2 antenas: 2 flujos de 150 Mbps).",
    [
        "a) Verdadero.",
        "b) Falso."
    ],
    "a"
),
(
    "Otro cambio es que los canales del 802.11n tienen un ancho de 40 MHz, a diferencia de los 22 MHz del canal de las anteriores normas 802.11b/g.",
    [
        "a) Verdadero.",
        "b) Falso."
    ],
    "a"
),
(
    "Los canales del 802.11n tienen un ancho de 40 MHz, a diferencia de los 22 MHz del canal de las anteriores normas 802.11b/g. Esto no es un problema en los 5 GHz, pero un AP en la frecuencia de 2,4 GHz debe emplear 2 canales que no se solapen de los ya establecidos (por ejemplo, el 1 y el 6), para conseguir los 40 MHz.",
    [
        "a) Verdadero.",
        "b) Falso."
    ],
    "a"
),
(
    "La norma 802.11n hace que los PA bajen inmediatamente a canales de 20MHz de ancho si detectan alguna red WIFI próxima o algún dispositivo que trabaje en la banda del 2,4GHz, reduciendo por tanto su tasa de transferencia real a la mitad.",
    [
        "a) Verdadero.",
        "b) Falso."
    ],
    "a"
),
(
    "En la comunicación por infrarrojos, ¿cuál es uno de los inconvenientes principales?",
    [
        "a) Alta penetración a través de objetos sólidos.",
        "b) Baja velocidad de transmisión.",
        "c) Resistencia a la interferencia solar.",
        "d) Elevado costo de implementación."
    ],
    "b"
),
(
    "¿Qué sucede en la norma 802.11n cuando los Puntos de Acceso (PA) detectan redes WIFI cercanas o dispositivos que operan en la banda de 2,4GHz?",
    [
        "a) Permanecen en canales de 40MHz de ancho y ajustan automáticamente su potencia de transmisión.",
        "b) Cambian automáticamente a canales de 40MHz de ancho para evitar interferencias.",
        "c) Bajan inmediatamente a canales de 20MHz de ancho, reduciendo su tasa de transferencia a la mitad.",
        "d) Aumentan su potencia de transmisión para superar las interferencias.",
    ],
    "c"
),
(
    "¿Cuál es una ventaja de trabajar en la frecuencia de 5GHz en la norma 802.11n?",
    [
        "a) Se experimentan menos interferencias debido a la mayor cantidad de canales disponibles.",
        "b) Los equipos pueden utilizar canales de 80MHz de ancho para una mayor velocidad de transferencia.",
        "c) Permite una mejor penetración a través de obstáculos sólidos.",
        "d) Los dispositivos pueden ajustar automáticamente su potencia de transmisión para evitar interferencias.",
    ],
    "a"
),
(
    "Dentro de la norma 802.11n: ¿Qué problema puede surgir al tener clientes que utilizan distintos protocolos, como uno en .n y otro en .g, en la misma red?",
    [
        "a) No hay problemas, ya que las normas son compatibles entre sí.",
        "b) La red funcionará a la perfección sin reducción de velocidad.",
        "c) Experimentarán una reducción significativa de velocidad al mezclar distintas normas.",
        "d) Los clientes ajustarán automáticamente su protocolo para evitar problemas.",
    ],
    "c"
),
(
    "¿Cuál es la mejora principal de la norma 802.11ac (WIFI-5) en comparación con las normas anteriores?",
    [
        "a) Mayor alcance de la señal.",
        "b) Mayor seguridad en la transmisión de datos.",
        "c) Mejora la tasa de transferencia teórica, llegando a 1,3 Gbps en la primera versión.",
        "d) Menor consumo de energía.",
    ],
    "c"
),
(
    "¿Cuáles son algunas de las características que distinguen a la norma 802.11ac (WIFI-5) de las normas anteriores?",
    [
        "a) Empleo de la banda de 2.4GHz.",
        "b) Reducción del ancho de cada canal a 40MHz.",
        "c) Aumento en las antenas múltiples de transmisión y recepción, llegando a 8 flujos, y uso de la modulación 256QAM.",
        "d) Modulación en baja densidad (16QAM).",
    ],
    "c"
),
(
    "¿Cuáles son algunas de las mejoras introducidas por la norma 802.11ac (WIFI-5) aprobada en enero de 2014?",
    [
        "c) Utilización de la banda de 2.4GHz.",
        "b) Reducción del ancho de cada canal a 40MHz.",
        "a) Incremento en la tasa de transferencia teórica a 1.3Gbps en la primera versión.",
        "d) Limitación a 4 flujos de transmisión y recepción.",
    ],
    "a"
),
(
    "¿Qué cambio introdujo la norma 802.11ac (WIFI-5), aprobada en enero de 2014, en relación al espectro de frecuencia utilizado?",
    [
        "a) Continuó utilizando la banda de 2.4GHz.",
        "b) Cambió a la banda de 3GHz para mayor alcance.",
        "c) Implementó el empleo de la banda de 5GHz.",
        "d) Utilizó ambas bandas de 2.4GHz y 5GHz de manera simultánea.",
    ],
    "c"
),
(
    "En cuanto al ancho de cada canal, ¿qué modificación introdujo la norma 802.11ac (WIFI-5), aprobada en enero de 2014?",
    [
        "a) Mantuvo el ancho de cada canal en 20MHz.",
        "b) Amplió el ancho de cada canal a 40MHz.",
        "c) Amplió el ancho de cada canal a 80 o 160MHz.",
        "d) Redujo el ancho de cada canal a 10MHz para mejorar la eficiencia.",
    ],
    "c"
),
(
    "¿Cuál fue una de las mejoras en el número de flujos de transmisión y recepción introducida por la norma 802.11ac (WIFI-5)?",
    [
        "a) Mantuvo el número de flujos en 4, igual que en la norma 802.11n.",
        "b) Incrementó el número de flujos a 6 para mejorar la estabilidad.",
        "c) Aumentó el número de flujos a 8 desde los 4 de la norma 802.11n.",
        "d) Redujo el número de flujos a 2 para simplificar la implementación.",
    ],
    "c"
),
(
    "En cuanto a la modulación utilizada, ¿qué cambio introdujo la norma 802.11ac (WIFI-5), aprobada en enero de 2014?",
    [
        "a) Continuó utilizando modulación de baja densidad (16QAM).",
        "b) Cambió a modulación de media densidad (64QAM) para mayor velocidad.",
        "d) Implementó el empleo de modulación en alta densidad (256QAM).",
        "c) Redujo la complejidad utilizando modulación de muy baja densidad (8QAM).",
    ],
    "d"
),
(
    "¿Cómo cambió la capacidad de envío del punto de acceso (AP) según la norma 802.11ac (WIFI-5)?",
    [
        "a) Limitó la capacidad de enviar a un solo usuario a la vez.",
        "b) Mejoró la eficiencia al enviar a múltiples usuarios con la misma frecuencia (Multiusuario-MIMO).",
        "c) Redujo la velocidad al enviar a varios usuarios simultáneamente.",
        "d) Incrementó la frecuencia para enviar a múltiples usuarios de manera independiente.",
    ],
    "b"
),
(
    "¿Cuáles son algunas de las mejoras introducidas por la norma 802.11ax (WIFI-6) en comparación con la norma 802.11ac?",
    [
        "a) Mantuvo el uso exclusivo de MIMO y MU-MIMO.",
        "b) Introdujo OFDMA para mejorar la eficiencia espectral global.",
        "c) No modificó la modulación y mantuvo 256-QAM.",
        "d) Redujo la velocidad teórica a 8Gbps para mayor estabilidad.",
    ],
    "b"
),
(
    "¿Qué nueva tecnología introdujo la norma 802.11ax (WIFI-6) para mejorar la eficiencia espectral global?",
    [
        "a) Mantuvo el uso exclusivo de MIMO y MU-MIMO.",
        "b) Incorporó OFDMA para mejorar la eficiencia espectral global.",
        "c) Redujo la velocidad teórica a 8Gbps para mayor estabilidad.",
        "d) Eliminó completamente el uso de múltiples antenas.",
    ],
    "b"
),
(
    "En términos de modulación, ¿qué característica introdujo la norma 802.11ax (WIFI-6) para mejorar el rendimiento?",
    [
        "a) Mantuvo la modulación en 256-QAM.",
        "b) Introdujo soporte de modulación 512-QAM.",
        "c) Incorporó soporte de modulación 1024-QAM para un mayor rendimiento.",
        "d) Eliminó completamente la modulación para simplificar la comunicación.",
    ],
    "c"
),
(
    "¿Cómo mejora la norma 802.11ax (WIFI-6) el rendimiento en entornos con alta densidad de dispositivos?",
    [
        "a) Utilizando un espectro de frecuencias más amplio.",
        "b) Manteniendo el uso exclusivo de MIMO y MU-MIMO.",
        "c) Aumentando el ancho de cada canal a 160MHz.",
        "d) Empleando el espectro de frecuencias de manera más eficiente.",
    ],
    "d"
),
(
    "¿Cuál es uno de los beneficios de la norma 802.11ax (WIFI-6) en términos de latencia y velocidad?",
    [
        "a) Mantiene la misma latencia que la norma 802.11ac.",
        "b) Aumenta la latencia en entornos con alta densidad de dispositivos.",
        "c) Reduce la latencia en un 75%.",
        "d) Promete una velocidad teórica de 11Gbps.",
    ],
    "c"
),
(
    "¿Cuál es la velocidad teórica prometida por la norma 802.11ax (WIFI-6)?",
    [
        "a) 5Gbps.",
        "b) 8Gbps.",
        "c) 11Gbps.",
        "d) 15Gbps.",
    ],
    "c"
),
(
    "En una red inalámbrica, ¿cuál es el identificador único asociado a un punto de acceso (AP) que forma parte de un BSS (Conjunto Básico de Servicio) en modo infraestructura?",
    [
        "a) BSSID (Basic Service Set Identifier).",
        "b) SSID (Service Set Identifier).",
        "c) MAC (Media Access Control) de la estación asociada.",
        "d) DS (Sistema de Distribución) Identifier.",
    ],
    "a"
),
(
    "En una red inalámbrica, ¿cómo se denomina el conjunto formado por un punto de acceso (AP) junto con sus estaciones asociadas?",
    [
        "a) MSS (Mobile Service Set).",
        "b) WSS (Wireless Service Set).",
        "c) BSS (Basic Service Set o Conjunto Básico de Servicio).",
        "d) ASS (Advanced Service Set).",
    ],
    "c"
),
(
    "En un BSS (Conjunto Básico de Servicio) que opera en modo infraestructura, ¿qué representa el identificador BSSID?",
    [
        "a) Es el identificador único de cada estación asociada al BSS.",
        "b) Es el identificador de la red inalámbrica (SSID) en modo infraestructura.",
        "c) Es la dirección IP asignada a cada estación dentro del BSS.",
        "d) Es la dirección MAC de la interfaz inalámbrica del punto de acceso que forma parte del BSS.",
    ],
    "d"
),
(
    "En una red inalámbrica en modo infraestructura, ¿qué afirmación es correcta sobre el BSSID?",
    [
        "a) El BSSID es un identificador dinámico que cambia automáticamente.",
        "b) El BSSID es configurable por el usuario para mayor flexibilidad.",
        "c) El BSSID es la dirección IP asignada al punto de acceso en el BSS.",
        "d) El BSSID no puede ser cambiado y corresponde a la dirección MAC de la interfaz inalámbrica del punto de acceso.",
    ],
    "d"
),
(
    "En una red inalámbrica, ¿cuál es el propósito del SSID (Service Set Identifier)?",
    [
        "a) Identificar la dirección MAC de cada estación asociada al punto de acceso.",
        "b) Ser un identificador único para cada estación en la red.",
        "c) Diferenciar entre varios BSS en el mismo canal.",
        "d) Facilitar la asignación de direcciones IP a los dispositivos en el BSS.",
    ],
    "c"
),
(
    "¿Cómo se conoce a veces al SSID cuando se extiende, abreviado como 'ESSID'?",
    [
        "a) Enhanced Service Set Identifier.",
        "b) Extended Secure Service Identifier.",
        "c) Extra Service Set Identifier.",
        "d) Extended SSID (ESSID).",
    ],
    "a"
),
(
    "¿Cuál es la característica relacionada con la longitud y configurabilidad del SSID (Service Set Identifier) en una red inalámbrica?",
    [
        "a) El SSID siempre tiene una longitud fija de 16 caracteres.",
        "b) El SSID tiene una longitud variable entre 2 y 32 caracteres y es configurable por el usuario.",
        "c) La longitud del SSID depende de la velocidad de la conexión.",
        "d) La configuración del SSID es automática y no puede ser modificada por el usuario.",
    ],
    "b"
),
(
    "Si tienes un único punto de acceso (AP) que opera de manera aislada (solo un BSS), ¿cómo se caracterizaría la configuración?",
    [
        "a) El AP tendría varios BSSID y SSID para mayor flexibilidad.",
        "b) El AP tendría un único BSSID y varios SSID para diversidad.",
        "c) El AP tendría un único BSSID y un único SSID.",
        "d) El AP tendría varios BSSID y un único SSID para identificación única de estaciones.",
    ],
    "c"
),
(
    "En una red inalámbrica empresarial u organizativa con varios puntos de acceso (APs) conectados por un DS (Sistema de Distribución), ¿cómo se configurarían los BSSID y SSID?",
    [
        "a) Cada AP tendría un BSSID diferente y un SSID único para mayor diversidad.",
        "b) Cada AP tendría el mismo BSSID y un SSID único para facilitar la identificación de estaciones.",
        "c) Cada AP tendría un BSSID diferente y todos compartirían el mismo SSID para ser parte de la misma red.",
        "d) Todos los AP tendrían el mismo BSSID y SSID para simplificar la administración de la red.",
    ],
    "c"
),
(
    "En una red inalámbrica empresarial u organizativa con varios puntos de acceso (APs) conectados por un DS (Sistema de Distribución), ¿cómo se configurarían los BSSID y SSID?",
    [
        "a) Cada AP tendría un BSSID diferente y un SSID único para mayor diversidad.",
        "b) Cada AP tendría el mismo BSSID y un SSID único para facilitar la identificación de estaciones.",
        "c) Cada AP tendría un BSSID diferente y todos compartirían el mismo SSID para ser parte de la misma red.",
        "d) Todos los AP tendrían el mismo BSSID y SSID para simplificar la administración de la red.",
    ],
    "c"
),
(
    "En una red inalámbrica, ¿cómo obtiene una estación información sobre los SSID disponibles a los que puede conectarse?",
    [
        "a) A través de mensajes unicast enviados por los puntos de acceso.",
        "b) Mediante la asignación automática de SSID por parte del punto de acceso.",
        "c) Recibiendo mensajes broadcast llamados 'beacon' enviados por los puntos de acceso.",
        "d) Consultando directamente la configuración del punto de acceso.",
    ],
    "c"
),
(
    "¿Cuál es un requisito esencial para que una estación participe en una red inalámbrica?",
    [
        "a) Tener una dirección IP asignada.",
        "b) Configurarse con el SSID correcto.",
        "c) Utilizar un cable de red en lugar de conexión inalámbrica.",
        "d) Tener una antena de alta potencia.",
    ],
    "b"
),
(
    "¿Cómo obtiene una estación información sobre los SSID disponibles a los que puede conectarse en un momento dado?",
    [
        "a) Mediante mensajes unicast enviados por otras estaciones en la red.",
        "b) A través de solicitudes ARP (Address Resolution Protocol).",
        "c) Recibiendo mensajes broadcast llamados 'beacon' enviados por los puntos de acceso.",
        "d) Consultando directamente la base de datos del enrutador más cercano.",
    ],
    "c"
),
(
    "En una red inalámbrica, ¿cuál es el propósito de los mensajes broadcast llamados 'beacon' enviados por los puntos de acceso?",
    [
        "c) Informar sobre la dirección IP del punto de acceso.",
        "b) Transmitir datos de forma segura a todas las estaciones en la red.",
        "a) Difundir información sobre el SSID de la red a la que pertenecen.",
        "d) Gestionar las conexiones de red mediante mensajes unicast.",
    ],
    "a"
),
(
    "En una red inalámbrica, ¿con qué frecuencia suelen enviarse los mensajes 'beacon' por cada punto de acceso?",
    [
        "a) Una vez por minuto.",
        "b) 10 veces por segundo (cada 100 milisegundos).",
        "c) 5 veces por segundo (cada 200 milisegundos).",
        "d) 20 veces por segundo (cada 50 milisegundos).",
    ],
    "b"
),
(
    "En una red inalámbrica, ¿es posible ajustar la frecuencia de envío de los mensajes 'beacon' en la configuración de un punto de acceso?",
    [
        "a) No, la frecuencia de envío de los 'beacon' siempre es fija.",
        "b) Sí, la frecuencia de envío puede ajustarse y cambiar en la configuración del punto de acceso.",
        "c) Depende de la norma utilizada en la red.",
        "d) La frecuencia de envío se ajusta automáticamente según la carga de la red.",
    ],
    "b"
),
(
    "¿Cuál es una medida de seguridad que un punto de acceso (AP) puede implementar con respecto a los SSID?",
    [
        "a) Deshabilitar la funcionalidad de punto de acceso.",
        "b) Enviar beacons continuos para ocultar la identidad del SSID.",
        "c) Cifrar los SSID para proteger su identidad.",
        "d) Ocultar el SSID o configurar el AP para no enviar beacons como medida de seguridad.",
    ],
    "d"
),
(
    "¿Cuál de las siguientes medidas de seguridad puede implementar un punto de acceso (AP) para proteger la identidad del SSID?",
    [
        "a) Desactivar la capacidad de punto de acceso.",
        "b) Enviar beacons de forma continua para ocultar el SSID.",
        "c) Cifrar los SSID para proteger su identidad.",
        "d) Ocultar el SSID o configurar el AP para no enviar beacons.",
    ],
    "d"
),
(
    "A pesar de las medidas de seguridad como ocultar el SSID, ¿por qué los SSID aún pueden ser identificados?",
    [
        "a) Los SSID siempre viajan cifrados en la red inalámbrica.",
        "b) Los SSID no pueden ser identificados incluso con mensajes intercambiados con el AP.",
        "c) Ocultar el SSID no afecta su visibilidad y puede identificarse capturando y analizando mensajes intercambiados con el AP.",
        "d) Los SSID se cifran automáticamente cuando se ocultan.",
    ],
    "c"
),
(
    "En una red inalámbrica, ¿qué hacen habitualmente las estaciones además de esperar a recibir beacons?",
    [
        "a) Enviar mensajes unicast a otros dispositivos en la red.",
        "b) Enviar mensajes 'probe' o 'probe request' en busca de las redes a las que se conecta habitualmente.",
        "c) Transmitir mensajes broadcast continuos para anunciar su presencia.",
        "d) Enviar solicitudes ARP para mapear direcciones IP.",
    ],
    "b"
),
(
    "En una red inalámbrica, ¿qué tipo de mensajes envían habitualmente las estaciones en busca de las redes a las que se conectan?",
    [
        "a) Mensajes unicast solicitando información sobre la red.",
        "b) Mensajes 'broadcast' para anunciar su presencia en la red.",
        "c) Mensajes 'probe' o 'probe request' en busca de las redes a las que se conectan habitualmente.",
        "d) Mensajes de solicitud ARP para mapear direcciones IP.",
    ],
    "c"
),
(
    "Cuando un punto de acceso (AP) recibe un 'probe request' que indica el SSID de ese AP, ¿cuál es su obligación?",
    [
        "c) Ignorar el 'probe request' ya que es una actividad no deseada.",
        "b) Enviar un mensaje de respuesta indicando que el SSID es desconocido.",
        "a) Responder al 'probe request' proporcionando información sobre la red.",
        "d) No responder al 'probe request' ya que la red ya está disponible para la estación.",
    ],
    "a"
),
(
    "Cuando un punto de acceso (AP) recibe un 'probe request' que indica un SSID de 0 bytes (SSID broadcast), ¿cuál es su obligación?",
    [
        "a) Ignorar el 'probe request' ya que es una actividad no deseada.",
        "b) Enviar un mensaje de respuesta indicando que el SSID es desconocido.",
        "c) Responder al 'probe request' proporcionando información sobre la red.",
        "d) No responder al 'probe request' ya que la red ya está disponible para la estación.",
    ],
    "c"
),
(
    "En una red inalámbrica, ¿qué ocurre durante el proceso de asociación entre una estación y un punto de acceso (AP)?",
    [
        "a) La estación envía un 'probe request' al AP solicitando la asociación.",
        "b) El AP ignora la solicitud de asociación si la red no está protegida.",
        "c) El AP reserva memoria para la estación, asigna un ID de asociación y responde con una trama que contiene información del AP.",
        "d) La estación envía directamente tramas de datos al AP después de asociarse sin un proceso previo.",
    ],
    "c"
),
(
    "En una red inalámbrica sin configuración de protección, ¿qué pueden hacer las estaciones para conectarse a un punto de acceso (AP)?",
    [
        "a) Las estaciones no pueden conectarse sin protección.",
        "b) Las estaciones pueden conectarse directamente sin necesidad de asociarse a un AP.",
        "c) Las estaciones pueden enviar mensajes 'broadcast' para solicitar asociación a un AP.",
        "d) Las estaciones pueden asociarse a un AP enviando una trama de solicitud de asociación.",
    ],
    "d"
),
(
    "En una red inalámbrica sin configuración de seguridad, ¿cómo se compara la situación de una estación con la de una estación autorizada en una red segura?",
    [
        "a) La estación no puede conectarse sin protección, a diferencia de una estación autorizada en una red segura.",
        "b) La estación tiene acceso total a la red sin restricciones, al igual que una estación autorizada en una red segura.",
        "c) La estación debe seguir un proceso de asociación similar al de una estación autorizada en una red segura.",
        "d) La estación está automáticamente asociada sin necesidad de realizar ningún proceso, al igual que en una red segura.",
    ],
    "c"
),
(
    "Durante el proceso de asociación en una red inalámbrica, ¿qué elementos son incluidos en la trama de solicitud de asociación enviada por la estación?",
    [
        "a) Solo la dirección MAC de la estación.",
        "b) El SSID y taxas de transferencia admitidas.",
        "c) Unicamente el ID de asociación asignado por el AP.",
        "d) Información detallada sobre la red y el historial de conexión de la estación.",
    ],
    "b"
),
(
    "Durante el proceso de asociación en una red inalámbrica, ¿qué hace el AP después de recibir la trama de solicitud de asociación?",
    [
        "a) Ignora la solicitud y no reserva memoria para el cliente.",
        "b) Reserva memoria para el cliente, asigna un ID de asociación y responde con una trama de asociación que contiene el ID asignado y otras características del AP.",
        "c) Rechaza la solicitud si la red está protegida.",
        "d) Solo envía una trama de respuesta si la estación ya está en la lista de clientes asociados.",
    ],
    "b"
),
(
    "Después de completar el proceso de asociación en una red inalámbrica, ¿qué sucede entre el adaptador de red y el punto de acceso (AP)?",
    [
        "a) La estación y el AP solo pueden intercambiar tramas de control, no tramas de datos.",
        "b) Ambos pueden comenzar a transmitir tramas de datos entre ellos.",
        "c) El AP continúa reservando memoria pero no permite la transmisión de datos.",
        "d) La estación debe esperar instrucciones adicionales del AP antes de poder transmitir tramas de datos.",
    ],
    "b"
),
(
    "En una red inalámbrica, ¿cómo gestiona cada punto de acceso (AP) la lista de estaciones asociadas?",
    [
        "a) Los AP no mantienen una lista de estaciones asociadas.",
        "b) Cada AP tiene una lista de estaciones asociadas identificadas por sus direcciones IP.",
        "c) Cada AP mantiene una lista de estaciones asociadas identificadas por sus direcciones MAC.",
        "d) Los AP solo almacenan información sobre estaciones que actualmente transmiten datos.",
    ],
    "c"
),
(
    "Cuando un punto de acceso (AP) recibe una trama del Sistema de Distribución en una red inalámbrica, ¿cómo se comporta en relación con su lista de estaciones asociadas?",
    [
        "a) Ignora la trama, ya que solo se preocupa por las tramas provenientes de estaciones asociadas.",
        "b) Verifica si la dirección MAC de destino está en su lista de estaciones asociadas y, en caso afirmativo, transmite la trama a todas las estaciones.",
        "c) Descarta la trama si la dirección MAC de destino pertenece a una estación no asociada.",
        "d) Solo procesa la trama si la dirección MAC de destino coincide con la dirección MAC del AP.",
    ],
    "c"
),
(
    "Cuando un punto de acceso (AP) recibe una trama en una red inalámbrica, ¿qué hace el AP si la dirección MAC de destino de la trama pertenece a una estación no asociada?",
    [
        "a) El AP transmite la trama a todas las estaciones, independientemente de su asociación.",
        "b) El AP descarta la trama sin transmitirla.",
        "c) El AP verifica la dirección IP de destino antes de tomar cualquier acción.",
        "d) El AP almacena la trama en un búfer hasta que la estación se asocie.",
    ],
    "b"
),
(
    "En el intercambio de tráfico entre la interfaz inalámbrica y la interfaz de cable de un punto de acceso (AP), ¿cómo se compara el funcionamiento del AP con el de un switch LAN?",
    [
        "a) El AP inunda la red inalámbrica con tramas destinadas a direcciones desconocidas, similar a un switch LAN.",
        "b) El AP descarta todas las tramas destinadas a direcciones desconocidas en la red inalámbrica.",
        "c) El AP transmite tramas a todas las estaciones asociadas y no asociadas, independientemente de su destino.",
        "d) El AP filtra selectivamente las tramas destinadas a direcciones desconocidas en la red inalámbrica.",
    ],
    "d"
),
(
    "En una red inalámbrica, para que una estación esté asociada (conectada) a un punto de acceso (AP), ¿qué proceso debe realizar primero la estación?",
    [
        "a) Enviar un mensaje de solicitud de asociación al AP.",
        "b) Identificarse con su dirección MAC al AP.",
        "c) Enviar un mensaje de solicitud de dirección IP al AP.",
        "d) Establecer una conexión directa con el AP a través de un cable Ethernet.",
    ],
    "b"
),
(
    "En una red inalámbrica, a diferencia de la situación inicial de un switch en una red cableada, ¿qué afirmación describe correctamente el proceso de asociación de una estación a un punto de acceso (AP)?",
    [
        "a) En una red inalámbrica, la estación puede estar asociada sin identificarse con su dirección MAC.",
        "b) En una red inalámbrica, la estación puede asociarse directamente sin necesidad de identificación previa.",
        "c) En una red inalámbrica, el AP permite la asociación incluso si la estación no tiene dirección MAC.",
        "d) En una red inalámbrica, la estación debe identificarse con su dirección MAC antes de poder asociarse al AP.",
    ],
    "d"
),
(
    "En resumen, en una red inalámbrica, ¿bajo qué condiciones una estación está asociada a un punto de acceso (AP)?",
    [
        "a) La estación debe tener una dirección MAC diferente a la del AP para estar asociada.",
        "b) La estación puede estar asociada incluso si el AP no conoce su dirección MAC.",
        "c) La estación debe identificarse con su dirección MAC antes de poder estar asociada al AP.",
        "d) La estación está asociada solo si el AP no tiene ninguna estación conectada a él.",
    ],
    "c"
),
(
    "En el funcionamiento con estaciones asociadas, ¿cómo opera la interfaz inalámbrica de un Punto de Acceso (AP) en una red inalámbrica?",
    [
        "a) La comunicación es bidireccional y simultánea (full-dúplex) entre el AP y las estaciones asociadas.",
        "b) La comunicación es unidireccional desde el AP hacia las estaciones asociadas.",
        "c) La comunicación es half-dúplex, bidireccional, pero nunca al mismo tiempo entre el AP y las estaciones asociadas.",
        "d) La comunicación solo se permite desde las estaciones asociadas hacia el AP.",
    ],
    "c"
),
(
    "En una red inalámbrica con estaciones asociadas a un Punto de Acceso (AP), ¿cómo se comportan las tramas enviadas desde cualquier elemento de la red?",
    [
        "a) Las tramas se envían exclusivamente al destinatario previsto, ignorando a las demás estaciones asociadas.",
        "b) Todas las estaciones asociadas al AP reciben las tramas, independientemente del destinatario.",
        "c) Solo el AP recibe las tramas y decide si retransmitirlas a las estaciones asociadas.",
        "d) Las tramas se envían a una única estación asociada, seleccionada al azar por el AP.",
    ],
    "b"
),
(
    "En las normas 802.11n y 802.11ac, que emplean diferentes flujos en la cobertura de cada Punto de Acceso (AP), ¿cómo funciona el AP con múltiples flujos?",
    [
        "a) Cada flujo se dirige exclusivamente a un único equipo asociado, similar a un switch cableado.",
        "b) El AP distribuye cada flujo a todas las estaciones asociadas de manera simultánea.",
        "c) El AP decide aleatoriamente a qué estación asociada enviar cada flujo.",
        "d) Cada flujo puede ir destinado a un equipo diferente, similar al funcionamiento de un switch inalámbrico.",
    ],
    "d"
),
(
    "En las normas 802.11n y 802.11ac, que emplean diferentes flujos en la cobertura de cada Punto de Acceso (AP), ¿cuál es el propósito principal de utilizar múltiples flujos?",
    [
        "a) Mejorar la seguridad de la red inalámbrica.",
        "b) Reducir la interferencia de otras redes inalámbricas.",
        "c) Aumentar la capacidad y velocidad de transmisión de datos.",
        "d) Optimizar la asignación de direcciones IP en la red.",
    ],
    "c"
),
(
    "En las normas 802.11n y 802.11ac, que utilizan diferentes flujos en la cobertura de cada Punto de Acceso (AP), ¿cómo se asemeja el funcionamiento del AP a un switch inalámbrico?",
    [
        "a) Cada flujo se dirige exclusivamente a un único equipo asociado.",
        "b) El AP distribuye cada flujo a todas las estaciones asociadas de manera simultánea.",
        "c) El AP decide aleatoriamente a qué estación asociada enviar cada flujo.",
        "d) Cada flujo puede ir destinado a un equipo diferente, similar al funcionamiento de un switch inalámbrico.",
    ],
    "d"
),
(
    "En una red inalámbrica, ¿por qué una estación debe reasociarse al cambiar de un AP a otro?",
    [
        "a) Para mejorar la velocidad de transmisión.",
        "b) Porque cada estación solo puede estar asociada a un AP a la vez.",
        "c) Para evitar conflictos de dirección MAC.",
        "d) Porque el estándar 802.11 lo requiere explícitamente.",
    ],
    "b"
),
(
    "¿Qué significa el término 'itinerancia' (handoff o roaming) en el contexto de las redes inalámbricas? ¿Cuál es la restricción principal relacionada con la asociación de una estación a múltiples APs al mismo tiempo?",
    [
        "a) Capacidad de transmitir datos a larga distancia.",
        "b) Proceso de cambiar de un AP a otro sin perder la conexión.",
        "c) Modo de operación exclusivo de la norma 802.11r.",
        "d) Restricción impuesta por la banda de frecuencia.",
    ],
    "b"
),
(
    "En el contexto de redes inalámbricas, ¿qué acción debe realizar una estación cuando se aleja de un AP y se acerca a otro AP en términos de itinerancia?",
    [
        "a) Permanecer asociada al primer AP.",
        "b) Desasociarse del primer AP y asociarse al segundo AP.",
        "c) Permanecer asociada a ambos APs simultáneamente.",
        "d) Desconectarse temporalmente de todos los APs.",
    ],
    "b"
),
(
    "En el contexto de itinerancia en redes inalámbricas, ¿por qué es importante realizar el proceso de cambio de AP con suficiente rapidez?",
    [
        "a) Para evitar la necesidad de reasociación.",
        "b) Para garantizar una transición sin pérdida de paquetes.",
        "c) Para reducir la velocidad de la estación.",
        "d) Para mejorar la calidad de la señal inalámbrica.",
    ],
    "b"
),
(
    "En el contexto de itinerancia en redes inalámbricas, ¿cuál es uno de los factores que influyen en la rapidez del proceso de cambio de AP?",
    [
        "a) La cantidad de dispositivos conectados a los AP.",
        "b) La potencia de la señal inalámbrica.",
        "c) El grado de solapamiento de las áreas de cobertura de los dos AP.",
        "d) La capacidad de almacenamiento de los AP.",
    ],
    "c"
),
(
    "¿Por qué la velocidad de movimiento de la estación es un factor relevante en el proceso de itinerancia?",
    [
        "a) Afecta la calidad de la señal inalámbrica.",
        "b) No tiene impacto en la itinerancia.",
        "c) Determina la cantidad de datos transferidos.",
        "d) Influye en la agresividad de la itinerancia.",
    ],
    "a"
),
(
    "¿Cómo se realiza la itinerancia ('handoff' o 'roaming') en una red inalámbrica?",
    [
        "a) Una estación puede estar asociada a múltiples AP al mismo tiempo.",
        "b) La estación debe permanecer siempre asociada al primer AP, independientemente de su ubicación.",
        "c) La estación se desasocia del primer AP y se asocia al segundo AP cuando se aleja.",
        "d) La itinerancia no es posible en redes inalámbricas.",
    ],
    "c"
),
(
    "La rapidez de la itinerancia depende de:",
    [
        "a) El grado de solapamiento de las áreas de cobertura de los dos APs.",
        "b) La velocidad a la que se mueve la estación.",
        "c) La agresividad de la itinerancia (configurable en la estación).",
        "d) Todas las anteriores.",
    ],
    "d"
),
(
    "¿Estaba contemplada la itinerancia en el estándar 802.11 inicial?",
    [
        "a) Sí, la itinerancia estaba completamente contemplada desde el inicio.",
        "b) No, la itinerancia no estaba contemplada en el estándar 802.11 inicial.",
        "c) La itinerancia estaba parcialmente contemplada.",
        "d) No, ni siquiera lo está ahora.",
    ],
    "b"
),
(
    "¿Qué impacto tuvo la aparición de los teléfonos 802.11 en la itinerancia?",
    [
        "a) No tuvo impacto en la itinerancia.",
        "b) Redujo la itinerancia a velocidades más lentas.",
        "c) Aumentó la itinerancia, haciéndola más rápida y segura.",
        "d) Generó problemas en la itinerancia.",
    ],
    "c"
),
(
    "¿Cuál es el tiempo máximo recomendado para que el cambio en la itinerancia mantenga la comunicación?",
    [
        "a) Menos de 10 milisegundos.",
        "b) Entre 10 y 30 milisegundos.",
        "c) Menos de 50 milisegundos.",
        "d) Más de 50 milisegundos.",
    ],
    "c"
),
(
    "¿Cuál es el propósito de la autenticación en redes WiFi con contraseñas?",
    [
        "a) Asegurar que todas las estaciones tengan el mismo nombre de red (SSID).",
        "b) Establecer una conexión segura entre el AP y las estaciones.",
        "c) Agilizar el proceso de itinerancia al cambiar de AP.",
        "d) Evitar la necesidad de contraseñas en la red WiFi.",
    ],
    "b"
),
(
    "¿Por qué se utiliza algún protocolo de cifrado como mecanismo de seguridad en redes WiFi?",
    [
        "a) Para acelerar la velocidad de la red.",
        "b) Para garantizar la compatibilidad con dispositivos más antiguos.",
        "c) Para cifrar la información y garantizar la seguridad de la comunicación.",
        "d) Solo como una recomendación, pero no es esencial para la seguridad.",
    ],
    "c"
),
(
    "¿Cuáles son algunos de los protocolos más empleados para la seguridad en redes WiFi?",
    [
        "a) SSL y TLS.",
        "b) WEP, WPA, y WPA2.",
        "c) TCP y UDP.",
        "d) HTTP y FTP.",
    ],
    "b"
),
(
    "¿Por qué se recomienda el uso de WPA2 en lugar de WEP en redes WiFi?",
    [
        "a) WPA2 es más antiguo y compatible con una variedad de dispositivos.",
        "b) WEP ha sido descontinuado, por lo que no es viable su uso actualmente.",
        "c) WPA2 es mucho más seguro que WEP, siendo este último considerado inseguro.",
        "d) WEP ofrece una mejor velocidad de conexión que WPA2.",
    ],
    "c"
),
(
    "Cuando hay una contraseña en la red, ¿qué hace el Punto de Acceso (AP) antes de permitir la asociación de las estaciones?",
    [
        "a) El AP solo verifica la velocidad de conexión de las estaciones.",
        "b) El AP permite la asociación sin autenticación.",
        "c) El AP obliga a las estaciones a autenticarse antes de permitir su asociación.",
        "d) La autenticación es opcional y depende de la configuración del dispositivo.",
    ],
    "c"
),
(
    "En una red WiFi, ¿cómo se realiza la autenticación y la asociación de una estación?",
    [
        "a) La autenticación se realiza con el BSSID y la asociación con el SSID.",
        "b) Tanto la autenticación como la asociación se realizan con el SSID.",
        "d) La autenticación se realiza con el SSID y un contrasinal, mientras que la asociación se realiza con el BSSID.",
        "c) La autenticación y la asociación se realizan exclusivamente con el BSSID.",
    ],
    "d"
),
(
    "¿Cuándo se realiza la autenticación en una red WiFi y cómo se simplifica durante el proceso de reasociación para acelerar la itinerancia?",
    [
        "a) La autenticación se realiza solo durante el cambio de AP.",
        "b) La autenticación se realiza antes de la asociación y se simplifica durante el proceso de reasociación (cambio de AP) para acelerar la itinerancia.",
        "c) La autenticación se realiza solo al unirse a la red por primera vez.",
        "d) La autenticación y la asociación siempre son procesos independientes, sin simplificación durante la reasociación.",
    ],
    "b"
),


















































































































































    # Hay que saber distinguir entre los dos tipos de cable, el b856 o como se llame del otro, el que cambian los colores.





    ]


######################################################################################

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