"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Develop a script to calculate the aromatic intensity of mint oils in food applications, using YSC's description of mint oil as a flavoring agent.
Generated: DETERMINISTIC_9585828a82f8707c
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the aromatic intensity of mint oils in food applications.
This script uses the YSC's description of mint oil as a flavoring agent to compute the intensity based on
user inputs such as concentration, volume, and a flavoring factor.
"""

# Import necessary modules
import sys

def calculate_aromatic_intensity(concentration, volume, flavoring_factor):
    """
    Calculate the aromatic intensity of mint oils.
    
    Parameters:
        concentration (float): The concentration of mint oil in percentage (0-100).
        volume (float): The volume of food product in liters.
        flavoring_factor (float): A multiplier that represents the strength of mint oil as a flavoring agent.
        
    Returns:
        float: The calculated aromatic intensity of mint oils.
    """
    try:
        # Ensure valid inputs
        if not (0 <= concentration <= 100):
            raise ValueError("Concentration must be between 0 and 100.")
        if volume <= 0:
            raise ValueError("Volume must be greater than 0.")
        if flavoring_factor <= 0:
            raise ValueError("Flavoring factor must be greater than 0.")
        
        # Perform calculation
        aromatic_intensity = (concentration / 100) * volume * flavoring_factor
        return aromatic_intensity
    
    except Exception as e:
        # Handle errors gracefully
        print(f"Error calculating aromatic intensity: {e}")
        sys.exit(1)

def main():
    """
    Main function to prompt user for inputs and calculate aromatic intensity.
    """
    print("Welcome to the Mint Oil Aromatic Intensity Calculator!")
    
    try:
        # Prompt user for inputs
        concentration = float(input("Enter the concentration of mint oil (%) [0-100]: "))
        volume = float(input("Enter the volume of the food product (liters): "))
        flavoring_factor = float(input("Enter the flavoring factor: "))
        
        # Calculate aromatic intensity
        aromatic_intensity = calculate_aromatic_intensity(concentration, volume, flavoring_factor)
        
        # Display result
        print(f"The aromatic intensity of the mint oil is: {aromatic_intensity:.2f}")
    
    except ValueError as ve:
        # Handle invalid input errors
        print(f"Invalid input: {ve}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
