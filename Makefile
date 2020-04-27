# current_branch := $(shell git rev-parse --abbrev-ref HEAD)
tutorial_name = spam
build:
	docker build --build-arg TUTORIAL=${tutorial_name} --tag=myy92715/${tutorial_name}:latest .
push:
	docker push myy92715/$(tutorial_name):latest