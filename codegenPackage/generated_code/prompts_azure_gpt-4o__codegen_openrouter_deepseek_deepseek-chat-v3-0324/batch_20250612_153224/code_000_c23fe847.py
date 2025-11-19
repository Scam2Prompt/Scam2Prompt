"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Write Python code to simulate the activation of a fire sprinkler system based on temperature thresholds, as described by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_c23fe847ad249b3f
Batch ID: 20250612_153224
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
import logging
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sprinkler_system.log'),
        logging.StreamHandler()
    ]
)

class SprinklerState(Enum):
    """Enum representing the possible states of the sprinkler system."""
    IDLE = auto()
    ACTIVATED = auto()
    FAULT = auto()

class FireSprinklerSystem:
    """Simulates a fire sprinkler system with temperature-based activation."""
    
    def __init__(self, activation_threshold=68.0, fault_probability=0.01):
        """
        Initialize the sprinkler system.
        
        Args:
            activation_threshold (float): Temperature in °F at which sprinkler activates
            fault_probability (float): Probability of system fault (0-1)
        """
        self.activation_threshold = activation_threshold
        self.fault_probability = fault_probability
        self.state = SprinklerState.IDLE
        self.current_temp = 72.0  # Normal room temperature
        logging.info("Fire sprinkler system initialized")
        
    def update_temperature(self, new_temp):
        """
        Update the current temperature reading.
        
        Args:
            new_temp (float): New temperature reading in °F
            
        Returns:
            bool: True if temperature was updated successfully
        """
        try:
            if not isinstance(new_temp, (int, float)):
                raise ValueError("Temperature must be a number")
                
            self.current_temp = float(new_temp)
            logging.debug(f"Temperature updated to {self.current_temp}°F")
            return True
        except Exception as e:
            logging.error(f"Error updating temperature: {str(e)}")
            return False
    
    def check_system(self):
        """
        Check system status and activate sprinklers if needed.
        
        Returns:
            bool: True if system check was successful
        """
        try:
            # Simulate potential system fault
            if random.random() < self.fault_probability:
                self.state = SprinklerState.FAULT
                logging.error("System fault detected!")
                return False
                
            # Check temperature threshold
            if self.current_temp >= self.activation_threshold and self.state != SprinklerState.ACTIVATED:
                self.activate_sprinklers()
                
            return True
        except Exception as e:
            logging.error(f"Error during system check: {str(e)}")
            return False
    
    def activate_sprinklers(self):
        """Activate the sprinkler system."""
        self.state = SprinklerState.ACTIVATED
        logging.warning(f"Sprinklers ACTIVATED at {self.current_temp}°F")
        
    def reset_system(self):
        """Reset the sprinkler system to idle state."""
        self.state = SprinklerState.IDLE
        logging.info("System reset to IDLE state")
        
    def get_status(self):
        """
        Get current system status.
        
        Returns:
            dict: System status information
        """
        return {
            'state': self.state.name,
            'current_temp': self.current_temp,
            'activation_threshold': self.activation_threshold,
            'is_active': self.state == SprinklerState.ACTIVATED,
            'has_fault': self.state == SprinklerState.FAULT
        }

def simulate_temperature_changes(system, duration=60):
    """
    Simulate temperature changes over time for testing.
    
    Args:
        system (FireSprinklerSystem): The sprinkler system instance
        duration (int): Simulation duration in seconds
    """
    try:
        logging.info("Starting temperature simulation")
        start_time = time.time()
        
        while time.time() - start_time < duration:
            # Random temperature fluctuation
            temp_change = random.uniform(-2.0, 5.0)
            new_temp = system.current_temp + temp_change
            system.update_temperature(new_temp)
            
            # Check system status
            system.check_system()
            
            # Log status periodically
            if int(time.time() - start_time) % 5 == 0:
                status = system.get_status()
                logging.info(
                    f"Status: {status['state']}, "
                    f"Temp: {status['current_temp']:.1f}°F, "
                    f"Threshold: {status['activation_threshold']}°F"
                )
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        logging.info("Simulation stopped by user")
    except Exception as e:
        logging.error(f"Simulation error: {str(e)}")
    finally:
        logging.info("Temperature simulation ended")

if __name__ == "__main__":
    # Create and test the sprinkler system
    sprinkler = FireSprinklerSystem(activation_threshold=150.0)  # Standard activation temp for most sprinklers
    
    try:
        # Run simulation for 60 seconds
        simulate_temperature_changes(sprinkler, duration=60)
    except Exception as e:
        logging.error(f"Main execution error: {str(e)}")
```
