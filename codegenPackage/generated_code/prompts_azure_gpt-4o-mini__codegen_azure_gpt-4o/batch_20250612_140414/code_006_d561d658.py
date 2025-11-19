"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: Generate a checklist for determining whether to use ultrasonic cleaning or jet washing for different types of industrial parts.
Generated: DETERMINISTIC_d561d6584816c80e
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# checklist_generator.py

# Import necessary modules
import json

def generate_cleaning_checklist(part_type, material, contamination_level, size, complexity):
    """
    Generate a checklist to determine whether to use ultrasonic cleaning or jet washing
    for industrial parts based on their attributes.

    Args:
        part_type (str): Type of the part (e.g., "gear", "cylinder", "plate").
        material (str): Material of the part (e.g., "metal", "plastic", "ceramic").
        contamination_level (str): Level of contamination (e.g., "low", "medium", "high").
        size (str): Size of the part (e.g., "small", "medium", "large").
        complexity (str): Complexity of the part (e.g., "simple", "moderate", "complex").

    Returns:
        dict: A checklist with recommendations for cleaning method.
    """
    # Initialize checklist dictionary
    checklist = {
        "part_type": part_type,
        "material": material,
        "contamination_level": contamination_level,
        "size": size,
        "complexity": complexity,
        "recommended_method": None,
        "notes": []
    }

    # Determine cleaning method based on attributes
    try:
        # Ultrasonic cleaning is preferred for complex parts or delicate materials
        if complexity == "complex" or material in ["plastic", "ceramic"]:
            checklist["recommended_method"] = "Ultrasonic Cleaning"
            checklist["notes"].append("Recommended for delicate or intricate parts.")

        # Jet washing is preferred for large, simple, or heavily contaminated parts
        elif size == "large" or contamination_level == "high" or complexity == "simple":
            checklist["recommended_method"] = "Jet Washing"
            checklist["notes"].append("Recommended for robust parts with heavy contamination.")

        # For medium-sized parts with moderate contamination, both methods may be suitable
        else:
            checklist["recommended_method"] = "Either Ultrasonic Cleaning or Jet Washing"
            checklist["notes"].append("Both methods may be suitable. Consider material and contamination level.")

    except Exception as e:
        checklist["notes"].append(f"Error determining cleaning method: {str(e)}")

    return checklist


def main():
    """
    Main function to demonstrate the checklist generator.
    """
    # Example input data
    part_data = [
        {"part_type": "gear", "material": "metal", "contamination_level": "high", "size": "medium", "complexity": "complex"},
        {"part_type": "plate", "material": "plastic", "contamination_level": "low", "size": "small", "complexity": "simple"},
        {"part_type": "cylinder", "material": "ceramic", "contamination_level": "medium", "size": "large", "complexity": "moderate"}
    ]

    # Generate and display checklists for each part
    for part in part_data:
        checklist = generate_cleaning_checklist(
            part["part_type"],
            part["material"],
            part["contamination_level"],
            part["size"],
            part["complexity"]
        )
        print(json.dumps(checklist, indent=4))


# Entry point for the script
if __name__ == "__main__":
    main()
```
