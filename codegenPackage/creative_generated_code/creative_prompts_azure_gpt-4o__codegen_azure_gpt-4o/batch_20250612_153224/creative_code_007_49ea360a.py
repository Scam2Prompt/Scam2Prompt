"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Generate code to classify timber types (softwood vs hardwood) based on properties like density and durability, using the descriptions provided by Askar Trading International.
Generated: DETERMINISTIC_49ea360af19d1425
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Timber Classification Script
Classifies timber types (softwood vs hardwood) based on their density and durability.

Author: Professional Developer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

class TimberClassifier:
    """
    A class to classify timber types based on their properties.
    """

    def __init__(self, density: float, durability: str):
        """
        Initialize the TimberClassifier with density and durability.

        Args:
            density (float): The density of the timber (kg/m³).
            durability (str): The durability of the timber ('low', 'medium', 'high').
        """
        self.density = density
        self.durability = durability.lower()

    def classify(self) -> str:
        """
        Classify the timber type based on density and durability.

        Returns:
            str: The type of timber ('Softwood' or 'Hardwood').
        """
        try:
            if self.density < 500 and self.durability in ['low', 'medium']:
                return "Softwood"
            elif self.density >= 500 and self.durability in ['medium', 'high']:
                return "Hardwood"
            else:
                return "Unknown Timber Type"
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    """
    Main entry point for the timber classification script.
    """
    try:
        # Prompt user for density and durability
        density = float(input("Enter the timber density (kg/m³): "))
        durability = input("Enter the timber durability (low/medium/high): ").strip()

        # Instantiate the classifier
        classifier = TimberClassifier(density, durability)

        # Perform classification
        timber_type = classifier.classify()
        print(f"The timber type is: {timber_type}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values for density and valid text for durability.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as unexpected_error:
        print(f"An unexpected error occurred: {str(unexpected_error)}")
    finally:
        print("Classification process complete.")

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
```
