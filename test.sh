#!/bin/sh

docker-compose build
docker-compose run --entrypoint ./test.sh web
