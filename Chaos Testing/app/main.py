# app/main.py
from fastapi import FastAPI, Query
from .chaos import delete_pod
from .config import K8S_NAMESPACE

app = FastAPI(title="Chaos Toolkit API")

@app.get("/")
def root():
    return {"message": "Chaos Toolkit is running 🚀"}

@app.post("/chaos/delete_pod")
def chaos_delete_pod(
    namespace: str = Query(K8S_NAMESPACE),
    label_selector: str | None = None,
):
    result = delete_pod(namespace, label_selector)
    return result
# --- IGNORE ---