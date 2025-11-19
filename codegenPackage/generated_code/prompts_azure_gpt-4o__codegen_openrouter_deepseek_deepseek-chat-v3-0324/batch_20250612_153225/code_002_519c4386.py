"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Generate code to integrate a gas fireplace system with both GLP and natural gas options, ensuring safety with a fully glass-enclosed design.
Generated: DETERMINISTIC_519c438613f76c5c
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
from enum import Enum

class GasType(Enum):
    """Enumeration for supported gas types."""
    NATURAL = "natural"
    GLP = "glp"

class FireplaceSystem:
    """Class representing a gas fireplace system with safety features."""
    
    def __init__(self, gas_type: GasType):
        """Initialize the fireplace system with specified gas type.
        
        Args:
            gas_type (GasType): Type of gas to be used (NATURAL or GLP)
        """
        self.gas_type = gas_type
        self.is_glass_enclosed = True
        self.is_ignited = False
        self.gas_flow = False
        self.safety_check_passed = False
        
    def perform_safety_check(self) -> bool:
        """Perform safety checks before ignition.
        
        Returns:
            bool: True if all safety checks pass, False otherwise
        """
        # Check glass enclosure
        if not self.is_glass_enclosed:
            print("Safety Error: Glass enclosure not detected!")
            return False
            
        # Check gas pressure based on gas type
        if self.gas_type == GasType.NATURAL:
            # Simulate natural gas pressure check
            self.safety_check_passed = True
        elif self.gas_type == GasType.GLP:
            # Simulate GLP pressure check
            self.safety_check_passed = True
        else:
            print(f"Error: Unsupported gas type {self.gas_type}")
            return False
            
        return self.safety_check_passed
    
    def ignite(self) -> bool:
        """Attempt to ignite the fireplace.
        
        Returns:
            bool: True if ignition successful, False otherwise
        """
        if not self.safety_check_passed:
            if not self.perform_safety_check():
                print("Ignition aborted: Safety checks failed")
                return False
                
        try:
            print(f"Igniting {self.gas_type.value} gas fireplace...")
            self.gas_flow = True
            time.sleep(1)  # Simulate ignition delay
            self.is_ignited = True
            print("Fireplace successfully ignited")
            return True
        except Exception as e:
            print(f"Ignition failed: {str(e)}")
            self.gas_flow = False
            return False
    
    def shutdown(self):
        """Safely shutdown the fireplace system."""
        print("Initiating shutdown sequence...")
        self.is_ignited = False
        self.gas_flow = False
        self.safety_check_passed = False
        print("Fireplace safely shut down")
    
    def __del__(self):
        """Destructor to ensure safe shutdown when object is destroyed."""
        if self.is_ignited or self.gas_flow:
            self.shutdown()

# Example usage
if __name__ == "__main__":
    try:
        # Create fireplace with natural gas
        fireplace = FireplaceSystem(GasType.NATURAL)
        
        # Attempt ignition
        if fireplace.ignite():
            print("Fireplace is running")
            time.sleep(5)  # Simulate running time
            fireplace.shutdown()
        else:
            print("Failed to start fireplace")
            
    except Exception as e:
        print(f"Fireplace system error: {str(e)}")
```
