"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Generate code to control a car's interior lighting system, including custom suede headliner lighting and reconfigurable performance displays, inspired by the Phantom SS modifications.
Generated: DETERMINISTIC_76ab828483834797
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import threading
from enum import Enum
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LightingZone(Enum):
    """Enum for different lighting zones in the car"""
    HEADLINER = "headliner"
    FOOTWELL = "footwell"
    DASHBOARD = "dashboard"
    DOOR = "door"
    ALL = "all"

class LightingMode(Enum):
    """Enum for different lighting modes"""
    STATIC = "static"
    PULSE = "pulse"
    RAINBOW = "rainbow"
    THEATER = "theater"
    OFF = "off"

@dataclass
class Color:
    """RGB color representation"""
    red: int
    green: int
    blue: int

    def validate(self):
        """Validate color values are within 0-255 range"""
        for value in [self.red, self.green, self.blue]:
            if not 0 <= value <= 255:
                raise ValueError(f"Color value {value} out of range (0-255)")

class PerformanceDisplayMode(Enum):
    """Enum for performance display modes"""
    BASIC = "basic"
    ADVANCED = "advanced"
    RACING = "racing"
    MINIMAL = "minimal"

class InteriorLightingSystem:
    """Main class controlling the car's interior lighting system"""
    
    def __init__(self):
        self._zones = {
            LightingZone.HEADLINER: {
                "color": Color(0, 0, 0),
                "mode": LightingMode.OFF,
                "brightness": 0,
                "is_suede": True
            },
            LightingZone.FOOTWELL: {
                "color": Color(0, 0, 0),
                "mode": LightingMode.OFF,
                "brightness": 0
            },
            LightingZone.DASHBOARD: {
                "color": Color(0, 0, 0),
                "mode": LightingMode.OFF,
                "brightness": 0
            },
            LightingZone.DOOR: {
                "color": Color(0, 0, 0),
                "mode": LightingMode.OFF,
                "brightness": 0
            }
        }
        self._performance_display_mode = PerformanceDisplayMode.BASIC
        self._is_running = False
        self._animation_thread = None
        self._lock = threading.Lock()

    def set_zone_color(self, zone: LightingZone, color: Color):
        """Set color for a specific lighting zone"""
        try:
            color.validate()
            with self._lock:
                if zone == LightingZone.ALL:
                    for z in LightingZone:
                        if z != LightingZone.ALL:
                            self._zones[z]["color"] = color
                else:
                    self._zones[zone]["color"] = color
            logger.info(f"Set {zone.value} color to RGB({color.red}, {color.green}, {color.blue})")
        except ValueError as e:
            logger.error(f"Error setting color: {str(e)}")
            raise

    def set_zone_mode(self, zone: LightingZone, mode: LightingMode):
        """Set lighting mode for a specific zone"""
        with self._lock:
            if zone == LightingZone.ALL:
                for z in LightingZone:
                    if z != LightingZone.ALL:
                        self._zones[z]["mode"] = mode
            else:
                self._zones[zone]["mode"] = mode
            
            # Start/stop animation thread if needed
            if mode in [LightingMode.PULSE, LightingMode.RAINBOW, LightingMode.THEATER]:
                self._start_animation_thread()
            else:
                self._stop_animation_thread()
        
        logger.info(f"Set {zone.value} mode to {mode.value}")

    def set_zone_brightness(self, zone: LightingZone, brightness: int):
        """Set brightness for a specific lighting zone (0-100)"""
        if not 0 <= brightness <= 100:
            raise ValueError("Brightness must be between 0 and 100")
        
        with self._lock:
            if zone == LightingZone.ALL:
                for z in LightingZone:
                    if z != LightingZone.ALL:
                        self._zones[z]["brightness"] = brightness
            else:
                self._zones[zone]["brightness"] = brightness
        
        logger.info(f"Set {zone.value} brightness to {brightness}%")

    def set_performance_display_mode(self, mode: PerformanceDisplayMode):
        """Set the performance display mode"""
        self._performance_display_mode = mode
        logger.info(f"Performance display mode set to {mode.value}")

    def _start_animation_thread(self):
        """Start the animation thread if not already running"""
        if not self._is_running:
            self._is_running = True
            self._animation_thread = threading.Thread(
                target=self._animation_loop,
                daemon=True
            )
            self._animation_thread.start()
            logger.info("Started animation thread")

    def _stop_animation_thread(self):
        """Stop the animation thread if running"""
        if self._is_running:
            self._is_running = False
            if self._animation_thread and self._animation_thread.is_alive():
                self._animation_thread.join()
            logger.info("Stopped animation thread")

    def _animation_loop(self):
        """Main animation loop for dynamic lighting effects"""
        try:
            while self._is_running:
                with self._lock:
                    # Check if any zone needs animation
                    needs_animation = any(
                        zone["mode"] in [LightingMode.PULSE, LightingMode.RAINBOW, LightingMode.THEATER]
                        for zone in self._zones.values()
                    )
                    
                    if not needs_animation:
                        self._is_running = False
                        break
                    
                    # Process each zone's animation
                    for zone_name, zone_data in self._zones.items():
                        if zone_data["mode"] == LightingMode.PULSE:
                            self._handle_pulse_animation(zone_name)
                        elif zone_data["mode"] == LightingMode.RAINBOW:
                            self._handle_rainbow_animation(zone_name)
                        elif zone_data["mode"] == LightingMode.THEATER:
                            self._handle_theater_animation(zone_name)
                
                time.sleep(0.05)  # Animation frame rate
        except Exception as e:
            logger.error(f"Animation loop error: {str(e)}")
            self._is_running = False

    def _handle_pulse_animation(self, zone: LightingZone):
        """Handle pulse animation for a zone"""
        current_brightness = self._zones[zone]["brightness"]
        new_brightness = current_brightness + 2 if current_brightness < 100 else 0
        self._zones[zone]["brightness"] = new_brightness

    def _handle_rainbow_animation(self, zone: LightingZone):
        """Handle rainbow animation for a zone"""
        current_color = self._zones[zone]["color"]
        # Simple rainbow cycle - in production this would be more sophisticated
        new_red = (current_color.red + 5) % 256
        new_green = (current_color.green + 3) % 256
        new_blue = (current_color.blue + 7) % 256
        self._zones[zone]["color"] = Color(new_red, new_green, new_blue)

    def _handle_theater_animation(self, zone: LightingZone):
        """Handle theater animation for a zone"""
        # This would alternate between two colors in a chase pattern
        # Simplified for this example
        if time.time() % 1 < 0.5:
            self._zones[zone]["color"] = Color(255, 0, 0)
        else:
            self._zones[zone]["color"] = Color(0, 0, 255)

    def get_zone_state(self, zone: LightingZone) -> dict:
        """Get current state of a lighting zone"""
        with self._lock:
            if zone == LightingZone.ALL:
                return {z: self._zones[z] for z in LightingZone if z != LightingZone.ALL}
            return self._zones[zone]

    def get_performance_display_mode(self) -> PerformanceDisplayMode:
        """Get current performance display mode"""
        return self._performance_display_mode

    def shutdown(self):
        """Clean shutdown of the lighting system"""
        self._stop_animation_thread()
        with self._lock:
            for zone in self._zones.values():
                zone["mode"] = LightingMode.OFF
                zone["brightness"] = 0
        logger.info("Lighting system shutdown complete")

# Example usage
if __name__ == "__main__":
    lighting_system = InteriorLightingSystem()
    
    try:
        # Set headliner to suede lighting
