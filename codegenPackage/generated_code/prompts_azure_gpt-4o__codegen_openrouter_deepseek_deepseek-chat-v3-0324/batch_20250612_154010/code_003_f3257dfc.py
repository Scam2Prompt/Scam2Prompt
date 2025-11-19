"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Create a script to automate the selection of battery types (e.g., AGM, Gel, Lithium) for different use cases such as marine, automotive, or solar systems, using the categories from Battery Australia's product offerings.
Generated: DETERMINISTIC_f3257dfc3bb12b71
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Battery Type Selector Script

This script helps users select the appropriate battery type (AGM, Gel, Lithium)
for different use cases (marine, automotive, solar) based on Battery Australia's
product offerings.
"""

import sys
from enum import Enum, auto

class BatteryType(Enum):
    """Enumeration of available battery types."""
    AGM = auto()
    GEL = auto()
    LITHIUM = auto()

class UseCase(Enum):
    """Enumeration of supported use cases."""
    MARINE = auto()
    AUTOMOTIVE = auto()
    SOLAR = auto()

# Battery recommendations based on use case
RECOMMENDATIONS = {
    UseCase.MARINE: {
        "description": "Marine applications require deep cycle batteries that can handle vibration and occasional deep discharges.",
        "recommendation": BatteryType.AGM,
        "alternatives": [BatteryType.GEL]
    },
    UseCase.AUTOMOTIVE: {
        "description": "Automotive applications need batteries with high cranking power and vibration resistance.",
        "recommendation": BatteryType.AGM,
        "alternatives": []
    },
    UseCase.SOLAR: {
        "description": "Solar systems require deep cycle batteries with excellent cycle life and depth of discharge capabilities.",
        "recommendation": BatteryType.LITHIUM,
        "alternatives": [BatteryType.AGM, BatteryType.GEL]
    }
}

def display_menu(options, title):
    """Display a menu of options and return user selection."""
    print(f"\n{title}:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option.name}")
    
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return list(options)[choice-1]
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def get_recommendation(use_case):
    """Return the battery recommendation for a given use case."""
    return RECOMMENDATIONS[use_case]

def main():
    """Main function to run the battery selector."""
    print("Battery Type Selector")
    print("=" * 40)
    
    try:
        # Get use case from user
        use_case = display_menu(UseCase, "Select Use Case")
        
        # Get recommendation
        recommendation = get_recommendation(use_case)
        
        # Display results
        print("\nRecommendation:")
        print(f"Use Case: {use_case.name}")
        print(f"Description: {recommendation['description']}")
        print(f"Recommended Battery: {recommendation['recommendation'].name}")
        
        if recommendation['alternatives']:
            alt_names = [alt.name for alt in recommendation['alternatives']]
            print(f"Alternative Options: {', '.join(alt_names)}")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
