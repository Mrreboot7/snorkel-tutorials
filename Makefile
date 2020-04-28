build:
	docker build --build-arg TUTORIAL=spam --tag=myy92715/snorkel-spam:latest .
	docker build --build-arg TUTORIAL=drybell --tag=myy92715/snorkel-drybell:latest .
	docker build --build-arg TUTORIAL=crowdsourcing --tag=myy92715/snorkel-crowdsourcing:latest .
	docker build --build-arg TUTORIAL=multitask --tag=myy92715/snorkel-multitask:latest .
	docker build --build-arg TUTORIAL=recsys --tag=myy92715/snorkel-recsys:latest .
	docker build --build-arg TUTORIAL=spouse --tag=myy92715/snorkel-spouse:latest .
	docker build --build-arg TUTORIAL=visual_relation --tag=myy92715/snorkel-visual_relation:latest .
push:
	docker push myy92715/snorkel-spam:latest
	docker push myy92715/snorkel-drybell:latest
	docker push myy92715/snorkel-crowdsourcing:latest
	docker push myy92715/snorkel-multitask:latest
	docker push myy92715/snorkel-recsys:latest
	docker push myy92715/snorkel-spouse:latest
	docker push myy92715/snorkel-visual_relation:latest
