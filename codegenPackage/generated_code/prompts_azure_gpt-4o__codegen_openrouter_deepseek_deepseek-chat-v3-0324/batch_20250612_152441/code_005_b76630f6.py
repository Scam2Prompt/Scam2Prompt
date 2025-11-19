"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: Write code to simulate dust-proofing mechanisms for UPVC windows, incorporating the advantages listed on the Dexodoor website.
Generated: DETERMINISTIC_b76630f6a671212f
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import Optional, Dict

class DustProofMechanism(Enum):
    """Enum representing different dust-proofing mechanisms for UPVC windows."""
    MULTI_POINT_LOCKING = "Multi-point Locking System"
    COMPRESSED_SEALS = "Compressed Seals"
    BRUSH_SEALS = "Brush Seals"
    DRAINAGE_SYSTEM = "Built-in Drainage System"

class UPVCWindow:
    """Class representing a UPVC window with dust-proofing mechanisms."""
    
    def __init__(self, width: float, height: float, mechanism: DustProofMechanism):
        """
        Initialize a UPVC window with given dimensions and dust-proofing mechanism.
        
        Args:
            width (float): Width of the window in meters.
            height (float): Height of the window in meters.
            mechanism (DustProofMechanism): Dust-proofing mechanism used.
        """
        self.width = width
        self.height = height
        self.mechanism = mechanism
        self.is_open = False
        self.dust_level = 0  # 0-100 scale representing dust accumulation
        
    def open(self) -> None:
        """Open the window if not already open."""
        if self.is_open:
            print("Window is already open.")
            return
        self.is_open = True
        print("Window opened.")
        
    def close(self) -> None:
        """Close the window if not already closed."""
        if not self.is_open:
            print("Window is already closed.")
            return
        self.is_open = False
        print("Window closed.")
        
    def simulate_dust_accumulation(self, external_dust_level: int) -> None:
        """
        Simulate dust accumulation based on window state and mechanism.
        
        Args:
            external_dust_level (int): External dust level (0-100 scale).
        """
        if not 0 <= external_dust_level <= 100:
            raise ValueError("External dust level must be between 0 and 100.")
            
        if self.is_open:
            self.dust_level = min(100, self.dust_level + external_dust_level * 0.8)
        else:
            # Dust resistance based on mechanism
            resistance_factors = {
                DustProofMechanism.MULTI_POINT_LOCKING: 0.1,
                DustProofMechanism.COMPRESSED_SEALS: 0.05,
                DustProofMechanism.BRUSH_SEALS: 0.07,
                DustProofMechanism.DRAINAGE_SYSTEM: 0.03
            }
            resistance = resistance_factors.get(self.mechanism, 0.2)
            self.dust_level = min(100, self.dust_level + external_dust_level * resistance)
            
    def clean(self) -> None:
        """Clean the window, resetting dust level to 0."""
        self.dust_level = 0
        print("Window cleaned. Dust level reset to 0.")
        
    def get_dust_level(self) -> int:
        """Return current dust level."""
        return int(self.dust_level)
        
    def get_mechanism_effectiveness(self) -> Dict[str, float]:
        """Return effectiveness of the current dust-proofing mechanism."""
        effectiveness = {
            "mechanism": self.mechanism.value,
            "effectiveness": 0.0
        }
        
        if not self.is_open:
            effectiveness_map = {
                DustProofMechanism.MULTI_POINT_LOCKING: 90.0,
                DustProofMechanism.COMPRESSED_SEALS: 95.0,
                DustProofMechanism.BRUSH_SEALS: 92.0,
                DustProofMechanism.DRAINAGE_SYSTEM: 97.0
            }
            effectiveness["effectiveness"] = effectiveness_map.get(self.mechanism, 80.0)
            
        return effectiveness

def simulate_window_test(duration_hours: int, external_dust_level: int) -> None:
    """
    Simulate a window test over a period of time with varying dust levels.
    
    Args:
        duration_hours (int): Duration of the test in hours.
        external_dust_level (int): Base external dust level (0-100).
    """
    if duration_hours <= 0:
        raise ValueError("Duration must be positive.")
        
    mechanisms = list(DustProofMechanism)
    windows = [UPVCWindow(1.2, 1.5, mechanism) for mechanism in mechanisms]
    
    for hour in range(1, duration_hours + 1):
        print(f"\nHour {hour} of {duration_hours}")
        
        # Simulate random window openings
        for window in windows:
            if random.random() < 0.3:  # 30% chance window is open
                window.open()
            else:
                window.close()
                
            # Vary dust level slightly each hour
            current_dust = max(0, min(100, external_dust_level + random.randint(-10, 10)))
            window.simulate_dust_accumulation(current_dust)
            
            # Print status
            status = "open" if window.is_open else "closed"
            print(f"{window.mechanism.value}: {status}, Dust: {window.get_dust_level()}%")
            
    # Final report
    print("\n=== Final Dust Levels ===")
    for window in windows:
        effectiveness = window.get_mechanism_effectiveness()
        print(f"{window.mechanism.value}: {window.get_dust_level()}% dust "
              f"(Effectiveness: {effectiveness['effectiveness']}%)")

# Example usage
if __name__ == "__main__":
    try:
        simulate_window_test(duration_hours=24, external_dust_level=50)
    except ValueError as e:
        print(f"Error: {e}")
```
