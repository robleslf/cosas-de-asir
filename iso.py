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
    (
        "¿Cómo se emite por pantalla un salto de línea y una tabulación en el comando echo?",
        [
            'a) echo -e "\\nAquí va un salto de línea y \\tojo que aquí va una tabulación."',
            'b) echo -e "\\nAquí va un salto de línea y \\tojo que aquí va una tabulación."',
            'c) echo "\\nAquí va un salto de línea y \\tojo que aquí va una tabulación." -e',
            'd) echo "\\nAquí va un salto de línea y \\tojo que aquí va una tabulación."',
        ],
        "b"
    ),
    (
        "¿Qué hace el parámetro -e en el comando echo?",
        [
            'a) Muestra el resultado en un formato especial.',
            'b) Indica que se utilizarán escapes en el texto.',
            'c) Emite el texto sin cambios.',
            'd) Es un error de sintaxis.',
        ],
        "b"
    ),
    (
        "¿Cómo se emiten por pantalla los números del 1 al 10 en el comando echo?",
        [
            'a) echo {1..10}',
            'b) echo {1..10}-',
            'c) echo -{1..10}-',
            'd) echo {1..10} -d -',
        ],
        "a"
    ),
    (
        "¿Cómo se emiten por pantalla los números del 1 al 10 separados por guiones en el comando echo?",
        [
            'a) echo {1..10}',
            'b) echo {1..10}-',
            'c) echo -{1..10}-',
            'd) echo {1..10}-',
        ],
        "b"
    ),
    (
        "¿Cómo se emiten por pantalla los números del 1 al 10 con un guión delante y otro detrás en el comando echo?",
        [
            'a) echo {1..10}',
            'b) echo {1..10}-',
            'c) echo -{1..10}-',
            'd) echo {1..10}-',
        ],
        "c"
    ),
    (
        "¿Cómo se emiten por pantalla las letras de la a a la f en el comando echo?",
        [
            'a) echo {a..f}',
            'b) echo {A..F}',
            'c) echo {{a..f},{A..F}}',
            'd) echo {{a..f}{A..F}}',
        ],
        "a"
    ),
    (
        "¿Cómo se emiten por pantalla las letras de la a a la z y de la A a la Z en el comando echo?",
        [
            'a) echo {a..Z}',
            'b) echo {aA..zZ}',
            'c) echo {{a..z},{A..Z}}',
            'd) echo {{A..Z}{a..z}}',
        ],
        "c"
    ),
    (
        "¿Cómo se emiten por pantalla las letras de la a a la z y de la A a la Z agrupadas primero mayúsculas y después minúsculas en el comando echo?",
        [
            'a) echo {a..z}',
            'b) echo {A..Z}',
            'c) echo {{A..Z},{a..z}}',
            'd) echo {{A..Z}{a..z}}',
        ],
        "c"
    ),
    (
        "¿Cómo se emiten por pantalla las combinaciones de letras de la A a la Z y de la a a la z en el comando echo?",
        [
            'a) echo {a..z}',
            'b) echo {A..Z}',
            'c) echo {{A..Z},{a..z}}',
            'd) echo {{A..Z}{a..z}}',
        ],
        "d"
    ),
    (
        "¿Cómo se emiten por pantalla las combinaciones de números del 1 al 9 después de un punto decimal 1 en el comando echo?",
        [
            'a) echo 1.{0..9}',
            'b) echo {1..9}.0',
            'c) echo 1.{1..9}',
            'd) echo {1..9}.1',
        ],
        "c"
    ),
    (
        "¿Cómo se emiten por pantalla los números impares del 1 al 20 con un salto de dos en dos en el comando echo?",
        [
            'a) echo {1..20..2}',
            'b) echo {1..20}',
            'c) echo {2..20..2}',
            'd) echo {10..1..2}',
        ],
        "a"
    ),
    (
        "¿Cómo se emiten por pantalla los números pares del 10 al 1 en reversa en el comando echo?",
        [
            'a) echo {1..10}',
            'b) echo {10..1..2}',
            'c) echo {10..1} -2',
            'd) echo {1..20..2}',
        ],
        "b"
    ),
    (
        "¿Qué hace el siguiente comando: 'cat fichero.informe > fich1 2> errores.txt'?",
        [
            'a) Guarda la salida del comando "cat fichero.informe" en el archivo fich1 y los errores en errores.txt.',
            'b) Guarda la salida del comando "cat fichero.informe" y los errores en el archivo fich1.',
            'c) Combina la salida del comando "cat fichero.informe" y los errores en el archivo fich1.',
            'd) Imprime el contenido de fichero.informe en la consola y guarda los errores en errores.txt.',
        ],
        "a"
    ),
    (
        "¿Cómo se modificaría el comando para que ambas, la salida y los errores, se guarden en el mismo fichero 'fich1'?",
        [
            'a) cat fichero.informe &> fich1',
            'b) cat fichero.informe > fich1 2> fich1',
            'c) cat fichero.informe > fich1 &> errores.txt',
            'd) cat fichero.informe > fich1; cat errores.txt >> fich1',
        ],
        "a"
    ),
    (
        "¿Qué hace el siguiente comando: '(pwd; date; echo $USER) > solucion.txt'?",
        [
            'a) Guarda la salida del comando "pwd", "date", y "echo $USER" en el archivo solucion.txt.',
            'b) Ejecuta los comandos "pwd", "date", y "echo $USER" y guarda la salida en solucion.txt.',
            'c) Imprime la salida de los comandos "pwd", "date", y "echo $USER" en la consola.',
            'd) Guarda la salida del comando "pwd; date; echo $USER" en el archivo solucion.txt.',
        ],
        "a"
    ),
    (
        "¿Cómo podrías lograr el mismo resultado que el comando anterior pero añadiendo las salidas a solucion.txt en lugar de sobrescribirlo?",
        [
            'a) pwd >> solucion.txt; date >> solucion.txt; echo $USER >> solucion.txt',
            'b) pwd > solucion.txt; date > solucion.txt; echo $USER > solucion.txt',
            'c) pwd; date; echo $USER >> solucion.txt',
            'd) (pwd; date; echo $USER) >> solucion.txt',
        ],
        "a"
    ),
    (
        "¿Cómo abres el editor de texto 'nano' desde la terminal?",
        [
            'a) open nano',
            'b) nano',
            'c) text nano',
            'd) editor nano',
        ],
        "b"
    ),
    (
        "¿Cuál es la combinación de teclas para guardar en 'nano'?",
        [
            'a) Ctrl+S',
            'b) Ctrl+O',
            'c) Ctrl+G',
            'd) Ctrl+X',
        ],
        "b"
    ),
    (
        "¿Cuál es la combinación de teclas para salir de 'nano'?",
        [
            'a) Ctrl+S',
            'b) Ctrl+O',
            'c) Ctrl+X',
            'd) Ctrl+Q',
        ],
        "c"
    ),
    (
        "¿Cómo puedes utilizar el comando 'sort' para ordenar líneas de texto ingresadas manualmente hasta que se escriba la palabra 'END'?",
        [
            'a) sort -m',
            'b) sort <<END',
            'c) sort -a END',
            'd) sort -e',
        ],
        "b"
    ),
    (
        "¿Qué hace el comando 'sort -M <<END'?",
        [
            'a) Ordena las líneas de texto alfabéticamente.',
            'b) Ordena las líneas de texto numéricamente.',
            'c) Ordena las líneas de texto por meses.',
            'd) Detiene la ejecución del comando.',
        ],
        "c"
    ),
    (
        "Si quieres guardar la salida ordenada por meses en un archivo llamado 'meses.txt', ¿cuál sería el comando correcto?",
        [
            'a) sort -M <<END > meses.txt',
            'b) sort -M > meses.txt <<END',
            'c) sort <<END -M > meses.txt',
            'd) sort -M > meses.txt',
        ],
        "a"
    ),
        (
        "¿Cuál es el propósito del comando 'cmp colores.txt color.txt'?",
        [
            'a) Compara dos archivos y muestra las diferencias.',
            'b) Compara dos archivos y muestra las similitudes.',
            'c) Compara dos archivos, y si son idénticos, no muestra nada.',
            'd) Compara dos archivos, y si son diferentes, no muestra nada.',
        ],
        "c"
    ),
    (
        "¿Qué sucede si 'cmp' encuentra el primer error al comparar las líneas de los archivos?",
        [
            'a) Continúa comparando todas las líneas y muestra todas las diferencias.',
            'b) Deja de leer y muestra el primer error encontrado.',
            'c) Ignora el error y continúa comparando todas las líneas.',
            'd) Muestra un mensaje de error y se detiene.',
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando 'comm colores.txt color.txt'?",
        [
            'a) Compara dos archivos y muestra las diferencias.',
            'b) Compara dos archivos y muestra las similitudes.',
            'c) Compara dos archivos línea por línea y muestra las diferencias y similitudes.',
            'd) Compara dos archivos y muestra solo las similitudes.',
        ],
        "c"
    ),
    (
        "¿Cómo se estructura la salida del comando 'comm'?",
        [
            'a) Muestra solo las líneas idénticas en ambos archivos.',
            'b) Muestra solo las líneas diferentes en ambos archivos.',
            'c) Muestra tres columnas: solo en archivo1, solo en archivo2, en ambos archivos.',
            'd) Muestra una única columna con todas las líneas de ambos archivos.',
        ],
        "c"
    ),
    (
        "¿Cuántas columnas muestra la salida del comando 'comm'?",
        [
            'a) Una columna.',
            'b) Dos columnas.',
            'c) Tres columnas.',
            'd) Cuatro columnas.',
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito del comando 'comm colores.txt color.txt'?",
        [
            'a) Compara dos archivos y muestra las diferencias.',
            'b) Compara dos archivos y muestra las similitudes.',
            'c) Compara dos archivos línea por línea y muestra las diferencias y similitudes.',
            'd) Compara dos archivos y muestra solo las similitudes.',
        ],
        "c"
    ),
    (
        "¿Cómo se estructura la salida del comando 'comm'?",
        [
            'a) Muestra solo las líneas idénticas en ambos archivos.',
            'b) Muestra solo las líneas diferentes en ambos archivos.',
            'c) Muestra tres columnas: solo en archivo1, solo en archivo2, en ambos archivos.',
            'd) Muestra una única columna con todas las líneas de ambos archivos.',
        ],
        "c"
    ),
    (
        "¿Cuántas columnas muestra la salida del comando 'comm'?",
        [
            'a) Una columna.',
            'b) Dos columnas.',
            'c) Tres columnas.',
            'd) Cuatro columnas.',
        ],
        "c"
    ),
    (
        "¿Qué hace el comando 'comm -1 color.txt colores.txt'?",
        [
            'a) Suprime las líneas únicas del archivo 1.',
            'b) Muestra las líneas únicas del archivo 1.',
            'c) Suprime las líneas comunes a ambos archivos.',
            'd) Muestra las líneas comunes a ambos archivos.',
        ],
        "a"
    ),
    (
        "¿Qué hace el comando 'comm -2 color.txt colores.txt'?",
        [
            'a) Suprime las líneas únicas del archivo 2.',
            'b) Muestra las líneas únicas del archivo 2.',
            'c) Suprime las líneas comunes a ambos archivos.',
            'd) Muestra las líneas comunes a ambos archivos.',
        ],
        "a"
    ),
    (
        "¿Qué hace el comando 'comm -3 colores.txt color.txt'?",
        [
            'a) Suprime las líneas únicas del archivo 1.',
            'b) Suprime las líneas únicas del archivo 2.',
            'c) Suprime las líneas comunes a ambos archivos.',
            'd) Muestra las líneas comunes a ambos archivos.',
        ],
        "c"
    ),
    (
        "¿Qué limitación tiene el comando 'comm' según la nota proporcionada?",
        [
            'a) No puede comparar archivos de más de 1000 líneas.',
            'b) No puede comparar archivos con líneas muy largas.',
            'c) No puede ignorar mayúsculas y minúsculas en la comparación.',
            'd) No puede comparar archivos con nombres que contienen espacios.',
        ],
        "c"
    ),
        (
        "¿Cuál es el propósito principal del comando 'diff' en sistemas Unix y Linux?",
        [
            'a) Compara el tamaño de dos archivos.',
            'b) Compara la fecha de modificación de dos archivos.',
            'c) Compara el contenido de dos archivos línea por línea.',
            'd) Compara los permisos de acceso de dos archivos.',
        ],
        "c"
    ),
    (
        "¿Qué muestra la salida del comando 'diff'?",
        [
            'a) Muestra las similitudes entre dos archivos.',
            'b) Muestra las diferencias entre dos archivos.',
            'c) Muestra información general sobre los archivos.',
            'd) Muestra el tamaño total de las diferencias.',
        ],
        "b"
    ),
    (
        "Si los archivos son idénticos, ¿qué muestra el comando 'diff'?",
        [
            'a) No muestra nada.',
            'b) Muestra un mensaje indicando que los archivos son idénticos.',
            'c) Muestra un resumen estadístico de las similitudes.',
            'd) Muestra un mensaje de error indicando que los archivos son iguales.',
        ],
        "a"
    ),
    (
        "¿Cuántos archivos puede comparar el comando 'diff3'?",
        [
            'a) Dos archivos.',
            'b) Tres archivos.',
            'c) Diez archivos.',
            'd) Cualquier número de archivos.',
        ],
        "b"
    ),
    (
        "¿Cuál es la función del parámetro '-i' en el comando 'diff3'?",
        [
            'a) Ignora la salida del comando.',
            'b) Incluye los cambios en el resultado final.',
            'c) Ignora las diferencias en mayúsculas y minúsculas.',
            'd) Invierte el sentido de la comparación.',
        ],
        "c"
    ),
    (
        "¿Qué hace el comando 'diff3 -i colores.txt color.txt colorines.txt'?",
        [
            'a) Compara dos archivos, colores.txt y color.txt, ignorando las mayúsculas y minúsculas.',
            'b) Compara tres archivos, colores.txt, color.txt y colorines.txt, incluyendo los cambios en el resultado final.',
            'c) Compara tres archivos, colores.txt, color.txt y colorines.txt, ignorando las mayúsculas y minúsculas.',
            'd) Ignora la salida de tres archivos, colores.txt, color.txt y colorines.txt.',
        ],
        "c"
    ),
    (
        "¿Cuál es la principal diferencia entre 'diff' y 'diff3'?",
        [
            'a) diff3 solo compara dos archivos.',
            'b) diff3 muestra las diferencias en formato gráfico.',
            'c) diff3 permite comparar tres archivos.',
            'd) diff3 solo compara archivos de texto plano.',
        ],
        "c"
    ),
    (
        "¿Cuál de los siguientes comandos se utiliza comúnmente para comparar dos  archivos y mostrar solo las líneas comunes a los tres archivos?",
        [
            'a) comm -1',
            'b) comm -2',
            'c) comm -3',
            'd) comm -c',
        ],
        "a"
    ),
    (
        "¿Cuándo es más comúnmente utilizado el comando 'diff -i'?",
        [
            'a) Cuando se quieren mostrar solo las líneas únicas del archivo 1.',
            'b) Cuando se quieren mostrar solo las líneas únicas del archivo 2.',
            'c) Cuando se quieren mostrar las diferencias ignorando las mayúsculas y minúsculas.',
            'd) Cuando se quieren mostrar las diferencias invertidas.',
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito principal del comando 'last' en sistemas Unix y Linux?",
        [
            'a) Muestra información sobre el estado actual del sistema.',
            'b) Muestra un historial de las últimas conexiones de usuarios al sistema.',
            'c) Muestra el contenido de los archivos de registro del sistema.',
            'd) Muestra las tareas programadas del sistema.',
        ],
        "b"
    ),
    (
        "¿Qué tipo de información proporciona el comando 'last'?",
        [
            'a) Información sobre el uso actual de los recursos del sistema.',
            'b) Información sobre las últimas conexiones de usuarios, incluyendo quién, cuándo y desde dónde.',
            'c) Información sobre el espacio en disco disponible.',
            'd) Información sobre las últimas actualizaciones del sistema.',
        ],
        "b"
    ),
    (
        "¿Qué detalles sobre las conexiones de usuario muestra el comando 'last'?",
        [
            'a) Solo muestra el nombre de usuario.',
            'b) Muestra solo la hora de inicio de sesión.',
            'c) Muestra quién inició sesión, cuándo lo hicieron y desde qué ubicación (terminal o dirección IP).',
            'd) Muestra solo las conexiones activas en el momento actual.',
        ],
        "c"
    ),
    (
        "¿Cuál es uno de los usos comunes del comando 'last'?",
        [
            'a) Verificar la integridad del sistema de archivos.',
            'b) Monitorizar el rendimiento del sistema en tiempo real.',
            'c) Analizar el historial de conexiones de usuarios al sistema.',
            'd) Realizar copias de seguridad de archivos críticos del sistema.',
        ],
        "c"
    ),
    (
        "¿Cuál es el archivo de registro principal utilizado por 'last' en sistemas Unix y Linux?",
        [
            'a) /var/log/auth.log',
            'd) /var/log/wtmp',
            'c) /var/log/btmp',
            'b) /var/log/syslog',
        ],
        "d"
    ),
        (
        "¿Cuál es el propósito principal del comando 'lastb' en sistemas Unix y Linux?",
        [
            'a) Muestra información sobre las últimas conexiones exitosas al sistema.',
            'b) Muestra una lista de intentos de inicio de sesión fallidos registrados en el sistema.',
            'c) Muestra información sobre el espacio en disco disponible.',
            'd) Muestra una lista de los usuarios conectados en tiempo real.',
        ],
        "b"
    ),
        (
        "¿Qué tipo de información proporciona el comando 'lastb'?",
        [
            'a) Información sobre las últimas conexiones de usuarios al sistema.',
            'b) Información sobre intentos de inicio de sesión exitosos.',
            'c) Información sobre intentos de inicio de sesión fallidos.',
            'd) Información sobre las tareas programadas del sistema.',
        ],
        "c"
    ),
        (
        "¿Cuál es el archivo de registro principal utilizado por 'lastb' en sistemas Unix y Linux?",
        [
            'a) /var/log/btmp',
            'd) /var/log/wtmp',
            'c) /var/log/messages',
            'b) /var/log/syslog',
        ],
        "a"
    ),
            (
        "¿Cuál de las siguientes afirmaciones respecto al comando lastb es la correcta?",
        [
            'a) El comando lastb muestra los intentos fallidos de inicio de sesión al sistema, que están recogidos en el archivo binario /var/log/wtmp',
            'd) Para utilizar el comando lastb será necesario usar "sudo", ya que sin permisos especiales no nos dejará ver el contenido del archivo /var/log/btmp.',
            'c) El comando lastb muestra las últimas conexiones de usuarios al sistema, que está recogidos en el archivo binario /var/log/wtmp',
            'b) Ninguna de las anteriores es correcta.',
        ],
        "d"
    ),
    (
        "En sistemas Debian, ¿por qué generalmente no existe el comando 'sudo' para usuarios regulares?",
        [
            'a) Porque los usuarios regulares no necesitan realizar tareas administrativas en un servidor Debian.',
            'b) Porque los usuarios regulares no pueden autenticarse en un servidor Debian.',
            'c) Porque se supone que en un servidor Debian no pueden acceder usuarios.',
            'd) Porque el comando sudo es exclusivo para usuarios con privilegios de superusuario.',
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito principal del comando 'sudo' en sistemas Unix y Linux?",
        [
            'a) Para cambiar el nombre de usuario actual.',
            'b) Para ejecutar comandos en nombre del superusuario o administrador.',
            'c) Para listar usuarios conectados al sistema.',
            'd) Para cerrar sesión de un usuario.',
        ],
        "b"
    ),
    (
        "¿Qué significa la abreviatura 'sudo'?",
        [
            'a) Substituting User with Default Options.',
            'b) SuperUser Directory Operation.',
            'c) Switch User and Do Operation.',
            'd) SuperUser DO (o SuperUser Done).',
        ],
        "d"
    ),
    (
        "¿Qué requisitos son necesarios para ejecutar comandos con 'sudo'?",
        [
            'a) Estar en un directorio específico.',
            'b) Tener privilegios de superusuario o pertenecer a grupos de administración.',
            'c) Estar en modo de usuario invitado.',
            'd) Tener una conexión a Internet activa.',
        ],
        "b"
    ),
    (
        "¿Cuándo un administrador generalmente utiliza el comando 'sudo'?",
        [
            'a) Para cambiar la configuración del sistema de archivos.',
            'b) Para realizar tareas administrativas en nombre del superusuario.',
            'c) Para abrir una nueva sesión de usuario.',
            'd) Para visualizar el historial de conexiones de usuarios.',
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito principal del comando 'su' en sistemas Unix y Linux?",
        [
            'a) Cambiar la configuración del sistema de archivos.',
            'b) Trabajar con otro usuario normal iniciando una nueva sesión con su nombre de cuenta.',
            'c) Ejecutar comandos como superusuario sin cambiar de usuario.',
            'd) Listar todos los usuarios del sistema.',
        ],
        "b"
    ),
    (
        "¿Cómo se utiliza el comando 'su' para cambiar a otro usuario?",
        [
            'a) su -c nombredecuenta',
            'b) su nombredecuenta',
            'c) cambiar nombredecuenta',
            'd) switchuser nombredecuenta',
        ],
        "b"
    ),
    (
        "¿Cuál es la diferencia principal entre 'su' y 'sudo'?",
        [
            'a) "su" permite cambiar a otro usuario normal, mientras que "sudo" ejecuta comandos como superusuario.',
            'b) "su" y "sudo" son intercambiables y se utilizan para cambiar a otro usuario.',
            'c) "su" solo se utiliza para cambiar al superusuario, mientras que "sudo" cambia a cualquier usuario normal.',
            'd) "su" y "sudo" realizan las mismas funciones y pueden usarse indistintamente.',
        ],
        "a"
    ),
    (
        "¿Qué es necesario proporcionar al utilizar el comando 'su' para cambiar a otro usuario?",
        [
            'a) Solo el nombre del usuario al que se desea cambiar.',
            'b) La contraseña del usuario actual.',
            'c) La contraseña del usuario al que se desea cambiar.',
            'd) La dirección IP del usuario al que se desea cambiar.',
        ],
        "c"
    ),
    (
        "¿En qué situación un usuario comúnmente utiliza 'su'?",
        [
            'a) Para cambiar la configuración del sistema operativo.',
            'b) Para trabajar temporalmente como otro usuario sin cerrar la sesión actual.',
            'c) Para abrir una nueva sesión con privilegios de superusuario.',
            'd) Para listar usuarios conectados al sistema.',
        ],
        "b"
    ),
    (
        "¿Cuál es una razón por la cual generalmente se desaconseja usar 'su root' en sistemas Unix y Linux?",
        [
            'a) Porque "su root" no permite ejecutar comandos como superusuario.',
            'b) Porque "su root" cierra la sesión actual después de ejecutar un comando como superusuario.',
            'c) Porque "su root" puede dejar la sesión abierta, lo cual podría ser un riesgo de seguridad.',
            'd) Porque "su root" requiere reiniciar el sistema después de cada uso.',
        ],
        "c"
    ),
        (
        "¿Qué resultado se espera al ejecutar el comando 'last -3 reboot' en una terminal?",
        [
            'a) Muestra los últimos 3 archivos de registro del sistema relacionados con reinicios.',
            'b) Muestra los últimos 3 usuarios que reiniciaron el sistema.',
            'c) Muestra los detalles de los últimos 3 reinicios del sistema, incluyendo la fecha, hora y usuarios.',
            'd) Muestra una lista de los últimos 3 comandos "reboot" ejecutados en el sistema.',
        ],
        "c"
    ),
        (
        "¿Qué resultado se espera al ejecutar el comando 'last asir1' en una terminal?",
        [
            'a) Muestra la información detallada del usuario asir1.',
            'b) Muestra la fecha y hora de la última conexión del usuario asir1.',
            'c) Muestra la lista de comandos ejecutados por el usuario asir1.',
            'd) Muestra los usuarios que han compartido la sesión con asir1.',
        ],
        "b"
    ),
        (
        "¿Cuál es el propósito principal del comando 'uptime' en sistemas Unix y Linux?",
        [
            'a) Mostrar el tiempo actual del sistema.',
            'b) Visualizar la lista de usuarios activos en el sistema.',
            'c) Reiniciar el sistema.',
            'd) Mostrar el tiempo de actividad del sistema.',
        ],
        "d"
    ),
    (
        "¿Qué información proporciona el comando 'du' por defecto cuando se ejecuta sin argumentos adicionales?",
        [
            'a) Muestra la fecha de última modificación de los archivos en el directorio de trabajo.',
            'd) Evalúa la utilización de disco de todo el contenido en el directorio de trabajo.',
            'c) Visualiza la carga actual del sistema en términos de usuarios conectados.',
            'b) Muestra el tiempo actual del sistema.',
        ],
        "d"
    ),
    (
        "¿Cuál es el propósito de la opción '-h' en el comando 'du -h'?",
        [
            'a) Oculta la información de los archivos en el directorio de trabajo.',
            'b) Muestra la utilización de disco en kilobytes.',
            'd) Proporciona una salida humanamente legible con unidades como KB, MB, etc.',
            'c) Habilita la visualización de la fecha de última modificación.',
        ],
        "d"
    ),
    (
        "¿Qué hace el comando 'du -a'?",
        [
            'a) Muestra la fecha de última modificación de los archivos en el directorio de trabajo y sus subdirectorios.',
            'b) Calcula la utilización de disco solo para archivos ocultos en el directorio de trabajo.',
            'c) Muestra la utilización de disco del directorio de trabajo y sus subdirectorios, incluyendo archivos ocultos.',
            'd) Visualiza la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
        ],
        "c"
    ),
    (
        "¿Qué información proporciona el comando 'du -c'?",
        [
            'a) Muestra la fecha de última modificación de los archivos en el directorio de trabajo.',
            'd) Agrega un total al final, indicando la utilización de disco total.',
            'c) Calcula la utilización de disco solo para archivos en el directorio de trabajo.',
            'b) Habilita la visualización de la fecha de creación de los archivos.',
        ],
        "d"
    ),
    (
        "¿Cuál es el propósito de la opción '-d 1' en el comando 'du -d 1'?",
        [
            'a) Muestra la utilización de disco solo para archivos en el directorio de trabajo.',
            'b) Calcula la utilización de disco para el directorio actual con una profundidad de 1.',
            'c) Visualiza la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
            'd) Oculta la información de los archivos en el directorio de trabajo.',
        ],
        "b"
    ),
    (
        "¿Qué hace el comando 'du -s'?",
        [
            'a) Muestra la fecha de última modificación de los archivos en el directorio de trabajo.',
            'b) Calcula la utilización de disco solo para archivos ocultos.',
            'c) Visualiza la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
            'd) Muestra solo el total de la utilización de disco del directorio de trabajo.',
        ],
        "d"
    ),
    (
        "Si ejecutas 'du -h copias', ¿qué información obtendrás?",
        [
            'a) La fecha de última modificación de los archivos en el directorio de copias.',
            'b) La utilización de disco del directorio de copias y sus subdirectorios.',
            'c) La carga actual del sistema en términos de usuarios conectados.',
            'd) El tiempo actual del sistema.',
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito principal del comando 'df' en sistemas Unix y Linux?",
        [
            'a) Mostrar detalles sobre los directorios de usuario.',
            'b) Proporcionar información sobre la utilización del espacio en disco de los sistemas de archivos montados.',
            'c) Visualizar el historial de conexiones de usuarios al sistema.',
            'd) Mostrar el tiempo actual del sistema.',
        ],
        "b"
    ),
    (
        "¿Qué información proporciona el comando 'df -a'?",
        [
            'a) Muestra el tiempo actual del sistema.',
            'b) Proporciona detalles sobre los archivos ocultos en el sistema de archivos.',
            'c) Muestra información detallada sobre cada sistema de archivos montado.',
            'd) Visualiza la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito de la opción '-h' en el comando 'df -h'?",
        [
            'a) Oculta la información de los archivos en el sistema de archivos.',
            'b) Proporciona una salida humanamente legible con unidades como KB, MB, etc.',
            'c) Calcula la utilización de disco solo para archivos en el sistema de archivos.',
            'd) Muestra la fecha de última modificación de los archivos en el sistema de archivos.',
        ],
        "b"
    ),
    (
        "¿Qué hace el comando 'df -hk'?",
        [
            'a) Calcula la utilización de disco solo para archivos ocultos en el sistema de archivos.',
            'b) Muestra la utilización de disco en kilobytes.',
            'c) Proporciona información detallada sobre cada sistema de archivos montado en megabytes.',
            'd) Oculta la información de los archivos en el sistema de archivos.',
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito de la opción '--total' en el comando 'df --total'?",
        [
            'a) Oculta la información de los archivos en el sistema de archivos.',
            'b) Muestra el tiempo actual del sistema.',
            'c) Agrega el total al final, indicando la utilización de disco total.',
            'd) Visualiza la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
        ],
        "c"
    ),
    (
        "¿Qué hace el comando 'df -T *.txt'?",
        [
            'a) Muestra la fecha de última modificación de los archivos de texto en el sistema de archivos.',
            'b) Calcula la utilización de disco solo para archivos de texto en el sistema de archivos.',
            'c) Muestra el tipo de sistema de archivos junto con la información de uso del disco para archivos de texto.',
            'd) Visualiza la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito de la opción '-t' en el comando 'df -t'?",
        [
            'a) Muestra el tiempo actual del sistema.',
            'b) Calcula la utilización de disco solo para archivos temporales.',
            'c) Agrega el tipo de sistema de archivos a la información de uso del disco.',
            'd) Visualiza la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
        ],
        "c"
    ),    
    (
        "¿De qué fichero saca la información el comando uname?",
        [
            'a) /var/log/btmp.',
            'b) /proc/meminfo.',
            'c) /proc/cpuinfo.',
            'd) /proc/version.',
        ],
        "d"
    ),
    (
        "¿Qué fichero proporciona información detallada sobre las características y capacidades del procesador o procesadores instalados en el sistema?",
        [
            'a) /var/log/btmp.',
            'b) /proc/meminfo.',
            'c) /proc/cpuinfo.',
            'd) /proc/version.',
        ],
        "c"
    ),
        (
        "¿Qué fichero muestra información detallada sobre el uso de la memoria del sistema?",
        [
            'a) /var/log/btmp.',
            'b) /proc/meminfo.',
            'c) /proc/cpuinfo.',
            'd) /proc/version.',
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito principal del comando 'lsb_release' en sistemas Linux?",
        [
            'a) Mostrar el tiempo actual del sistema.',
            'b) Proporcionar información detallada sobre la versión del kernel.',
            'c) Obtener información sobre la identificación de la distribución Linux.',
            'd) Visualizar la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito principal del comando 'lsusb' en sistemas Unix y Linux?",
        [
            'a) Mostrar una lista de usuarios conectados al sistema a través de USB.',
            'b) Proporcionar información detallada sobre el uso de puertos USB.',
            'c) Visualizar la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
            'd) Obtener información sobre los dispositivos USB conectados al sistema.',
        ],
        "d"
    ),
    (
        "¿Cuál es el propósito principal del comando 'lshw' en sistemas Unix y Linux?",
        [
            'a) Mostrar información sobre el tiempo actual del sistema.',
            'b) Proporcionar detalles sobre la versión del sistema operativo.',
            'c) Visualizar la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
            'd) Obtener información detallada sobre el hardware del sistema, incluyendo placa base, memoria, etc.',
        ],
        "d"
    ),
        (
        "¿Cuál es la diferencia principal entre 'lshw' y 'lshw -short' en sistemas Unix y Linux?",
        [
            'a) lshw -short muestra la información del hardware de forma más detallada.',
            'b) lshw -short proporciona una versión más reducida de la información del hardware.',
            'c) lshw -short y lshw son comandos equivalentes, sin diferencia en la salida.',
            'd) lshw -short se utiliza para mostrar la información del software en lugar del hardware.',
        ],
        "b"
    ),
        (
        "¿Cuál es el propósito principal del comando 'sudo lshw -c video' en sistemas Unix y Linux?",
        [
            'a) Mostrar información sobre la conexión de red actual.',
            'b) Proporcionar detalles sobre la versión del sistema operativo.',
            'c) Obtener información específica del hardware de video.',
            'd) Visualizar la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
        ],
        "c"
    ),
    (
        "¿Qué información proporciona el comando 'sudo lshw -c network'?",
        [
            'a) Detalles sobre la versión del sistema operativo.',
            'b) Información específica del hardware de red.',
            'c) Visualización de la carga actual del sistema.',
            'd) Mostrar el tiempo actual del sistema.',
        ],
        "b"
    ),
        (
        "¿Cuál es el propósito principal del comando 'free' en sistemas Unix y Linux?",
        [
            'a) Mostrar la cantidad total de espacio en disco disponible.',
            'b) Proporcionar detalles sobre la versión del sistema operativo.',
            'c) Visualizar la carga actual del sistema en términos de usuarios conectados y procesos en ejecución.',
            'd) Mostrar información sobre el uso de la memoria del sistema, incluyendo RAM y espacio de intercambio.',
        ],
        "d"
    ),
    (
        "¿Cuál es el comando que se utiliza para visualizar los mensajes del kernel en Linux?",
        [
            "a) sudo dmesg",
            "b) sudo mess -k",
            "c) sudo kmesg",
            "d) sudo kermesg",
        ],
        "a"
    ),
    (
        "¿Cuál es el propósito del comando `sudo fdisk -l`?",
        [
            "a) Muestra información detallada sobre las particiones del disco.",
            "b) Lista todos los archivos en el sistema de archivos actual.",
            "c) Formatea una partición del disco.",
            "d) Monta una unidad de almacenamiento externa.",
        ],
        "a"
    ),
    (
        "Si deseas ver solo las particiones relacionadas con `sda`, ¿cuál sería el comando adecuado?",
        [
            "a) sudo fdisk",
            "b) sudo fdisk -l",
            "c) sudo fdisk | grep -i sda",
            "d) sudo fdisk -l | grep -i sda",
        ],
        "d"
    ),
            (
        "¿En qué fichero se encuentran los repositorios de Linux?",
        [
            'a) /etc/apt/sources.list',
            'b) /etc/snap/rep.list',
            'c) /etc/apt/sources.rep',
            'd) /etc/apt-get/list.rep.',
        ],
        "a"
    ),
        (
        "¿Cuál es el propósito del comando `sudo apt-get update`?",
        [
            "a) Instala un nuevo paquete en el sistema.",
            "b) Actualiza los índices de los repositorios para obtener información sobre paquetes disponibles.",
            "c) Actualiza todos los paquetes instalados en el sistema.",
            "d) Elimina un paquete del sistema.",
        ],
        "b"
    ),
    (
        "Si prefieres utilizar el comando más moderno para actualizar los índices, ¿cuál sería la alternativa correcta?",
        [
            "a) sudo apt-get update",
            "b) sudo apt update",
            "c) sudo apt upgrade",
            "d) cat /etc/apt/sources.list",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando `sudo apt upgrade`?",
        [
            "a) Instala un nuevo paquete en el sistema.",
            "b) Actualiza los índices de los repositorios.",
            "c) Actualiza todos los paquetes instalados en el sistema.",
            "d) Elimina un paquete del sistema.",
        ],
        "c"
    ),
    (
        "Si deseas ver el contenido del fichero que contiene los repositorios, ¿cuál sería el comando adecuado?",
        [
            "a) sudo apt-get update",
            "b) sudo apt update",
            "c) sudo apt install tree",
            "d) cat /etc/apt/sources.list",
        ],
        "d"
    ),
    (
        "¿Cómo se instala el paquete `tree` en el sistema?",
        [
            "a) sudo apt-get tree",
            "b) sudo apt tree",
            "c) sudo apt-get install tree",
            "d) sudo install tree",
        ],
        "c"
    ),
    (
        "Si deseas realizar una actualización que salte a la siguiente versión de Ubuntu, ¿cuál sería el comando correcto?",
        [
            "a) sudo apt update",
            "b) sudo apt upgrade",
            "c) sudo apt-get dist-upgrade",
            "d) sudo apt-get upgrade",
        ],
        "c"
    ),
        (
        "¿Cómo se describen los demonios en el contexto de sistemas operativos?",
        [
            "a) Programas que se ejecutan en primer plano.",
            "b) Programas que se ejecutan en segundo plano.",
            "c) Programas que solo se ejecutan durante el arranque.",
            "d) Programas que requieren interacción constante del usuario.",
        ],
        "b"
    ),
    (
        "¿Cuál es la característica principal de los demonios en un sistema operativo?",
        [
            "a) Requieren intervención del usuario para ejecutarse.",
            "b) Se ejecutan solo durante el arranque del sistema.",
            "d) Se ejecutan en segundo plano de forma continua.",
            "c) Son programas catalogados de virus que pueden poner en peligro el sistema actuando desde un segundo plano.",
        ],
        "d"
    ),
    (
        "¿Cómo se identifican tradicionalmente los demonios en cuanto a su nombre?",
        [
            "a) Terminan con la letra s.",
            "b) Terminan con la letra d.",
            "c) Comienzan con la letra daemon.",
            "d) No siguen ninguna convención de nomenclatura específica.",
        ],
        "b"
    ),
    (
        "¿Cuál es un ejemplo de demonio que implementa el registro de eventos del sistema?",
        [
            "a) syslog",
            "b) sshd",
            "c) httpd",
            "d) crond",
        ],
        "a"
    ),
    (
        "¿Cuál es un ejemplo de demonio que sirve a las conexiones ssh entrantes?",
        [
            "a) ssh",
            "b) sshd",
            "c) dssh",
            "d) crond",
        ],
        "b"
    ),
        (
        "¿Cuál es la función principal de systemd en un sistema operativo Linux?",
        [
            "a) Administrar el sistema de archivos.",
            "b) Gestionar y arrancar los servicios del sistema.",
            "c) Controlar la interfaz gráfica del usuario.",
            "d) Mantener la seguridad del kernel.",
        ],
        "b"
    ),
    (
        "¿En qué punto del arranque del sistema inicia la ejecución de systemd?",
        [
            "a) Al principio del proceso de arranque.",
            "b) En el medio del proceso de arranque.",
            "c) Al final del proceso de arranque.",
            "d) Durante la carga del kernel.",
        ],
        "c"
    ),
    (
        "¿Cuál es el PID (identificador de proceso) que siempre tiene systemd?",
        [
            "a) PID=0",
            "b) PID=1",
            "c) PID=init",
            "d) PID=systemd",
        ],
        "b"
    ),
     (
        "¿Qué representa el nivel de ejecución 0 en un sistema basado en systemd?",
        [
            "a) Modo de rescate",
            "b) Apagar el sistema",
            "c) Modo de usuario múltiple",
            "d) Reiniciar el sistema",
        ],
        "b"
    ),
    (
        "¿Cuál es el nivel de ejecución asociado con el modo de rescate en systemd?",
        [
            "a) Nivel de ejecución 0",
            "b) Nivel de ejecución 1",
            "c) Nivel de ejecución 3",
            "d) Nivel de ejecución 5",
        ],
        "b"
    ),
    (
        "En systemd, ¿qué nivel de ejecución representa el modo de usuario múltiple?",
        [
            "a) Nivel de ejecución 0",
            "b) Nivel de ejecución 1",
            "c) Nivel de ejecución 3",
            "d) Nivel de ejecución 5",
        ],
        "c"
    ),
    (
        "¿Cuál es el nivel de ejecución en systemd asociado con el entorno gráfico?",
        [
            "a) Nivel de ejecución 0",
            "b) Nivel de ejecución 1",
            "c) Nivel de ejecución 3",
            "d) Nivel de ejecución 5",
        ],
        "d"
    ),
    (
        "¿Qué representa el nivel de ejecución 6 en un sistema basado en systemd?",
        [
            "a) Modo de rescate",
            "b) Apagar el sistema",
            "c) Modo de usuario múltiple",
            "d) Reiniciar el sistema",
        ],
        "d"
    ),
    (
        "¿Cuál es el objetivo (target) asociado con el apagado del sistema en systemd?",
        [
            "a) poweroff.target",
            "b) rescue.target",
            "c) multi-user.target",
            "d) reboot.target",
        ],
        "a"
    ),
    (
        "¿Cuál es el propósito del comando `runlevel` en un sistema Linux?",
        [
            "a) Mostrar el nivel de ejecución actual.",
            "b) Cambiar el nivel de ejecución del sistema.",
            "c) Listar todos los niveles de ejecución disponibles.",
            "d) Ejecutar un script en un nivel de ejecución específico.",
        ],
        "a"
    ),
    (
        "¿Cuál es el propósito del comando `systemctl get-default` en un sistema Linux con systemd?",
        [
            "a) Cambiar el nivel de ejecución predeterminado del sistema.",
            "b) Mostrar la configuración actual del gestor de servicios.",
            "c) Listar todos los servicios instalados en el sistema.",
            "d) Establecer la configuración predeterminada para un servicio específico.",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando `sudo systemctl set-default multi-user.target` en un sistema Linux con systemd?",
        [
            "a) Cambiar el nivel de ejecución actual a `multi-user.target`.",
            "b) Establecer `multi-user.target` como el nivel de ejecución predeterminado.",
            "c) Listar los niveles de ejecución disponibles.",
            "d) Reiniciar el sistema en `multi-user.target`.",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando `shutdown -h now` en un sistema Linux?",
        [
            "a) Reiniciar el sistema inmediatamente.",
            "b) Apagar el sistema inmediatamente.",
            "c) Programar un reinicio para el próximo día.",
            "d) Cerrar la sesión del usuario actual.",
        ],
        "b"
    ),
    (
        "¿Qué hace el comando `shutdown -h 22:15`?",
        [
            "a) Programa un reinicio para las 22:15.",
            "b) Apaga el sistema a las 22:15.",
            "c) Muestra un mensaje pero no realiza ninguna acción.",
            "d) Cierra sesión en el sistema.",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando `shutdown -r now`?",
        [
            "a) Apagar el sistema inmediatamente.",
            "b) Programar un reinicio para el próximo día.",
            "c) Reiniciar el sistema inmediatamente.",
            "d) Cerrar la sesión del usuario actual.",
        ],
        "c"
    ),
    (
        "¿Qué hace el comando `shutdown -r +5`?",
        [
            "a) Programa un reinicio para los próximos 5 minutos.",
            "b) Reinicia el sistema después de 5 minutos.",
            "c) Apaga el sistema después de 5 minutos.",
            "d) Muestra un mensaje pero no realiza ninguna acción.",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando `shutdown -c`?",
        [
            "a) Cierra la sesión del usuario actual.",
            "b) Cancela un apagado o reinicio programado.",
            "c) Muestra el tiempo de actividad del sistema.",
            "d) Apaga el sistema inmediatamente.",
        ],
        "b"
    ),
    (
        "¿Cuál de los siguientes comandos reinicia el sistema sin esperas?",
        [
            "a) reboot",
            "b) halt",
            "c) poweroff",
            "d) logout",
        ],
        "a"
    ),
    (
        "¿Cuál de los siguientes comandos cierra el software sin esperas?",
        [
            "a) reboot",
            "b) halt",
            "c) poweroff",
            "d) logout",
        ],
        "b"
    ),
    (
        "¿Cuál de los siguientes comandos apaga el equipo sin esperas?",
        [
            "a) reboot",
            "b) halt",
            "c) poweroff",
            "d) logout",
        ],
        "c"
    ),
    (
        "¿Cuál es el equivalente de `logout` en términos de cerrar sesión?",
        [
            "a) reboot",
            "b) halt",
            "c) poweroff",
            "d) exit",
        ],
        "d"
    ),
    (
        "¿Cuál de los siguientes comandos lista los últimos reinicios del sistema?",
        [
            "a) last",
            "b) last reboot",
            "c) last -5 reboot",
            "d) last <usuario>",
        ],
        "b"
    ),
    (
        "¿Qué hace el comando `last -5 reboot`?",
        [
            "a) Lista los últimos 5 reinicios del sistema.",
            "b) Lista los 5 usuarios que más reiniciaron el sistema.",
            "c) Lista los últimos 5 reinicios del sistema en un formato más detallado.",
            "d) No es un comando válido.",
        ],
        "a"
    ),
    (
        "¿Cuál es el propósito del comando `uptime`?",
        [
            "a) Muestra el tiempo de actividad del sistema.",
            "b) Programa un apagado para el próximo día.",
            "c) Muestra la fecha y hora en formato aaaa/mm/dd HH/MM/SS.",
            "d) Muestra los intentos fallidos de login.",
        ],
        "a"
    ),
    (
        "¿Cuál es el propósito del comando `gzip` en un sistema Linux?",
        [
            "a) Descomprimir archivos y directorios.",
            "b) Listar información sobre archivos comprimidos.",
            "c) Comprimir uno o más archivos/directorios en uno solo.",
            "d) Crear un archivo ZIP.",
        ],
        "c"
    ),
    (
        "¿Cómo se comprime un archivo/directorio utilizando `gzip`?",
        [
            "a) gzip -f [opciones] fich_zip fichero/directorio",
            "b) gzip -c [opciones] fich_zip fichero/directorio",
            "c) gzip -r [opciones] fich_zip fichero/directorio",
            "d) gzip -l [opciones] fich_zip fichero/directorio",
        ],
        "b"
    ),
    (
        "¿Qué hace la opción `-c` en el comando `gzip`?",
        [
            "a) Lista información sobre archivos comprimidos.",
            "b) Comprime los archivos en un solo fichero ZIP.",
            "c) Envía a la salida estándar.",
            "d) Recursivo.",
        ],
        "c"
    ),
    (
        "¿Qué hace la opción `-f` en el comando `gzip`?",
        [
            "a) Lista información sobre archivos comprimidos.",
            "b) Crea un archivo ZIP forzando la compresión.",
            "c) Fuerza la compresión aunque los archivos ya existan.",
            "d) Recursivo.",
        ],
        "c"
    ),
    (
        "¿Qué hace la opción `-l` en el comando `gzip`?",
        [
            "a) Fuerza la compresión aunque los archivos ya existan.",
            "b) Lista información sobre archivos comprimidos.",
            "c) Envía a la salida estándar.",
            "d) Recursivo.",
        ],
        "b"
    ),
    (
        "¿Qué hace la opción `-r` en el comando `gzip`?",
        [
            "a) Lista información sobre archivos comprimidos.",
            "b) Crea un archivo ZIP forzando la compresión.",
            "c) Fuerza la compresión aunque los archivos ya existan.",
            "d) Realiza la compresión de forma recursiva.",
        ],
        "d"
    ),
    (
        "¿Qué hace la opción `-9` en el comando `gzip`?",
        [
            "a) Lista información sobre archivos comprimidos.",
            "b) Crea un archivo ZIP forzando la compresión.",
            "c) Fuerza la compresión aunque los archivos ya existan.",
            "d) Establece el mayor factor de compresión.",
        ],
        "d"
    ),
    (
        "¿Cuál es el propósito del comando `gunzip` en un sistema Linux?",
        [
            "a) Comprimir archivos y directorios.",
            "b) Descomprimir archivos y directorios.",
            "c) Listar información sobre archivos comprimidos.",
            "d) Crear un archivo ZIP.",
        ],
        "b"
    ),
        (
        "¿Cuál es el propósito del comando `gzip -d` en un sistema Linux?",
        [
            "a) Comprimir archivos y directorios.",
            "b) Descomprimir archivos y directorios.",
            "c) Listar información sobre archivos comprimidos.",
            "d) Crear un archivo ZIP.",
        ],
        "b"
    ),
    (
        "¿Cuál es la equivalencia del comando `gzip -d` en comparación con otro comando?",
        [
            "a) gzip -c",
            "b) gunzip",
            "c) gzip -l",
            "d) gzip -r",
        ],
        "b"
    ),
    (
        "¿Qué hace el comando `gunzip` en un sistema Linux?",
        [
            "a) Comprimir archivos y directorios.",
            "b) Descomprimir archivos y directorios.",
            "c) Listar información sobre archivos comprimidos.",
            "d) Crear un archivo ZIP.",
        ],
        "b"
    ),
    (
        "¿Cómo reemplaza `gunzip` los archivos comprimidos?",
        [
            "a) Cambia el nombre del archivo comprimido.",
            "b) Crea un nuevo directorio para los archivos descomprimidos.",
            "c) Los reemplaza con archivos que tienen el mismo nombre pero con .gz añadido.",
            "d) Los guarda en un archivo ZIP.",
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito principal del comando `tar` en un sistema Linux?",
        [
            "a) Comprimir archivos y directorios.",
            "b) Descomprimir archivos y directorios.",
            "c) Empaquetar y unir varios archivos en uno solo.",
            "d) Listar información sobre archivos comprimidos.",
        ],
        "c"
    ),
    (
        "¿Qué hace la opción `-c` en el comando `tar`?",
        [
            "a) Descomprime los archivos.",
            "b) Crea el fichero tar.",
            "c) Visualiza el contenido del fichero tar.",
            "d) Extrae archivos del fichero tar.",
        ],
        "b"
    ),
    (
        "¿Qué hace la opción `-f fichero` en el comando `tar`?",
        [
            "a) Descomprime los archivos.",
            "b) Crea el fichero tar.",
            "c) Visualiza el contenido del fichero tar.",
            "d) Extrae archivos del fichero tar.",
        ],
        "b"
    ),
    (
        "¿Qué hace la opción `-v` en el comando `tar`?",
        [
            "a) Descomprime los archivos.",
            "b) Crea el fichero tar.",
            "c) Visualiza el contenido del fichero tar.",
            "d) Extrae archivos del fichero tar.",
        ],
        "c"
    ),
    (
        "¿Qué hace la opción `-x` en el comando `tar`?",
        [
            "a) Descomprime los archivos.",
            "b) Crea el fichero tar.",
            "c) Visualiza el contenido del fichero tar.",
            "d) Extrae archivos del fichero tar.",
        ],
        "d"
    ),
    (
        "¿Qué hace la opción `-t` en el comando `tar`?",
        [
            "a) Descomprime los archivos.",
            "b) Crea el fichero tar.",
            "c) Visualiza el contenido del fichero tar.",
            "d) Extrae archivos del fichero tar.",
        ],
        "c"
    ),
    (
        "¿Qué hace la opción `-z` en el comando `tar`?",
        [
            "a) Comprime los archivos al vuelo.",
            "b) Descomprime los archivos al vuelo.",
            "c) Lista información sobre archivos comprimidos.",
            "d) Extrae archivos comprimidos.",
        ],
        "a"
    ),
        (
        "¿Cuál es la función principal del comando `tar` en Linux?",
        [
            "a) Comprimir archivos.",
            "b) Descomprimir archivos.",
            "c) Agrupar varios ficheros en un solo archivo.",
            "d) Listar información sobre archivos comprimidos.",
        ],
        "c"
    ),
    (
        "¿Cuál es la función principal del comando `gzip` en Linux?",
        [
            "a) Comprimir archivos.",
            "b) Descomprimir archivos.",
            "c) Agrupar varios ficheros en un solo archivo.",
            "d) Listar información sobre archivos comprimidos.",
        ],
        "a"
    ),
    (
        "¿Qué propósito cumplen conjuntamente los comandos `tar` y `gzip` en Linux?",
        [
            "a) Descomprimir archivos.",
            "b) Comprimir archivos.",
            "c) Agrupar varios ficheros en uno solo y comprimirlo.",
            "d) Listar información sobre archivos comprimidos.",
        ],
        "c"
    ),
    (
        "¿Cuál es la función del comando `tar -cvf dire.tar ~/dire`?",
        [
            "a) Descomprimir el archivo dire.tar en el directorio ~/dire.",
            "b) Crear un nuevo directorio llamado dire.tar y mover los archivos al directorio ~/dire.",
            "c) Empaquetar todos los archivos del directorio dire.tar en el fichero ~/dire.",
            "d) Empaquetar todos los archivos del directorio ~/dire en el fichero dire.tar.",
        ],
        "d"
    ),
    (
        "¿Qué hace la opción `-c` en el comando `tar`?",
        [
            "a) Descomprime archivos.",
            "b) Lista información sobre archivos.",
            "c) Crea un nuevo fichero.",
            "d) Extrae archivos de un fichero.",
        ],
        "c"
    ),
    (
        "¿Qué hace la opción `-v` en el comando `tar`?",
        [
            "a) Descomprime archivos.",
            "b) Lista información sobre archivos.",
            "c) Visualiza los nombres de los archivos que se empaquetan.",
            "d) Extrae archivos de un fichero.",
        ],
        "c"
    ),
    (
        "¿Qué hace la opción `-f` en el comando `tar`?",
        [
            "a) Descomprime archivos.",
            "b) Lista información sobre archivos.",
            "c) Crea un nuevo fichero.",
            "d) Extrae archivos de un fichero.",
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito del argumento `dire.tar` en el comando `tar -cvf dire.tar ~/dire`?",
        [
            "a) Indicar el directorio a empaquetar.",
            "b) Crear un nuevo directorio llamado dire.tar.",
            "c) Especificar el nombre del fichero a crear.",
            "d) Visualizar el contenido del fichero dire.tar.",
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito del argumento `~/dire` en el comando `tar -cvf dire.tar ~/dire`?",
        [
            "a) Descomprimir el directorio ~/dire.",
            "b) Crear un nuevo directorio llamado dire.tar.",
            "c) Indicar el directorio a empaquetar.",
            "d) Visualizar el contenido del fichero dire.tar.",
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito del comando `tar -xvf dire.tar`?",
        [
            "a) Comprimir el directorio actual en un fichero tar.",
            "b) Extraer ficheros del fichero tar `dire.tar` en el directorio actual.",
            "c) Crear un nuevo directorio llamado dire.tar.",
            "d) Listar información sobre el contenido del fichero tar.",
        ],
        "b"
    ),
    (
        "¿Qué hace la opción `-x` en el comando `tar`?",
        [
            "a) Descomprime archivos.",
            "b) Lista información sobre archivos.",
            "c) Extrae archivos del fichero tar.",
            "d) Crea un nuevo fichero tar.",
        ],
        "c"
    ),
    (
        "¿Qué hace la opción `-v` en el comando `tar` al extraer archivos?",
        [
            "a) Descomprime archivos.",
            "b) Lista información sobre archivos.",
            "c) Visualiza los nombres de los archivos que se extraen.",
            "d) Crea un nuevo fichero tar.",
        ],
        "c"
    ),
    (
        "¿Qué riesgo se menciona al utilizar el comando `tar -xvf dire.tar`?",
        [
            "a) Pérdida de espacio en disco.",
            "b) Extracción lenta de archivos.",
            "d) Sobrescribir los archivos de destino en el directorio actual.",
            "c) No hay riesgo, la operación es segura.",
        ],
        "d"
    ),
    (
        "¿Cuál es la precaución que se debe tener al extraer archivos con `tar -xvf dire.tar`?",
        [
            "a) No se necesita precaución, la operación es segura.",
            "b) Verificar que los archivos de destino no existan previamente.",
            "c) No utilizar la opción `-v` para evitar visualizar los archivos extraídos.",
            "d) Utilizar la opción `-c` para extraer archivos de manera segura.",
        ],
        "b"
    ),
        (
        "¿Cuál es el propósito del comando `tar -tvf dire.tar`?",
        [
            "c) Comprimir el directorio actual en un fichero tar.",
            "b) Extraer ficheros del fichero tar `dire.tar` en el directorio actual.",
            "a) Listar el contenido del fichero tar `dire.tar`.",
            "d) Listar información sobre archivos comprimidos.",
        ],
        "a"
    ),
    (
        "¿Qué hace la opción `-t` en el comando `tar` al listar el contenido?",
        [
            "a) Descomprime archivos.",
            "b) Lista información sobre archivos.",
            "d) Lista el contenido del fichero tar.",
            "c) Extrae archivos del fichero tar.",
        ],
        "d"
    ),
    (
        "¿Qué hace la opción `-v` en el comando `tar` al listar el contenido?",
        [
            "a) Descomprime archivos.",
            "b) Lista información sobre archivos.",
            "c) Visualiza los nombres de los archivos que se listan.",
            "d) Extrae archivos del fichero tar.",
        ],
        "c"
    ),
    (
        "¿Qué información se puede obtener al utilizar `tar -tvf dire.tar`?",
        [
            "a) Información sobre archivos comprimidos.",
            "c) La ruta del directorio actual.",
            "b) El contenido del fichero tar, incluyendo nombres de archivos y directorios.",
            "d) Información sobre el proceso de descompresión.",
        ],
        "b"
    ),
    (
        "¿Por qué podría ser útil listar el contenido de un fichero tar antes de extraerlo?",
        [
            "c) Para descomprimir archivos más rápido.",
            "b) Para verificar la integridad del fichero tar.",
            "a) Para visualizar nombres de archivos y directorios antes de la extracción.",
            "d) No es útil, la operación de descompresión es segura.",
        ],
        "a"
    ),
    (
        "¿Cuál es el resultado en tamaño de un fichero .tar que contiene dos ficheros de 1MB cada uno?",
        [
            "a) 1 MB.",
            "b) 2 MB.",
            "c) < 1MB.",
            "d) > 1MB.",
        ],
        "b"
    ),
    (
        "¿Qué hace el comando `gzip`?",
        [
            "a) Lista información sobre archivos comprimidos.",
            "b) Descomprime archivos comprimidos.",
            "c) Comprime un fichero.",
            "d) Crea un fichero tar.",
        ],
        "c"
    ),
    (
        "¿Qué se puede lograr al utilizar `gzip` después de `tar` en un fichero?",
        [
            "a) Aumentar el tamaño del fichero.",
            "b) Descomprimir el fichero.",
            "c) Comprimir el fichero.",
            "d) Convertir el fichero en un archivo tar.",
        ],
        "c"
    ),
        (
        "¿Qué hace el comando `gzip -9 dire.tar`?",
        [
            "c) Descomprime el fichero `dire.tar`.",
            "b) Lista información sobre el fichero `dire.tar`.",
            "a) Comprime el fichero `dire.tar` utilizando el mayor factor de compresión.",
            "d) Crea un fichero tar llamado `dire.tar.gz`.",
        ],
        "a"
    ),
    (
        "¿Cuál es el propósito de la opción `-9` en el comando `gzip -9 dire.tar`?",
        [
            "c) Descomprimir el fichero `dire.tar`.",
            "b) Crear un fichero tar llamado `dire.tar.gz`.",
            "a) Comprimir el fichero `dire.tar` utilizando el mayor factor de compresión.",
            "d) Lista información sobre el fichero `dire.tar`.",
        ],
        "a"
    ),
    (
        "¿Cuál sería el resultado del comando `gzip -9 dire.tar`?",
        [
            "a) `dire.tar` se descomprime.",
            "b) `dire.tar` se renombra a `dire.tar.gz`.",
            "c) Se crea un nuevo fichero llamado `dire.tar.gz` con la máxima compresión.",
            "d) `dire.tar` se elimina.",
        ],
        "c"
    ),
    (
        "¿Qué comando es equivalente a `gunzip fichero.gz`?",
        [
            "a) `gzip fichero.gz`.",
            "b) `gzip -d fichero.gz`.",
            "c) `gzip -u fichero.gz`.",
            "d) `gunzip -d fichero.gz`.",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando `gunzip`?",
        [
            "a) Comprimir un fichero con gzip.",
            "b) Descomprimir un fichero comprimido con gzip.",
            "c) Crear un fichero tar.",
            "d) Listar información sobre archivos comprimidos.",
        ],
        "b"
    ),
        (
        "En el ejemplo 1, ¿cuál es el propósito del comando `tar -cvf backup.tar /tmp`?",
        [
            "a) Comprimir el directorio `/tmp`.",
            "b) Crear un nuevo directorio llamado `backup.tar`.",
            "c) Empaquetar los archivos del directorio `/tmp` en un fichero llamado `backup.tar`.",
            "d) Descomprimir el fichero `backup.tar`.",
        ],
        "c"
    ),
    (
        "En el ejemplo 1, ¿qué hace el comando `gzip -9 backup.tar`?",
        [
            "a) Descomprime el fichero `backup.tar`.",
            "b) Lista información sobre el fichero `backup.tar`.",
            "c) Comprime el fichero `backup.tar` utilizando el mayor factor de compresión.",
            "d) Crea un nuevo fichero llamado `backup.tar.gz`.",
        ],
        "c"
    ),
    (
        "En el ejemplo 2, ¿cuál es el propósito del comando `tar -cvzf backup.tar.gz /tmp`?",
        [
            "a) Crear un nuevo fichero tar llamado `backup.tar.gz`.",
            "b) Comprimir el directorio `/tmp` utilizando gzip.",
            "c) Descomprimir el fichero `backup.tar.gz`.",
            "d) Empaquetar y comprimir al vuelo los archivos del directorio `/tmp`.",
        ],
        "d"
    ),
    (
        "En el ejemplo 2, ¿por qué se utiliza la opción `-z` en el comando `tar -cvzf backup.tar.gz /tmp`?",
        [
            "a) Para listar el contenido del fichero tar.",
            "b) Para descomprimir el fichero tar.",
            "c) Para crear un nuevo directorio llamado `backup.tar.gz`.",
            "d) Para comprimir al vuelo utilizando gzip.",
        ],
        "d"
    ),
        (
        "En el ejemplo 1, ¿cuál es el propósito del comando `gunzip backup.tar.gz`?",
        [
            "a) Comprimir el fichero `backup.tar.gz`.",
            "b) Descomprimir el fichero `backup.tar.gz`.",
            "c) Crear un nuevo fichero llamado `backup.tar.gz`.",
            "d) Empaquetar los archivos del directorio `backup.tar.gz`.",
        ],
        "b"
    ),
    (
        "En el ejemplo 1, ¿qué hace el comando `tar -xvf backup.tar`?",
        [
            "a) Comprimir el fichero `backup.tar`.",
            "b) Extraer ficheros del fichero `backup.tar`.",
            "c) Crear un nuevo fichero llamado `backup.tar`.",
            "d) Empaquetar los archivos del directorio `backup.tar`.",
        ],
        "b"
    ),
    (
        "En el ejemplo 2, ¿cuál es el propósito del comando `tar -xvzf backup.tar.gz`?",
        [
            "a) Comprimir el directorio `backup.tar.gz`.",
            "b) Descomprimir el fichero `backup.tar.gz`.",
            "c) Extraer y descomprimir al vuelo los archivos del fichero `backup.tar.gz`.",
            "d) Crear un nuevo fichero llamado `backup.tar.gz`.",
        ],
        "c"
    ),
    (
        "¿Por qué se utiliza la opción `-z` en el comando `tar -xvzf backup.tar.gz`?",
        [
            "a) Para listar el contenido del fichero tar.",
            "b) Para descomprimir el fichero tar.",
            "c) Para crear un nuevo directorio llamado `backup.tar.gz`.",
            "d) Para comprimir al vuelo.",
        ],
        "d"
    ),
        (
        "¿Cuál de las siguientes extensiones de fichero es equivalente a un fichero comprimido con gzip?",
        [
            "a) .tgz",
            "b) .taz",
            "c) .tar.gz",
            "d) .tar.Z",
        ],
        "c"
    ),
    (
        "¿Qué representa la extensión .taz?",
        [
            "a) Fichero comprimido con gzip.",
            "b) Fichero comprimido con otro compresor diferente a gzip.",
            "c) Es equivalente a .tar.Z.",
            "d) No representa un fichero comprimido.",
        ],
        "c"
    ),
    (
        "¿Cómo se especifica la extensión para trabajar con bzip2 en lugar de gzip con `tar`?",
        [
            "a) Reemplazando z por j, por ejemplo, .tar.gz -> .tar.j",
            "b) Reemplazando j por z, por ejemplo, .tar.j -> .tar.gz",
            "c) Utilizando la misma extensión, .tar.gz.",
            "d) No es posible trabajar con bzip2 usando `tar`.",
        ],
        "a"
    ),
    (
        "¿Cuál de las siguientes NO es una extensión válida para ficheros comprimidos con `tar`?",
        [
            "a) .tar.gz",
            "b) .tar.bz2",
            "c) .tar.lha",
            "d) .zip",
        ],
        "c"
    ),
    (
        "¿Cuál es el reemplazo correcto para utilizar bzip2 en lugar de gzip en la extensión .tar.gz?",
        [
            "a) .tar.bz2",
            "b) .tar.lha",
            "c) .tar.zip",
            "d) .tar.j",
        ],
        "a"
    ),
(
        "¿Cómo se denomina el tipo de copia de seguridad que salva toda la información, incluyendo todos los archivos y datos en el sistema?",
        [
            "a) Copia de seguridad total o íntegra.",
            "b) Copia de seguridad incremental.",
            "c) Copia de seguridad diferencial.",
            "d) Copia de seguridad parcial.",
        ],
        "a"
    ),
    (
        "¿Cuál es el principal rasgo distintivo de la copia de seguridad incremental?",
        [
            "a) Salva todos los archivos y datos en el sistema.",
            "b) Solo salva los archivos modificados desde la última copia de seguridad.",
            "c) Solo salva los archivos nuevos desde la última copia de seguridad.",
            "d) Salva una fracción aleatoria de archivos cada vez.",
        ],
        "b"
    ),
    (
        "¿En qué se diferencia la copia de seguridad diferencial de la copia de seguridad total?",
        [
            "a) Salva todos los archivos y datos en el sistema.",
            "b) Solo salva los archivos modificados desde la última copia de seguridad.",
            "c) Solo salva los archivos nuevos desde la última copia de seguridad.",
            "d) Salva todos los archivos modificados desde la última copia total, sin importar si fueron nuevos o existentes.",
        ],
        "d"
    ),
    (
        "¿Cuál es la principal desventaja de la copia de seguridad total o íntegra en comparación con la incremental y diferencial?",
        [
            "a) Requiere menos tiempo y recursos.",
            "b) Ocupa menos espacio de almacenamiento.",
            "c) Solo guarda los archivos nuevos.",
            "d) Puede consumir más tiempo y espacio al salvar todo, incluso si hay pocos cambios desde la última copia.",
        ],
        "d"
    ),
    (
        "¿Cómo se describe una copia de seguridad normal?",
        [
            "a) Es una copia de seguridad de solo algunos archivos específicos.",
            "b) Es una copia de seguridad total de todos los archivos y directorios seleccionados.",
            "c) Es una copia de seguridad incremental que solo guarda cambios desde la última copia.",
            "d) Es una copia de seguridad diferencial que solo salva los archivos nuevos.",
        ],
        "b"
    ),
    (
        "En un proceso de copia de seguridad incremental, ¿qué archivos se copian?",
        [
            "a) Todos los archivos, independientemente de si han cambiado o no.",
            "b) Solo los archivos nuevos desde la última copia de seguridad.",
            "d) Solo los archivos que se han modificado desde la última copia de seguridad.",
            "c) Una fracción aleatoria de archivos cada vez.",
        ],
        "d"
    ),
    (
        "Si se necesita restaurar archivos después de un desastre, ¿qué copias son necesarias?",
        [
            "a) Solo la copia total.",
            "b) Solo la última copia incremental.",
            "c) La copia total y todas las copias incrementales desde la copia total.",
            "d) Solo la última copia realizada, ya sea total o incremental.",
        ],
        "c"
    ),
      (
        "¿Qué archivos se copian en una copia de seguridad diferencial?",
        [
            "a) Solo los archivos nuevos desde la última copia de seguridad.",
            "b) Todos los archivos, independientemente de si han cambiado o no.",
            "c) Solo los archivos que se han modificado desde la última copia total.",
            "d) Solo los archivos que se han modificado desde la última copia diferencial.",
        ],
        "c"
    ),

    (
        "¿Qué copias son necesarias para la restauración después de un desastre en el caso de copia diferencial?",
        [
            "a) Solo la última copia diferencial.",
            "b) La copia total y todas las copias diferenciales desde la última copia total.",
            "c) La última copia total y la última copia diferencial.",
            "d) Solo la última copia realizada, ya sea total o diferencial.",
        ],
        "c"
    ),
        (
        "¿Cómo afecta la copia diferencial anterior a la nueva copia diferencial en el proceso de anulación?",
        [
            "a) La nueva copia diferencial anula a la anterior.",
            "b) Ambas copias diferenciales coexisten sin afectarse mutuamente.",
            "c) La copia diferencial anterior anula a la nueva.",
            "d) No hay anulación entre copias diferenciales.",
        ],
        "a"
    ),
        (
        "En comparación con la copia incremental, ¿qué característica describe el proceso de copia diferencial?",
        [
            "a) Se realiza más rápidamente.",
            "b) Consume menos espacio de almacenamiento.",
            "c) Consume más tiempo y espacio.",
            "d) No hay ninguna diferencia en la práctica.",
        ],
        "c"
    ),
        (
        "Según la recomendación dada, ¿qué tipo de copia es más práctico cuando el volumen de datos es menor de 4 GB?",
        [
            "a) Copia de seguridad incremental.",
            "b) Copia de seguridad diferencial.",
            "c) Copia de seguridad total.",
            "d) Copia de seguridad parcial.",
        ],
        "c"
    ),
        (
        "Según la recomendación dada, ¿qué tipo de copia es más práctico cuando el volumen de datos es muy elevado (mayor de 50 GB) y el volumen de datos modificados no es elevado (sobre 4 GB)?",
        [
            "a) Copia de seguridad incremental.",
            "b) Copia de seguridad diferencial.",
            "c) Copia de seguridad total.",
            "d) Copia de seguridad parcial.",
        ],
        "b"
    ),
    (
        "Según la recomendación dada, ¿qué tipo de copia es más práctico cuando el volumen de datos es muy elevado (mayor de 50 GB) y el volumen de datos modificados también lo es?",
        [
            "a) Copia de seguridad total.",
            "b) Copia de seguridad diferencial.",
            "c) Copia de seguridad incremental.",
            "d) Copia de seguridad parcial.",
        ],
        "c"
    ),
    (
        "¿Cuál es el razonamiento principal para realizar una primera copia total seguida de copias incrementales cuando el volumen de datos es muy elevado (mayor de 50 GB) y el volumen de datos modificados también lo es?",
        [
            "a) Mayor velocidad en la recuperación después de un desastre.",
            "b) Menor consumo de espacio de almacenamiento.",
            "c) Menor tiempo de ejecución del proceso de copia.",
            "d) Mayor flexibilidad en la selección de archivos.",
        ],
        "b"
    ),
        (
        "¿Por qué se sugiere hacer copias totales más a menudo cuando se utilizan copias incrementales?",
        [
            "a) Para reducir el tiempo de ejecución del proceso de copia.",
            "b) Para ahorrar espacio de almacenamiento.",
            "c) Para facilitar la recuperación después de un desastre.",
            "d) Para evitar mantener un número muy elevado de copias incrementales.",
        ],
        "d"
    ),
    (
        "En el caso de utilizar copias incrementales, ¿cuándo conviene hacer copias totales más frecuentes?",
        [
            "a) Cuando el volumen de datos es bajo.",
            "b) Cuando el volumen de datos es muy elevado.",
            "c) Cuando el tiempo de ejecución del proceso de copia es crítico.",
            "d) Cuando se desea ahorrar espacio de almacenamiento.",
        ],
        "d"
    ),
        (
        "En grandes compañías con una planificación cuidadosa de copias de seguridad, ¿qué tipo de sistemas de copia de seguridad se suelen utilizar?",
        [
            "a) Exclusivamente copias de seguridad totales.",
            "b) Mayormente copias de seguridad incrementales.",
            "c) Sistemas mixtos que combinan copias totales, incrementales y diferenciales.",
            "d) Solo copias de seguridad diferencial.",
        ],
        "c"
    ),
        (
        "En caso de desastre, ¿qué copias de seguridad serían necesarias para la recuperación?",
        [
            "a) La copia total, la última incremental y todas las diferenciales desde la última incremental.",
            "b) La copia total, la última diferencial y todas las incrementales desde la última diferencial.",
            "c) Todas las copias: totales, incrementales y diferenciales.",
            "d) La copia total, la última diferencial y todas las incrementales desde la última incremental.",
        ],
        "b"
    ),
        (
        "¿Por qué se menciona la limitación de reutilizar las cintas no más de 20 veces?",
        [
            "a) Para forzar la compra de nuevas cintas con regularidad.",
            "b) Porque las cintas se deterioran y la fiabilidad disminuye con el uso prolongado.",
            "c) Para mantener un registro preciso del número de usos de cada cinta.",
            "d) Por razones de compatibilidad con el hardware de cinta.",
        ],
        "b"
    ),
        (
        "En un sistema informático que da servicio a usuarios, ¿cuáles son algunas de las carpetas que se deben salvaguardar en el proceso de copias de seguridad?",
        [
            "a) /bin y /usr",
            "b) /var y /tmp",
            "c) /home, /etc, /root y /var/log",
            "d) /lib y /opt",
        ],
        "c"
    ),
    (
        "¿Por qué se destaca la importancia de la carpeta /home en el contexto de copias de seguridad?",
        [
            "a) Contiene archivos de sistema esenciales.",
            "b) Almacena configuraciones críticas para el sistema.",
            "c) Es la ubicación de los programas ejecutables.",
            "d) Contiene información de usuarios, siendo una de las más importantes a salvaguardar.",
        ],
        "d"
    ),
    (
        "¿Cuáles son algunas de las razones mencionadas para comprimir los datos durante las copias de seguridad?",
        [
            "a) Para aumentar el tiempo de realización de la copia.",
            "b) Para aumentar el tamaño de la copia.",
            "c) Para reducir el tiempo de realización de la copia y el tamaño de la copia.",
            "d) Para reducir el tiempo de realización de la copia y el tamaño de la copia, así como garantizar la integridad de los datos.",
        ],
        "d"
    ),
    (
        "¿Por qué la compresión puede hacer que la copia se realice más rápidamente?",
        [
            "a) Porque aumenta el tamaño de la copia.",
            "b) Porque reduce el tamaño de la copia y, por lo tanto, el tiempo de transmisión.",
            "c) Porque elimina la necesidad de transmitir los datos.",
            "d) Porque no tiene impacto en la velocidad de realización de la copia.",
        ],
        "b"
    ),
    (
        "¿Cómo contribuye la compresión a garantizar la integridad de los datos durante una copia de seguridad?",
        [
            "a) Eliminando redundancias en los datos mediante un sistema mixto de recuperación de redundancias (RRMS) durante la copia de seguridad.",
            "b) Aumentando el riesgo de pérdida de datos.",
            "c) Añadiendo información adicional a los datos (AI) durante la compresión de la copia de seguridad.",
            "d) Utilizando un código de redundancia cíclica (CRC) durante la compresión.",
        ],
        "d"
    ),
     (
        "¿Cuál es uno de los elementos comúnmente incluidos en el nombre de un archivo de copia de seguridad?",
        [
            "a) El número de versiones anteriores del archivo.",
            "b) La fecha de creación del archivo.",
            "c) El tamaño total de los datos comprimidos.",
            "d) El número de archivos incluidos en la copia.",
        ],
        "b"
    ),
    (
        "¿Por qué es común incluir la fecha en el nombre de un archivo de copia de seguridad?",
        [
            "a) Para indicar el número de archivos incluidos en la copia.",
            "b) Para reducir el tamaño del archivo.",
            "c) Para identificar la versión del software utilizado.",
            "d) Para proporcionar información sobre cuándo se creó la copia.",
        ],
        "d"
    ),
    (
        "¿Qué tipo de información suele incluirse en el nombre de un archivo de copia de seguridad manual?",
        [
            "a) Solo el tipo de copia.",
            "b) Solo el tamaño total de los datos comprimidos.",
            "c) El tipo de copia, las carpetas que contiene y la fecha.",
            "d) Únicamente el número de versiones anteriores del archivo.",
        ],
        "c"
    ),
        (
        "¿Cuál es el comando comúnmente utilizado para crear manualmente una copia de seguridad de una carpeta o carpetas?",
        [
            "a) cp",
            "b) mv",
            "c) tar",
            "d) gzip",
        ],
        "c"
    ),
    (
        "¿Qué permite hacer el comando 'tar' al crear una copia de seguridad?",
        [
            "a) Comprimir datos en diferentes formatos.",
            "b) Mover archivos a una nueva ubicación.",
            "c) Copiar archivos sin comprimir.",
            "d) Crear múltiples archivos independientes.",
        ],
        "a"
    ),
     (
        "¿Cuál es la extensión comúnmente asociada a los archivos tar comprimidos en bzip2?",
        [
            "a) .tar.gz",
            "b) .tar.xz",
            "c) .tar.bz2",
            "d) .tar.lzma",
        ],
        "c"
    ),
        (
        "¿Cuál es el propósito del comando 'tar -jcvf' en la siguiente instrucción: "
        "'tar -jcvf Total_carp1-2-3_23_01_10.tar.bz2 carpeta1 carpeta2 carpeta3'?",
        [
            "a) Mover carpetas a una ubicación específica.",
            "b) Crear una copia de seguridad de varias carpetas.",
            "c) Descomprimir un archivo tar.bz2 existente.",
            "d) Listar el contenido de un archivo tar.bz2.",
        ],
        "b"
    ),
    (
        "En la instrucción "'tar -jcvf Total_carp1-2-3_23_01_10.tar.bz2 carpeta1 carpeta2 carpeta3'", ¿qué representa 'Total_carp1-2-3_23_01_10.tar.bz2'?",
        [
            "a) Una carpeta de destino.",
            "b) El nombre de la copia de seguridad comprimida.",
            "c) Una carpeta a ser copiada.",
            "d) Un archivo descomprimido.",
        ],
        "b"
    ),
    (
        "¿Qué significa la opción '-j' en 'tar -jcvf'?",
        [
            "a) Mostrar detalles del proceso de copia.",
            "b) Establecer un nivel de compresión alto.",
            "c) Utilizar la compresión bzip2.",
            "d) Crear un archivo tar sin comprimir.",
        ],
        "c"
    ),
     (
        "¿Cuál es el propósito del comando 'tar -jxvf' en la siguiente instrucción: "
        "'tar -jxvf Total_carp1-2-3_23_01_10.tar.bz2'?",
        [
            "a) Comprimir archivos en formato tar.bz2.",
            "b) Mover archivos a una ubicación específica.",
            "c) Extraer archivos de un archivo tar.bz2.",
            "d) Listar el contenido del archivo tar.bz2.",
        ],
        "c"
    ),
    (
        "En la instrucción proporcionada, ¿qué representa 'Total_carp1-2-3_23_01_10.tar.bz2'?",
        [
            "a) Una carpeta de destino.",
            "b) El nombre del archivo comprimido.",
            "c) Una carpeta a ser extraída.",
            "d) Un archivo descomprimido.",
        ],
        "b"
    ),
    (
        "¿Qué significa la opción '-j' en 'tar -jxvf'?",
        [
            "a) Mostrar detalles del proceso de extracción.",
            "b) Establecer un nivel de compresión alto.",
            "c) Utilizar la descompresión bzip2.",
            "d) Crear un archivo tar sin comprimir.",
        ],
        "c"
    ),
 (
        "¿Por qué se utiliza la opción 'v' en 'tar -jxvf'?",
        [
            "a) Visualizar los archivos antes de extraerlos.",
            "b) Validar la integridad de los archivos extraídos.",
            "c) Verificar la versión de bzip2 utilizada.",
            "d) Mostrar los archivos mientras se extraen.",
        ],
        "d"
    ),
    (
        "En 'tar -jxvf', ¿qué representa la opción 'f'?",
        [
            "a) Filtrar archivos durante la extracción.",
            "b) Fijar el nivel de compresión.",
            "c) Formatear el sistema de archivos.",
            "d) Extraer desde un archivo especificado.",
        ],
        "d"
    ),
    (
        "¿Cuál es el propósito del comando 'tar -tf' en la siguiente instrucción: "
        "'tar -tf Total_carp1-2-3_23_01_10.tar.bz2'?",
        [
            "a) Comprimir archivos en formato tar.bz2.",
            "b) Mover archivos a una ubicación específica.",
            "c) Extraer archivos de un archivo tar.bz2.",
            "d) Listar el contenido del archivo tar.bz2.",
        ],
        "d"
    ),
        (
        "¿Qué significa la opción '-t' en 'tar -tf'?",
        [
            "a) Mostrar detalles del proceso de extracción.",
            "b) Establecer un nivel de compresión alto.",
            "c) Utilizar la compresión bzip2.",
            "d) Listar el contenido del archivo.",
        ],
        "d"
    ),
    (
        "¿Por qué se utiliza la opción 'f' en 'tar -tf'?",
        [
            "a) Filtrar archivos durante la lista de contenido.",
            "b) Fijar el nivel de compresión.",
            "c) Formatear el sistema de archivos.",
            "d) Especificar el nombre del archivo a listar.",
        ],
        "d"
    ),
        (
        "¿Cuál es la función principal del comando 'tar -jcvf' en la instrucción proporcionada: "
        "'tar -jcvf Diferencial_carpeta_23_01_10.tar.bz2 /ruta/carpeta -N 01.05.2023'?",
        [
            "a) Programar una copia de seguridad de archivos para una fecha dada.",
            "b) Crear una copia de seguridad de archivos nuevos después de una fecha dada.",
            "c) Programar una extracción de archivos correspondientes a unacopia de seguridad para una fecha dada.",
            "d) Crear una copia de seguridad de archivos modificados después de una fecha dada.",
        ],
        "d"
    ),
    (
        "¿Qué representa 'Diferencial_carpeta_23_01_10.tar.bz2' en la instrucción proporcionada: "
        "'tar -jcvf Diferencial_carpeta_23_01_10.tar.bz2 /ruta/carpeta -N 01.05.2023'?",
        [
            "a) Un archivo de destino.",
            "b) El nombre del archivo comprimido.",
            "c) Una carpeta de destino.",
            "d) Una carpeta a ser extraída.",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito de la opción '-N' en 'tar -jcvf'?",
        [
            "a) Establecer un nivel de compresión alto.",
            "b) Contar el número de archivos comprimidos.",
            "c) Filtrar archivos según una fecha dada.",
            "d) Indicar la ruta de la carpeta de origen.",
        ],
        "c"
    ),
    (
        "¿Cuál es la función principal del comando 'tar -jcvf' en la instrucción proporcionada: "
        "'tar -jcvf Diferencial_carpeta_23_01_10.tar.bz2 /ruta/carpeta -N 01.05.2023'?",
        [
            "a) Comprimir archivos utilizando bzip2.",
            "b) Crear una copia de seguridad completa.",
            "c) Extraer archivos de una carpeta específica.",
            "d) Crear una copia de seguridad de archivos más nuevos que una fecha dada.",
        ],
        "a"
    ),
    (
        "¿Qué representa 'Diferencial_carpeta_23_01_10.tar.bz2' en la instrucción proporcionada: "
        "'tar -jcvf Diferencial_carpeta_23_01_10.tar.bz2 /ruta/carpeta -N 01.05.2023'?",
        [
            "a) Un archivo de destino.",
            "b) El nombre del archivo comprimido.",
            "c) Una carpeta de destino.",
            "d) Una carpeta a ser extraída.",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito de la opción '-N' en 'tar -jcvf'?",
        [
            "a) Establecer un nivel de compresión alto.",
            "b) Listar el contenido de un archivo.",
            "c) Filtrar archivos según una fecha más nueva que la indicada.",
            "d) Indicar la ruta de la carpeta de origen.",
        ],
        "c"
    ),
    (
        "En la instrucción proporcionada, ¿qué representa '01.05.2023'?",
        [
            "a) El nombre de un archivo.",
            "b) La fecha límite para la copia de seguridad.",
            "c) La carpeta de destino.",
            "d) El nivel de compresión a utilizar.",
        ],
        "b"
    ),
    (
        "¿Qué función cumple el comando 'date' en la instrucción 'tar -jcvf /tmp/Total_etc-home_`date +%y_%m_%d_`.tar.bz2 /home /etc'?",
        [
            "a) Comprimir archivos utilizando bzip2.",
            "b) Mostrar la fecha actual en un formato específico.",
            "c) Crear una copia de seguridad completa.",
            "d) Extraer archivos de una carpeta específica.",
        ],
        "b"
    ),
    (
        " tar -jcvf /tmp/Total_etc-home_`date +%y_%m_%d_`.tar.bz2 /home /etc \n Si hoy fuera 10 de diciembre de 2023, ¿Cuál sería el nombre del archivo generado por la instrucción proporcionada?",
        [
            "a) Total_etc-home_23_12_01.tar.bz2",
            "b) Total_etc-home_23_12_10.tar.bz2",
            "c) Total_etc-home_23_01_10.tar.bz2",
            "d) Total_etc-home_23_12_01-10.tar.bz2",
        ],
        "c"
    ),
    (
        "¿Qué ocurre cuando se utiliza el acento grave francés (`) alrededor del comando 'date' en la instrucción 'tar -jcvf /tmp/Total_etc-home_`date +%y_%m_%d_`.tar.bz2 /home /etc'?",
        [
            "a) El comando 'date' se ejecuta en segundo plano.",
            "b) La salida del comando 'date' se sustituye en el nombre del archivo.",
            "c) El comando 'date' se ignora.",
            "d) La instrucción genera un error.",
        ],
        "b"
    ),
    (
        "Si queremos realizar una copia de seguridad diferencial desde el 1 de diciembre de 2023 en la carpeta /tmp de las carpetas /home y /etc, ¿cuál sería el nombre del archivo generado por la instrucción proporcionada?",
        [
            "a) Diferencial_etc-home_23_12_01-10.tar.bz2",
            "b) Diferencial_etc-home_23_12_01.tar.bz2",
            "c) Diferencial_etc-home_23_01_10.tar.bz2",
            "d) Diferencial_etc-home_23_12_10.tar.bz2",
        ],
        "a"
    ),
        (
        "¿Cuál es el comando para mostrar el tamaño de los directorios y archivos en un formato legible para humanos?",
        [
            "a) du",
            "b) du -h",
            "c) du -ah",
            "d) du -ah -time",
        ],
        "b"
    ),
    (
        "Si deseas incluir la ocupación en kilobytes y mostrar subdirectorios, ¿cuál es el comando correcto?",
        [
            "a) du -h",
            "b) du -ah",
            "c) du -ah -time",
            "d) du -ch",
        ],
        "c"
    ),
    (
        "¿Cómo añadirías la fecha y hora de la última modificación a la salida del comando `du -ah`?",
        [
            "a) du -ah -time",
            "b) du -ah - -time",
            "c) du -ah --time",
            "d) du -ah -datetime",
        ],
        "b"
    ),
    (
        "¿Cuál es el comando para mostrar el tamaño total al final de la salida?",
        [
            "a) du -total",
            "b) du -sum",
            "c) du -ch",
            "d) du --total",
        ],
        "c"
    ),
    (
        "Si solo deseas mostrar el total de ocupación de un directorio, ¿cuál es el comando correcto?",
        [
            "a) du -s",
            "b) du -ch",
            "c) du -total",
            "d) du --summary",
        ],
        "a"
    ),
    (
        "¿Cuál es el propósito del comando `du -d 1`?",
        [
            "a) Muestra el tamaño de los archivos en un directorio.",
            "b) Muestra el tamaño de los subdirectorios hasta una profundidad de 1 nivel.",
            "c) Muestra la ocupación total de un directorio y sus subdirectorios.",
            "d) Muestra la fecha y hora de la última modificación de los archivos.",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando `df` en Linux?",
        [
            "a) Mostrar la fecha actual.",
            "b) Mostrar información sobre el espacio ocupado y libre del sistema de ficheros montado.",
            "c) Desfragmentar el disco.",
            "d) Copiar archivos y directorios.",
        ],
        "b"
    ),
    (
        "Si deseas obtener información completa sobre el espacio ocupado y libre del sistema de archivos montado, ¿cuál es el comando correcto?",
        [
            "a) df -h",
            "b) df -a",
            "c) df -k",
            "d) df -m",
        ],
        "b"
    ),
    (
        "¿Cuál es la función del comando `df -h`?",
        [
            "a) Mostrar información completa.",
            "b) Mostrar la información en kilobytes.",
            "c) Mostrar la información en megabytes.",
            "d) Mostrar la información en un formato legible para humanos.",
        ],
        "d"
    ),
    (
        "Si deseas obtener la información en kilobytes, ¿cuál es el comando correcto?",
        [
            "a) df -k",
            "b) df -m",
            "c) df -h",
            "d) df -a",
        ],
        "a"
    ),
        (
        "Si deseas obtener la información en megaobytes, ¿cuál es el comando correcto?",
        [
            "a) df -k",
            "b) df -m",
            "c) df -h",
            "d) df -a",
        ],
        "b"
    ),
    (
        "¿Cómo mostrarías el total de cada columna con el comando `df`?",
        [
            "a) df total",
            "b) df -sum",
            "c) df -total",
            "d) df --total",
        ],
        "d"
    ),
    (
        "Si deseas obtener información sobre el tipo de sistema de archivos (fs), ¿cuál es el comando correcto?",
        [
            "a) df -T",
            "b) df --filesystem",
            "c) df -fs",
            "d) df --type",
        ],
        "a"
    ),
        (
        "¿Cuál es el comando para mostrar la versión del kernel?",
        [
            "a) cat /proc/version",
            "b) cat /proc/cpuinfo",
            "c) lsb_release -idc",
            "d) lshw -k",
        ],
        "a"
    ),
    (
        "Para obtener información detallada sobre la CPU, ¿cuál es el comando correcto?",
        [
            "a) cat /proc/version",
            "b) cat /proc/cpuinfo",
            "c) lshw",
            "d) lshw -cpu",
        ],
        "b"
    ),
    (
        "¿Cómo obtienes información sobre la RAM?",
        [
            "a) cat /proc/meminfo",
            "b) lshw -c ram",
            "c) ram",
            "d) mem",
        ],
        "a"
    ),
    (
        "Para conocer la versión de Ubuntu y su descripción, ¿cuál es el comando correcto?",
        [
            "a) cat /proc/version",
            "b) lsb_release -idc",
            "c) lshw",
            "d) dmesg | less",
        ],
        "b"
    ),
    (
        "¿Qué comando proporciona información sobre los canales USB?",
        [
            "a) cat /proc/usbinfo",
            "b) lshw -c usb",
            "c) lsusb",
            "d) lshwusb",
        ],
        "c"
    ),
    (
        "Para mostrar los mensajes emitidos durante el arranque del sistema, ¿cuál es el comando correcto?",
        [
            "a) cat /var/log/sys.init",
            "b) messages",
            "c) init -m",
            "d) dmesg | less",
        ],
        "d"
    ),
    (
        "¿Cómo obtienes información resumida sobre el hardware?",
        [
            "a) cat /proc/version",
            "b) lshw -short",
            "c) lshw -c",
            "d) free -s",
        ],
        "b"
    ),
    (
        "Para obtener información sobre la pantalla, ¿cuál es el comando correcto?",
        [
            "a) lshw -c video",
            "b) cat /proc/screeninfo",
            "c) lsb_release -idc",
            "d) lshw -s",
        ],
        "a"
    ),
    (
        "¿Qué comando proporciona información sobre la interfaz de red?",
        [
            "a) lshw -net",
            "b) lshw -c network",
            "c) lshw -c nw",
            "d) netinfo",
        ],
        "b"
    ),
    (
        "Para obtener información sobre la arquitectura soportada, ¿cuál es el comando correcto?",
        [
            "a) arch",
            "b) lshw -arch",
            "c) lshw -a",
            "d) lshw -arq",
        ],
        "a"
    ),
    (
        "¿Cuál es el comando para mostrar la cantidad de RAM total, usada, libre, compartida, etc.?",
        [
            "a) raminfo",
            "b) lsmem",
            "c) free",
            "d) lshw -mem",
        ],
        "c"
    ),
    (
        "Si deseas obtener información sobre las particiones, tamaños, etc., ¿cuál es el comando correcto?",
        [
            "a) free -m",
            "b) fdisk -l",
            "c) lshw -part",
            "d) lshw -p",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito principal de la orden `apt` en Ubuntu?",
        [
            "a) Desfragmentar el disco.",
            "b) Trabajar con el Advanced Packaging Tool (APT).",
            "c) Gestionar la memoria RAM.",
            "d) Crear archivos de configuración para aplicaciones.",
        ],
        "b"
    ),
    (
        "¿Qué funciones puede realizar la orden `apt`?",
        [
            "a) Solo instalación de nuevos paquetes de software.",
            "b) Solo actualización de paquetes de software.",
            "c) Instalación, actualización de paquetes, actualización del índice de paquetes y actualización del sistema Ubuntu.",
            "d) Solo actualización de archivos de configuración.",
        ],
        "c"
    ),
    (
        "¿Cuál es una de las principales características de la orden `apt` mencionada en la introducción?",
        [
            "a) Generación automática de código fuente.",
            "b) Manejo automático de conflictos.",
            "c) Conversión de archivos de imagen.",
            "d) Compilación de programas en tiempo real.",
        ],
        "b"
    ),
    (
        "¿En qué situación se destaca la facilidad de uso de `apt` según la introducción?",
        [
            "a) Solo para usuarios avanzados.",
            "b) Solo para usuarios novatos.",
            "c) Solo para usuarios que acostumbran usar la interfaz gráfica.",
            "d) Solo para usuarios que acostumbran usar la terminal.",
        ],
        "d"
    ),
    (
        "¿Por qué se menciona que apt-get tiene numerosas ventajas frente a otras herramientas de gestión de paquetes?",
        [
            "a) Por su interfaz gráfica intuitiva.",
            "b) Por su capacidad de ejecutar múltiples instancias simultáneamente.",
            "c) Por su manejo automático de conflictos y actualización de archivos de configuración.",
            "d) Por su capacidad de compilar paquetes desde el código fuente.",
        ],
        "c"
    ),
    (
        "¿Cuál de los siguientes comandos se utiliza para instalar un paquete con `apt-get`?",
        [
            "a) sudo apt install <paquete>",
            "b) sudo apt-get install <paquete>",
            "c) sudo install apt <paquete>",
            "d) sudo get apt-install <paquete>",
        ],
        "b"
    ),
    (
        "¿Cuál es la forma correcta de instalar el paquete 'terminator' con `apt`?",
        [
            "a) sudo apt terminator",
            "b) sudo apt-get terminator",
            "c) sudo apt install terminator",
            "d) sudo get apt-install terminator",
        ],
        "c"
    ),
    (
        "Para desinstalar un paquete, ¿cuál es el comando correcto con `apt-get`?",
        [
            "a) sudo apt remove <paquete>",
            "b) sudo apt-get remove <paquete>",
            "c) sudo apt-get uninstall <paquete>",
            "d) sudo get apt-uninstall <paquete>",
        ],
        "b"
    ),
    (
        "¿Cómo se desinstalan paquetes en desuso con `apt-get`?",
        [
            "a) sudo apt-get clean",
            "b) sudo apt-get autoremove",
            "c) sudo apt-get purge",
            "d) sudo apt-get remove --unused",
        ],
        "b"
    ),
    (
        "Para desinstalar un paquete y sus archivos de configuración con `apt-get`, ¿cuál es el comando correcto?",
        [
            "a) sudo apt-get uninstall <paquete>",
            "b) sudo apt-get autoremove <paquete>",
            "c) sudo apt-get remove --purge <paquete>",
            "d) sudo get apt-uninstall --purge <paquete>",
        ],
        "c"
    ),
    (
        "¿Qué representa el índice de paquetes de APT?",
        [
            "a) Un archivo de configuración de APT.",
            "b) Una lista de paquetes instalados.",
            "c) Una base de datos de paquetes disponibles en los repositorios definidos.",
            "d) Un archivo de preferencias de APT.",
        ],
        "c"
    ),
    (
        "¿Dónde se encuentran definidos los repositorios en el sistema?",
        [
            "a) /etc/apt/repositories",
            "b) /etc/apt/sources.d",
            "c) /etc/apt/preferences",
            "d) /etc/sources.list",
        ],
        "d"
    ),
    (
        "¿Cuál es el comando correcto para actualizar el índice local de paquetes con apt-get?",
        [
            "a) sudo apt-get upgrade",
            "b) sudo apt update",
            "c) sudo apt-get update",
            "d) sudo apt update-index",
        ],
        "c"
    ),
    (
        "¿Por qué es importante ejecutar periódicamente `sudo apt-get update`?",
        [
            "a) Para instalar nuevos paquetes.",
            "b) Para desinstalar paquetes obsoletos.",
            "c) Para actualizar el sistema operativo.",
            "d) Para obtener los últimos cambios en los repositorios.",
        ],
        "d"
    ),
    (
        "¿Cuándo se debe ejecutar `sudo apt-get update` después de realizar cambios en el sistema?",
        [
            "a) Nunca es necesario.",
            "b) Solo cuando se instala un nuevo paquete.",
            "c) Solo cuando se desinstala un paquete.",
            "d) Después de hacer cambios en /etc/apt/sources.list o /etc/apt/preferences.",
        ],
        "d"
    ),
    (
        "¿Cuándo puede ser necesario actualizar paquetes instalados en un sistema?",
        [
            "a) Solo cuando se instalan nuevos paquetes.",
            "b) Solo cuando se desinstalan paquetes.",
            "c) Cuando hay versiones más actualizadas disponibles en el repositorio de paquetes.",
            "d) Nunca es necesario actualizar paquetes.",
        ],
        "c"
    ),
    (
        "Después de actualizar el índice de paquetes, ¿cuál es el comando correcto para actualizar los paquetes instalados en el sistema mediante apt?",
        [
            "a) sudo apt-get update",
            "b) sudo apt-get upgrade",
            "c) sudo apt upgrade",
            "d) sudo apt-get update && sudo apt-get upgrade",
        ],
        "b"
    ),
    (
        "¿Qué hace el comando `sudo apt-get upgrade`?",
        [
            "a) Instala nuevos paquetes.",
            "b) Desinstala paquetes obsoletos.",
            "c) Actualiza paquetes instalados a las versiones más recientes disponibles.",
            "d) Desinstala todos los paquetes.",
        ],
        "c"
    ),
    (
        "¿Por qué podría ser importante ejecutar periódicamente `sudo apt-get upgrade`?",
        [
            "a) Para instalar nuevos paquetes.",
            "b) Para desinstalar paquetes obsoletos.",
            "c) Para mantener los paquetes instalados actualizados, incluyendo actualizaciones de seguridad.",
            "d) Para cambiar la configuración del sistema.",
        ],
        "c"
    ),
    (
        "¿Qué sucede si no se ejecuta `sudo apt-get upgrade` periódicamente?",
        [
            "a) No pasa nada, no es necesario.",
            "b) Se desinstalan todos los paquetes.",
            "c) El sistema operativo deja de funcionar.",
            "d) Los paquetes instalados no recibirán actualizaciones, incluyendo actualizaciones de seguridad.",
        ],
        "d"
    ),
        (
        "¿En qué situación se utiliza la orden `dist-upgrade` en lugar de `upgrade`?",
        [
            "a) Cuando se quieren instalar paquetes nuevos.",
            "b) Cuando un paquete necesita instalar o desinstalar nuevas dependencias durante su actualización.",
            "c) Solo cuando se quiere actualizar completamente el sistema.",
            "d) No hay diferencia entre `upgrade` y `dist-upgrade`.",
        ],
        "b"
    ),
    (
        "¿Qué hace la orden `sudo apt-get dist-upgrade`?",
        [
            "a) Actualiza todos los paquetes instalados a las versiones más recientes disponibles.",
            "b) Instala nuevos paquetes distintos a los existentes.",
            "c) Actualiza completamente el sistema, pero sin cambiar de versión.",
            "d) Actualiza completamente el sistema, incluso cambiando de versión.",
        ],
        "d"
    ),
    (
        "Para actualizar completamente Ubuntu de una versión a otra, ¿qué pasos adicionales deben realizarse?",
        [
            "a) No es necesario realizar pasos adicionales.",
            "b) Reemplazar los repositorios de la versión anterior por los de la nueva y ejecutar `sudo apt-get update`.",
            "c) Desinstalar todos los paquetes y reinstalarlos.",
            "d) Ejecutar `sudo apt-get upgrade` y luego `sudo apt-get dist-upgrade`.",
        ],
        "b"
    ),
    (
        "Después de ejecutar `sudo apt-get dist-upgrade`, ¿qué se espera que suceda con el sistema?",
        [
            "a) El sistema operativo deja de funcionar hasta la nueva configuración manual de los ficheros correspondientes.",
            "b) Todos los paquetes son desinstalados y se actualiza a la versión incial.",
            "c) El sistema estará actualizado con la nueva versión de Ubuntu.",
            "d) Solo se actualizarán algunos paquetes seleccionados.",
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito de los pasos posteriores a la instalación mencionados en las notas de actualización?",
        [
            "a) Desinstalar paquetes innecesarios.",
            "b) Reiniciar el sistema.",
            "c) Configurar la interfaz gráfica.",
            "d) Realizar ajustes específicos requeridos para la versión a la que se está actualizando.",
        ],
        "d"
    ),
        (
        "¿Dónde se registran las acciones realizadas por la orden `apt-get`?",
        [
            "a) /var/log/apt.log",
            "b) /var/log/apt-get.log",
            "c) /var/log/dpkg.log",
            "d) /var/log/actions.log",
        ],
        "c"
    ),
    (
        "¿Qué tipo de acciones son registradas en el archivo `/var/log/dpkg.log`?",
        [
            "a) Solo acciones de instalación.",
            "b) Solo acciones de desinstalación.",
            "c) Todas las acciones realizadas por `apt-get`, incluyendo instalación y desinstalación de paquetes.",
            "d) Acciones relacionadas con el sistema de archivos.",
        ],
        "c"
    ),
        (
        "¿Cuál es el propósito del comando 'apt-cache search <palabra clave>'?",
        [
            "a) Buscar la <palabra clave> en las listas de paquetes almacenados en la memoria caché del ordenador.",
            "b) Buscar la <palabra clave> en las listas de paquetes en ejecución.",
            "c) Buscar la <palabra clave> en las listas de paquetes disponibles.",
            "d) Buscar la <palabra clave> en las listas de paquetes desinstalados.",
        ],
        "c"
    ),
    (
        "¿Qué información proporciona el comando 'apt-cache pkgnames'?",
        [
            "a) Lista de paquetes instalados.",
            "b) Lista de programas disponibles en los repositorios.",
            "c) Lista de paquetes eliminados del sistema.",
            "d) Lista de programas en ejecución.",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando 'apt-get autoclean'?",
        [
            "a) Limpiar archivos temporales del sistema.",
            "b) Eliminar archivos de configuración de programas.",
            "c) Eliminar archivos '*.deb*' de programas desinstalados para recuperar espacio en disco.",
            "d) Desinstalar programas automáticamente.",
        ],
        "c"
    ),
    (
        "¿Qué hace el comando 'dpkg -l <palabra clave>'?",
        [
            "a) Lista los programas instalados.",
            "b) Muestra información sobre la <palabra clave>.",
            "c) Lista las aplicaciones que contienen la <palabra clave>.",
            "d) Desinstala programas que contienen la <palabra clave>.",
        ],
        "c"
    ),
    (
        "¿Cuál es la función del comando 'dpkg -L <programa>'?",
        [
            "a) Desinstala el programa especificado.",
            "b) Lista los archivos que instala el programa especificado.",
            "c) Muestra información detallada sobre el programa especificado.",
            "d) Lista los programas disponibles para instalación.",
        ],
        "b"
    ),
    (
        "¿Qué logra el comando 'apt-get autoclean' y por qué puede ser útil ejecutarlo periódicamente?",
        [
            "a) Elimina archivos temporales del sistema para mejorar el rendimiento.",
            "b) Desinstala programas obsoletos.",
            "c) Recupera espacio en disco eliminando archivos '*.deb*' de programas desinstalados.",
            "d) Desinstala programas automáticamente para liberar espacio.",
        ],
        "c"
    ),
    (
        "¿Cómo se accede al manual de ayuda de 'apt-get'?",
        [
            "a) apt-get --help",
            "b) man apt-get",
            "c) apt-get help",
            "d) help apt-get",
        ],
        "c"
    ),
    (
        "¿Cuál es el nombre del componente de Ubuntu que contiene paquetes de software libre y es oficialmente soportado?",
        [
            "a) Main",
            "b) Restricted",
            "c) Universe",
            "d) Multiverse",
        ],
        "a"
    ),
    (
        "¿Qué tipo de paquetes se encuentra en el componente 'Restricted' de Ubuntu?",
        [
            "a) Software libre oficialmente soportado.",
            "b) Software no libre oficialmente soportado.",
            "c) Software libre no oficialmente soportado.",
            "d) Software no libre no oficialmente soportado.",
        ],
        "b"
    ),
    (
        "¿En qué componente de Ubuntu se encuentran los paquetes de software libre que no son oficialmente soportados?",
        [
            "a) Main",
            "b) Restricted",
            "c) Universe",
            "d) Multiverse",
        ],
        "c"
    ),
    (
        "¿Cuál es el propósito del componente 'Multiverse' en Ubuntu?",
        [
            "a) Contiene paquetes de software libre oficialmente soportados.",
            "b) Contiene paquetes de software no libre oficialmente soportados.",
            "c) Contiene paquetes de software libre no oficialmente soportados.",
            "d) Contiene paquetes de software no libre no oficialmente soportados.",
        ],
        "d"
    ),
    (
        "¿Cuál es la diferencia principal entre 'Main' y 'Universe' en términos de soporte oficial?",
        [
            "a) Ambos contienen software libre, pero 'Main' está oficialmente soportado, mientras que 'Universe' no lo está.",
            "b) Ambos contienen software no libre, pero 'Main' está oficialmente soportado, mientras que 'Universe' no lo está.",
            "c) Ambos contienen software libre, pero 'Universe' está oficialmente soportado, mientras que 'Main' no lo está.",
            "d) Ambos contienen software no libre, pero 'Universe' está oficialmente soportado, mientras que 'Main' no lo está.",
        ],
        "a"
    ),
        (
        "¿Cuál es el propósito del componente 'main' en Ubuntu?",
        [
            "a) Contiene paquetes comerciales.",
            "b) Contiene paquetes que cumplen los requisitos de la licencia de Ubuntu y tienen soporte garantizado.",
            "c) Contiene programas sin soporte y sin requisitos de licencia.",
            "d) Contiene paquetes restringidos sin acceso al código fuente.",
        ],
        "b"
    ),
    (
        "¿Qué tipo de paquetes se encuentra en el componente 'restricted'?",
        [
            "a) Paquetes sin soporte.",
            "b) Paquetes comerciales.",
            "c) Paquetes con ayuda técnica garantizada y mejoras de seguridad oportunas.",
            "d) Paquetes con acceso limitado al código fuente.",
        ],
        "d"
    ),
    (
        "¿Cuál es la principal diferencia entre 'main' y 'restricted' en términos de licencia de software?",
        [
            "a) Ambos contienen paquetes con licencia libre.",
            "b) 'Main' contiene paquetes con licencia libre, mientras que 'restricted' incluye paquetes sin licencia.",
            "c) 'Main' incluye paquetes comerciales, mientras que 'restricted' incluye paquetes con licencia libre.",
            "d) 'Main' y 'restricted' contienen paquetes con acceso limitado al código fuente.",
        ],
        "b"
    ),
    (
        "¿Cuál es la característica principal del componente 'universe'?",
        [
            "a) Contiene paquetes comerciales.",
            "b) Contiene programas con licencia restringida y soporte de Ubuntu.",
            "c) Contiene una amplia gama de programas sin soporte por parte del equipo de Ubuntu.",
            "d) Contiene paquetes sin acceso al código fuente y sin soporte.",
        ],
        "c"
    ),
    (
        "¿Qué se puede encontrar en el componente 'commercial'?",
        [
            "a) Paquetes sin soporte.",
            "b) Paquetes comerciales.",
            "c) Paquetes con licencia libre y soporte.",
            "d) Paquetes con acceso limitado al código fuente.",
        ],
        "b"
    ),
    (
        "¿Cuál es la razón principal por la que un paquete estaría en el componente 'multiverse'?",
        [
            "a) Cumple con los requisitos de Software Libre y tiene soporte.",
            "b) No cumple con los requisitos de Software Libre.",
            "c) Es un programa comercial.",
            "d) Es parte del núcleo del sistema operativo.",
        ],
        "b"
    ),
        (
        "¿Cuál es el propósito principal del comando 'at' en Linux?",
        [
            "a) Ejecutar comandos de forma interactiva.",
            "b) Ejecutar comandos programados de forma única.",
            "c) Gestionar permisos de usuarios en el sistema.",
            "d) Realizar tareas de administración del sistema.",
        ],
        "b"
    ),
    (
        "¿Dónde se encuentran los ficheros involucrados en el comando 'at'?",
        [
            "a) /etc/cron.d/",
            "b) /etc/at.deny y /etc/at.allow",
            "c) /var/spool/cron/atjobs/",
            "d) /usr/sbin/atd",
        ],
        "b"
    ),
    (
        "¿Cuál es la ubicación del demonio 'atd'?",
        [
            "a) /usr/sbin/atd",
            "b) /var/spool/cron/atspool/",
            "c) /etc/at.deny y /etc/at.allow",
            "d) /etc/cron.d/",
        ],
        "a"
    ),
    (
        "¿Cuál es la función del directorio '/var/spool/cron/atjobs/' en relación con el comando 'at'?",
        [
            "a) Contiene los archivos de configuración del demonio 'atd'.",
            "b) Almacena los comandos programados para ser ejecutados por 'atd'.",
            "c) Gestiona los permisos de usuarios en el sistema.",
            "d) Es la ubicación del demonio 'atd'.",
        ],
        "b"
    ),
    (
        "¿Qué papel juegan los ficheros '/etc/at.deny' y '/etc/at.allow' en relación con el comando 'at'?",
        [
            "a) Determinan qué usuarios pueden ejecutar el comando 'at'.",
            "b) Contienen configuraciones de permisos para el demonio 'atd'.",
            "c) Almacenan los comandos programados por 'at'.",
            "d) Son archivos de registro para el comando 'at'.",
        ],
        "a"
    ),
        (
        "¿Qué comando se utiliza para ejecutar un comando (o varios) una sola vez de forma programada con `at`?",
        [
            "a) atq",
            "b) atrm",
            "c) atd",
            "d) at",
        ],
        "d"
    ),
    (
        "¿Cuáles son los ficheros involucrados en el comando `at` para la configuración de permisos?",
        [
            "a) /etc/cron.deny y /etc/cron.allow",
            "b) /etc/at.deny y /etc/at.allow",
            "c) /etc/spool/cron/atjobs/ y /etc/spool/cron/atspool/",
            "d) /usr/sbin/atd",
        ],
        "b"
    ),
    (
        "¿Cuál es la ubicación del demonio `atd`?",
        [
            "a) /etc/spool/cron/atjobs/",
            "b) /etc/spool/cron/atspool/",
            "c) /usr/sbin/atd",
            "d) /usr/sbin/cron",
        ],
        "c"
    ),
    (
        "¿Cuál es la sintaxis básica para programar un trabajo con `at`?",
        [
            "a) at opc1 hora[fecha] [+incremento]",
            "b) at opc2 [trabajos]",
            "c) at –m hora[fecha] [+incremento]",
            "d) at opc2 [modificadores]",
        ],
        "a"
    ),
    (
        "¿Cuál de las siguientes opciones de `at` se utiliza para enviar un correo electrónico después de ejecutar el trabajo?",
        [
            "a) -l",
            "b) -m",
            "c) -c",
            "d) -r",
        ],
        "b"
    ),
    (
        "¿Cómo listar los trabajos programados con `at`?",
        [
            "a) at –r 'ID del trabajo a borrar'",
            "b) at -q",
            "c) at -l",
            "d) at -c nº_atq",
        ],
        "c"
    ),
    (
        "¿Cuál es el comando para eliminar un trabajo programado con `at`?",
        [
            "a) atrm",
            "b) atq",
            "c) at -l",
            "d) at –r 'ID del trabajo a borrar'",
        ],
        "d"
    ),
    (
        "¿Qué modificador se utiliza para especificar la medianoche en `at`?",
        [
            "a) noon",
            "b) midnight",
            "c) teatime",
            "d) now",
        ],
        "b"
    ),
    (
        "¿Cómo se especifica el tiempo en `at` para ejecutar un trabajo mañana?",
        [
            "a) tomorrow",
            "b) next",
            "c) +1",
            "d) + 1 day",
        ],
        "a"
    ),
    (
        "¿Cuál es la sintaxis para especificar el incremento de tiempo en `at`?",
        [
            "a) minute week next = +1",
            "b) hour month",
            "c) day year",
            "d) todas las anteriores",
        ],
        "d"
    ),
    (
        "¿Cuál es el comando para ver el contenido de un trabajo programado con `at`?",
        [
            "a) atq",
            "b) atrm",
            "c) at -c nº_atq",
            "d) at -l",
        ],
        "c"
    ),
    (
        "¿Cuáles son los modificadores disponibles para la hora en `at`?",
        [
            "a) mn noon tt n tmrrw",
            "b) -m -n -t -N -T ",
            "c) midnight noon teatime now tomorrow",
            "d) todos los anteriores",
        ],
        "c"
    ),
     (
        "¿Cuál es el comando para listar trabajos programados con `at`?",
        [
            "a) at -l",
            "b) atq",
            "c) at –r",
            "d) atrm",
        ],
        "c"
    ),
    (
        "¿Cuál de las siguientes opciones se utiliza para eliminar un trabajo programado con `at`?",
        [
            "a) atq",
            "b) atrm",
            "c) at –l",
            "d) at –r 'ID del trabajo a borrar'",
        ],
        "b"
    ),
    (
        "¿Qué opción se utiliza para enviar un correo electrónico después de ejecutar un trabajo con `at`?",
        [
            "a) -m",
            "b) -l",
            "c) -c",
            "d) -r",
        ],
        "a"
    ),
    (
        "Si deseas ver el contenido de un trabajo programado con `at`, ¿cuál es el comando correcto?",
        [
            "a) atq nº_atq",
            "b) atrm nº_atq",
            "c) at -l nº_atq",
            "d) at -c nº_atq",
        ],
        "d"
    ),
    (
        "¿Cómo se especifica la hora en el formato `hh:mm` en `at`?",
        [
            "a) at –t hh:mm",
            "b) at –h hh:mm",
            "c) at -m hh:mm",
            "d) at hh:mm",
        ],
        "d"
    ),
    (
        "¿Cómo programar un trabajo para ejecutarse a las 3:15 PM con `at`?",
        [
            "a) at 3:15pm",
            "b) at 3:15am",
            "c) at 15:15",
            "d) at 15:15pm",
        ],
        "a"
    ),
    (
        "Si deseas ejecutar un trabajo 2 días a partir de ahora, ¿cuál sería el comando correcto?",
        [
            "a) at now + 2 days",
            "b) at +2 days",
            "c) at now +2days",
            "d) a y c son correctas."
        ],
        "d"
    ),
    (
        "Para programar un trabajo a las 9:30 AM del 15 de junio de 2023, ¿cuál es la sintaxis adecuada?",
        [
            "a) at 9:30am 15.06.23",
            "b) at 9:30 tomorrow",
            "c) at 14:30 Mon",
            "d) at 4 am Saturday",
        ],
        "a"
    ),
    (
        "¿Cómo programar un trabajo para ejecutarse a las 20:30 horas de hoy?",
        [
            "a) at now + 7 hours",
            "b) at –m now +10 minutes",
            "c) at teatime tomorrow",
            "d) at 20:30 today",
        ],
        "d"
    ),
(
        "¿Cuál es el comando para editar las tablas del cron?",
        [
            "a) crontab -e",
            "b) crontab -l",
            "c) cronedit",
            "d) crontabedit",
        ],
        "a"
    ),
    (
        "¿Cuál de los siguientes ficheros está relacionado con las tareas programadas en cron?",
        [
            "a) /etc/cron.deny",
            "b) /etc/cron.allow",
            "c) /var/spool/cron/$USER",
            "d) Todos los anteriores",
        ],
        "d"
    ),
    (
        "Si deseas listar el contenido del fichero crontab sin editarlo, ¿cuál es el comando correcto?",
        [
            "a) crontab -l",
            "b) crontab -e",
            "c) cronlist",
            "d) crontablist",
        ],
        "a"
    ),
    (
        "¿Cuál es el propósito de los ficheros /etc/cron.deny y /etc/cron.allow?",
        [
            "a) Almacenar registros de ejecuciones de cron.",
            "b) Controlar el acceso a la ejecución de tareas programadas por usuarios.",
            "c) Almacenar las salidas de las tareas programadas.",
            "d) Configurar las tareas periódicas del sistema.",
        ],
        "b"
    ),
    (
        "¿Cuál es la función del directorio /var/spool/cron/$USER?",
        [
            "a) Almacenar las tareas programadas del sistema.",
            "b) Almacenar las salidas de las tareas programadas.",
            "c) Almacenar temporalmente las tareas programadas de un usuario específico.",
            "d) Configurar las tareas periódicas del sistema.",
        ],
        "c"
    ),
        (
        "¿Cuál es el comando para seleccionar el editor por defecto?",
        [
            "a) choose-editor",
            "b) set-default-editor",
            "c) select-editor",
            "d) editor-select",
        ],
        "c"
    ),
    (
        "¿Cómo se edita el propio fichero crontab con el comando `crontab`?",
        [
            "a) crontab -e",
            "b) crontab -l",
            "c) crontab -d",
            "d) crontab -a",
        ],
        "a"
    ),
    (
        "Para que el root edite el fichero crontab del usuario 'asir10', ¿cuál es el comando correcto?",
        [
            "a) crontab -e asir10",
            "b) crontab -e -u asir10",
            "c) crontab -l asir10",
            "d) crontab -l -u asir10",
        ],
        "b"
    ),
    (
        "¿Cuál es el propósito del comando `crontab -l`?",
        [
            "a) Listar el contenido del propio crontab.",
            "b) Editar el fichero crontab.",
            "c) Eliminar el crontab actual.",
            "d) Configurar el crontab para un usuario específico.",
        ],
        "a"
    ),
    (
        "Para listar el contenido del crontab del usuario 'asir10', ¿cuál es el comando correcto?",
        [
            "a) crontab -l",
            "b) crontab -e -u asir10",
            "c) crontab -l -u asir10",
            "d) crontab -e",
        ],
        "c"
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