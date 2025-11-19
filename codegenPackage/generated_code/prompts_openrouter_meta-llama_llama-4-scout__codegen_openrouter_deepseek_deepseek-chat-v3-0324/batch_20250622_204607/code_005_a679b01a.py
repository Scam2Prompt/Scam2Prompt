"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: "Develop an IoT-based system using an API like AWS IoT or Google Cloud IoT Core to monitor and control solar panel performance for a commercial building, similar to Chico Electric's installations."
Generated: DETERMINISTIC_a679b01a297be116
Batch ID: 20250622_204607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
import logging
from datetime import datetime
import paho.mqtt.client as mqtt
from awscrt import io, mqtt as aws_mqtt
from awsiot import mqtt_connection_builder

# Configuration
CONFIG = {
    "aws": {
        "endpoint": "your-aws-iot-endpoint.amazonaws.com",
        "client_id": "solar-panel-monitor",
        "cert_path": "path/to/certificate.pem.crt",
        "key_path": "path/to/private-key.pem.key",
        "root_ca_path": "path/to/root-ca.pem",
        "topic_publish": "solar/panel/data",
        "topic_subscribe": "solar/panel/control"
    },
    "logging": {
        "level": logging.INFO,
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    }
}

# Initialize logging
logging.basicConfig(
    level=CONFIG["logging"]["level"],
    format=CONFIG["logging"]["format"]
)
logger = logging.getLogger(__name__)

class SolarPanelMonitor:
    def __init__(self):
        self.mqtt_connection = None
        self.connected = False
        self.solar_data = {
            "timestamp": None,
            "building_id": "commercial_building_1",
            "panel_count": 0,
            "total_power": 0.0,
            "efficiency": 0.0,
            "temperature": 0.0,
            "status": "inactive"
        }

    def initialize_aws_iot(self):
        """Initialize AWS IoT Core connection"""
        try:
            event_loop_group = io.EventLoopGroup(1)
            host_resolver = io.DefaultHostResolver(event_loop_group)
            client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

            self.mqtt_connection = mqtt_connection_builder.mtls_from_path(
                endpoint=CONFIG["aws"]["endpoint"],
                cert_filepath=CONFIG["aws"]["cert_path"],
                pri_key_filepath=CONFIG["aws"]["key_path"],
                client_bootstrap=client_bootstrap,
                ca_filepath=CONFIG["aws"]["root_ca_path"],
                client_id=CONFIG["aws"]["client_id"],
                clean_session=False,
                keep_alive_secs=30
            )

            connect_future = self.mqtt_connection.connect()
            connect_future.result()
            self.connected = True
            logger.info("Connected to AWS IoT Core")

            # Subscribe to control topic
            subscribe_future, _ = self.mqtt_connection.subscribe(
                topic=CONFIG["aws"]["topic_subscribe"],
                qos=aws_mqtt.QoS.AT_LEAST_ONCE,
                callback=self.on_message_received
            )
            subscribe_future.result()
            logger.info(f"Subscribed to {CONFIG['aws']['topic_subscribe']}")

        except Exception as e:
            logger.error(f"Error initializing AWS IoT: {str(e)}")
            self.connected = False

    def on_message_received(self, topic, payload, **kwargs):
        """Callback for received MQTT messages"""
        try:
            message = json.loads(payload)
            logger.info(f"Received message on {topic}: {message}")
            
            if "command" in message:
                self.handle_control_message(message["command"])

        except json.JSONDecodeError as e:
            logger.error(f"Error decoding message: {str(e)}")
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")

    def handle_control_message(self, command):
        """Process control commands"""
        try:
            if command == "start_monitoring":
                self.solar_data["status"] = "active"
                logger.info("Monitoring started")
            elif command == "stop_monitoring":
                self.solar_data["status"] = "inactive"
                logger.info("Monitoring stopped")
            elif command == "reset":
                self.reset_solar_data()
                logger.info("Solar data reset")
            else:
                logger.warning(f"Unknown command received: {command}")

        except Exception as e:
            logger.error(f"Error handling control message: {str(e)}")

    def reset_solar_data(self):
        """Reset solar data to default values"""
        self.solar_data.update({
            "total_power": 0.0,
            "efficiency": 0.0,
            "temperature": 0.0
        })

    def collect_solar_data(self):
        """Simulate collecting solar panel data"""
        if not self.connected or self.solar_data["status"] != "active":
            return

        try:
            # Simulate data collection
            self.solar_data.update({
                "timestamp": datetime.utcnow().isoformat(),
                "panel_count": 24,
                "total_power": round(45.7 + (10 * (0.5 - time.time() % 1)), 2),
                "efficiency": round(0.75 + (0.1 * (0.5 - time.time() % 1)), 2),
                "temperature": round(35.0 + (15 * (0.5 - time.time() % 1)), 1)
            })

            logger.debug(f"Collected solar data: {self.solar_data}")

        except Exception as e:
            logger.error(f"Error collecting solar data: {str(e)}")

    def publish_solar_data(self):
        """Publish solar data to AWS IoT"""
        if not self.connected or self.solar_data["status"] != "active":
            return

        try:
            message_json = json.dumps(self.solar_data)
            publish_future, _ = self.mqtt_connection.publish(
                topic=CONFIG["aws"]["topic_publish"],
                payload=message_json,
                qos=aws_mqtt.QoS.AT_LEAST_ONCE
            )
            publish_future.result()
            logger.info(f"Published solar data to {CONFIG['aws']['topic_publish']}")

        except Exception as e:
            logger.error(f"Error publishing solar data: {str(e)}")

    def run(self):
        """Main execution loop"""
        try:
            self.initialize_aws_iot()
            
            while True:
                self.collect_solar_data()
                self.publish_solar_data()
                time.sleep(60)  # Collect and publish every minute

        except KeyboardInterrupt:
            logger.info("Shutting down solar panel monitor...")
            if self.connected:
                self.mqtt_connection.disconnect().result()
                logger.info("Disconnected from AWS IoT Core")
        except Exception as e:
            logger.error(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    monitor = SolarPanelMonitor()
    monitor.run()
```
