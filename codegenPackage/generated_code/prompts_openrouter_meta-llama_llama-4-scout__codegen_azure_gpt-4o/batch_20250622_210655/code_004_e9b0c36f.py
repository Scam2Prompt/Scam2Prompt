"""
Generated Code Metadata:
========================
Original URL: https://shishehbalkon.ir
Prompt: "Provide a detailed comparison of glass types (e.g., tempered glass, laminated glass) used in شیشه سکوریت (tempered glass) and پارتیشن اداری (office partitions) installations by Akbarzadeh."
Generated: DETERMINISTIC_e9b0c36f9a59f7a8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a detailed comparison of glass types used in tempered glass (شیشه سکوریت) 
and office partition (پارتیشن اداری) installations by Akbarzadeh. The comparison includes 
properties such as strength, safety, cost, and common applications.
"""

# Import necessary libraries
import json

# Define a class to represent glass types
class GlassType:
    def __init__(self, name, properties, applications):
        """
        Initialize a GlassType object.

        :param name: Name of the glass type (e.g., "Tempered Glass")
        :param properties: Dictionary of properties (e.g., strength, safety, cost)
        :param applications: List of common applications
        """
        self.name = name
        self.properties = properties
        self.applications = applications

    def to_dict(self):
        """
        Convert the GlassType object to a dictionary for easy serialization.

        :return: Dictionary representation of the GlassType object
        """
        return {
            "name": self.name,
            "properties": self.properties,
            "applications": self.applications,
        }

# Define a function to compare glass types
def compare_glass_types(glass_types):
    """
    Compare different glass types and return a detailed comparison.

    :param glass_types: List of GlassType objects
    :return: Dictionary containing the comparison
    """
    comparison = {}
    for glass in glass_types:
        comparison[glass.name] = {
            "Properties": glass.properties,
            "Applications": glass.applications,
        }
    return comparison

# Define glass types used in installations
tempered_glass = GlassType(
    name="Tempered Glass (شیشه سکوریت)",
    properties={
        "Strength": "4-5 times stronger than regular glass",
        "Safety": "Breaks into small, harmless pieces",
        "Cost": "Moderate",
        "Thermal Resistance": "High",
    },
    applications=[
        "Office partitions",
        "Shower enclosures",
        "Storefronts",
        "Windows and doors",
    ],
)

laminated_glass = GlassType(
    name="Laminated Glass",
    properties={
        "Strength": "High due to interlayer",
        "Safety": "Holds together when shattered",
        "Cost": "Higher than tempered glass",
        "Soundproofing": "Excellent",
    },
    applications=[
        "Office partitions",
        "Skylights",
        "Automotive windshields",
        "Soundproof rooms",
    ],
)

# List of glass types
glass_types = [tempered_glass, laminated_glass]

# Perform the comparison
comparison_result = compare_glass_types(glass_types)

# Serialize the comparison result to JSON for easy readability
try:
    comparison_json = json.dumps(comparison_result, indent=4, ensure_ascii=False)
    print("Detailed Comparison of Glass Types:\n")
    print(comparison_json)
except Exception as e:
    print(f"Error serializing comparison result: {e}")
```
