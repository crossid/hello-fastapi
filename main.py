import os

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/api")
def read_root(request: Request):
    # list all env vars starting with HELLO-
    hello_env_vars = {k: v for k, v in os.environ.items() if k.startswith("HELLO_")}
    headers = dict(request.headers)
    return {"message": "Hello, World!", "envs": hello_env_vars, "headers": headers}
