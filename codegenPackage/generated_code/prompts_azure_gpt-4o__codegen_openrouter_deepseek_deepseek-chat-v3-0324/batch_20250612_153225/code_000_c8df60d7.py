"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Write Python code to simulate the cutting of cardboard tubes into desired sizes using a fully automatic PLC-controlled machine, referencing the features of the Paper Core Cutting Machine described on the Aayra International website.
Generated: DETERMINISTIC_c8df60d70b627b2a
Batch ID: 20250612_153225
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
from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto

class MachineState(Enum):
    """Possible states of the cutting machine."""
    IDLE = auto()
    LOADING = auto()
    CUTTING = auto()
    EJECTING = auto()
    ERROR = auto()

@dataclass
class TubeSpec:
    """Specifications for a cardboard tube."""
    diameter: float  # in mm
    length: float    # in mm
    thickness: float # in mm

@dataclass
class CuttingJob:
    """A job containing tube specifications and desired cuts."""
    tube: TubeSpec
    desired_lengths: List[float]  # desired cut lengths in mm
    quantity: int                 # number of tubes to process

class CuttingMachine:
    """Simulates a PLC-controlled cardboard tube cutting machine."""
    
    def __init__(self):
        self.state = MachineState.IDLE
        self.current_job: Optional[CuttingJob] = None
        self.cut_tolerance = 0.5  # mm tolerance for cuts
        self.max_cuts_per_minute = 120  # machine capacity
        self.safety_sensors_active = True
    
    def load_job(self, job: CuttingJob) -> bool:
        """Load a new cutting job into the machine."""
        if self.state != MachineState.IDLE:
            print("Error: Machine is not idle. Cannot load new job.")
            return False
        
        if not self._validate_job(job):
            return False
        
        self.current_job = job
        self.state = MachineState.LOADING
        print(f"Job loaded: {job.quantity} tubes to cut into {len(job.desired_lengths)} pieces each.")
        return True
    
    def _validate_job(self, job: CuttingJob) -> bool:
        """Validate if the job parameters are within machine capabilities."""
        if job.tube.diameter > 300:  # assuming max diameter is 300mm
            print("Error: Tube diameter exceeds machine capacity.")
            return False
        
        if max(job.desired_lengths) > 6000:  # assuming max length is 6000mm
            print("Error: Desired cut length exceeds machine capacity.")
            return False
        
        if sum(job.desired_lengths) > job.tube.length * 1.05:  # 5% tolerance for waste
            print("Error: Desired cuts exceed original tube length.")
            return False
        
        return True
    
    def start_cutting(self) -> bool:
        """Start the cutting process."""
        if self.state != MachineState.LOADING:
            print("Error: Machine not ready for cutting.")
            return False
        
        if not self.current_job:
            print("Error: No job loaded.")
            return False
        
        if not self.safety_sensors_active:
            print("Error: Safety sensors not active. Cannot start.")
            return False
        
        self.state = MachineState.CUTTING
        print("Starting cutting process...")
        self._simulate_cutting()
        return True
    
    def _simulate_cutting(self):
        """Simulate the cutting process with realistic timing."""
        if not self.current_job:
            return
        
        job = self.current_job
        cuts_per_tube = len(job.desired_lengths)
        total_cuts = job.quantity * cuts_per_tube
        
        # Calculate estimated time based on machine speed
        estimated_time = (total_cuts / self.max_cuts_per_minute) * 60
        print(f"Estimated cutting time: {estimated_time:.2f} seconds")
        
        # Simulate cutting each tube
        for tube_num in range(1, job.quantity + 1):
            if self.state == MachineState.ERROR:
                break
                
            print(f"\nProcessing tube {tube_num}/{job.quantity}")
            self._simulate_single_tube(job.tube, job.desired_lengths)
        
        if self.state != MachineState.ERROR:
            self.state = MachineState.EJECTING
            print("\nCutting complete. Ejecting finished pieces...")
            time.sleep(2)  # simulate ejection time
            self.state = MachineState.IDLE
            print("Job completed successfully.")
    
    def _simulate_single_tube(self, tube: TubeSpec, desired_lengths: List[float]):
        """Simulate cutting a single tube into desired lengths."""
        # Simulate loading tube
        time.sleep(0.5)
        
        # Simulate each cut
        for i, length in enumerate(desired_lengths, 1):
            if random.random() < 0.01:  # 1% chance of error
                self._trigger_error(f"Cutting error at piece {i}")
                return
            
            # Simulate cutting time based on tube thickness
            cut_time = 0.1 + (tube.thickness * 0.01)
            time.sleep(cut_time)
            
            # Simulate slight variation in cut length
            actual_length = length + random.uniform(-self.cut_tolerance, self.cut_tolerance)
            print(f"Cut piece {i}: {actual_length:.2f}mm (target: {length}mm)")
    
    def _trigger_error(self, message: str):
        """Handle error conditions."""
        self.state = MachineState.ERROR
        print(f"ERROR: {message}")
        print("Machine stopped. Please resolve the issue and reset.")
    
    def emergency_stop(self):
        """Simulate emergency stop functionality."""
        self.state = MachineState.ERROR
        print("EMERGENCY STOP ACTIVATED!")
    
    def reset_machine(self):
        """Reset the machine after an error or completion."""
        if self.state == MachineState.ERROR:
            print("Resetting machine after error...")
        else:
            print("Resetting machine...")
        
        time.sleep(2)  # simulate reset time
        self.state = MachineState.IDLE
        self.current_job = None
        print("Machine reset to idle state.")

# Example usage
if __name__ == "__main__":
    # Create a sample tube specification
    tube = TubeSpec(diameter=150.0, length=3000.0, thickness=5.0)
    
    # Create a cutting job
    job = CuttingJob(
        tube=tube,
        desired_lengths=[500.0, 750.0, 1000.0, 750.0],
        quantity=10
    )
    
    # Initialize and run the machine
    machine = CuttingMachine()
    machine.load_job(job)
    machine.start_cutting()
    
    # Simulate error handling
    if machine.state == MachineState.ERROR:
        machine.reset_machine()
```
