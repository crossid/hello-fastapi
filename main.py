import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # list all env vars starting with HELLO-
    hello_env_vars = {k: v for k, v in os.environ.items() if k.startswith("HELLO_")}
    return {"message": "Hello, World!", "envs": hello_env_vars}
