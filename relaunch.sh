#!/bin/bash

# Relaunch the docker-compose stack
sudo docker-compose down && \
sudo docker-compose build && \
sudo docker-compose up -d
