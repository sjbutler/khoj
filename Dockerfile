# syntax=docker/dockerfile:1
FROM ubuntu:jammy
LABEL org.opencontainers.image.source https://github.com/khoj-ai/khoj

# Install System Dependencies
RUN apt update -y && apt -y install python3-pip git

# Install Application
COPY . .
RUN sed -i 's/dynamic = \["version"\]/version = "0.0.0"/' pyproject.toml && \
    pip install --no-cache-dir .

# Run the Application
# There are more arguments required for the application to run,
# but these should be passed in through the docker-compose.yml file.
ARG PORT
EXPOSE ${PORT}
ENTRYPOINT ["khoj"]
