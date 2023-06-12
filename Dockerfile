# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Bark repository into the container
COPY bark /app/bark
COPY main.py /app

# Install dependencies
RUN pip install /app/bark
RUN pip install --no-cache-dir fastapi uvicorn

# Expose the FastAPI port
EXPOSE 15320

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15320", "--reload"]

