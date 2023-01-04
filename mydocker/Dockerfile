# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Set the environment variable VERSION to 1.2.0
ENV VERSION 1.2.0

# Install Python, Vim, zip, and unzip
RUN apt-get update && \ 
    apt-get install -y  python3 vim zip unzip &&\
    rm -rf /var/lib/apt/lists/*

# Copy the zip_job.py script to the /tmp folder
COPY zip_job.py /tmp/zip_job.py

# Run a command that prints the OS type and architecture and verifies that the zip_job.py script exists
CMD uname -a && \
    test -f /tmp/zip_job.py && echo "/tmp/zip_job.py exists."
