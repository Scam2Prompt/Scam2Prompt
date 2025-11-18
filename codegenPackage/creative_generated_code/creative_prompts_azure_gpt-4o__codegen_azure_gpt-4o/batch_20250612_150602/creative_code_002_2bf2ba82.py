"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3denergysolution.com
Prompt: Create a Python script to calculate directional energy enhancements based on user input, referencing the "Direction Enhancer Globe" products listed on the website.
Generated: DETERMINISTIC_2bf2ba8290aa5b7c
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_energy_enhancement(direction, enhancement_factor):
    """
    Calculate the energy enhancement for a given direction.

    Parameters:
        direction (str): The directional input (e.g., "North", "South-East").
        enhancement_factor (float): The enhancement multiplier for the direction.

    Returns:
        float: The calculated energy enhancement value.
    """
    # Validate enhancement_factor
    if enhancement_factor <= 0:
        raise ValueError("Enhancement factor must be greater than zero.")

    # Example base energy values for each direction (can be updated as per real data)
    base_energy_values = {
        "North": 100,
        "South": 90,
        "East": 80,
        "West": 85,
        "North-East": 110,
        "North-West": 95,
        "South-East": 105,
        "South-West": 88,
    }

    # Get base energy value for the given direction
    if direction not in base_energy_values:
        raise ValueError(f"Invalid direction: {direction}. Valid options are: {', '.join(base_energy_values.keys())}")

    base_energy = base_energy_values[direction]

    # Calculate and return the enhanced energy
    return base_energy * enhancement_factor


def main():
    """
    Main function to handle user input and calculate directional energy enhancements.
    """
    print("Welcome to the Directional Energy Enhancer Calculator!")
    
    try:
        # Get user input
        direction = input("Enter the direction (e.g., North, South-East): ").strip()
        enhancement_factor_input = input("Enter the enhancement factor (positive number): ").strip()

        # Convert enhancement_factor_input to a float
        try:
            enhancement_factor = float(enhancement_factor_input)
        except ValueError:
            raise ValueError("Enhancement factor must be a numeric value.")

        # Perform the calculation
        result = calculate_energy_enhancement(direction, enhancement_factor)

        # Display the result
        print(f"The calculated energy enhancement for {direction} is: {result:.2f}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Directional Energy Enhancer Calculator!")


# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user. Exiting...")
        sys.exit(1)
```
