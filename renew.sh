
sudo certbot certonly --standalone --preferred-challenges http --http-01-port 81 -d rogerroan.ddns.me

cat /etc/letsencrypt/live/rogerroan.ddns.me-0003/fullchain.pem /etc/letsencrypt/live/rogerroan.ddns.me-0003/privkey.pem > \
/root/docker/haproxy/config/server.pem
