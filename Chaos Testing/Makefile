IMAGE_NAME=chaos-toolkit

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -it --rm -p 8000:8000 \
		-v ~/.kube:/root/.kube \
		-e K8S_NAMESPACE=default \
		$(IMAGE_NAME)

test:
	curl -X POST "http://localhost:8000/chaos/delete_pod?namespace=default"
