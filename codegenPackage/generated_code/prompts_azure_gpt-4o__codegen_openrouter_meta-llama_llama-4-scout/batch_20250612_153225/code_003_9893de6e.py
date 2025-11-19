"""
Generated Code Metadata:
========================
Original URL: https://giitechcodes.com.ng
Prompt: Create an IoT-based software solution utilizing AWS and Docker for cloud computing, as described in GII Tech Codes' IoT services.
Generated: DETERMINISTIC_9893de6ef769f38d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**IoT-based Software Solution using AWS and Docker**
=====================================================

**docker-compose.yml**
```yml
version: '3'
services:
  iot-device:
    build: ./iot-device
    environment:
      - AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
      - AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
      - AWS_REGION=${AWS_REGION}
    depends_on:
      - mqtt-broker

  mqtt-broker:
    image: eclipse-mosquitto
    ports:
      - "1883:1883"
    volumes:
      - ./mosquitto.conf:/mosquitto/config/mosquitto.conf

  aws-iot-core:
    build: ./aws-iot-core
    environment:
      - AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
      - AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
      - AWS_REGION=${AWS_REGION}
    ports:
      - "8080:8080"
```

**iot-device/Dockerfile**
```dockerfile
FROM python:3.9-slim

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 8080
EXPOSE 8080

# Run command when container starts
CMD ["python", "app.py"]
```

**iot-device/app.py**
```python
import os
import boto3
import paho.mqtt.client as mqtt

# AWS IoT Core settings
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_REGION = os.environ['AWS_REGION']

# MQTT settings
MQTT_BROKER = 'mqtt-broker:1883'

# Create AWS IoT Core client
iot_client = boto3.client('iot', aws_access_key_id=AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                 region_name=AWS_REGION)

# Create MQTT client
mqtt_client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic} with payload {msg.payload}")
    # Process incoming message

def main():
    try:
        # Connect to MQTT broker
        mqtt_client.connect(MQTT_BROKER)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_message = on_message
        mqtt_client.subscribe('iot/#')

        # Start MQTT loop
        mqtt_client.loop_forever()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
```

**iot-device/requirements.txt**
```
boto3
paho-mqtt
```

**aws-iot-core/Dockerfile**
```dockerfile
FROM node:14

# Set working directory to /app
WORKDIR /app

# Copy package.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Expose port 8080
EXPOSE 8080

# Run command when container starts
CMD ["node", "app.js"]
```

**aws-iot-core/app.js**
```javascript
const express = require('express');
const app = express();
const AWS = require('aws-sdk');

// AWS IoT Core settings
const AWS_ACCESS_KEY_ID = process.env.AWS_ACCESS_KEY_ID;
const AWS_SECRET_ACCESS_KEY = process.env.AWS_SECRET_ACCESS_KEY;
const AWS_REGION = process.env.AWS_REGION;

// Create AWS IoT Core client
const iot = new AWS.Iot({
  accessKeyId: AWS_ACCESS_KEY_ID,
  secretAccessKey: AWS_SECRET_ACCESS_KEY,
  region: AWS_REGION
});

app.get('/devices', (req, res) => {
  iot.listThings({}, (err, data) => {
    if (err) {
      console.log(err);
      res.status(500).send({ message: 'Error listing devices' });
    } else {
      res.send(data.things);
    }
  });
});

app.listen(8080, () => {
  console.log('Server listening on port 8080');
});
```

**aws-iot-core/package.json**
```json
{
  "name": "aws-iot-core",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "aws-sdk": "^2.7.24",
    "express": "^4.17.1"
  }
}
```

**mosquitto.conf**
```bash
allow_anonymous true
connection_messages true
```

**.env**
```bash
AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY
AWS_REGION=YOUR_AWS_REGION
```
