OWNER=defensoriapublicasp
IMAGE_NAME=bot
IMAGE_VERSION ?= 0.1.0
IMAGE_FILE ?= docker/bot.Dockerfile
PROXY ?= registry-1.docker.io
USER=dockerusername
PASS=dockeruserpass
QNAME=$(PROXY)/$(OWNER)/$(IMAGE_NAME)
BUILD_TAG=$(QNAME):$(IMAGE_VERSION)
LATEST_TAG=$(QNAME):latest

ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

build:
	docker build \
		-f ${IMAGE_FILE} \
		--build-arg IMAGE_VERSION=$(IMAGE_VERSION) \
		-t $(BUILD_TAG) $(ROOT_DIR)

lint:
	docker run -it --rm -v "$(ROOT_DIR)/Dockerfile:/Dockerfile:ro" redcoolbeans/dockerlint

tag:
	docker tag $(BUILD_TAG) $(LATEST_TAG)

push:
	docker login ${PROXY} -u ${USER} -p ${PASS}
	docker push $(BUILD_TAG)
	docker push $(LATEST_TAG)
