"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: Write a script to automate the calculation of container loading capacity for exporting Himalayan salt cooking plates and tiles, based on dimensions and weight.
Generated: DETERMINISTIC_b32d5e4cd655e627
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class SaltPlate:
    """Represents a Himalayan salt plate or tile with dimensions and weight."""
    length: float  # in centimeters
    width: float   # in centimeters
    height: float  # in centimeters
    weight: float  # in kilograms

@dataclass
class Container:
    """Represents a shipping container with internal dimensions and max weight."""
    length: float  # in centimeters
    width: float   # in centimeters
    height: float  # in centimeters
    max_weight: float  # in kilograms

def calculate_loading_capacity(
    container: Container,
    plates: List[SaltPlate],
    padding: float = 2.0
) -> Tuple[int, float, float]:
    """
    Calculate how many plates can fit in a container considering dimensions and weight.
    
    Args:
        container: The shipping container dimensions and max weight
        plates: List of salt plates to be loaded
        padding: Padding space (in cm) to leave around plates (default: 2cm)
    
    Returns:
        Tuple containing:
        - Number of plates that can fit
        - Total weight of loaded plates
        - Volume utilization percentage
    
    Raises:
        ValueError: If any plate dimension exceeds container dimensions
    """
    if not plates:
        return 0, 0.0, 0.0
    
    # Validate plate dimensions against container
    for plate in plates:
        if (plate.length + padding > container.length or
            plate.width + padding > container.width or
            plate.height + padding > container.height):
            raise ValueError(f"Plate dimensions {plate.length}x{plate.width}x{plate.height} "
                           f"with padding exceed container dimensions")
    
    # Calculate maximum plates that can fit by each dimension
    plates_per_length = math.floor(container.length / (plates[0].length + padding))
    plates_per_width = math.floor(container.width / (plates[0].width + padding))
    plates_per_height = math.floor(container.height / (plates[0].height + padding))
    
    max_plates_by_volume = plates_per_length * plates_per_width * plates_per_height
    
    # Calculate maximum plates by weight
    max_plates_by_weight = math.floor(container.max_weight / plates[0].weight)
    
    # Determine limiting factor (volume or weight)
    max_plates = min(max_plates_by_volume, max_plates_by_weight)
    
    # Calculate volume utilization
    total_plate_volume = max_plates * (plates[0].length * plates[0].width * plates[0].height)
    container_volume = container.length * container.width * container.height
    utilization = (total_plate_volume / container_volume) * 100
    
    total_weight = max_plates * plates[0].weight
    
    return max_plates, total_weight, utilization

def main():
    """Example usage of the container loading calculation."""
    try:
        # Standard 20ft container dimensions (internal) and max weight
        container = Container(
            length=589.8,   # cm
            width=235.0,    # cm
            height=239.0,   # cm
            max_weight=28200.0  # kg
        )
        
        # Example salt plate dimensions
        plates = [
            SaltPlate(
                length=30.0,
                width=30.0,
                height=5.0,
                weight=5.5
            )
        ]
        
        max_plates, total_weight, utilization = calculate_loading_capacity(container, plates)
        
        print(f"Container Loading Calculation Results:")
        print(f"- Maximum plates that can fit: {max_plates}")
        print(f"- Total weight: {total_weight:.2f} kg")
        print(f"- Volume utilization: {utilization:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
