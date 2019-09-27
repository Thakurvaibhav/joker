SHELL := /bin/bash
SHA=$(shell git rev-parse HEAD)

.PHONY: build
build:
	$(info Make: Building docker images: TAG=${SHA})
	@TAG=${SHA} docker-compose -f docker-compose.yml build

.PHONY: clean
clean:
	$(info Make: Clean docker containers)
	@TAG=${SHA} docker-compose down -v --remove-orphans

.PHONY: run
run:
	$(info Make: Bring local docker cluster up)
	@TAG=${SHA} docker-compose -f docker-compose.yml up

.PHONY: test
test:
	$(info Make: Run tests)
	@TAG=${SHA} docker-compose -f docker-compose.yml -f docker-compose.test.yml up
