# D

## 5ta clase - 18/Marzo/2017 @ Startup Studio Monterrey

### Preparativos

En la terminal de comandos de su computadora

```bash
$ docker run -e GRANT_SUDO=yes --user root -d -p 8888:8888 jupyter/pyspark-notebook start-notebook.sh
```

Abrir puerto 4040 en el contenedor y reiniciarlo.

Dentro del contenedor

```bash
$ git clone https://github.com/israelzuniga/spark_streaming_class.git
$ sudo apt-get update
$ sudo apt-get install netcat
$ nc -lkv 127.0.0.1 -p 9999
```
