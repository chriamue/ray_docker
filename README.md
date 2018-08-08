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

## pyenv

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
pyenv install 3.6.5
pyenv virtualenv 3.6.5 ray
pyenv activate ray
```