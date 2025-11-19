"""
Generated Code Metadata:
========================
Original URL: https://www.projectortechnology.gr
Prompt: "Develop an IoT-based system for monitoring smoke and door/window sensors in a smart home setup."
Generated: DETERMINISTIC_3a6796fcc2f5fdb9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Smart Home IoT Sensor Monitoring System**
=============================================

### Requirements

* Python 3.9+
* `paho-mqtt` library for MQTT communication
* `RPi.GPIO` library for GPIO interactions (for Raspberry Pi)

### Code

```python
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MQTT settings
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'smart_home/sensors'

# GPIO pin settings
SMOKE_SENSOR_PIN = 17
DOOR_SENSOR_PIN = 23
WINDOW_SENSOR_PIN = 24

def on_connect(client, userdata, flags, rc):
    """Callback for MQTT connection"""
    if rc == 0:
        logger.info('Connected to MQTT broker')
        client.subscribe(MQTT_TOPIC)
    else:
        logger.error(f'Failed to connect to MQTT broker, return code {rc}')

def on_message(client, userdata, msg):
    """Callback for MQTT message"""
    logger.info(f'Received message on topic {msg.topic}: {msg.payload}')

def read_smoke_sensor():
    """Read smoke sensor value"""
    try:
        return GPIO.input(SMOKE_SENSOR_PIN)
    except Exception as e:
        logger.error(f'Error reading smoke sensor: {e}')
        return None

def read_door_sensor():
    """Read door sensor value"""
    try:
        return GPIO.input(DOOR_SENSOR_PIN)
    except Exception as e:
        logger.error(f'Error reading door sensor: {e}')
        return None

def read_window_sensor():
    """Read window sensor value"""
    try:
        return GPIO.input(WINDOW_SENSOR_PIN)
    except Exception as e:
        logger.error(f'Error reading window sensor: {e}')
        return None

def main():
    # Set up GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SMOKE_SENSOR_PIN, GPIO.IN)
    GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN)
    GPIO.setup(WINDOW_SENSOR_PIN, GPIO.IN)

    # Create MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        # Connect to MQTT broker
        client.connect(MQTT_BROKER, MQTT_PORT)

        # Start MQTT loop
        client.loop_start()

        while True:
            # Read sensor values
            smoke_value = read_smoke_sensor()
            door_value = read_door_sensor()
            window_value = read_window_sensor()

            # Publish sensor values to MQTT topic
            if smoke_value is not None:
                client.publish(MQTT_TOPIC, f'smoke:{smoke_value}')
            if door_value is not None:
                client.publish(MQTT_TOPIC, f'door:{door_value}')
            if window_value is not None:
                client.publish(MQTT_TOPIC, f'window:{window_value}')

            # Wait for 1 minute before publishing again
            time.sleep(60)

    except KeyboardInterrupt:
        logger.info('Stopping MQTT loop')
        client.loop_stop()
        client.disconnect()

    except Exception as e:
        logger.error(f'Error: {e}')

    finally:
        # Clean up GPIO pins
        GPIO.cleanup()

if __name__ == '__main__':
    main()
```

### Requirements File

Create a `requirements.txt` file with the following contents:

```
paho-mqtt
RPi.GPIO
```

### Running the Code

1. Install dependencies: `pip install -r requirements.txt`
2. Run the code: `python smart_home_iot.py`
