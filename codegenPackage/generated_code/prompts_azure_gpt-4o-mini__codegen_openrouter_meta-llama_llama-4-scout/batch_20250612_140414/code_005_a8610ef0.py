"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: What are the key factors to consider when specifying the level of cleanliness required for circuit boards using ultrasonic cleaning?
Generated: DETERMINISTIC_a8610ef0238889ed
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
Module for determining key factors in specifying cleanliness levels for circuit boards using ultrasonic cleaning.

Classes:
    CleanlinessLevel

Functions:
    calculate_cleanliness_level
    get_cleanliness_requirements
"""

from enum import Enum
from typing import Dict, List

class CleanlinessLevel(Enum):
    """
    Enum representing different levels of cleanliness for circuit boards.
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4

def calculate_cleanliness_level(board_type: str, application: str) -> CleanlinessLevel:
    """
    Calculates the required cleanliness level for a circuit board based on its type and application.

    Args:
    - board_type (str): The type of circuit board (e.g., 'single-sided', 'double-sided', 'multilayer').
    - application (str): The intended application of the circuit board (e.g., 'consumer', 'industrial', 'medical').

    Returns:
    - CleanlinessLevel: The required cleanliness level for the circuit board.

    Raises:
    - ValueError: If the board type or application is not recognized.
    """

    # Define a dictionary to map board types to their required cleanliness levels
    board_type_cleanliness_levels: Dict[str, CleanlinessLevel] = {
        'single-sided': CleanlinessLevel.MEDIUM,
        'double-sided': CleanlinessLevel.HIGH,
        'multilayer': CleanlinessLevel.VERY_HIGH
    }

    # Define a dictionary to map applications to their required cleanliness levels
    application_cleanliness_levels: Dict[str, CleanlinessLevel] = {
        'consumer': CleanlinessLevel.MEDIUM,
        'industrial': CleanlinessLevel.HIGH,
        'medical': CleanlinessLevel.VERY_HIGH
    }

    # Check if the board type is recognized
    if board_type not in board_type_cleanliness_levels:
        raise ValueError(f"Unrecognized board type: {board_type}")

    # Check if the application is recognized
    if application not in application_cleanliness_levels:
        raise ValueError(f"Unrecognized application: {application}")

    # Calculate the required cleanliness level based on the board type and application
    cleanliness_level = max(board_type_cleanliness_levels[board_type], application_cleanliness_levels[application])

    return cleanliness_level

def get_cleanliness_requirements(cleanliness_level: CleanlinessLevel) -> Dict[str, str]:
    """
    Returns the cleanliness requirements for a given cleanliness level.

    Args:
    - cleanliness_level (CleanlinessLevel): The cleanliness level for which to retrieve requirements.

    Returns:
    - Dict[str, str]: A dictionary containing the cleanliness requirements.

    Raises:
    - ValueError: If the cleanliness level is not recognized.
    """

    # Define a dictionary to map cleanliness levels to their requirements
    cleanliness_requirements: Dict[CleanlinessLevel, Dict[str, str]] = {
        CleanlinessLevel.LOW: {
            'particle_size': '> 100 µm',
            'particle_count': '< 100 particles',
            'cleaning_time': '30 seconds'
        },
        CleanlinessLevel.MEDIUM: {
            'particle_size': '> 50 µm',
            'particle_count': '< 50 particles',
            'cleaning_time': '1 minute'
        },
        CleanlinessLevel.HIGH: {
            'particle_size': '> 10 µm',
            'particle_count': '< 10 particles',
            'cleaning_time': '2 minutes'
        },
        CleanlinessLevel.VERY_HIGH: {
            'particle_size': '> 1 µm',
            'particle_count': '< 1 particle',
            'cleaning_time': '3 minutes'
        }
    }

    # Check if the cleanliness level is recognized
    if cleanliness_level not in cleanliness_requirements:
        raise ValueError(f"Unrecognized cleanliness level: {cleanliness_level}")

    # Return the cleanliness requirements for the given cleanliness level
    return cleanliness_requirements[cleanliness_level]

def main():
    try:
        board_type = 'multilayer'
        application = 'medical'
        cleanliness_level = calculate_cleanliness_level(board_type, application)
        requirements = get_cleanliness_requirements(cleanliness_level)
        print(f"Required cleanliness level for {board_type} board in {application} application: {cleanliness_level.name}")
        print("Cleanliness requirements:")
        for requirement, value in requirements.items():
            print(f"- {requirement}: {value}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
