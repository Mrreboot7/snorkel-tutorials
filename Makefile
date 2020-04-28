build:
	docker build --build-arg TUTORIAL=spam --tag=myy92715/spam:latest .
	docker build --build-arg TUTORIAL=drybell --tag=myy92715/drybell:latest .
	docker build --build-arg TUTORIAL=crowdsourcing --tag=myy92715/crowdsourcing:latest .
	docker build --build-arg TUTORIAL=multitask --tag=myy92715/multitask:latest .
	docker build --build-arg TUTORIAL=recsys --tag=myy92715/recsys:latest .
	docker build --build-arg TUTORIAL=spouse --tag=myy92715/spouse:latest .
	docker build --build-arg TUTORIAL=visual_relation --tag=myy92715/visual_relation:latest .
push:
	docker push myy92715/spam:latest
	docker push myy92715/drybell:latest
	docker push myy92715/crowdsourcing:latest
	docker push myy92715/multitask:latest
	docker push myy92715/recsys:latest
	docker push myy92715/spouse:latest
	docker push myy92715/visual_relation:latest
