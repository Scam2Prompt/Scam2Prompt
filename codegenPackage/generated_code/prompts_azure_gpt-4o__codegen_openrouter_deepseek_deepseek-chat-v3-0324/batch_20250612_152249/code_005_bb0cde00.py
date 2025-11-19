"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: Write code to simulate thermal processing of plexiglass for creating custom signage, referencing Nova Forma's capabilities and equipment.
Generated: DETERMINISTIC_bb0cde007bf926be
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Thermal Processing Simulation for Plexiglass Signage

This script simulates the thermal processing of plexiglass for custom signage production,
inspired by Nova Forma's capabilities and equipment. It models heating, forming, and cooling
stages with safety checks and quality control parameters.

Key Features:
- Temperature control simulation
- Time-based processing stages
- Material property tracking
- Quality assurance checks
"""

import time
import random
from enum import Enum, auto

class ProcessingStage(Enum):
    """Enum representing different stages of thermal processing"""
    IDLE = auto()
    PREHEATING = auto()
    FORMING = auto()
    COOLING = auto()
    QUALITY_CHECK = auto()
    COMPLETE = auto()

class PlexiglassSignageSimulator:
    """
    Simulates thermal processing of plexiglass for custom signage production.
    
    Attributes:
        thickness (float): Thickness of plexiglass in mm (3-10mm typical)
        target_temp (float): Target forming temperature in °C (150-180°C)
        current_temp (float): Current material temperature
        stage (ProcessingStage): Current processing stage
        quality_rating (float): Final product quality (0-1)
    """
    
    def __init__(self, thickness=5.0, target_temp=160.0):
        """
        Initialize the simulator with material parameters.
        
        Args:
            thickness: Plexiglass thickness in mm (default 5.0)
            target_temp: Target forming temperature in °C (default 160.0)
        """
        if not 3.0 <= thickness <= 10.0:
            raise ValueError("Thickness must be between 3-10mm")
        if not 150.0 <= target_temp <= 180.0:
            raise ValueError("Target temp must be between 150-180°C")
            
        self.thickness = thickness
        self.target_temp = target_temp
        self.current_temp = 20.0  # Room temperature
        self.stage = ProcessingStage.IDLE
        self.quality_rating = 0.0
        self._heating_rate = 2.5  # °C per second
        self._cooling_rate = 0.8  # °C per second
        self._start_time = None
        
    def start_processing(self):
        """Begin the thermal processing cycle"""
        if self.stage != ProcessingStage.IDLE:
            raise RuntimeError("Processing already in progress")
            
        self.stage = ProcessingStage.PREHEATING
        self._start_time = time.time()
        print(f"Starting thermal processing for {self.thickness}mm plexiglass")
        
    def update(self):
        """
        Advance the simulation by one time step.
        
        Returns:
            bool: True if processing is complete, False otherwise
        """
        if self.stage == ProcessingStage.IDLE:
            return False
            
        elapsed = time.time() - self._start_time
        
        # Preheating stage
        if self.stage == ProcessingStage.PREHEATING:
            self.current_temp += self._heating_rate
            if self.current_temp >= self.target_temp:
                self.stage = ProcessingStage.FORMING
                print("Material reached forming temperature")
                
        # Forming stage (hold temperature)
        elif self.stage == ProcessingStage.FORMING:
            # Simulate temperature fluctuations during forming
            self.current_temp += random.uniform(-0.5, 0.5)
            if elapsed > 30:  # Typical forming time
                self.stage = ProcessingStage.COOLING
                print("Forming complete, beginning cooling")
                
        # Cooling stage
        elif self.stage == ProcessingStage.COOLING:
            self.current_temp -= self._cooling_rate
            if self.current_temp <= 50.0:  # Safe handling temperature
                self.stage = ProcessingStage.QUALITY_CHECK
                
        # Quality check
        elif self.stage == ProcessingStage.QUALITY_CHECK:
            self._perform_quality_check()
            self.stage = ProcessingStage.COMPLETE
            return True
            
        return False
        
    def _perform_quality_check(self):
        """Calculate final product quality based on process parameters"""
        # Base quality based on temperature control
        temp_variance = abs(self.current_temp - self.target_temp) / self.target_temp
        temp_quality = max(0, 1.0 - temp_variance * 2)
        
        # Thickness factor (thicker is more forgiving)
        thickness_factor = min(1.0, self.thickness / 5.0)
        
        # Random production variations
        production_variance = random.uniform(0.95, 1.05)
        
        self.quality_rating = temp_quality * thickness_factor * production_variance
        print(f"Quality check complete. Rating: {self.quality_rating:.2f}/1.0")
        
    def emergency_shutdown(self):
        """Immediately halt processing for safety"""
        print("EMERGENCY SHUTDOWN INITIATED")
        self.stage = ProcessingStage.IDLE
        self.current_temp = 20.0
        
    def get_status(self):
        """Return current processing status as a dictionary"""
        return {
            "stage": self.stage.name,
            "current_temp": round(self.current_temp, 1),
            "elapsed_time": round(time.time() - self._start_time, 1) if self._start_time else 0,
            "quality": self.quality_rating if self.stage == ProcessingStage.COMPLETE else None
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a simulator for 5mm plexiglass
        simulator = PlexiglassSignageSimulator(thickness=5.0, target_temp=160.0)
        
        # Start the process
        simulator.start_processing()
        
        # Run the simulation
        while True:
            time.sleep(1)  # Simulate 1 second per update
            complete = simulator.update()
            
            # Print status
            status = simulator.get_status()
            print(f"[{status['stage']}] Temp: {status['current_temp']}°C | Time: {status['elapsed_time']}s")
            
            if complete:
                print("Processing complete!")
                break
                
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
        simulator.emergency_shutdown()
    except Exception as e:
        print(f"Error during processing: {e}")
        simulator.emergency_shutdown()
```
