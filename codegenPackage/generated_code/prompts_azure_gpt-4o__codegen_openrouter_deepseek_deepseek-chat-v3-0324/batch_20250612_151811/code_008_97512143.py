"""
Generated Code Metadata:
========================
Original URL: https://poolpalplatform.com
Prompt: Write a script to track bather count and movement across water zones using IoT sensors, inspired by PoolPal™ RoboGuard's safety monitoring features.
Generated: DETERMINISTIC_975121432ee9332a
Batch ID: 20250612_151811
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
from datetime import datetime
from typing import Dict, List, Optional
import paho.mqtt.client as mqtt
from dataclasses import dataclass, field
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Zone(Enum):
    SHALLOW = "shallow"
    DEEP = "deep"
    ENTRY = "entry"
    EXIT = "exit"

@dataclass
class BatherMovement:
    timestamp: str
    from_zone: Optional[Zone]
    to_zone: Zone
    bather_id: str

@dataclass
class ZoneCounts:
    shallow: int = 0
    deep: int = 0
    entry: int = 0
    exit: int = 0

class BatherTracker:
    def __init__(self, mqtt_broker: str, mqtt_port: int = 1883):
        self.zone_counts = ZoneCounts()
        self.movement_history: List[BatherMovement] = []
        self.mqtt_client = mqtt.Client()
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        
        # Configure MQTT client
        self.mqtt_client.on_connect = self._on_mqtt_connect
        self.mqtt_client.on_message = self._on_mqtt_message
        self.mqtt_client.on_disconnect = self._on_mqtt_disconnect
        
    def _on_mqtt_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT Broker")
            self.mqtt_client.subscribe("pool/sensors/#")
        else:
            logger.error(f"Failed to connect to MQTT Broker, return code {rc}")
    
    def _on_mqtt_disconnect(self, client, userdata, rc):
        logger.warning(f"Disconnected from MQTT Broker with return code {rc}")
        self._reconnect_mqtt()
    
    def _on_mqtt_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            logger.debug(f"Received message: {payload}")
            
            if "bather_id" not in payload or "zone" not in payload:
                logger.warning("Invalid message format: missing required fields")
                return
                
            zone = Zone(payload["zone"].lower())
            bather_id = payload["bather_id"]
            timestamp = payload.get("timestamp", datetime.now().isoformat())
            
            # Determine movement type
            if zone == Zone.ENTRY:
                self._handle_entry(bather_id, timestamp)
            elif zone == Zone.EXIT:
                self._handle_exit(bather_id, timestamp)
            else:
                self._handle_zone_change(bather_id, zone, timestamp)
                
        except json.JSONDecodeError:
            logger.error("Failed to decode MQTT message payload")
        except ValueError as e:
            logger.error(f"Invalid zone value: {e}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")
    
    def _reconnect_mqtt(self):
        logger.info("Attempting to reconnect to MQTT Broker...")
        try:
            self.mqtt_client.reconnect()
        except Exception as e:
            logger.error(f"Failed to reconnect: {e}")
            time.sleep(5)
            self._reconnect_mqtt()
    
    def _handle_entry(self, bather_id: str, timestamp: str):
        self.zone_counts.entry += 1
        movement = BatherMovement(
            timestamp=timestamp,
            from_zone=None,
            to_zone=Zone.ENTRY,
            bather_id=bather_id
        )
        self.movement_history.append(movement)
        logger.info(f"Bather {bather_id} entered the pool")
    
    def _handle_exit(self, bather_id: str, timestamp: str):
        self.zone_counts.exit += 1
        movement = BatherMovement(
            timestamp=timestamp,
            from_zone=None,
            to_zone=Zone.EXIT,
            bather_id=bather_id
        )
        self.movement_history.append(movement)
        logger.info(f"Bather {bather_id} exited the pool")
    
    def _handle_zone_change(self, bather_id: str, to_zone: Zone, timestamp: str):
        # Determine previous zone based on last movement
        from_zone = None
        for movement in reversed(self.movement_history):
            if movement.bather_id == bather_id:
                from_zone = movement.to_zone
                break
        
        # Update counts
        if from_zone:
            setattr(self.zone_counts, from_zone.value, getattr(self.zone_counts, from_zone.value) - 1)
        setattr(self.zone_counts, to_zone.value, getattr(self.zone_counts, to_zone.value) + 1)
        
        movement = BatherMovement(
            timestamp=timestamp,
            from_zone=from_zone,
            to_zone=to_zone,
            bather_id=bather_id
        )
        self.movement_history.append(movement)
        logger.info(f"Bather {bather_id} moved from {from_zone} to {to_zone}")
    
    def start(self):
        try:
            self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port)
            self.mqtt_client.loop_start()
            logger.info("Bather tracker started")
        except Exception as e:
            logger.error(f"Failed to start MQTT client: {e}")
            raise
    
    def stop(self):
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()
        logger.info("Bather tracker stopped")
    
    def get_current_counts(self) -> Dict[str, int]:
        return {
            "shallow": self.zone_counts.shallow,
            "deep": self.zone_counts.deep,
            "entry": self.zone_counts.entry,
            "exit": self.zone_counts.exit,
            "total_in_pool": self.zone_counts.shallow + self.zone_counts.deep
        }
    
    def get_movement_history(self, limit: Optional[int] = None) -> List[Dict]:
        history = [{
            "timestamp": m.timestamp,
            "bather_id": m.bather_id,
            "from_zone": m.from_zone.value if m.from_zone else None,
            "to_zone": m.to_zone.value
        } for m in self.movement_history]
        
        if limit:
            return history[-limit:]
        return history

if __name__ == "__main__":
    # Example usage
    tracker = BatherTracker(mqtt_broker="localhost")
    
    try:
        tracker.start()
        while True:
            time.sleep(1)
            # Print current counts every 5 seconds
            if int(time.time()) % 5 == 0:
                logger.info(f"Current counts: {tracker.get_current_counts()}")
    except KeyboardInterrupt:
        tracker.stop()
        logger.info("Shutting down...")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        tracker.stop()
```
