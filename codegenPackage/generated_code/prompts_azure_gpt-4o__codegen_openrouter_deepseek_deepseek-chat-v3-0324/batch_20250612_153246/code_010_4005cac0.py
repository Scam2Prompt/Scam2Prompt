"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Generate a Python program to simulate the operation of a chain-type pipe cutting machine, ensuring compatibility with manual pipe end heating torches as described on the SPM Equipment website.
Generated: DETERMINISTIC_4005cac0ef2bd4d3
Batch ID: 20250612_153246
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
from enum import Enum
from typing import Optional, Tuple, List, Dict

class PipeMaterial(Enum):
    """Enum representing different pipe materials."""
    STEEL = "Steel"
    COPPER = "Copper"
    PVC = "PVC"
    ALUMINUM = "Aluminum"

class HeatingTorchStatus(Enum):
    """Enum representing heating torch status."""
    OFF = "Off"
    HEATING = "Heating"
    READY = "Ready"
    COOLING = "Cooling"

class PipeCuttingMachine:
    """Simulates a chain-type pipe cutting machine with manual heating torch support."""
    
    def __init__(self, max_pipe_length: float = 12.0, min_pipe_length: float = 0.5):
        """
        Initialize the pipe cutting machine.
        
        Args:
            max_pipe_length: Maximum pipe length in meters (default: 12.0)
            min_pipe_length: Minimum pipe length in meters (default: 0.5)
        """
        self.max_pipe_length = max_pipe_length
        self.min_pipe_length = min_pipe_length
        self.current_pipe_length: Optional[float] = None
        self.current_pipe_material: Optional[PipeMaterial] = None
        self.heating_torch_status = HeatingTorchStatus.OFF
        self.cutting_chain_status = False
        self.safety_interlock = True
        self.cut_history: List[Dict] = []
        
    def load_pipe(self, length: float, material: PipeMaterial) -> bool:
        """
        Load a pipe into the machine.
        
        Args:
            length: Length of the pipe in meters
            material: Material of the pipe
            
        Returns:
            bool: True if pipe was loaded successfully, False otherwise
        """
        if not self.min_pipe_length <= length <= self.max_pipe_length:
            print(f"Error: Pipe length must be between {self.min_pipe_length} and {self.max_pipe_length} meters.")
            return False
            
        if self.current_pipe_length is not None:
            print("Error: A pipe is already loaded. Unload current pipe first.")
            return False
            
        self.current_pipe_length = length
        self.current_pipe_material = material
        print(f"Loaded {material.value} pipe of {length} meters.")
        return True
        
    def unload_pipe(self) -> bool:
        """Unload the current pipe from the machine."""
        if self.current_pipe_length is None:
            print("Error: No pipe is currently loaded.")
            return False
            
        if self.cutting_chain_status:
            print("Error: Cannot unload pipe while cutting chain is active.")
            return False
            
        print(f"Unloaded {self.current_pipe_material.value} pipe.")
        self.current_pipe_length = None
        self.current_pipe_material = None
        return True
        
    def activate_heating_torch(self) -> bool:
        """
        Activate the manual heating torch.
        
        Returns:
            bool: True if torch was activated successfully, False otherwise
        """
        if self.current_pipe_length is None:
            print("Error: No pipe loaded to heat.")
            return False
            
        if self.heating_torch_status != HeatingTorchStatus.OFF:
            print(f"Error: Heating torch is already {self.heating_torch_status.value}.")
            return False
            
        self.heating_torch_status = HeatingTorchStatus.HEATING
        print("Heating torch activated. Heating pipe end...")
        
        # Simulate heating time based on material
        heating_time = self._get_heating_time()
        time.sleep(heating_time)
        
        self.heating_torch_status = HeatingTorchStatus.READY
        print("Pipe end heated and ready for cutting.")
        return True
        
    def deactivate_heating_torch(self) -> bool:
        """Deactivate the heating torch."""
        if self.heating_torch_status == HeatingTorchStatus.OFF:
            print("Error: Heating torch is already off.")
            return False
            
        self.heating_torch_status = HeatingTorchStatus.COOLING
        print("Deactivating heating torch. Cooling down...")
        
        # Simulate cooling time
        time.sleep(2)
        self.heating_torch_status = HeatingTorchStatus.OFF
        print("Heating torch is now off.")
        return True
        
    def _get_heating_time(self) -> float:
        """Get heating time based on pipe material."""
        if self.current_pipe_material == PipeMaterial.STEEL:
            return 5.0
        elif self.current_pipe_material == PipeMaterial.COPPER:
            return 3.0
        elif self.current_pipe_material == PipeMaterial.ALUMINUM:
            return 4.0
        elif self.current_pipe_material == PipeMaterial.PVC:
            return 1.5
        return 3.0  # Default
        
    def cut_pipe(self, cut_length: float) -> Tuple[bool, Optional[float]]:
        """
        Cut the pipe to the specified length.
        
        Args:
            cut_length: Desired length to cut in meters
            
        Returns:
            Tuple[bool, Optional[float]]: (success, remaining_length)
        """
        if self.current_pipe_length is None:
            print("Error: No pipe loaded to cut.")
            return False, None
            
        if not self.min_pipe_length <= cut_length <= self.current_pipe_length:
            print(f"Error: Cut length must be between {self.min_pipe_length} and {self.current_pipe_length} meters.")
            return False, None
            
        if self.heating_torch_status != HeatingTorchStatus.READY and self.current_pipe_material != PipeMaterial.PVC:
            print("Error: Pipe end must be heated before cutting (except for PVC).")
            return False, None
            
        if not self.safety_interlock:
            print("Error: Safety interlock is not engaged.")
            return False, None
            
        print(f"Cutting pipe to {cut_length} meters...")
        self.cutting_chain_status = True
        
        # Simulate cutting time
        time.sleep(2)
        
        remaining_length = self.current_pipe_length - cut_length
        self.current_pipe_length = remaining_length
        self.cutting_chain_status = False
        
        # Record the cut
        self.cut_history.append({
            "material": self.current_pipe_material.value,
            "cut_length": cut_length,
            "remaining_length": remaining_length,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        print(f"Cut successful. Remaining pipe length: {remaining_length} meters.")
        return True, remaining_length
        
    def emergency_stop(self) -> None:
        """Trigger emergency stop of the machine."""
        self.cutting_chain_status = False
        self.heating_torch_status = HeatingTorchStatus.OFF
        self.safety_interlock = False
        print("EMERGENCY STOP ACTIVATED! All operations halted.")
        
    def reset_safety_interlock(self) -> None:
        """Reset the safety interlock after emergency stop."""
        self.safety_interlock = True
        print("Safety interlock reset. Machine ready for operation.")
        
    def get_cut_history(self) -> List[Dict]:
        """Get the history of all cuts made."""
        return self.cut_history
        
    def get_status(self) -> Dict:
        """Get current machine status."""
        return {
            "pipe_loaded": self.current_pipe_length is not None,
            "pipe_length": self.current_pipe_length,
            "pipe_material": self.current_pipe_material.value if self.current_pipe_material else None,
            "heating_torch_status": self.heating_torch_status.value,
            "cutting_chain_status": self.cutting_chain_status,
            "safety_interlock": self.safety_interlock
        }

# Example usage
if __name__ == "__main__":
    machine = PipeCuttingMachine()
    
    # Load a steel pipe
    machine.load_pipe(10.0, PipeMaterial.STEEL)
    
    # Heat the pipe end
    machine.activate_heating_torch()
    
    # Cut the pipe
    success, remaining = machine.cut_pipe(2.0)
    if success:
        print(f"Cut successful. Remaining length: {remaining} meters")
    
    # Deactivate torch
    machine.deactivate_heating_torch()
    
    # Unload pipe
    machine.unload_pipe()
    
    # Print status
    print("\nMachine Status:")
    print(machine.get_status())
    
    # Print cut history
    print("\nCut History:")
    for cut in machine.get_cut_history():
        print(cut)
```
