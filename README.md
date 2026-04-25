# Python API Monitor
Simple python app that monitors HTTP endpoints

## Features
- Checks HTTP status codes
- Saves logs to a JSON file
- Dockerized
- Basic CI pipeline with automated tests via GitHub Actions
## Configuration
Edit app/config.json to define endpoints:
```
{
 "urls": [
   "https://google.com",
   "https://wikipedia.org",
   "https://httpbin.org/status/500",
   "https://httpbin.org/status/404"
 ]
}
```
## Run locally
```
python app/main.py
```
## Run with Docker
```
docker build -t python-api-monitor .
docker run python-api-monitor
```
## To-do improvements
- Configurable timeout
- Retry for failed requests
- Cloud deployment (Azure/AWS)

## About
Project created for learning DevOps concepts and technologies