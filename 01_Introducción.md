# Desafío LATAM
## Introducción a Big Data
## 5ta clase - 18/Marzo/2017 @ Startup Studio Monterrey



### Repaso de Arquitectura Lambda

![LA Overview](http://lambda-architecture.net/img/la-overview_small.png)

### Preparativos
1. Iniciar Docker
2. En la terminal de comandos de su computadora:

```bash
$ docker run -e GRANT_SUDO=yes --user root -d -p 8888:8888 jupyter/pyspark-notebook start-notebook.sh
```
Problemas en Windows: https://medium.com/@neil.avery_68603/running-docker-from-windows-cmd-prompt-6540daebedad#.lae8p2oiz


Dentro del contenedor

```bash
# apt-get update
# apt-get install netcat
# su jovyan
$ git clone https://github.com/israelzuniga/spark_streaming_class.git
$ cd spark_streaming_class
$ nc -lkv 127.0.0.1 -p 9999
```
