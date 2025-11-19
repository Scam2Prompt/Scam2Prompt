"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Write a Python code snippet to recommend a mattress firmness level based on a user's back pain type and preferred sleeping posture, considering the Spinetress mattress features.
Generated: DETERMINISTIC_a150f4d6dfda2846
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Optional

def recommend_mattress(back_pain_type: str, sleeping_posture: str) -> Optional[str]:
    """
    Recommend a mattress firmness level based on back pain type and sleeping posture.

    Parameters:
        back_pain_type (str): Type of back pain (e.g., "lower", "upper", "none").
        sleeping_posture (str): Preferred sleeping posture (e.g., "side", "back", "stomach").

    Returns:
        Optional[str]: Recommended mattress firmness level (e.g., "soft", "medium", "firm").
                      Returns None if inputs are invalid.
    """
    # Validate inputs
    valid_back_pain_types = {"lower", "upper", "none"}
    valid_sleeping_postures = {"side", "back", "stomach"}
    
    if back_pain_type not in valid_back_pain_types or sleeping_posture not in valid_sleeping_postures:
        return None  # Return None for invalid inputs

    # Mattress recommendation logic
    if back_pain_type == "lower":
        if sleeping_posture == "side":
            return "medium"
        elif sleeping_posture == "back":
            return "firm"
        elif sleeping_posture == "stomach":
            return "firm"
    elif back_pain_type == "upper":
        if sleeping_posture == "side":
            return "soft"
        elif sleeping_posture == "back":
            return "medium"
        elif sleeping_posture == "stomach":
            return "medium"
    elif back_pain_type == "none":
        if sleeping_posture == "side":
            return "soft"
        elif sleeping_posture == "back":
            return "medium"
        elif sleeping_posture == "stomach":
            return "firm"

    # Default case (should not be reached due to validation)
    return None

# Example usage
if __name__ == "__main__":
    try:
        # User inputs
        back_pain = input("Enter your back pain type (lower, upper, none): ").strip().lower()
        posture = input("Enter your preferred sleeping posture (side, back, stomach): ").strip().lower()

        # Get recommendation
        recommendation = recommend_mattress(back_pain, posture)

        if recommendation:
            print(f"Recommended mattress firmness level: {recommendation}")
        else:
            print("Invalid input. Please provide valid back pain type and sleeping posture.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
