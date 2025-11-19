"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a program to simulate the ultrasonic cleaning process for marine fuel injectors, referencing the specific services for marine vehicles offered by Fuel Injector Services.
Generated: DETERMINISTIC_66d78e2ddc9dd49b
Batch ID: 20250612_151611
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

class CleaningStatus(Enum):
    """Enum representing the status of the cleaning process."""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    FAILED = auto()

class UltrasonicCleaner:
    """Simulates an ultrasonic cleaning machine for marine fuel injectors."""
    
    def __init__(self, model: str = "FIS-MarinePro-3000"):
        """Initialize the ultrasonic cleaner with default settings."""
        self.model = model
        self.status = CleaningStatus.NOT_STARTED
        self.cleaning_time = 0
        self.temperature = 0
        self.solution_level = 0
        
    def _check_ready(self) -> bool:
        """Check if the cleaner is ready to start."""
        if self.status != CleaningStatus.NOT_STARTED:
            print("Error: Cleaning already in progress or completed.")
            return False
        if self.solution_level < 50:
            print("Error: Cleaning solution level too low.")
            return False
        return True
    
    def load_injectors(self, count: int) -> bool:
        """Simulate loading fuel injectors into the cleaner."""
        if count <= 0 or count > 8:
            print("Error: Invalid number of injectors (1-8 allowed).")
            return False
        print(f"Loaded {count} marine fuel injectors into {self.model}.")
        return True
    
    def fill_solution(self, level: int) -> bool:
        """Fill the cleaning solution to specified level (0-100%)."""
        if level < 0 or level > 100:
            print("Error: Solution level must be between 0-100%.")
            return False
        self.solution_level = level
        print(f"Cleaning solution filled to {level}%.")
        return True
    
    def set_parameters(self, time_min: int, temp_c: int) -> bool:
        """Set cleaning time and temperature."""
        if time_min < 5 or time_min > 30:
            print("Error: Cleaning time must be 5-30 minutes.")
            return False
        if temp_c < 40 or temp_c > 80:
            print("Error: Temperature must be 40-80°C.")
            return False
        self.cleaning_time = time_min
        self.temperature = temp_c
        print(f"Parameters set: {time_min} minutes at {temp_c}°C.")
        return True
    
    def start_cleaning(self) -> bool:
        """Start the ultrasonic cleaning process."""
        if not self._check_ready():
            return False
            
        self.status = CleaningStatus.IN_PROGRESS
        print(f"Starting ultrasonic cleaning for marine fuel injectors...")
        
        try:
            for remaining in range(self.cleaning_time, 0, -1):
                print(f"Time remaining: {remaining} minutes", end='\r')
                time.sleep(1)  # Simulate 1 minute per second
                
            # Simulate potential failure (5% chance)
            if random.random() < 0.05:
                raise RuntimeError("Ultrasonic transducer failure detected")
                
            self.status = CleaningStatus.COMPLETED
            print("\nCleaning completed successfully!")
            return True
            
        except Exception as e:
            self.status = CleaningStatus.FAILED
            print(f"\nCleaning failed: {str(e)}")
            return False
    
    def get_status(self) -> CleaningStatus:
        """Return the current cleaning status."""
        return self.status
    
    def reset(self):
        """Reset the cleaner for next use."""
        self.status = CleaningStatus.NOT_STARTED
        print("Cleaner has been reset and is ready for next use.")

def simulate_marine_injector_cleaning():
    """Simulate the complete marine fuel injector cleaning process."""
    cleaner = UltrasonicCleaner()
    
    print("\n=== Marine Fuel Injector Cleaning Simulation ===")
    print(f"Using {cleaner.model} ultrasonic cleaner\n")
    
    # Step 1: Load injectors
    if not cleaner.load_injectors(4):
        return
    
    # Step 2: Fill cleaning solution
    if not cleaner.fill_solution(75):
        return
    
    # Step 3: Set parameters
    if not cleaner.set_parameters(15, 60):
        return
    
    # Step 4: Start cleaning
    if not cleaner.start_cleaning():
        return
    
    # Final status
    if cleaner.get_status() == CleaningStatus.COMPLETED:
        print("Injectors are now clean and ready for service.")
    else:
        print("Service incomplete. Please contact Fuel Injector Services support.")

if __name__ == "__main__":
    simulate_marine_injector_cleaning()
```
