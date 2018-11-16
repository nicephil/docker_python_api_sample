# docker python restful api sample

This is a sample project to demo how to use docker + python to quickly develop and publish a restful API server

## what's going on
This example:
1. build a sample docker image
2. run this image with: (1) map ``host $(pwd) to docker:/oakridge``, (2) map host ``port 8000 -> 80``
3. mannually run inside docker to start http service

Then you can browse to ``host.ip.addr:8000``.\n
The source code is on host directory ``$(pwd)/src/server.py``

## how-to
You must install docker and start docker service.
After git clone, run following:
1. build/list/run image:
```shell
    docker build -t testimg:latest  .
    docker image ls
    docker run -v $(pwd)/src:/oakridge -it -p 8000:80 --name mycontainer testimg:latest bash
```
2. detach/attach to docker:
```shell
    ctrl-p ctrl-q                       # Detach from docker back to host shell
    docker attach mycontainer           # Attach from host shell to docker
```
3. manual start uwsgi service within docker, see <a href="https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html" target="_blank">python wsgi</a> for detail.
```shell
    uwsgi --http :80 --wsgi-file /oakridge/server.py --callable app
```
a more handy WSGI server is <a href="http://docs.gunicorn.org/en/stable/index.html">gunicoren</a>, but keep in mind the focus here is python, either one works.
