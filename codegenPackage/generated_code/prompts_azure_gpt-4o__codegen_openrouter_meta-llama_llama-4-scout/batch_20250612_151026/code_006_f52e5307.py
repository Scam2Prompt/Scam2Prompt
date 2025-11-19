"""
Generated Code Metadata:
========================
Original URL: https://myatom.online
Prompt: Provide a step-by-step guide for setting up a server infrastructure similar to ATOM's IPTV platform, focusing on stability and high-quality streaming.
Generated: DETERMINISTIC_f52e5307761304d4
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Setting Up a Server Infrastructure for IPTV Platform**
===========================================================

**Infrastructure Overview**
---------------------------

This guide provides a basic infrastructure setup for an IPTV platform similar to ATOM's. The setup includes:

*   Load balancing with HAProxy
*   Streaming servers with Nginx and RTMP
*   Database with MySQL
*   Storage with NFS

**docker-compose.yml**
```yml
version: '3'

services:
  # Load Balancer
  haproxy:
    image: haproxy:2.4
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./haproxy.cfg:/etc/haproxy/haproxy.cfg
    depends_on:
      - nginx

  # Streaming Server
  nginx:
    image: nginx:1.22
    ports:
      - "8080:8080"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./stream:/usr/share/nginx/stream
    depends_on:
      - mysql
      - nfs

  # Database
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - ./mysql:/var/lib/mysql

  # Storage
  nfs:
    image: nfs-server
    volumes:
      - ./nfs:/exports
    ports:
      - "2049:2049"
```

**haproxy.cfg**
```bash
global
  maxconn 256

defaults
  mode http
  timeout connect 5000ms
  timeout client  50000ms
  timeout server  50000ms

frontend http
  bind *:80
  default_backend nginx

backend nginx
  mode http
  balance roundrobin
  server nginx 127.0.0.1:8080 check

frontend https
  bind *:443 ssl crt /etc/haproxy/certs/haproxy.crt
  default_backend nginx
```

**nginx.conf**
```nginx
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;

    keepalive_timeout  65;

    server {
        listen       8080;
        server_name  localhost;

        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm;
        }

        location /stream {
            alias /usr/share/nginx/stream;
        }
    }
}

rtmp {
    server {
        listen 1935;
        chunk_size 4096;

        application live {
            live on;
            record off;
            allow publish all;
            allow play all;
        }
    }
}
```

**mysql.sql**
```sql
CREATE DATABASE IF NOT EXISTS iptv;

USE iptv;

CREATE TABLE IF NOT EXISTS channels (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  url VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS programs (
  id INT AUTO_INCREMENT,
  channel_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  start_time DATETIME NOT NULL,
  end_time DATETIME NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (channel_id) REFERENCES channels(id)
);
```

**.env**
```bash
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=iptv
MYSQL_USER=user
MYSQL_PASSWORD=password
```

**Run with**
```bash
docker-compose up -d
```
