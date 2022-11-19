# Smart Compost

[![CI](https://github.com/smartcompost/smartcompost-backend/actions/workflows/backend.yml/badge.svg)](https://github.com/nekeal/smartcompost/actions)

Backend for Smart Compost app for HackYeah2022

# Prerequisites

## Native way with virtualenv
- [Python3.11](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Docker way
- [Docker](https://docs.docker.com/engine/install/)  
- [Docker Compose](https://docs.docker.com/compose/install/)

## Local Development

## Native way with virtualenv

First create postgresql database:

```sql
create user smartcompost with createdb;
alter user smartcompost password 'smartcompost';
create database smartcompost owner smartcompost;
```
Now you can setup virtualenv and django:
```bash
virtualenv venv
source venv/bin/activate
pip install pip-tools
make bootstrap
```

## Docker way

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
