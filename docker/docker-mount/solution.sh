curl -O https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf
curl -O https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip
unzip jusan-docker-mount.zip
docker run -d -p 9999:80 --name jusan-docker-mount -v /home/user/Downloads/jusan-docker-mount.conf:/etc/nginx/conf.d/jusan-docker-mount.conf -v /home/user/Downloads/jusan-docker-mount/:/var/www/example nginx:mainline

# Надо использовать curl -H "Host: example.com" http://localhost:9999/
