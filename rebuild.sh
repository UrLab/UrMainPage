#/bin/sh

CSV=

python3 src/main.py $CSV
mv index.html content/
docker-compose down
docker-compose up -d
