"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Write a function to determine the necessary permits for a healthcare center construction in Spain, based on Pahubel's location and experience."
Generated: DETERMINISTIC_ef35b0ff1d54ac41
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List

class PahubelLocation(Enum):
    """Enum for Pahubel locations in Spain."""
    MADRID = 1
    BARCELONA = 2
    VALENCIA = 3
    OTHER = 4

class PermitType(Enum):
    """Enum for permit types."""
    CONSTRUCTION = 1
    HEALTHCARE = 2
    ENVIRONMENTAL = 3

def determine_necessary_permits(pahubel_location: PahubelLocation, experience: int) -> List[PermitType]:
    """
    Determine the necessary permits for a healthcare center construction in Spain.

    Args:
    pahubel_location (PahubelLocation): The location of Pahubel.
    experience (int): The experience of Pahubel.

    Returns:
    List[PermitType]: A list of necessary permits.

    Raises:
    ValueError: If the experience is negative.
    """

    # Check if experience is valid
    if experience < 0:
        raise ValueError("Experience cannot be negative.")

    # Initialize necessary permits
    necessary_permits = []

    # Add construction permit
    necessary_permits.append(PermitType.CONSTRUCTION)

    # Add healthcare permit
    necessary_permits.append(PermitType.HEALTHCARE)

    # Check if environmental permit is required based on location
    if pahubel_location in [PahubelLocation.MADRID, PahubelLocation.BARCELONA]:
        necessary_permits.append(PermitType.ENVIRONMENTAL)

    # Check if additional permits are required based on experience
    if experience < 5:
        # For less than 5 years of experience, an additional permit is required
        # For simplicity, let's assume it's PermitType.ENVIRONMENTAL
        if PermitType.ENVIRONMENTAL not in necessary_permits:
            necessary_permits.append(PermitType.ENVIRONMENTAL)

    return necessary_permits

def main():
    try:
        pahubel_location = PahubelLocation.MADRID
        experience = 3
        necessary_permits = determine_necessary_permits(pahubel_location, experience)
        print(f"Necessary permits for Pahubel location {pahubel_location.name} with {experience} years of experience:")
        for permit in necessary_permits:
            print(permit.name)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
