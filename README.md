# ADA3-Listas

##Libreríaas
-json: Esta librería permite agregar el código necesario para crear el archivo JSON donde la información se guardará, así como acceder a dicho archivo.

-time: Esta librería permite en este caso acceder a la función "sleep" que permite realizar pausas entre las acciones del programa. En el programa se usa en el menú para que el cambio entre opciones no sea tan brusca.

##Métodos
-init: Es el método constructor. Carga los datos del archivo JSON al programa.

-cargar_datos: Verifica si existe el archivo JSON en la carpeta donde también se encuentra el archivo py del programa, de no ser así, crea el archivo. El archivo .json se guardará con el nombre de "postres.json".

-guardar_datos: Guarda los cambios que el usuario realice a la información de los postres dentro del archivo JSON, sobreescribiendo la información.

-mostrar_ingredientes: Le pide al usuario el postre que el programa debe mostrar sus ingredientes. Verifica si dicho postre existe, si existe mostrará una lista de los ingredientes, en el caso contraio se mostrará el mensaje "el postre no existe"

-alta_postre: Le permite al usuario agregar un postre; iniciando por el nombre del postre y después por sus ingredientes. Los ingredientes se pueden agregar de corrido, solo hay que separarlos por comas; los ingredientes duplicados se eliminan automaticamente hasta dejar uno. Si el postre ya existe se mostrará el mesaje "El postre ya existe".

-baja_postre: Le permite al usuario eliminar un postre por su nombre. Si el postre ya existe se mostrará el mesaje "El postre no existe".

-agregar_ingredientes: Le pide al usuario el nombre del postre a modificarle los ingredientes*, seguido de eso le pide el nuevo ingrediente a agregar. Si se intenta agregar un ingrediente existente el programa elimina el duplicado automaticamente.

-eliminar_ingrediente: Le pide al usuario el nombre del postre a modificarle los ingredientes, seguido de eso le pide el ingrediente a eliminar, si el ingrediente existe se elimina, si no existe se mostrará el mensaje "El ingrediente no existe en la lista". Si el postre no existe se mostra el mensaje "El postre no existe"

-menu: Despliega un menú con opciones que el usuario puede usar para interactuar con el programa.
