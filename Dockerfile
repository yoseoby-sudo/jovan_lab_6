#Use an official lightweight Python runtime as a parent image.
FROM python:3.11-slim

#Set the working directory in the container.
WORKDIR /app

#Copy all project files into the container.
COPY . /app

#Run the Python script interactively when the container starts.
CMD ["python", "systems.py"]