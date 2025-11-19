"""
Generated Code Metadata:
========================
Original URL: https://xanade.com
Prompt: Compare the features and pricing of the M5Stack UnitV2 AI camera development kit and the Raspberry Pi 5 single-board computer (8GB), and suggest a use case for each.
Generated: DETERMINISTIC_7d72845214aaaa0c
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of M5Stack UnitV2 AI Camera and Raspberry Pi 5 (8GB) with use case suggestions.
"""

import json
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Feature:
    """Class representing a feature of a device."""
    name: str
    description: str

@dataclass
class PricingTier:
    """Class representing a pricing tier for a device."""
    quantity: int
    price: float
    currency: str = "USD"

@dataclass
class Device:
    """Class representing a hardware device."""
    name: str
    description: str
    features: List[Feature]
    pricing: List[PricingTier]
    use_case: str

def compare_devices(device1: Device, device2: Device) -> Dict:
    """
    Compare two devices and return a structured comparison.
    
    Args:
        device1: First device to compare
        device2: Second device to compare
    
    Returns:
        Dictionary containing comparison results
    """
    comparison = {
        "devices": [device1.name, device2.name],
        "feature_comparison": [],
        "price_comparison": {
            "single_unit": {
                device1.name: f"{device1.pricing[0].price} {device1.pricing[0].currency}",
                device2.name: f"{device2.pricing[0].price} {device2.pricing[0].currency}"
            }
        },
        "use_cases": {
            device1.name: device1.use_case,
            device2.name: device2.use_case
        }
    }

    # Compare features
    max_features = max(len(device1.features), len(device2.features))
    for i in range(max_features):
        feature1 = device1.features[i] if i < len(device1.features) else None
        feature2 = device2.features[i] if i < len(device2.features) else None
        
        comparison["feature_comparison"].append({
            "feature_number": i + 1,
            device1.name: feature1.description if feature1 else "N/A",
            device2.name: feature2.description if feature2 else "N/A"
        })

    return comparison

def main():
    """Main function to demonstrate device comparison."""
    # M5Stack UnitV2 AI Camera
    m5stack_features = [
        Feature("AI Processor", "Dual-core 400MHz CPU + 4 TOPS NPU"),
        Feature("Camera", "1/4-inch CMOS, 2MP, 1080p@30fps"),
        Feature("Connectivity", "Wi-Fi 4, Bluetooth 4.2"),
        Feature("RAM", "16MB PSRAM"),
        Feature("Storage", "16MB Flash"),
        Feature("OS", "Built-in TensorFlow Lite, MicroPython support")
    ]
    
    m5stack_pricing = [
        PricingTier(1, 99.00)
    ]
    
    m5stack = Device(
        name="M5Stack UnitV2 AI Camera",
        description="Standalone AI camera development kit",
        features=m5stack_features,
        pricing=m5stack_pricing,
        use_case="Edge AI applications like object recognition, face detection, and smart surveillance without needing a host computer."
    )

    # Raspberry Pi 5 (8GB)
    rpi5_features = [
        Feature("Processor", "Broadcom BCM2712 2.4GHz quad-core 64-bit ARM Cortex-A76"),
        Feature("RAM", "8GB LPDDR4X"),
        Feature("GPU", "VideoCore VII, supports 4Kp60 HEVC decode"),
        Feature("Connectivity", "2.4GHz/5GHz 802.11ac Wi-Fi, Bluetooth 5.0, Gigabit Ethernet"),
        Feature("Ports", "2x USB 3.0, 2x USB 2.0, 2x micro-HDMI, PCIe 2.0 interface"),
        Feature("Storage", "MicroSD card slot"),
        Feature("OS", "Raspberry Pi OS (Linux-based), supports various OS options")
    ]
    
    rpi5_pricing = [
        PricingTier(1, 80.00)
    ]
    
    rpi5 = Device(
        name="Raspberry Pi 5 (8GB)",
        description="High-performance single-board computer",
        features=rpi5_features,
        pricing=rpi5_pricing,
        use_case="General-purpose computing, media center, home automation, robotics, and projects requiring full Linux capabilities."
    )

    # Compare devices
    comparison = compare_devices(m5stack, rpi5)
    
    # Output results in JSON format for readability
    print(json.dumps(comparison, indent=2))

if __name__ == "__main__":
    main()
```
