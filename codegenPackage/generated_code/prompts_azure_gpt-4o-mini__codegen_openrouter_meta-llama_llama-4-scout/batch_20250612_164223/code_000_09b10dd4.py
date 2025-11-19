"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Generate a Python function that recommends the best mattress firmness for back pain relief based on user input regarding their body type and sleeping posture, referencing the Spinetress medium-firm mattress guidelines.
Generated: DETERMINISTIC_09b10dd424a3d754
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mattress Firmness Recommendation Function

This module provides a function to recommend the best mattress firmness for back pain relief
based on user input regarding their body type and sleeping posture, referencing the Spinetress
medium-firm mattress guidelines.
"""

def recommend_mattress_firmness(body_type: str, sleeping_posture: str) -> str:
    """
    Recommends the best mattress firmness for back pain relief based on user input.

    Args:
    - body_type (str): The user's body type. Can be 'petite', 'average', 'athletic', or 'curvy'.
    - sleeping_posture (str): The user's sleeping posture. Can be 'side', 'back', or 'stomach'.

    Returns:
    - str: The recommended mattress firmness.

    Raises:
    - ValueError: If the body type or sleeping posture is not recognized.
    """

    # Define a dictionary to map body types to recommended firmness levels
    body_type_firmness = {
        'petite': 'soft-medium',
        'average': 'medium',
        'athletic': 'medium-firm',
        'curvy': 'medium-soft'
    }

    # Define a dictionary to map sleeping postures to recommended firmness levels
    sleeping_posture_firmness = {
        'side': 'soft-medium',
        'back': 'medium-firm',
        'stomach': 'firm'
    }

    # Check if the body type is recognized
    if body_type not in body_type_firmness:
        raise ValueError(f"Unrecognized body type: {body_type}. Please choose from: {list(body_type_firmness.keys())}")

    # Check if the sleeping posture is recognized
    if sleeping_posture not in sleeping_posture_firmness:
        raise ValueError(f"Unrecognized sleeping posture: {sleeping_posture}. Please choose from: {list(sleeping_posture_firmness.keys())}")

    # Get the recommended firmness levels for the body type and sleeping posture
    body_type_recommendation = body_type_firmness[body_type]
    sleeping_posture_recommendation = sleeping_posture_firmness[sleeping_posture]

    # Determine the final recommended firmness level
    if body_type == 'average' and sleeping_posture == 'back':
        recommended_firmness = 'medium-firm'
    elif body_type == 'athletic' and sleeping_posture in ['back', 'stomach']:
        recommended_firmness = 'firm'
    else:
        # Use the firmer of the two recommendations
        firmness_levels = ['soft', 'soft-medium', 'medium', 'medium-soft', 'medium-firm', 'firm']
        recommended_firmness = max([body_type_recommendation, sleeping_posture_recommendation], key=lambda x: firmness_levels.index(x))

    return recommended_firmness


def main():
    try:
        body_type = input("Enter your body type (petite, average, athletic, or curvy): ")
        sleeping_posture = input("Enter your sleeping posture (side, back, or stomach): ")
        recommended_firmness = recommend_mattress_firmness(body_type, sleeping_posture)
        print(f"Based on your body type and sleeping posture, we recommend a mattress with a firmness level of: {recommended_firmness}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
