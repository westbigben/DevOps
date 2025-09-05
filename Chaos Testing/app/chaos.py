# app/chaos.py
from .k8s_client import get_k8s_client
import random

def delete_pod(namespace="default", label_selector=None):
    """
    Deletes a random pod in the given namespace with optional label selector.
    """
    v1 = get_k8s_client()
    pods = v1.list_namespaced_pod(namespace, label_selector=label_selector).items
    if not pods:
        return {"status": "no pods found"}
    
    pod = random.choice(pods)
    v1.delete_namespaced_pod(pod.metadata.name, namespace)
    return {"status": "deleted", "pod": pod.metadata.name}
# --- IGNORE ---