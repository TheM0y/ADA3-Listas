# ADA3-Listas

##Libreríaas
-json: Esta librería permite agregar el código necesario para crear el archivo JSON donde la información se guardará, así como acceder a dicho archivo.

-time: Esta librería permite en este caso acceder a la función "sleep()" que permite realizar pausas entre las acciones del programa. En el programa se usa en el menú para que el cambio entre opciones no sea tan brusca.

##Métodos
-init: Es el método constructor. Carga los datos del archivo JSON al programa.

-cargar_datos: Verifica si existe el archivo JSON en la carpeta donde también se encuentra el archivo py del programa, de no ser así, crea el archivo. El archivo .json se guardará con el nombre de "postres.json".

-guardar_datos: Guarda los cambios que el usuario realice a la información de los postres dentro del archivo JSON, sobreescribiendo la información.

-mostrar_ingredientes: Le pregunta al usuario el postre que el programa debe mostrar sus ingredientes. Verifica si dicho postre existe, si existe mostrara una lista de los ingredientes, en el caso contraio se mostrará el mensaje "el postre no existe"
