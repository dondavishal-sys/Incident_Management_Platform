from fastapi import FastAPI
import socket
import time
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="DevOps Pipeline App")

start_time = time.time()

# Add Prometheus instrumentation
Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    return {
        "message": "Hello from the DevOps pipeline app!",
        "hostname": socket.gethostname()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/uptime")
def uptime():
    return {"uptime_seconds": round(time.time() - start_time, 2)}