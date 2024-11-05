curl -O https://raw.githubusercontent.com/BakhmetovRustam/TechOrda/main/docker/docker-bind/nginx.conf
docker run -d -p 7777:80 -v /home/user/Downloads/nginx.conf:/etc/nginx/nginx.conf --name jusan-docker-bind nginx:mainline
