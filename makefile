.PHONY: build start stop clean healthcheck

DOT := $(shell docker --version)

healthcheck:
ifndef DOT
	$(error "docker is not available")
endif
	@echo "ok. docker is available"

clean: stop
	sudo docker image rm mm
	rm build_ -f

stop:
	sudo docker stop mm_start

start: build
	sudo docker run --rm --name mm_start -p 8080:8080 mm

build: build_

build_:
	sudo docker volume create my-volume
	sudo docker build . --tag mm
	echo "" > build_
