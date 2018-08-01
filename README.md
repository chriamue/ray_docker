# ray_docker

docker compose and dockerfile for using ray framework

## start server

```bash
docker-compose up -d server
```

## connect as client

```bash
docker-compose run client
ray start --redis-address=localhost:6379
```