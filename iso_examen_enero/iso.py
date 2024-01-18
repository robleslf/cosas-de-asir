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
            'b) echo -e "\nAquí va un salto de línea y \tojo que aquí va una tabulación."',
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
            'd) echo {1..10}-',
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
            'c) echo {{a..z},{A..<}}',
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
        "a"
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
            'c) echo {10..1..2}',
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
        "¿Cuál de los siguientes comandos se utiliza comúnmente para comparar tres archivos y mostrar solo las líneas comunes a los tres archivos?",
        [
            'a) comm -1',
            'b) comm -2',
            'c) comm -3',
            'd) comm -c',
        ],
        "c"
    ),
    (
        "En el contexto de la comparación de archivos, ¿cuándo es más comúnmente utilizado el comando 'comm -3'?",
        [
            'a) Cuando se quieren mostrar solo las líneas únicas del archivo 1.',
            'b) Cuando se quieren mostrar solo las líneas únicas del archivo 2.',
            'c) Cuando se quieren mostrar solo las líneas comunes a los tres archivos.',
            'd) Cuando se quieren mostrar las líneas comunes y únicas de todos los archivos.',
        ],
        "c"
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