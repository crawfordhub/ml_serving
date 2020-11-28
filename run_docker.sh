echo killingold docker processes
docker-compose rm -fs

echo building docker containers
docker-compose up --build -d
