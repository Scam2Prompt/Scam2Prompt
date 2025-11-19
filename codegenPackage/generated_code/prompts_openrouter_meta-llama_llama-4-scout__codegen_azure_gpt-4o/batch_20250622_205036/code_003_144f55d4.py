"""
Generated Code Metadata:
========================
Original URL: https://worldiscoveryperu.com
Prompt: "Compare and contrast the 'Perú Andino 1' and 'Perú Ancestral 1' travel packages offered by World Discovery Perù, highlighting their unique features and experiences."
Generated: DETERMINISTIC_144f55d4906a9a61
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_packages_comparison.py

# Import necessary modules
import json

def load_travel_packages():
    """
    Load travel package data from a JSON file or database.
    For simplicity, we'll use hardcoded data in this example.
    """
    return [
        {
            "name": "Perú Andino 1",
            "duration": "7 days",
            "price": 1200,
            "features": [
                "Visit to Machu Picchu",
                "Exploration of the Sacred Valley",
                "Guided tour of Cusco",
                "Andean cultural experiences"
            ],
            "unique_experiences": [
                "Traditional Andean weaving workshop",
                "Hike to Rainbow Mountain"
            ]
        },
        {
            "name": "Perú Ancestral 1",
            "duration": "5 days",
            "price": 950,
            "features": [
                "Visit to Machu Picchu",
                "Guided tour of Cusco",
                "Exploration of ancient ruins"
            ],
            "unique_experiences": [
                "Cooking class with ancestral Peruvian recipes",
                "Visit to pre-Inca archaeological sites"
            ]
        }
    ]

def compare_packages(package1, package2):
    """
    Compare two travel packages and highlight their unique features and experiences.
    
    Args:
        package1 (dict): The first travel package.
        package2 (dict): The second travel package.
    
    Returns:
        dict: A comparison summary highlighting differences and similarities.
    """
    comparison = {
        "common_features": list(set(package1["features"]) & set(package2["features"])),
        "unique_to_package1": {
            "features": list(set(package1["features"]) - set(package2["features"])),
            "unique_experiences": package1["unique_experiences"]
        },
        "unique_to_package2": {
            "features": list(set(package2["features"]) - set(package1["features"])),
            "unique_experiences": package2["unique_experiences"]
        }
    }
    return comparison

def display_comparison(comparison):
    """
    Display the comparison results in a user-friendly format.
    
    Args:
        comparison (dict): The comparison summary.
    """
    print("=== Travel Package Comparison ===")
    print("\nCommon Features:")
    for feature in comparison["common_features"]:
        print(f"- {feature}")
    
    print("\nUnique to Perú Andino 1:")
    print("Features:")
    for feature in comparison["unique_to_package1"]["features"]:
        print(f"- {feature}")
    print("Unique Experiences:")
    for experience in comparison["unique_to_package1"]["unique_experiences"]:
        print(f"- {experience}")
    
    print("\nUnique to Perú Ancestral 1:")
    print("Features:")
    for feature in comparison["unique_to_package2"]["features"]:
        print(f"- {feature}")
    print("Unique Experiences:")
    for experience in comparison["unique_to_package2"]["unique_experiences"]:
        print(f"- {experience}")

def main():
    """
    Main function to execute the travel package comparison.
    """
    try:
        # Load travel packages
        packages = load_travel_packages()
        
        # Ensure there are at least two packages to compare
        if len(packages) < 2:
            raise ValueError("Insufficient travel packages to compare.")
        
        # Compare the first two packages
        comparison = compare_packages(packages[0], packages[1])
        
        # Display the comparison results
        display_comparison(comparison)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
