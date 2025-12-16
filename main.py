from fastapi import FastAPI
from prometheus_client import make_asgi_app
from metrics import request_counter

app = FastAPI()

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/hello")
def hello():
    request_counter.inc()
    return {"message": "Hello world"}
