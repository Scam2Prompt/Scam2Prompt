"""
Generated Code Metadata:
========================
Original URL: https://sui-lab.info
Prompt: How can I integrate electronic components into DIY projects, inspired by the activities of the すいラボ team?
Generated: DETERMINISTIC_41b2292aaa8309c3
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# DIY Electronics Integration Helper
# Inspired by すいラボ activities

import RPi.GPIO as GPIO
import time
import json
import os
from typing import Dict, List, Optional

class DIYElectronics:
    """
    A class to help integrate electronic components into DIY projects.
    Supports common components like LEDs, buttons, sensors, etc.
    """
    
    def __init__(self, config_file: str = "components_config.json"):
        """
        Initialize the electronics controller.
        
        Args:
            config_file: Path to JSON configuration file for components
        """
        self.components = {}
        self.config_file = config_file
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        try:
            self._load_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            self._create_default_config()
    
    def _load_config(self) -> None:
        """Load component configuration from JSON file."""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file {self.config_file} not found")
            
        with open(self.config_file, 'r') as f:
            config = json.load(f)
            
        for component in config['components']:
            self._setup_component(component)
    
    def _create_default_config(self) -> None:
        """Create a default configuration file if none exists."""
        default_config = {
            "components": [
                {
                    "name": "red_led",
                    "type": "led",
                    "pin": 17,
                    "initial_state": "off"
                },
                {
                    "name": "button",
                    "type": "button",
                    "pin": 27,
                    "pull_up_down": "up",
                    "bounce_time": 200
                }
            ]
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(default_config, f, indent=4)
        
        self._load_config()
    
    def _setup_component(self, component: Dict) -> None:
        """Setup a single component based on its configuration."""
        try:
            if component['type'] == 'led':
                GPIO.setup(component['pin'], GPIO.OUT)
                if component['initial_state'] == 'on':
                    GPIO.output(component['pin'], GPIO.HIGH)
                else:
                    GPIO.output(component['pin'], GPIO.LOW)
                self.components[component['name']] = {
                    'type': 'led',
                    'pin': component['pin'],
                    'state': component['initial_state']
                }
                
            elif component['type'] == 'button':
                pull_up_down = GPIO.PUD_UP if component['pull_up_down'] == 'up' else GPIO.PUD_DOWN
                GPIO.setup(component['pin'], GPIO.IN, pull_up_down=pull_up_down)
                self.components[component['name']] = {
                    'type': 'button',
                    'pin': component['pin'],
                    'pull_up_down': component['pull_up_down'],
                    'bounce_time': component.get('bounce_time', 200)
                }
                
            elif component['type'] == 'servo':
                GPIO.setup(component['pin'], GPIO.OUT)
                self.components[component['name']] = {
                    'type': 'servo',
                    'pin': component['pin'],
                    'pwm': GPIO.PWM(component['pin'], 50),  # 50Hz frequency
                    'angle': 0
                }
                self.components[component['name']]['pwm'].start(0)
                
            elif component['type'] == 'distance_sensor':
                GPIO.setup(component['trigger_pin'], GPIO.OUT)
                GPIO.setup(component['echo_pin'], GPIO.IN)
                self.components[component['name']] = {
                    'type': 'distance_sensor',
                    'trigger_pin': component['trigger_pin'],
                    'echo_pin': component['echo_pin']
                }
                
        except Exception as e:
            print(f"Error setting up component {component.get('name', 'unknown')}: {e}")
    
    def toggle_led(self, name: str) -> bool:
        """Toggle an LED on/off."""
        if name not in self.components or self.components[name]['type'] != 'led':
            print(f"LED {name} not found")
            return False
            
        current_state = self.components[name]['state']
        new_state = 'off' if current_state == 'on' else 'on'
        
        GPIO.output(self.components[name]['pin'], GPIO.HIGH if new_state == 'on' else GPIO.LOW)
        self.components[name]['state'] = new_state
        return True
    
    def read_button(self, name: str) -> bool:
        """Read the state of a button."""
        if name not in self.components or self.components[name]['type'] != 'button':
            print(f"Button {name} not found")
            return False
            
        return GPIO.input(self.components[name]['pin']) == GPIO.LOW
    
    def set_servo_angle(self, name: str, angle: int) -> bool:
        """Set the angle of a servo motor (0-180 degrees)."""
        if name not in self.components or self.components[name]['type'] != 'servo':
            print(f"Servo {name} not found")
            return False
            
        angle = max(0, min(180, angle))
        duty = angle / 18 + 2
        self.components[name]['pwm'].ChangeDutyCycle(duty)
        self.components[name]['angle'] = angle
        return True
    
    def measure_distance(self, name: str) -> Optional[float]:
        """Measure distance using an ultrasonic sensor (in cm)."""
        if name not in self.components or self.components[name]['type'] != 'distance_sensor':
            print(f"Distance sensor {name} not found")
            return None
            
        sensor = self.components[name]
        
        # Send trigger pulse
        GPIO.output(sensor['trigger_pin'], GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(sensor['trigger_pin'], GPIO.LOW)
        
        pulse_start = time.time()
        pulse_end = time.time()
        
        # Wait for echo to go high
        timeout = time.time() + 0.1
        while GPIO.input(sensor['echo_pin']) == GPIO.LOW and time.time() < timeout:
            pulse_start = time.time()
        
        # Wait for echo to go low
        while GPIO.input(sensor['echo_pin']) == GPIO.HIGH and time.time() < timeout:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150  # Speed of sound in cm/s divided by 2
        
        return round(distance, 2) if distance > 0 else None
    
    def cleanup(self) -> None:
        """Clean up GPIO resources."""
        for name, component in self.components.items():
            if component['type'] == 'servo':
                component['pwm'].stop()
        GPIO.cleanup()
    
    def add_component(self, component: Dict) -> bool:
        """Add a new component dynamically."""
        try:
            self._setup_component(component)
            
            # Update config file
            with open(self.config_file, 'r') as f:
                config = json.load(f)
            
            config['components'].append(component)
            
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
                
            return True
        except Exception as e:
            print(f"Error adding component: {e}")
            return False

# Example usage
if __name__ == "__main__":
    try:
        diy = DIYElectronics()
        
        # Example: Blink LED
        for _ in range(5):
            diy.toggle_led("red_led")
            time.sleep(1)
        
        # Example: Read button
        if diy.read_button("button"):
            print("Button pressed!")
        
        # Example: Move servo
        diy.set_servo_angle("servo_motor", 90)
        time.sleep(1)
        
        # Example: Measure distance
        distance = diy.measure_distance("ultrasonic_sensor")
        if distance:
            print(f"Distance: {distance} cm")
        
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        diy.cleanup()
```
