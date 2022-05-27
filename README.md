# Docker
* Crear repo en GitHub (Docker_Demo)
* Crear workspace en Gitpod
```` shell
docker pull ubuntu : 20.04
docker run -it --net=host --name ubuntu -h yael ubuntu : 20.04
````
(it == consola interactiva) (--net == indicar que el contendedor va tener el mismo acceso a internet que mi computadora)(--name == nombre del contenedor)(-h == host el nombre del host)(apartir de que imagen creara el contenedor)(-v ruta a usar )
```` shell
docker run -it -v ruta:rutaaquerer --net=host --name ubuntu -h yael ubuntu : 20.04
````
* Actualizar ubuntu
```` shell
apt update
````
* Instalar python y pip
```` shell
apt install python3 -y
apt install python3-pip -y
````
* Instalar webpy
```` shell
pip3 install web.py
````
 
## Docker comandos
### Mostrar todos los contenedores
```` shell
docker ps -a
````

### Iniciar docker 
```` shell
docker start -i id
````
(i == para interactuar)

### Apagar contenedor 
```` shell
docker stop id
````

### Docker File
#### Archivo Dockerfile
```` shell
From ubuntu:18.04
LABEL description = "Descripcion"
Run apt update
RUN apt upgrade -y
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 installl web.py

````
#### Comando para crearla
```` shell
docker build -t mi_imagen:v1 .
````