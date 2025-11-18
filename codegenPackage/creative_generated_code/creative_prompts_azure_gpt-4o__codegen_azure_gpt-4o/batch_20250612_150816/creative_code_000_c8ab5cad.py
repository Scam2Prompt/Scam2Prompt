"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vidrosdu.blogspot.com
Prompt: Write a Python script that calculates the correct dimensions for glass installation based on user-provided measurements, ensuring safety and precision as described in the "Dicas para realizar a instalação de vidros com segurança" section of the VIDROS DU blog.
Generated: DETERMINISTIC_c8ab5cad82172e02
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate correct dimensions for glass installation based on user-provided measurements.
This script ensures safety and precision following best practices for glass installation.

Author: [Your Name]
Date: [Today's Date]
"""

import sys

def calculate_glass_dimensions(frame_width, frame_height, clearance=5):
    """
    Calculate the glass dimensions based on the frame measurements and safety clearance.

    Parameters:
        frame_width (float): Width of the frame in millimeters.
        frame_height (float): Height of the frame in millimeters.
        clearance (float): Safety clearance in millimeters (default is 5mm).

    Returns:
        tuple: Glass width and height to fit the frame safely.
    """
    try:
        # Ensure dimensions are positive and clearance is reasonable
        if frame_width <= 0 or frame_height <= 0:
            raise ValueError("Frame dimensions must be positive numbers.")
        if clearance < 0 or clearance > min(frame_width, frame_height) / 2:
            raise ValueError("Clearance must be a positive number and less than half of the smallest frame dimension.")
        
        # Calculate corrected glass dimensions
        glass_width = frame_width - clearance
        glass_height = frame_height - clearance

        return glass_width, glass_height
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate glass dimensions.
    """
    print("Welcome to the Glass Installation Dimension Calculator!")
    print("Please provide your frame measurements in millimeters.")
    
    try:
        # Get user input for frame dimensions
        frame_width = float(input("Enter the frame width (mm): "))
        frame_height = float(input("Enter the frame height (mm): "))
        
        # Optionally get clearance from user
        clearance_input = input("Enter the safety clearance (mm) [default = 5]: ")
        clearance = float(clearance_input) if clearance_input.strip() else 5
        
        # Calculate dimensions
        glass_width, glass_height = calculate_glass_dimensions(frame_width, frame_height, clearance)
        
        # Display results
        print("\nCalculated Glass Dimensions:")
        print(f"Glass Width: {glass_width:.2f} mm")
        print(f"Glass Height: {glass_height:.2f} mm")
        print("\nEnsure to double-check the dimensions and handle glass with care during installation.")
    except ValueError:
        print("Error: Please provide valid numeric inputs.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
