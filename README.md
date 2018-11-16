# docker python restful api sample

This is a sample project to demo how to use docker + python to quickly develop and publish a restful API server

## how-to
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
3. manual start uwsgi service within docker
```shell
    uwsgi --http :80 --wsgi-file /oakridge/server.py --callable app
```
