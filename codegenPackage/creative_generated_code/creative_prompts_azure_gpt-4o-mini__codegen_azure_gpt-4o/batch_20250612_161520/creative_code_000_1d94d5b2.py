"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geektech.uk
Prompt: Generate a comparison code snippet that evaluates the features of the Nokia Edge Max 2024 5G against the iPhone 16 Pro based on their specifications.
Generated: DETERMINISTIC_1d94d5b2ea2fdfc1
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the JSON module for easy handling of specifications data
import json

# Define specifications for Nokia Edge Max 2024 5G and iPhone 16 Pro
nokia_edge_max_specs = {
    "model": "Nokia Edge Max 2024 5G",
    "display": "6.8-inch AMOLED, 1440 x 3200 pixels",
    "processor": "Snapdragon 8 Gen 3",
    "RAM": "12GB",
    "storage": "256GB / 512GB",
    "battery": "8000mAh",
    "camera": "108MP + 32MP + 8MP rear, 32MP front",
    "connectivity": "5G, Wi-Fi 6, Bluetooth 5.3",
    "OS": "Android 14"
}

iphone_16_pro_specs = {
    "model": "iPhone 16 Pro",
    "display": "6.7-inch Super Retina XDR, 1290 x 2796 pixels",
    "processor": "A19 Bionic",
    "RAM": "8GB",
    "storage": "256GB / 512GB / 1TB",
    "battery": "4500mAh",
    "camera": "48MP + 12MP + 12MP rear, 12MP front",
    "connectivity": "5G, Wi-Fi 6E, Bluetooth 5.3",
    "OS": "iOS 18"
}

def compare_specs(specs_1, specs_2):
    """
    Compare features of two devices based on their specifications.

    Args:
        specs_1 (dict): Specifications of device 1.
        specs_2 (dict): Specifications of device 2.

    Returns:
        dict: Comparison results highlighting differences.
    """
    comparison_result = {}
    for key in specs_1:
        value_1 = specs_1[key]
        value_2 = specs_2.get(key)
        
        if value_2 is not None:
            if value_1 != value_2:  # Highlight differences
                comparison_result[key] = {
                    specs_1["model"]: value_1,
                    specs_2["model"]: value_2
                }
    return comparison_result

# Compare the specifications
comparison = compare_specs(nokia_edge_max_specs, iphone_16_pro_specs)

# Output the comparison results in a readable format
print("Comparison of Nokia Edge Max 2024 5G vs iPhone 16 Pro:")
print(json.dumps(comparison, indent=4))
```
