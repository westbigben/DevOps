# app/config.py
import os

K8S_NAMESPACE = os.getenv("K8S_NAMESPACE", "default")
