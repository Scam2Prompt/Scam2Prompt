"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hildeinox.com
Prompt: Create a function in Python to classify stainless steel grades based on the descriptions provided in the "Paslanmaz Çelik Kaliteleri" section of Hilde Inox.
Generated: DETERMINISTIC_0433f3b7585fcc1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from typing import Optional

def classify_stainless_steel_grade(description: str) -> Optional[str]:
    """
    Classifies stainless steel grades based on the given description.
    
    Parameters:
    description (str): A textual description of the stainless steel grade.
    
    Returns:
    Optional[str]: The classified stainless steel grade or None if no match is found.
    """
    # Predefined mapping based on descriptions commonly associated with stainless steel grades.
    grade_mapping = {
        "corrosion-resistant and durable": "304",
        "high strength and better resistance to corrosion": "316",
        "magnetic and lower corrosion resistance": "430",
        "economical and good for decoration": "201",
        "high heat resistance and oxidation resistance": "310",
    }

    # Normalize the input description to lower case for case-insensitive matching
    normalized_description = description.lower()

    # Iterate through the mapping to find a matching grade
    for key, grade in grade_mapping.items():
        if key in normalized_description:
            return grade

    # Return None if no match is found
    return None


# Example usage
if __name__ == "__main__":
    try:
        # Sample descriptions
        sample_descriptions = [
            "This material is corrosion-resistant and durable.",
            "Used in applications requiring high strength and better resistance to corrosion.",
            "A magnetic material with lower corrosion resistance.",
            "Economical material good for decoration purposes.",
            "Material with high heat resistance and oxidation resistance."
        ]

        # Classify and print results
        for desc in sample_descriptions:
            grade = classify_stainless_steel_grade(desc)
            print(f"Description: \"{desc}\" -> Grade: {grade}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
```
