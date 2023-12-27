FROM gitpod/workspace-full
RUN brew install scala

FROM python:3.7
RUN apt update -y && apt upgrade -y
RUN pip install pipenv