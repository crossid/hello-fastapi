# hello-fastapi

Hello FastAPI is a tiny web server that responds to a GET request with a JSON response.

It exposes the following endpoints:

- `/api` - returns a JSON response with a message "Hello, FastAPI!", env vars starting with `HELLO_` and request headers.
- `/docs` - FastAPI's auto-generated API documentation.
- `/openapi.json` - FastAPI's auto-generated OpenAPI schema.

# Setup

```bash
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

Run via uvicorn cli:

```bash
uvicorn main:app --port 5001 --reload
```

Bulild and run via docker:

```bash
docker build -t hello-fastapi .
docker run --rm -p 5001:8000 hello-fastapi
```
