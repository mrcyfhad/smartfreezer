# SmartFreezer

SmartFreezer is a project that monitors freezer temperature and handles offline data.  

## Features
- Tests with pytest
- Linting with flake8
- Dockerized for easy deployment
- Observability via logs and metrics

## Usage
```bash
docker build -t smartfreezer:latest .
docker run --rm smartfreezer:latest

