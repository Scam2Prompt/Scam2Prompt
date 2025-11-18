"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rubberflooringindonesia.com
Prompt: Create a function to estimate the cost of installing rubber flooring for a jogging track, incorporating the pricing details and material options (e.g., EPDM, TPV Rubber) provided by Rubber Flooring Indonesia.
Generated: DETERMINISTIC_f7ee3a3bf5838d17
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
def estimate_rubber_flooring_cost(track_length_meters, track_width_meters, material_type):
    """
    Estimate the cost of installing rubber flooring for a jogging track.

    Parameters:
    - track_length_meters (float): The length of the jogging track in meters.
    - track_width_meters (float): The width of the jogging track in meters.
    - material_type (str): The type of rubber material. Options: 'EPDM', 'TPV'.

    Returns:
    - float: Estimated cost for the project.
    - str: Error message if any issue is encountered.
    """
    try:
        # Validate input types
        if not isinstance(track_length_meters, (int, float)) or track_length_meters <= 0:
            return None, "Error: Invalid track length. Must be a positive number."
        if not isinstance(track_width_meters, (int, float)) or track_width_meters <= 0:
            return None, "Error: Invalid track width. Must be a positive number."
        if material_type not in ['EPDM', 'TPV']:
            return None, "Error: Invalid material type. Options are 'EPDM' or 'TPV'."
        
        # Define pricing details (price per square meter)
        pricing = {
            'EPDM': 50.0,  # Example price per square meter
            'TPV': 60.0    # Example price per square meter
        }

        # Calculate the area of the track in square meters
        area_square_meters = track_length_meters * track_width_meters

        # Calculate the cost based on the material type
        cost = area_square_meters * pricing[material_type]

        return cost, None
    except Exception as e:
        # Handle unexpected errors
        return None, f"An unexpected error occurred: {str(e)}"


# Example usage:
track_length = 100.0  # Length of the track in meters
track_width = 5.0     # Width of the track in meters
material = 'EPDM'     # Material type: 'EPDM' or 'TPV'

estimated_cost, error = estimate_rubber_flooring_cost(track_length, track_width, material)

if error:
    print(error)
else:
    print(f"The estimated cost for installing rubber flooring is: ${estimated_cost:.2f}")
```
