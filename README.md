# Práctica contenedores Francesc Blanco

Esta práctica consiste de una aplicación web escrita en Python con Django y una base de datos Postgres. Esta aplicación permite crear y eliminar registros en una lista de To-dos (quehaceres).

# Requisitos

La aplicación se puede instalar de varias formas, según la que usemos deberemos tener diferentes requisitos:
- Instalación local
	- Docker con Docker-Compose
- Instalación en la nube en Cluster de kubernetes
	- Kubectl (instalación manual)
	- Helm

# Instalación en local con Docker Compose

Desde el directorio raíz del proyecto ejecutar el siguiente comando:

```mermaid
docker-compose up
```

Este proceso te creará 2 contenedores, uno web y otro de base de datos. Además generará un volumen myPostgres para garantizar la persistencia de datos.

Una vez desplegados los contenedores, se podrá comprobar que la aplicación está funcionando en http:\\localhost:8000 (puerto por defecto)

En el fichero .env podremos configurar algunas cosas:
-   WEB_PORT: puerto desde el que queremos atacar a la aplicación desde localhost
-   DB_HOST: nombre que queremos que tenga el host de postgres
-   DB_NAME: nombre que va a tener la base de datos
-   DB_USER: nombre del usuario de la base de datos que usará la aplicación
-   DB_PASS: password del usuario de la base de datos que usará la aplicación