# Instalación con Helm

Se requiere disponer de un clúster Kubernetes.

Para esta parte instalaremos lo mismo que hemos hecho en el apartado con kubectl pero a través de Helm, dándole más configurabilidad y facilidad a la hora de hacer el despliegue.

Primero de todo tendremos que movernos a la carpeta charts del proyecto.

Una vez dentro, podremos configurar los diferentes recursos, para que funcione todo como deseamos.

## Values

Revisar el values.yaml, podremos modificar varios valores que cambiarán el comportamiento de nuestra aplicación.

Estos son los valores que se puede modificar:

|Clave |Definición |Default|
|-|-|-|
|replicaCount|Número de replicas de la aplicación web, sin efecto si HPA está habilitado|1|
|image.repository|Imagen de la aplicaión web|fblanco86/django-todo
|image.pullPolicy|Política de descarga de la imagen|Always|
|image.tag|Versión de la imagen|alpine-2|
|service.type|Tipo del Servicio de la aplicación web - ClusterIP (requiere Ingress) o LoadBalancer -|ClusterIP|
|service.port|Puerto del Servicio web|8000|
|deploy.labelKey|Nombre de la label del Deployment web|app|
|deploy.label|Valor de la label del Deployment web|web|
|deploy.port|Puerto de entrada de la aplicación web|8000|
|db.setName|Nombre del StatefulSet de la Base de Datos|db|
|db.imageTag|Versión de la imagen postgres|13.0-alpine|
|db.labelKey|Nombre de la label del Stateful db|app|
|db.label|Valor de la label del Stateful db|db|
|db.name|Nombre de la base de datos|todo|
|db.user|Usuario de la base de datos|docker|
|db.password|Password de la base de datos|docker|
|db.dataDir|Directorio donde se guardarán los datos|/data|
|db.port|Puerto de la base de datos|5432|
|ingress.enabled|Indica si Ingress está habilitado|true|
|ingress.externalIP|IP externo del Controlador Ingress|34.141.78.174|
|autoscaling.enabled|Indica si el autoescalado está habilitado|true|
|autoscaling.minreplicas|Réplicas mínimas|1|
|autoscaling.maxreplicas|Réplicas máximas|3|
|autoscaling.cpuPercentage|% de uso de CPU para el autoescalado|75|
|autoscaling.memPercentage|% de uso de memoria para el autoescalado|75|

## Instalación

Ahora ya podemos Instalar la aplicación web Django + base de datos Postgres:

```mermaid
helm install to-dos .
```

Esto levantará una aplicación web (Deployment) Django y un StatefulSet de una sola replica de un contenedor con una base de datos PostgreSQL. 
Además lanzará los Servicios necesarios para que la aplicación sea accesible desde el exterior. Comporabarlo según la configuración.

## Ingress

Para hacerlo accesible desde el exterior con Ingerss, necesitaremos seguir los siguientes pasos:
-   Instalaremos un controlador Ingress en nuestro cluster, en este caso el controlador de Nginx siguiendo la URL: https://kubernetes.github.io/ingress-nginx/deploy
-   Cuando se tenga el controlador instalado, tendremos que modificar el fichero values.yaml para informarle su externalIP.
-   Una vez levantada la aplicación puedes comprobar que funciona con la URL dev.<TU_IP>.nip.io


## Desinstalación
```mermaid
kubecctl uninstall to-dos
```

