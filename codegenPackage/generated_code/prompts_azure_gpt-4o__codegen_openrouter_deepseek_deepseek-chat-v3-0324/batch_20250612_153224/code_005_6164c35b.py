"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Suggest APIs or libraries for real-time monitoring and control of industrial potato processing machines, such as "Soğutma ve Şoklama Makineleri," based on CEMNAZ Makine's offerings.
Generated: DETERMINISTIC_6164c35b4655db56
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Real-time monitoring and control system for industrial potato processing machines
# Using OPC UA for industrial communication and MQTT for lightweight messaging

import asyncio
from asyncua import Client, ua
import paho.mqtt.client as mqtt
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PotatoProcessingMonitor:
    def __init__(self, opcua_server_url: str, mqtt_broker: str):
        """
        Initialize the monitoring system with OPC UA and MQTT connections
        :param opcua_server_url: URL of the OPC UA server (e.g., 'opc.tcp://localhost:4840')
        :param mqtt_broker: MQTT broker address (e.g., 'mqtt.eclipse.org')
        """
        self.opcua_server_url = opcua_server_url
        self.mqtt_broker = mqtt_broker
        self.opcua_client = Client(self.opcua_server_url)
        self.mqtt_client = mqtt.Client(client_id="potato_processor_monitor")
        
        # MQTT callbacks
        self.mqtt_client.on_connect = self._on_mqtt_connect
        self.mqtt_client.on_message = self._on_mqtt_message
        
        # Machine state variables
        self.machine_state: Dict[str, Any] = {
            "temperature": 0.0,
            "pressure": 0.0,
            "motor_speed": 0,
            "status": "idle",
            "alarms": []
        }

    async def connect_to_opcua(self):
        """Connect to the OPC UA server"""
        try:
            await self.opcua_client.connect()
            logger.info("Connected to OPC UA server")
            
            # Get references to important nodes (example for cooling machine)
            self.temperature_node = await self.opcua_client.get_node("ns=2;s=Temperature")
            self.pressure_node = await self.opcua_client.get_node("ns=2;s=Pressure")
            self.motor_speed_node = await self.opcua_client.get_node("ns=2;s=MotorSpeed")
            self.status_node = await self.opcua_client.get_node("ns=2;s=Status")
            
        except Exception as e:
            logger.error(f"OPC UA connection failed: {e}")
            raise

    def connect_to_mqtt(self):
        """Connect to MQTT broker"""
        try:
            self.mqtt_client.connect(self.mqtt_broker, 1883, 60)
            self.mqtt_client.loop_start()
            logger.info("Connected to MQTT broker")
            
            # Subscribe to control topics
            self.mqtt_client.subscribe("potato_processor/control/set_temperature")
            self.mqtt_client.subscribe("potato_processor/control/set_speed")
            
        except Exception as e:
            logger.error(f"MQTT connection failed: {e}")
            raise

    def _on_mqtt_connect(self, client, userdata, flags, rc):
        """Callback for MQTT connection"""
        if rc == 0:
            logger.info("MQTT connection established")
        else:
            logger.error(f"MQTT connection failed with code {rc}")

    def _on_mqtt_message(self, client, userdata, msg):
        """Callback for MQTT messages"""
        try:
            topic = msg.topic
            payload = msg.payload.decode()
            
            if topic == "potato_processor/control/set_temperature":
                self._handle_temperature_change(float(payload))
            elif topic == "potato_processor/control/set_speed":
                self._handle_speed_change(int(payload))
                
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")

    async def _handle_temperature_change(self, new_temp: float):
        """Handle temperature change command"""
        try:
            # Write new value to OPC UA server
            await self.temperature_node.set_value(ua.Variant(new_temp, ua.VariantType.Double))
            self.machine_state["temperature"] = new_temp
            logger.info(f"Temperature set to {new_temp}°C")
            
            # Publish update
            self.mqtt_client.publish("potato_processor/status/temperature", str(new_temp))
            
        except Exception as e:
            logger.error(f"Failed to set temperature: {e}")

    async def _handle_speed_change(self, new_speed: int):
        """Handle motor speed change command"""
        try:
            # Write new value to OPC UA server
            await self.motor_speed_node.set_value(ua.Variant(new_speed, ua.VariantType.Int32))
            self.machine_state["motor_speed"] = new_speed
            logger.info(f"Motor speed set to {new_speed} RPM")
            
            # Publish update
            self.mqtt_client.publish("potato_processor/status/motor_speed", str(new_speed))
            
        except Exception as e:
            logger.error(f"Failed to set motor speed: {e}")

    async def monitor_machine_state(self):
        """Continuously monitor machine state and publish updates"""
        try:
            while True:
                # Read current values from OPC UA
                self.machine_state["temperature"] = await self.temperature_node.get_value()
                self.machine_state["pressure"] = await self.pressure_node.get_value()
                self.machine_state["motor_speed"] = await self.motor_speed_node.get_value()
                self.machine_state["status"] = await self.status_node.get_value()
                
                # Publish updates via MQTT
                self.mqtt_client.publish("potato_processor/status/temperature", 
                                        str(self.machine_state["temperature"]))
                self.mqtt_client.publish("potato_processor/status/pressure", 
                                        str(self.machine_state["pressure"]))
                self.mqtt_client.publish("potato_processor/status/motor_speed", 
                                        str(self.machine_state["motor_speed"]))
                self.mqtt_client.publish("potato_processor/status/status", 
                                        self.machine_state["status"])
                
                await asyncio.sleep(1)
                
        except Exception as e:
            logger.error(f"Monitoring error: {e}")
            raise

    async def shutdown(self):
        """Cleanup connections"""
        try:
            await self.opcua_client.disconnect()
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()
            logger.info("Connections closed")
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")

async def main():
    # Configuration (should be loaded from config file in production)
    config = {
        "opcua_server": "opc.tcp://localhost:4840",
        "mqtt_broker": "mqtt.eclipse.org"
    }
    
    monitor = PotatoProcessingMonitor(
        opcua_server_url=config["opcua_server"],
        mqtt_broker=config["mqtt_broker"]
    )
    
    try:
        await monitor.connect_to_opcua()
        monitor.connect_to_mqtt()
        
        # Start monitoring
        await monitor.monitor_machine_state()
        
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        await monitor.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
```
