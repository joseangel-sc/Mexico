IMAGE_TAG:=python-mx
RUN:=docker run --rm -v $$(pwd):/app -w /app -e COVERAGE_PROCESS_START=.coveragerc $(IMAGE_TAG)
RUN_INTERACTIVE:=docker run --rm -it -v $$(pwd):/app -w /app $(IMAGE_TAG)
REVISION=$(shell git rev-parse --short HEAD)

all: build

.PHONY: build

build:
	docker build -t $(IMAGE_TAG):$(REVISION) .
	docker tag $(IMAGE_TAG):$(REVISION) $(IMAGE_TAG):latest

test:
	python -m unittest

coverage: test
	$(RUN) coverage combine
	$(RUN) coverage report --fail-under=98
	$(RUN) coverage html

shell:
	$(RUN_INTERACTIVE) ipython
