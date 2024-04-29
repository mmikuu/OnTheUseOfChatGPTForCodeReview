docker-compose down -v
docker rmi $(docker images -q) --force
docker rm $(docker ps -aq) --force
docker-compose build
docker-compose up