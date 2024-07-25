# hello-python-fastapi

Python FastAPI Hello App

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
docker build -t hello-python-fastapi .
docker run --rm -p 5001:8000 hello-python-fastapi
```
