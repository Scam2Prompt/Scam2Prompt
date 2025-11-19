"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Write a program to simulate the dyeing process for acrylic yarns, including variables like dye type, temperature, and duration.
Generated: DETERMINISTIC_082fc2f370d1824a
Batch ID: 20250612_152249
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
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Dict, List

class DyeType(Enum):
    ACID = "Acid"
    REACTIVE = "Reactive"
    DIRECT = "Direct"
    DISPERSE = "Disperse"

@dataclass
class DyeingParameters:
    dye_type: DyeType
    temperature_celsius: float
    duration_minutes: int
    dye_concentration_percent: float
    ph_level: float

class YarnBatch:
    def __init__(self, batch_id: str, weight_kg: float, fiber_content: str):
        self.batch_id = batch_id
        self.weight_kg = weight_kg
        self.fiber_content = fiber_content
        self.dyed = False
        self.color_result: Optional[str] = None
        self.dyeing_parameters: Optional[DyeingParameters] = None

    def __str__(self):
        return (f"YarnBatch(batch_id={self.batch_id}, weight={self.weight_kg}kg, "
                f"fiber={self.fiber_content}, dyed={self.dyed}, color={self.color_result})")

class DyeingSimulator:
    def __init__(self):
        self.color_library = {
            "red": ["scarlet", "crimson", "ruby"],
            "blue": ["navy", "sky", "royal"],
            "yellow": ["lemon", "gold", "mustard"],
            "green": ["forest", "lime", "olive"],
            "purple": ["lavender", "violet", "eggplant"]
        }
    
    def _validate_parameters(self, params: DyeingParameters) -> bool:
        if params.temperature_celsius < 20 or params.temperature_celsius > 120:
            raise ValueError("Temperature must be between 20°C and 120°C")
        if params.duration_minutes < 5 or params.duration_minutes > 240:
            raise ValueError("Duration must be between 5 and 240 minutes")
        if params.dye_concentration_percent <= 0 or params.dye_concentration_percent > 10:
            raise ValueError("Dye concentration must be between 0 and 10%")
        if params.ph_level < 2 or params.ph_level > 10:
            raise ValueError("pH level must be between 2 and 10")
        return True
    
    def _simulate_dye_absorption(self, params: DyeingParameters) -> float:
        base_absorption = 0.7  # Base absorption rate
        temp_factor = min(1.0, params.temperature_celsius / 100)
        time_factor = min(1.0, params.duration_minutes / 120)
        concentration_factor = min(1.0, params.dye_concentration_percent / 5)
        
        # pH effect: optimal around 4.5-5.5 for acrylic
        ph_effect = 1.0 - abs(params.ph_level - 5) * 0.1
        
        return base_absorption * temp_factor * time_factor * concentration_factor * ph_effect
    
    def _generate_color_result(self, dye_type: DyeType, absorption: float) -> str:
        base_colors = list(self.color_library.keys())
        base_color = random.choice(base_colors)
        shades = self.color_library[base_color]
        
        # Higher absorption leads to darker shades
        shade_index = min(len(shades) - 1, int(absorption * len(shades)))
        shade = shades[shade_index]
        
        # Dye type can affect color tone
        if dye_type == DyeType.ACID:
            return f"vibrant {shade}"
        elif dye_type == DyeType.REACTIVE:
            return f"rich {shade}"
        else:
            return f"deep {shade}"
    
    def dye_yarn(self, yarn_batch: YarnBatch, params: DyeingParameters) -> YarnBatch:
        try:
            self._validate_parameters(params)
            
            print(f"Starting dyeing process for batch {yarn_batch.batch_id}...")
            print(f"Parameters: {params.dye_type.value} dye at {params.temperature_celsius}°C "
                  f"for {params.duration_minutes} minutes")
            
            # Simulate dyeing process
            for minute in range(1, params.duration_minutes + 1):
                time.sleep(0.1)  # Simulate time passing
                progress = minute / params.duration_minutes * 100
                print(f"\rProgress: {progress:.1f}%", end="", flush=True)
            
            absorption = self._simulate_dye_absorption(params)
            color = self._generate_color_result(params.dye_type, absorption)
            
            yarn_batch.dyed = True
            yarn_batch.color_result = color
            yarn_batch.dyeing_parameters = params
            
            print(f"\nDyeing complete! Result: {color}")
            return yarn_batch
            
        except ValueError as e:
            print(f"Error in dyeing process: {str(e)}")
            return yarn_batch
        except Exception as e:
            print(f"Unexpected error during dyeing: {str(e)}")
            return yarn_batch

def main():
    simulator = DyeingSimulator()
    
    # Create a yarn batch
    yarn = YarnBatch("AC-2023-001", 5.0, "100% acrylic")
    print(f"Created yarn batch: {yarn}")
    
    # Set up dyeing parameters
    params = DyeingParameters(
        dye_type=DyeType.ACID,
        temperature_celsius=85.0,
        duration_minutes=45,
        dye_concentration_percent=3.5,
        ph_level=4.8
    )
    
    # Run the dyeing process
    dyed_yarn = simulator.dye_yarn(yarn, params)
    print(f"Final yarn status: {dyed_yarn}")

if __name__ == "__main__":
    main()
```
