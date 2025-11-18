"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruxindustrial.com.br
Prompt: Develop a script to categorize industrial materials into three sections (as mentioned in Rux Industrial's blog) and suggest their applications in various engineering projects.
Generated: DETERMINISTIC_09f63c83022b27cc
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define material categories and their applications
MATERIAL_CATEGORIES = {
    "Metals": {
        "description": "Durable materials used for structural and conductive purposes.",
        "examples": ["Steel", "Aluminum", "Copper", "Titanium"],
        "applications": [
            "Building construction",
            "Electrical wiring",
            "Machine parts",
            "Automobile manufacturing"
        ]
    },
    "Polymers": {
        "description": "Lightweight, flexible materials derived from synthetic or natural compounds.",
        "examples": ["Polyethylene", "Polypropylene", "PVC", "Polystyrene"],
        "applications": [
            "Packaging",
            "Insulation",
            "Medical devices",
            "Automotive interiors"
        ]
    },
    "Composites": {
        "description": "Materials combining two or more distinct substances for enhanced properties.",
        "examples": ["Carbon fiber", "Fiberglass", "Kevlar", "Concrete"],
        "applications": [
            "Aerospace engineering",
            "Sports equipment",
            "Bridge construction",
            "Military armor"
        ]
    }
}

def categorize_material(material_name):
    """
    Categorizes the given material into one of the predefined categories.
    
    Args:
        material_name (str): The name of the material to categorize.
    
    Returns:
        dict: A dictionary containing the category, description, and applications if the material
              is found, or None if the material is not recognized.
    """
    for category, details in MATERIAL_CATEGORIES.items():
        if material_name.capitalize() in details["examples"]:
            return {
                "category": category,
                "description": details["description"],
                "applications": details["applications"]
            }
    return None

def main():
    """
    Main function to interactively categorize materials and suggest applications.
    """
    print("Welcome to the Industrial Material Categorizer!")
    print("Enter a material name to find its category and applications.")
    print("Type 'exit' to quit.\n")
    
    while True:
        material_name = input("Enter material name: ").strip()
        
        # Exit condition
        if material_name.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        
        # Categorize material
        try:
            result = categorize_material(material_name)
            if result:
                print("\nMaterial Information:")
                print(f"Category: {result['category']}")
                print(f"Description: {result['description']}")
                print("Applications:")
                for app in result["applications"]:
                    print(f"- {app}")
            else:
                print(f"The material '{material_name}' is not recognized. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        print("\n")

# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"A critical error occurred: {e}")
```
