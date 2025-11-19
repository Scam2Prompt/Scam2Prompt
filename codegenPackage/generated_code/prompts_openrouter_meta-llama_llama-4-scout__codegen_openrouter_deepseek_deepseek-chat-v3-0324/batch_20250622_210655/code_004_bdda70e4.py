"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: "Write a program to monitor and control the lighting system in an industrial facility, such as a petrochemical plant, using IoT protocols."
Generated: DETERMINISTIC_bdda70e41c04a096
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import json
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional

import paho.mqtt.client as mqtt
from aiohttp import web

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class LightController:
    """Represents a single light controller unit."""
    id: str
    name: str
    status: bool = False
    brightness: int = 100
    area: str = "default"
    last_updated: Optional[str] = None

class LightingSystem:
    """Main class to manage the industrial lighting system."""
    
    def __init__(self):
        self.controllers: Dict[str, LightController] = {}
        self.mqtt_client = mqtt.Client(client_id="lighting_system_server")
        self.mqtt_client.on_connect = self._on_mqtt_connect
        self.mqtt_client.on_message = self._on_mqtt_message
        
    def _on_mqtt_connect(self, client, userdata, flags, rc):
        """Callback for MQTT connection."""
        if rc == 0:
            logger.info("Connected to MQTT broker")
            client.subscribe("lighting/control/#")
            client.subscribe("lighting/status/#")
        else:
            logger.error(f"Connection failed with code {rc}")
    
    def _on_mqtt_message(self, client, userdata, msg):
        """Callback for MQTT messages."""
        try:
            topic = msg.topic
            payload = json.loads(msg.payload.decode())
            
            if topic.startswith("lighting/control/"):
                controller_id = topic.split("/")[-1]
                self._handle_control_message(controller_id, payload)
            elif topic.startswith("lighting/status/"):
                controller_id = topic.split("/")[-1]
                self._handle_status_update(controller_id, payload)
                
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")
    
    def _handle_control_message(self, controller_id: str, payload: dict):
        """Process control messages from MQTT."""
        if controller_id not in self.controllers:
            logger.warning(f"Unknown controller ID: {controller_id}")
            return
            
        controller = self.controllers[controller_id]
        
        if "status" in payload:
            controller.status = payload["status"]
            logger.info(f"Controller {controller_id} status set to {controller.status}")
        
        if "brightness" in payload:
            brightness = max(0, min(100, payload["brightness"]))
            controller.brightness = brightness
            logger.info(f"Controller {controller_id} brightness set to {brightness}")
        
        controller.last_updated = payload.get("timestamp")
        
        # Publish updated status
        self._publish_status(controller)
    
    def _handle_status_update(self, controller_id: str, payload: dict):
        """Process status updates from devices."""
        if controller_id not in self.controllers:
            logger.info(f"Registering new controller: {controller_id}")
            self.controllers[controller_id] = LightController(
                id=controller_id,
                name=payload.get("name", f"Light-{controller_id}"),
                area=payload.get("area", "unknown")
            )
            
        controller = self.controllers[controller_id]
        controller.status = payload.get("status", controller.status)
        controller.brightness = payload.get("brightness", controller.brightness)
        controller.last_updated = payload.get("timestamp")
        
        logger.info(f"Status updated for controller {controller_id}")
    
    def _publish_status(self, controller: LightController):
        """Publish controller status to MQTT."""
        status = {
            "status": controller.status,
            "brightness": controller.brightness,
            "timestamp": controller.last_updated
        }
        self.mqtt_client.publish(
            f"lighting/status/{controller.id}",
            json.dumps(status)
        )
    
    def connect_mqtt(self, host: str, port: int = 1883):
        """Connect to MQTT broker."""
        try:
            self.mqtt_client.connect(host, port)
            self.mqtt_client.loop_start()
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}")
    
    async def start_web_server(self, host: str = "0.0.0.0", port: int = 8080):
        """Start the web server for API access."""
        app = web.Application()
        app.add_routes([
            web.get('/api/lights', self._get_lights),
            web.get('/api/lights/{id}', self._get_light),
            web.post('/api/lights/{id}/control', self._control_light),
        ])
        
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host, port)
        await site.start()
        logger.info(f"Web server started on {host}:{port}")
    
    async def _get_lights(self, request):
        """Return list of all light controllers."""
        lights = [{
            "id": c.id,
            "name": c.name,
            "status": c.status,
            "brightness": c.brightness,
            "area": c.area,
            "last_updated": c.last_updated
        } for c in self.controllers.values()]
        
        return web.json_response(lights)
    
    async def _get_light(self, request):
        """Return details for a specific light controller."""
        controller_id = request.match_info['id']
        if controller_id not in self.controllers:
            return web.json_response(
                {"error": "Controller not found"},
                status=404
            )
            
        controller = self.controllers[controller_id]
        return web.json_response({
            "id": controller.id,
            "name": controller.name,
            "status": controller.status,
            "brightness": controller.brightness,
            "area": controller.area,
            "last_updated": controller.last_updated
        })
    
    async def _control_light(self, request):
        """Control a specific light controller."""
        controller_id = request.match_info['id']
        if controller_id not in self.controllers:
            return web.json_response(
                {"error": "Controller not found"},
                status=404
            )
            
        try:
            data = await request.json()
            controller = self.controllers[controller_id]
            
            if "status" in data:
                controller.status = data["status"]
            
            if "brightness" in data:
                controller.brightness = max(0, min(100, data["brightness"]))
            
            controller.last_updated = data.get("timestamp")
            
            # Publish control command to MQTT
            self.mqtt_client.publish(
                f"lighting/control/{controller_id}",
                json.dumps({
                    "status": controller.status,
                    "brightness": controller.brightness
                })
            )
            
            return web.json_response({"status": "success"})
        
        except json.JSONDecodeError:
            return web.json_response(
                {"error": "Invalid JSON"},
                status=400
            )
        except Exception as e:
            logger.error(f"Error controlling light: {e}")
            return web.json_response(
                {"error": "Internal server error"},
                status=500
            )

async def main():
    """Main entry point for the lighting system application."""
    lighting_system = LightingSystem()
    
    # Connect to MQTT broker
    lighting_system.connect_mqtt("mqtt.broker.local")
    
    # Start web server
    await lighting_system.start_web_server()
    
    # Keep the application running
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Shutting down lighting system")
    except Exception as e:
        logger.error(f"Application error: {e}")
```
