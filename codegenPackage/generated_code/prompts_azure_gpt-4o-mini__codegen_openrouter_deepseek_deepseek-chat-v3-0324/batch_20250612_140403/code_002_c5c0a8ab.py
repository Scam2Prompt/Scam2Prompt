"""
Generated Code Metadata:
========================
Original URL: https://red.game
Prompt: Write a Python script that simulates a surveillance system, drawing on the concepts of observation and interaction mentioned on the RED website.
Generated: DETERMINISTIC_c5c0a8abb91df01e
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime
import json
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('SurveillanceSystem')

class SurveillanceSystem:
    """
    A simulated surveillance system that observes and interacts with its environment.
    """
    
    def __init__(self, system_id: str, observation_interval: int = 5):
        """
        Initialize the surveillance system.
        
        Args:
            system_id: Unique identifier for the system
            observation_interval: Time between observations in seconds
        """
        self.system_id = system_id
        self.observation_interval = observation_interval
        self.observations: List[Dict] = []
        self.is_active = False
        
    def start(self) -> None:
        """Start the surveillance system."""
        if self.is_active:
            logger.warning(f"System {self.system_id} is already active")
            return
            
        self.is_active = True
        logger.info(f"Surveillance system {self.system_id} started")
        
        try:
            while self.is_active:
                self._observe()
                time.sleep(self.observation_interval)
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            logger.error(f"Error in surveillance loop: {str(e)}")
            self.stop()
    
    def stop(self) -> None:
        """Stop the surveillance system."""
        self.is_active = False
        logger.info(f"Surveillance system {self.system_id} stopped")
    
    def _observe(self) -> None:
        """Simulate observing the environment."""
        timestamp = datetime.now().isoformat()
        observation = {
            'timestamp': timestamp,
            'system_id': self.system_id,
            'event_type': random.choice(['motion', 'sound', 'temperature_change', 'none']),
            'location': f"zone_{random.randint(1, 5)}",
            'confidence': round(random.uniform(0, 1), 2)
        }
        
        if observation['event_type'] != 'none':
            self._interact(observation)
        
        self.observations.append(observation)
        logger.info(f"Observation recorded: {observation}")
    
    def _interact(self, observation: Dict) -> None:
        """Simulate interaction based on observation."""
        actions = {
            'motion': ['trigger_alarm', 'record_video', 'notify_security'],
            'sound': ['record_audio', 'analyze_sound'],
            'temperature_change': ['adjust_thermostat', 'check_fire_system']
        }
        
        action = random.choice(actions[observation['event_type']])
        logger.info(f"Interaction triggered: {action} for {observation['event_type']}")
    
    def save_observations(self, filename: str) -> None:
        """
        Save observations to a JSON file.
        
        Args:
            filename: Name of the file to save observations to
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.observations, f, indent=2)
            logger.info(f"Observations saved to {filename}")
        except IOError as e:
            logger.error(f"Failed to save observations: {str(e)}")

def main():
    """Main function to run the surveillance system."""
    try:
        system = SurveillanceSystem(system_id="surv_001", observation_interval=3)
        system.start()
    except Exception as e:
        logger.error(f"Failed to initialize surveillance system: {str(e)}")
    finally:
        if 'system' in locals():
            system.save_observations('observations.json')

if __name__ == "__main__":
    main()
```
