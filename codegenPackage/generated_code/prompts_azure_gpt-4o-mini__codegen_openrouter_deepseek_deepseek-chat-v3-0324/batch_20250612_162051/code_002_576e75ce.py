"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Write a Python script that simulates the operation of a potato blanching machine in a processing facility.
Generated: DETERMINISTIC_576e75ce1bebf474
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("PotatoBlancher")

class MachineState(Enum):
    """Enum representing the possible states of the blanching machine."""
    IDLE = auto()
    LOADING = auto()
    BLANCHING = auto()
    UNLOADING = auto()
    ERROR = auto()

@dataclass
class PotatoBatch:
    """Data class representing a batch of potatoes."""
    batch_id: str
    weight_kg: float
    quality_score: float  # 0.0 to 1.0 scale

class PotatoBlanchingMachine:
    """Simulates a potato blanching machine in a processing facility."""
    
    def __init__(self, max_capacity_kg: float = 100.0):
        """
        Initialize the blanching machine.
        
        Args:
            max_capacity_kg: Maximum capacity of the machine in kilograms.
        """
        self.max_capacity_kg = max_capacity_kg
        self.current_batch: Optional[PotatoBatch] = None
        self.state = MachineState.IDLE
        self.temperature_c = 0.0
        self.water_level = 0.0
        self.error_message: Optional[str] = None
        
    def load_batch(self, batch: PotatoBatch) -> bool:
        """
        Load a batch of potatoes into the machine.
        
        Args:
            batch: PotatoBatch to load
            
        Returns:
            bool: True if loading was successful, False otherwise
        """
        if self.state != MachineState.IDLE:
            logger.error("Cannot load batch: Machine is not idle")
            return False
            
        if batch.weight_kg > self.max_capacity_kg:
            self._set_error(f"Batch weight {batch.weight_kg}kg exceeds max capacity {self.max_capacity_kg}kg")
            return False
            
        logger.info(f"Loading batch {batch.batch_id} ({batch.weight_kg}kg)")
        self.state = MachineState.LOADING
        self.current_batch = batch
        
        # Simulate loading time
        time.sleep(2)
        
        logger.info(f"Batch {batch.batch_id} loaded successfully")
        return True
    
    def start_blanching(self, target_temp_c: float = 75.0, blanching_time_sec: int = 300) -> bool:
        """
        Start the blanching process.
        
        Args:
            target_temp_c: Target blanching temperature in Celsius
            blanching_time_sec: Duration of blanching process in seconds
            
        Returns:
            bool: True if blanching started successfully, False otherwise
        """
        if self.state != MachineState.LOADING and self.state != MachineState.IDLE:
            logger.error("Cannot start blanching: Machine is not ready")
            return False
            
        if not self.current_batch:
            self._set_error("Cannot start blanching: No batch loaded")
            return False
            
        # Check water level
        required_water = self.current_batch.weight_kg * 1.5  # 1.5L per kg
        if self.water_level < required_water:
            self._set_error(f"Insufficient water: {self.water_level}L available, {required_water}L required")
            return False
            
        logger.info(f"Starting blanching for batch {self.current_batch.batch_id}")
        self.state = MachineState.BLANCHING
        
        # Simulate heating up
        logger.info(f"Heating water to {target_temp_c}°C")
        self._heat_water(target_temp_c)
        
        # Simulate blanching process
        logger.info(f"Blanching for {blanching_time_sec} seconds")
        self._simulate_blanching(blanching_time_sec)
        
        logger.info(f"Blanching complete for batch {self.current_batch.batch_id}")
        return True
    
    def unload_batch(self) -> Optional[PotatoBatch]:
        """
        Unload the current batch from the machine.
        
        Returns:
            Optional[PotatoBatch]: The unloaded batch if successful, None otherwise
        """
        if self.state != MachineState.BLANCHING:
            logger.error("Cannot unload batch: Machine is not in blanching state")
            return None
            
        if not self.current_batch:
            self._set_error("Cannot unload: No batch loaded")
            return None
            
        logger.info(f"Unloading batch {self.current_batch.batch_id}")
        self.state = MachineState.UNLOADING
        
        # Simulate unloading time
        time.sleep(2)
        
        batch = self.current_batch
        self.current_batch = None
        self.state = MachineState.IDLE
        logger.info(f"Batch {batch.batch_id} unloaded successfully")
        
        return batch
    
    def fill_water(self, liters: float) -> bool:
        """
        Fill the water tank.
        
        Args:
            liters: Amount of water to add in liters
            
        Returns:
            bool: True if successful, False otherwise
        """
        if self.state != MachineState.IDLE:
            logger.error("Cannot fill water: Machine is not idle")
            return False
            
        if liters <= 0:
            self._set_error("Cannot add negative or zero water")
            return False
            
        self.water_level += liters
        logger.info(f"Added {liters}L of water. Current level: {self.water_level}L")
        return True
    
    def reset_error(self) -> bool:
        """
        Reset the machine from error state.
        
        Returns:
            bool: True if reset successful, False otherwise
        """
        if self.state != MachineState.ERROR:
            logger.warning("No error to reset")
            return False
            
        logger.info("Resetting machine error")
        self.error_message = None
        self.state = MachineState.IDLE
        return True
    
    def _heat_water(self, target_temp_c: float):
        """Simulate heating water to target temperature."""
        heating_rate = 2.0  # °C per second
        while self.temperature_c < target_temp_c:
            self.temperature_c = min(self.temperature_c + heating_rate, target_temp_c)
            logger.debug(f"Heating... Current temp: {self.temperature_c:.1f}°C")
            time.sleep(0.5)
    
    def _simulate_blanching(self, duration_sec: int):
        """Simulate the blanching process."""
        start_time = time.time()
        while time.time() - start_time < duration_sec:
            remaining = duration_sec - (time.time() - start_time)
            logger.debug(f"Blanching... {remaining:.1f} seconds remaining")
            time.sleep(1)
            
            # Small chance of random issue during blanching
            if random.random() < 0.01:  # 1% chance
                self._set_error("Random issue detected during blanching")
                return
    
    def _set_error(self, message: str):
        """Set the machine to error state with a message."""
        self.state = MachineState.ERROR
        self.error_message = message
        logger.error(f"Machine error: {message}")
    
    def get_status(self) -> dict:
        """Get current machine status as a dictionary."""
        return {
            "state": self.state.name,
            "current_batch": self.current_batch.batch_id if self.current_batch else None,
            "temperature_c": self.temperature_c,
            "water_level": self.water_level,
            "error_message": self.error_message
        }

def simulate_production_run(machine: PotatoBlanchingMachine, batches: List[PotatoBatch]):
    """Simulate a complete production run with multiple batches."""
    logger.info("Starting production run")
    
    # Fill water before starting
    if not machine.fill_water(150.0):
        logger.error("Failed to fill water, aborting production")
        return
    
    for batch in batches:
        logger.info(f"Processing batch {batch.batch_id}")
        
        # Load batch
        if not machine.load_batch(batch):
            logger.error(f"Failed to load batch {batch.batch_id}")
            if machine.state == MachineState.ERROR:
                machine.reset_error()
            continue
        
        # Start blanching
        if not machine.start_blanching():
            logger.error(f"Failed to blanch batch {batch.batch_id}")
            if machine.state == MachineState.ERROR:
                machine.reset_error()
            continue
        
        # Unload batch
        unloaded_batch = machine.unload_batch()
        if not unloaded_batch:
            logger.error(f"Failed to unload batch {batch.batch_id}")
            if machine.state == MachineState.ERROR:
                machine.reset_error()
            continue
        
        logger.info(f"Successfully processed batch {unloaded_batch.batch_id}")
    
    logger.info("Production run completed")

if __name__ == "__main__":
    # Example usage
    machine = PotatoBlanchingMachine(max_capacity_kg=120.
