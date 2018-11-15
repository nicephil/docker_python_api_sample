# docker python restful api sample

This is a sample project to demo how to use docker + python to quickly develop and publish a restful API server

## Files:
..* Dockerfile: 定义了docker image
..* .dockerignore: 哪些文件在build docker image 的时候要排除在外

## pre-requirement
需要install docker 并启动docker service

## how-to
1. build/list/run image:
```shell
    docker build -t ykang:v0.0.1  .
    docker image ls
    docker docker run -p $(pwd):/oakridge -it ykang:v0.0.1 bash
```
