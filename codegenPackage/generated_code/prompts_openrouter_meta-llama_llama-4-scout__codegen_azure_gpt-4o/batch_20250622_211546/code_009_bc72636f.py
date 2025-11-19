"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Recommend a suitable pipe beveling machine for a specific application, including the type of material and thickness of the pipes to be beveled.
Generated: DETERMINISTIC_bc72636fb3e605c1
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define a function to recommend a pipe beveling machine
def recommend_pipe_beveling_machine(material: str, thickness: float) -> str:
    """
    Recommends a suitable pipe beveling machine based on the material and thickness of the pipe.

    Args:
        material (str): The type of material (e.g., "steel", "aluminum", "stainless steel").
        thickness (float): The thickness of the pipe in millimeters.

    Returns:
        str: A recommendation for a suitable pipe beveling machine.
    """
    try:
        # Validate inputs
        if not isinstance(material, str) or not material.strip():
            raise ValueError("Material must be a non-empty string.")
        if not isinstance(thickness, (int, float)) or thickness <= 0:
            raise ValueError("Thickness must be a positive number.")

        # Normalize material input
        material = material.lower()

        # Define machine recommendations based on material and thickness
        machine_recommendations = {
            "steel": {
                "light": "Model A - Lightweight Steel Beveler",
                "medium": "Model B - Medium-Duty Steel Beveler",
                "heavy": "Model C - Heavy-Duty Steel Beveler",
            },
            "aluminum": {
                "light": "Model D - Lightweight Aluminum Beveler",
                "medium": "Model E - Medium-Duty Aluminum Beveler",
                "heavy": "Model F - Heavy-Duty Aluminum Beveler",
            },
            "stainless steel": {
                "light": "Model G - Lightweight Stainless Steel Beveler",
                "medium": "Model H - Medium-Duty Stainless Steel Beveler",
                "heavy": "Model I - Heavy-Duty Stainless Steel Beveler",
            },
        }

        # Determine thickness category
        if thickness <= 5:
            thickness_category = "light"
        elif 5 < thickness <= 15:
            thickness_category = "medium"
        else:
            thickness_category = "heavy"

        # Check if material is supported
        if material not in machine_recommendations:
            return f"Material '{material}' is not supported. Please choose from: {', '.join(machine_recommendations.keys())}."

        # Get the recommended machine
        recommended_machine = machine_recommendations[material][thickness_category]
        return f"Recommended Machine: {recommended_machine} (Material: {material.capitalize()}, Thickness: {thickness}mm)"

    except ValueError as ve:
        return f"Input Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
if __name__ == "__main__":
    # Input parameters
    pipe_material = "steel"  # Example: "steel", "aluminum", "stainless steel"
    pipe_thickness = 10.0    # Example: Thickness in millimeters

    # Get recommendation
    recommendation = recommend_pipe_beveling_machine(pipe_material, pipe_thickness)

    # Print the recommendation
    print(recommendation)
```
