"""
Generated Code Metadata:
========================
Original URL: https://elfworldvape.com
Prompt: Compare the features of Elfworld Vape devices, including the Big-B, PB45000, and AI22000, and suggest which one is best for a specific use case.
Generated: DETERMINISTIC_8e499724fc8eac5d
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

class VapeFeature(Enum):
    """Enum representing different features of vape devices."""
    LONG_BATTERY_LIFE = auto()
    HIGH_CAPACITY = auto()
    AI_TEMPERATURE_CONTROL = auto()
    COMPACT_DESIGN = auto()
    FAST_CHARGING = auto()
    CUSTOMIZABLE_SETTINGS = auto()

@dataclass
class VapeDevice:
    """Data class representing a vape device with its features."""
    name: str
    battery_life_hours: int
    capacity_ml: int
    features: list[VapeFeature]
    price_usd: float

def compare_vapes(devices: list[VapeDevice]) -> dict:
    """
    Compare vape devices and return a summary of their features.
    
    Args:
        devices: List of VapeDevice objects to compare
        
    Returns:
        dict: A dictionary with comparison data
    """
    comparison = {}
    for device in devices:
        comparison[device.name] = {
            'battery_life': f"{device.battery_life_hours}h",
            'capacity': f"{device.capacity_ml}ml",
            'features': [feature.name for feature in device.features],
            'price': f"${device.price_usd:.2f}"
        }
    return comparison

def suggest_device(devices: list[VapeDevice], 
                  priority_features: list[VapeFeature],
                  max_price: Optional[float] = None) -> Optional[VapeDevice]:
    """
    Suggest the best vape device based on priority features and optional max price.
    
    Args:
        devices: List of VapeDevice objects to consider
        priority_features: List of VapeFeature enums that are most important
        max_price: Optional maximum price limit
        
    Returns:
        Optional[VapeDevice]: Best matching device or None if no match found
    """
    best_device = None
    best_score = -1
    
    for device in devices:
        if max_price and device.price_usd > max_price:
            continue
            
        score = sum(1 for feature in priority_features if feature in device.features)
        
        if score > best_score or (score == best_score and 
                                 (best_device is None or device.price_usd < best_device.price_usd)):
            best_device = device
            best_score = score
            
    return best_device

# Example usage
if __name__ == "__main__":
    # Define available devices
    devices = [
        VapeDevice(
            name="Big-B",
            battery_life_hours=12,
            capacity_ml=8,
            features=[VapeFeature.LONG_BATTERY_LIFE, VapeFeature.FAST_CHARGING],
            price_usd=49.99
        ),
        VapeDevice(
            name="PB45000",
            battery_life_hours=24,
            capacity_ml=12,
            features=[VapeFeature.HIGH_CAPACITY, VapeFeature.LONG_BATTERY_LIFE, VapeFeature.CUSTOMIZABLE_SETTINGS],
            price_usd=79.99
        ),
        VapeDevice(
            name="AI22000",
            battery_life_hours=18,
            capacity_ml=10,
            features=[VapeFeature.AI_TEMPERATURE_CONTROL, VapeFeature.COMPACT_DESIGN, VapeFeature.CUSTOMIZABLE_SETTINGS],
            price_usd=89.99
        )
    ]
    
    # Compare all devices
    print("Device Comparison:")
    comparison = compare_vapes(devices)
    for name, data in comparison.items():
        print(f"\n{name}:")
        for key, value in data.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
    
    # Suggest best device for specific use case
    print("\nRecommendation for use case:")
    priority = [VapeFeature.LONG_BATTERY_LIFE, VapeFeature.HIGH_CAPACITY]
    budget = 80.00
    recommended = suggest_device(devices, priority, budget)
    
    if recommended:
        print(f"Best device within ${budget:.2f} for your needs: {recommended.name}")
    else:
        print("No suitable device found within the specified criteria.")
```
