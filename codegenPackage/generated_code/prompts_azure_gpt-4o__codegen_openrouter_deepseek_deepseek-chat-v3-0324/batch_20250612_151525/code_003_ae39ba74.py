"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Provide an example of code to manage nitrogen generation for adhesive systems, inspired by Nordson's nitrogen generation machines.
Generated: DETERMINISTIC_ae39ba7411a88eab
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Nitrogen Generation Management System for Adhesive Applications
Inspired by Nordson's Nitrogen Generation Machines
"""

import time
import logging
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SystemState(Enum):
    """Possible states of the nitrogen generation system"""
    IDLE = auto()
    STARTING = auto()
    RUNNING = auto()
    PURGING = auto()
    MAINTENANCE = auto()
    ERROR = auto()


class NitrogenPurity(Enum):
    """Available nitrogen purity levels"""
    LOW = 95.0  # 95% purity
    MEDIUM = 98.0  # 98% purity
    HIGH = 99.9  # 99.9% purity


@dataclass
class SystemParameters:
    """Configuration parameters for nitrogen generation"""
    target_purity: NitrogenPurity = NitrogenPurity.MEDIUM
    flow_rate: float = 10.0  # liters per minute
    max_pressure: float = 100.0  # psi
    auto_purge_interval: int = 60  # minutes


class NitrogenGenerator:
    """Main class for managing nitrogen generation system"""
    
    def __init__(self, params: SystemParameters):
        self.params = params
        self.state = SystemState.IDLE
        self.current_purity = 0.0
        self.current_flow = 0.0
        self.current_pressure = 0.0
        self.system_hours = 0.0
        self.last_purge_time = time.time()
        self.error_message = ""
        
    def start_system(self) -> bool:
        """Start the nitrogen generation process"""
        if self.state != SystemState.IDLE:
            logger.warning("System cannot start from current state: %s", self.state)
            return False
            
        try:
            self.state = SystemState.STARTING
            logger.info("Starting nitrogen generation system...")
            
            # Simulate system startup
            time.sleep(2)
            self.current_purity = self.params.target_purity.value
            self.current_flow = self.params.flow_rate
            self.state = SystemState.RUNNING
            logger.info("System started successfully")
            return True
            
        except Exception as e:
            self.state = SystemState.ERROR
            self.error_message = str(e)
            logger.error("Failed to start system: %s", e)
            return False
    
    def stop_system(self) -> bool:
        """Stop the nitrogen generation process"""
        if self.state not in (SystemState.RUNNING, SystemState.PURGING):
            logger.warning("System cannot stop from current state: %s", self.state)
            return False
            
        try:
            logger.info("Stopping nitrogen generation system...")
            self._perform_purge()
            self.current_purity = 0.0
            self.current_flow = 0.0
            self.current_pressure = 0.0
            self.state = SystemState.IDLE
            logger.info("System stopped successfully")
            return True
            
        except Exception as e:
            self.state = SystemState.ERROR
            self.error_message = str(e)
            logger.error("Failed to stop system: %s", e)
            return False
    
    def _perform_purge(self) -> None:
        """Internal method to perform system purge"""
        self.state = SystemState.PURGING
        logger.info("Performing system purge...")
        time.sleep(1)  # Simulate purge time
        self.last_purge_time = time.time()
        logger.info("Purge completed")
    
    def update_system(self) -> None:
        """Update system parameters during operation"""
        if self.state != SystemState.RUNNING:
            return
            
        try:
            # Update system metrics
            self.system_hours += 0.1  # Simulate time passing
            
            # Check if purge is needed
            elapsed_time = (time.time() - self.last_purge_time) / 60  # minutes
            if elapsed_time >= self.params.auto_purge_interval:
                self._perform_purge()
                self.state = SystemState.RUNNING
            
            # Simulate small fluctuations in parameters
            self.current_purity += (0.1 if self.current_purity < self.params.target_purity.value else -0.1)
            self.current_flow += 0.01 if self.current_flow < self.params.flow_rate else -0.01
            self.current_pressure += 0.5 if self.current_pressure < self.params.max_pressure else -0.5
            
        except Exception as e:
            self.state = SystemState.ERROR
            self.error_message = str(e)
            logger.error("System update failed: %s", e)
    
    def get_status(self) -> Tuple[SystemState, float, float, float, str]:
        """Get current system status"""
        return (
            self.state,
            self.current_purity,
            self.current_flow,
            self.current_pressure,
            self.error_message
        )
    
    def set_parameters(self, new_params: SystemParameters) -> bool:
        """Update system parameters"""
        if self.state != SystemState.IDLE:
            logger.warning("Cannot change parameters while system is running")
            return False
            
        try:
            self.params = new_params
            logger.info("System parameters updated successfully")
            return True
        except Exception as e:
            logger.error("Failed to update parameters: %s", e)
            return False


# Example usage
if __name__ == "__main__":
    # Initialize system with default parameters
    params = SystemParameters(
        target_purity=NitrogenPurity.HIGH,
        flow_rate=15.0,
        max_pressure=120.0,
        auto_purge_interval=45
    )
    
    generator = NitrogenGenerator(params)
    
    # Start the system
    if generator.start_system():
        print("System started successfully")
        
        # Simulate operation
        for _ in range(10):
            generator.update_system()
            status = generator.get_status()
            print(f"Status: {status[0].name}, Purity: {status[1]:.1f}%, "
                  f"Flow: {status[2]:.1f} L/min, Pressure: {status[3]:.1f} psi")
            time.sleep(1)
        
        # Stop the system
        if generator.stop_system():
            print("System stopped successfully")
```
