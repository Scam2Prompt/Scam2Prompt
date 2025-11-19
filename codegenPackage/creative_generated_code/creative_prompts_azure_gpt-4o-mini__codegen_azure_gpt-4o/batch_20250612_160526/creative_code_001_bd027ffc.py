"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderplanet.ee
Prompt: Write a Python function that recommends entertainment packages for different age groups based on the offerings from Wonderplanet.ee, focusing on their unique programs for children, teenagers, and adults.
Generated: DETERMINISTIC_bd027ffca6f70a64
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List

def recommend_package(age: int) -> List[str]:
    """
    Recommends entertainment packages based on age groups for Wonderplanet.ee.

    Parameters:
    age (int): Age of the individual for whom the package is recommended.

    Returns:
    List[str]: A list of recommended packages based on the age group.
    """
    try:
        # Validate input
        if age < 0:
            raise ValueError("Age cannot be negative.")

        # Define packages for different age groups
        packages_for_children = [
            "Interactive Storytelling",
            "Creative Art Workshops",
            "Magic Show"
        ]

        packages_for_teenagers = [
            "Virtual Reality Gaming",
            "Music Jam Sessions",
            "Escape Room Challenges"
        ]

        packages_for_adults = [
            "Wine Tasting Nights",
            "Stand-Up Comedy Shows",
            "Outdoor Adventure Tours"
        ]

        # Recommend packages based on age
        if age <= 12:
            return packages_for_children
        elif 13 <= age <= 18:
            return packages_for_teenagers
        else:
            return packages_for_adults

    except ValueError as e:
        # Handle invalid age input
        return [f"Error: {str(e)}"]
    except Exception as e:
        # Handle unexpected errors
        return [f"An unexpected error occurred: {str(e)}"]

# Example usage
if __name__ == "__main__":
    # Test the function with various age inputs
    print(recommend_package(8))   # Output: Recommendations for children
    print(recommend_package(15))  # Output: Recommendations for teenagers
    print(recommend_package(25))  # Output: Recommendations for adults
    print(recommend_package(-5))  # Output: Error handling for invalid age
```
