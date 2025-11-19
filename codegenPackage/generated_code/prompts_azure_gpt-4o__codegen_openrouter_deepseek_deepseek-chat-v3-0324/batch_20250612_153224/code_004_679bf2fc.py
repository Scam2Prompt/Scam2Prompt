"""
Generated Code Metadata:
========================
Original URL: https://watpac.in
Prompt: Create a Python program to recommend Watpac waterproofing solutions based on user input for specific requirements, such as "Exterior Shield" or "Heat Diminish White."
Generated: DETERMINISTIC_679bf2fc6f5effc5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum

class WaterproofingSolution(Enum):
    EXTERIOR_SHIELD = "Exterior Shield"
    HEAT_DIMINISH_WHITE = "Heat Diminish White"
    FLEXI_SHIELD = "Flexi Shield"
    AQUA_BLOCK = "Aqua Block"
    THERMA_GUARD = "Therma Guard"

SOLUTION_DESCRIPTIONS = {
    WaterproofingSolution.EXTERIOR_SHIELD: (
        "A high-performance waterproofing membrane for exterior surfaces. "
        "Provides excellent protection against water ingress and weathering."
    ),
    WaterproofingSolution.HEAT_DIMINISH_WHITE: (
        "A reflective waterproof coating that reduces heat absorption. "
        "Ideal for roofs and surfaces exposed to direct sunlight."
    ),
    WaterproofingSolution.FLEXI_SHIELD: (
        "A flexible waterproofing solution for areas prone to movement or cracking. "
        "Perfect for balconies, terraces, and concrete structures."
    ),
    WaterproofingSolution.AQUA_BLOCK: (
        "A water-based waterproofing solution for interior and exterior use. "
        "Environmentally friendly and easy to apply."
    ),
    WaterproofingSolution.THERMA_GUARD: (
        "A thermal insulating waterproofing system. "
        "Provides both waterproofing and thermal insulation benefits."
    ),
}

def get_user_input():
    """Get user input for waterproofing requirements."""
    print("Available Watpac Waterproofing Solutions:")
    for solution in WaterproofingSolution:
        print(f"- {solution.value}")
    
    while True:
        user_input = input("\nEnter your waterproofing requirement: ").strip()
        try:
            return WaterproofingSolution(user_input)
        except ValueError:
            print("Error: Invalid solution. Please enter one of the options listed above.")

def recommend_solution(requirement):
    """Recommend a waterproofing solution based on user requirement."""
    description = SOLUTION_DESCRIPTIONS.get(requirement, "No description available.")
    print(f"\nRecommended Solution: {requirement.value}")
    print(f"Description: {description}")

def main():
    """Main function to run the waterproofing solution recommender."""
    try:
        print("Watpac Waterproofing Solution Recommender")
        print("----------------------------------------")
        requirement = get_user_input()
        recommend_solution(requirement)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
