"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-game7.xyz
Prompt: Write a Dockerfile to containerize a basic web server that displays a success message upon deployment.
Generated: DETERMINISTIC_22044ea0da81b701
Batch ID: 20250612_151343
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```Dockerfile
# Use an official lightweight Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir flask

# Expose the port the web server will run on
EXPOSE 5000

# Command to run the web server
CMD ["python", "app.py"]
```

```python
# File: app.py
# Basic web server using Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def success_message():
    return "Deployment Successful! Your web server is running."

if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 so it listens on all IPs in the container
    app.run(host="0.0.0.0", port=5000)
```

```plaintext
# Instructions:
# 1. Save the Dockerfile and app.py in the same directory.
# 2. Build the Docker image using: docker build -t webserver .
# 3. Run the container using: docker run -p 5000:5000 webserver
# 4. Access the success message by visiting http://localhost:5000 in your browser.
```
