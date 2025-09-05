# Chaos Toolkit (Python + FastAPI + Kubernetes)

A simple chaos testing service built with FastAPI that allows you to perform chaos engineering experiments on Kubernetes clusters via a REST API. Perfect for practicing fault injection and resilience testing.

## � Prerequisites

- Python 3.8+
- Docker
- Kubernetes cluster (local or remote)
- kubectl configured with cluster access
- Make

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chaos-toolkit.git
cd chaos-toolkit
```

2. Build and run:
```bash
make build
make run
```

The API server will start on http://localhost:8000

## 🔥 Features

- Pod Deletion: Randomly delete pods in specified namespaces
- Kubernetes Integration: Direct interaction with K8s API
- RESTful API: Easy to integrate with existing tools
- Docker Support: Containerized for easy deployment
- Extensible: Ready for adding more chaos experiments

## 📡 API Endpoints

### Health Check
```
GET /health
Response: {"status": "ok"}
```

### Delete Random Pod
```
POST /chaos/pod/delete
Body: {
    "namespace": "default",
    "label_selector": "app=myapp"  # Optional
}
Response: {
    "success": true,
    "deleted_pod": "pod-name"
}
```

## 💡 Usage Examples

### Curl Examples
```bash
# Health check
curl http://localhost:8000/health

# Delete a random pod in default namespace
curl -X POST http://localhost:8000/chaos/pod/delete \
  -H "Content-Type: application/json" \
  -d '{"namespace": "default"}'
```

### Python Client Example
```python
import requests

response = requests.post(
    "http://localhost:8000/chaos/pod/delete",
    json={"namespace": "default", "label_selector": "app=myapp"}
)
print(response.json())
```

## 🛠️ Development

### Project Structure
```
chaos-toolkit/
├── app/
│   ├── main.py          # FastAPI application
│   ├── k8s.py           # Kubernetes client logic
│   └── schemas.py       # Pydantic models
├── tests/               # Unit tests
├── Dockerfile          
└── Makefile            
```

### Running Tests
```bash
make test
```

## 🔜 Future Enhancements

- CPU Stress Testing: Simulate high CPU load conditions
- Network Chaos: Add latency, packet loss, and bandwidth restrictions
- Memory Pressure: Simulate memory-intensive scenarios
- Metrics Integration: Grafana/Prometheus integration for monitoring chaos effects
- Authentication: Secure endpoints with basic/token authentication
- More Chaos Experiments: Disk I/O, Pod scaling, and service disruptions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
