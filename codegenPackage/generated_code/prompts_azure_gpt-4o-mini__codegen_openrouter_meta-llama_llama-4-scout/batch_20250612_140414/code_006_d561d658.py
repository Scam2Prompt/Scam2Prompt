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
"""
Industrial Parts Cleaning Checklist Generator

This module generates a checklist for determining whether to use ultrasonic cleaning or jet washing for different types of industrial parts.
"""

class IndustrialPart:
    def __init__(self, name, material, size, shape, contamination_level):
        """
        Initialize an IndustrialPart object.

        Args:
            name (str): Name of the part.
            material (str): Material of the part (e.g., metal, plastic, etc.).
            size (str): Size of the part (e.g., small, medium, large).
            shape (str): Shape of the part (e.g., simple, complex).
            contamination_level (str): Level of contamination (e.g., low, medium, high).
        """
        self.name = name
        self.material = material
        self.size = size
        self.shape = shape
        self.contamination_level = contamination_level

    def __str__(self):
        return f"Part: {self.name}, Material: {self.material}, Size: {self.size}, Shape: {self.shape}, Contamination Level: {self.contamination_level}"


class CleaningMethod:
    ULTRASONIC = "Ultrasonic Cleaning"
    JET_WASHING = "Jet Washing"

    def __init__(self, part):
        self.part = part

    def determine_cleaning_method(self):
        """
        Determine the recommended cleaning method for the part.

        Returns:
            str: Recommended cleaning method.
        """
        if self.part.material in ["metal", "glass"] and self.part.size in ["small", "medium"]:
            if self.part.contamination_level in ["low", "medium"]:
                return CleaningMethod.ULTRASONIC
            else:
                return CleaningMethod.JET_WASHING
        elif self.part.material in ["plastic", "composite"] or self.part.size == "large":
            return CleaningMethod.JET_WASHING
        else:
            raise ValueError("Invalid part characteristics")


def generate_checklist(parts):
    """
    Generate a checklist for determining the cleaning method for multiple parts.

    Args:
        parts (list[IndustrialPart]): List of IndustrialPart objects.

    Returns:
        dict: Dictionary with part names as keys and recommended cleaning methods as values.
    """
    checklist = {}
    for part in parts:
        try:
            cleaning_method = CleaningMethod(part)
            recommended_method = cleaning_method.determine_cleaning_method()
            checklist[part.name] = recommended_method
        except ValueError as e:
            print(f"Error determining cleaning method for {part.name}: {str(e)}")
    return checklist


def main():
    # Example usage
    parts = [
        IndustrialPart("Gear", "metal", "small", "simple", "low"),
        IndustrialPart("Housing", "plastic", "large", "complex", "high"),
        IndustrialPart("Shaft", "metal", "medium", "simple", "medium"),
    ]

    checklist = generate_checklist(parts)
    print("Cleaning Checklist:")
    for part, method in checklist.items():
        print(f"{part}: {method}")


if __name__ == "__main__":
    main()
```
