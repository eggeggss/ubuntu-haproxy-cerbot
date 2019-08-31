docker-compose -f /root/docker/docker-compose.yml build &&\
docker-compose -f /root/docker/docker-compose.yml up -d --force-recreate --scale web=3
