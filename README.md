# ray_docker

docker compose and dockerfile for using ray framework

## start server

```bash
docker-compose up -d server
```

## connect as client

```bash
docker-compose up -d server
```

## connect for development

```bash
docker-compose run develop
ray start --redis-address=$HOST:$PORT
python
```