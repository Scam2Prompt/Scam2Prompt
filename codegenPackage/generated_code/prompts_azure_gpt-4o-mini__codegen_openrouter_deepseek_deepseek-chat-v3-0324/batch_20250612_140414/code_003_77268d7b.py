"""
Generated Code Metadata:
========================
Original URL: https://trialsonicsolutions.com
Prompt: Describe the process of ultrasonic cleaning and how it can be applied to plastic and polymer extrusion filters.
Generated: DETERMINISTIC_77268d7b972f0742
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the process of ultrasonic cleaning and its application 
to plastic and polymer extrusion filters through a simulation.
"""

import time
from enum import Enum, auto

class CleaningStage(Enum):
    """Enum representing different stages of the ultrasonic cleaning process."""
    PRE_RINSE = auto()
    ULTRASONIC_CLEANING = auto()
    POST_RINSE = auto()
    DRYING = auto()

class UltrasonicCleaner:
    """
    A class to simulate an ultrasonic cleaning process for plastic/polymer extrusion filters.
    """
    
    def __init__(self, frequency_khz: float = 40.0, temperature_c: float = 50.0):
        """
        Initialize the ultrasonic cleaner with default frequency and temperature.
        
        Args:
            frequency_khz: Ultrasonic frequency in kHz (default 40 kHz)
            temperature_c: Cleaning solution temperature in Celsius (default 50°C)
        """
        self.frequency = frequency_khz
        self.temperature = temperature_c
        self.current_stage = None
        self.cleaning_time = 0
        
    def _validate_filter(self, filter_material: str) -> bool:
        """
        Validate if the filter material is suitable for ultrasonic cleaning.
        
        Args:
            filter_material: The material of the filter to be cleaned
            
        Returns:
            bool: True if material is suitable, False otherwise
            
        Raises:
            ValueError: If material is not suitable for ultrasonic cleaning
        """
        suitable_materials = ['polypropylene', 'polyethylene', 'nylon', 'PTFE', 'PVDF']
        if filter_material.lower() not in suitable_materials:
            raise ValueError(f"Material {filter_material} not suitable for ultrasonic cleaning")
        return True
    
    def _log_stage(self, stage: CleaningStage, duration: int):
        """
        Log the current cleaning stage and its duration.
        
        Args:
            stage: The current cleaning stage
            duration: Duration of the stage in seconds
        """
        self.current_stage = stage
        print(f"Stage: {stage.name.replace('_', ' ').title()} - {duration} seconds")
        
    def pre_rinse(self, duration: int = 120):
        """Simulate the pre-rinse stage to remove large particles."""
        self._log_stage(CleaningStage.PRE_RINSE, duration)
        time.sleep(1)  # Simulate time passing
        self.cleaning_time += duration
        
    def ultrasonic_clean(self, duration: int = 300):
        """
        Simulate the main ultrasonic cleaning stage.
        
        Args:
            duration: Cleaning duration in seconds (default 5 minutes)
        """
        self._log_stage(CleaningStage.ULTRASONIC_CLEANING, duration)
        print(f"Applying ultrasonic waves at {self.frequency} kHz")
        print(f"Maintaining solution at {self.temperature}°C")
        time.sleep(1)  # Simulate time passing
        self.cleaning_time += duration
        
    def post_rinse(self, duration: int = 120):
        """Simulate the post-rinse stage to remove cleaning solution residues."""
        self._log_stage(CleaningStage.POST_RINSE, duration)
        time.sleep(1)  # Simulate time passing
        self.cleaning_time += duration
        
    def dry(self, duration: int = 180):
        """Simulate the drying stage."""
        self._log_stage(CleaningStage.DRYING, duration)
        time.sleep(1)  # Simulate time passing
        self.cleaning_time += duration
        
    def clean_filter(self, filter_material: str):
        """
        Execute the complete cleaning cycle for a plastic/polymer extrusion filter.
        
        Args:
            filter_material: The material of the filter to be cleaned
            
        Returns:
            int: Total cleaning time in seconds
        """
        try:
            self._validate_filter(filter_material)
            print(f"\nStarting ultrasonic cleaning for {filter_material} filter")
            
            self.pre_rinse()
            self.ultrasonic_clean()
            self.post_rinse()
            self.dry()
            
            print(f"\nCleaning complete. Total time: {self.cleaning_time} seconds")
            return self.cleaning_time
            
        except ValueError as e:
            print(f"Error: {e}")
            return 0

# Example usage
if __name__ == "__main__":
    cleaner = UltrasonicCleaner(frequency_khz=40.0, temperature_c=45.0)
    cleaner.clean_filter("polypropylene")
```
