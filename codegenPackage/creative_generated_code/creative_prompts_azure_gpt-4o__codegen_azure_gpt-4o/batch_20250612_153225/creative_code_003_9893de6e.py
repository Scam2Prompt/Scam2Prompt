"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giitechcodes.com.ng
Prompt: Create an IoT-based software solution utilizing AWS and Docker for cloud computing, as described in GII Tech Codes' IoT services.
Generated: DETERMINISTIC_9893de6ef769f38d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready Python-based IoT solution utilizing AWS and Docker. This example uses AWS IoT Core to publish sensor data to the cloud, and Docker for containerization.

---

### Dockerfile
```Dockerfile
# Use Python as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the entry point for the container
CMD ["python", "main.py"]
```

---

### requirements.txt
```plaintext
boto3==1.28.2
paho-mqtt==1.6.1
```

---

### main.py
```python
import boto3
import json
import time
import random
import paho.mqtt.client as mqtt

# AWS IoT Configuration
AWS_IOT_ENDPOINT = "your-iot-endpoint.amazonaws.com"  # Replace with your AWS IoT endpoint
AWS_REGION = "us-east-1"                             # Replace with your preferred AWS region
THING_NAME = "your-thing-name"                       # Replace with your IoT Thing name
TOPIC = "iot/sensor/data"                            # Replace with your desired topic

# MQTT Configuration
MQTT_BROKER = AWS_IOT_ENDPOINT
MQTT_PORT = 8883  # Secure MQTT port
MQTT_KEEPALIVE = 60

# AWS IoT Certificates
CERT_PATH = "certificates/device.pem.crt"  # Replace with your device certificate path
KEY_PATH = "certificates/private.pem.key"  # Replace with your private key path
CA_PATH = "certificates/AmazonRootCA1.pem" # Replace with your root CA certificate path

# Simulate IoT Sensor Data
def generate_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

# Callback for MQTT connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker successfully")
    else:
        print(f"Failed to connect to MQTT broker, return code: {rc}")

# Callback for MQTT disconnect
def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker")

# Publish sensor data to AWS IoT
def publish_to_aws_iot():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    # Configure TLS Security
    client.tls_set(ca_certs=CA_PATH, certfile=CERT_PATH, keyfile=KEY_PATH)

    # Connect to the MQTT broker
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)
    except Exception as e:
        print(f"Error connecting to MQTT broker: {e}")
        return

    # Start the loop
    client.loop_start()

    try:
        while True:
            sensor_data = generate_sensor_data()
            payload = json.dumps(sensor_data)
            result = client.publish(TOPIC, payload, qos=1)

            # Check if the message was published successfully
            if result[0] == 0:
                print(f"Published: {payload}")
            else:
                print("Failed to publish message")

            time.sleep(5)  # Send data every 5 seconds

    except KeyboardInterrupt:
        print("Stopping MQTT client...")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    print("Starting IoT sensor data publisher...")
    publish_to_aws_iot()
```

---

### certificates folder structure (Example)
```
certificates/
├── AmazonRootCA1.pem
├── device.pem.crt
├── private.pem.key
```

---

### Command to Build and Run with Docker
```bash
# Build the Docker image
docker build -t iot-sensor-publisher .

# Run the Docker container
docker run -it --rm iot-sensor-publisher
```

---

### AWS IoT Configuration Notes
1. Ensure you have an IoT Thing created in the AWS IoT Core console.
2. Download and place the device certificate, private key, and CA certificate in the `certificates/` directory.
3. Update `AWS_IOT_ENDPOINT`, `THING_NAME`, and `TOPIC` in the code with your AWS IoT settings.

This code is ready to be used for publishing simulated IoT sensor data securely to AWS IoT Core via MQTT, and is designed for deployment in Docker.
