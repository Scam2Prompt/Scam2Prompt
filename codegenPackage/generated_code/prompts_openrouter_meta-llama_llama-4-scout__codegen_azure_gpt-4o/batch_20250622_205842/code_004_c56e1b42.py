"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: "What is the importance of TKPH in selecting tires for industrial equipment, and how to calculate it?"
Generated: DETERMINISTIC_c56e1b42464e22a6
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script calculates the TKPH (Ton Kilometer Per Hour) value for industrial equipment tires.
TKPH is a critical metric used to select tires based on their ability to handle heat buildup
and load during operation. It ensures the tire can withstand the operational demands without
failure.

Formula:
TKPH = (Average Load per Tire in Tons) * (Average Speed in km/h)

Inputs:
- Average load per tire (in tons)
- Average speed (in km/h)

Outputs:
- TKPH value
"""

def calculate_tkph(load_per_tire, speed):
    """
    Calculate the TKPH value for industrial equipment tires.

    Parameters:
        load_per_tire (float): Average load per tire in tons.
        speed (float): Average speed in kilometers per hour.

    Returns:
        float: TKPH value.
    """
    try:
        # Validate inputs
        if load_per_tire <= 0:
            raise ValueError("Load per tire must be greater than 0.")
        if speed <= 0:
            raise ValueError("Speed must be greater than 0.")

        # Calculate TKPH
        tkph = load_per_tire * speed
        return tkph

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate TKPH.
    """
    print("Welcome to the TKPH Calculator for Industrial Equipment Tires!")
    try:
        # Get user input
        load_per_tire = float(input("Enter the average load per tire (in tons): "))
        speed = float(input("Enter the average speed (in km/h): "))

        # Calculate TKPH
        tkph = calculate_tkph(load_per_tire, speed)

        if tkph is not None:
            print(f"The calculated TKPH value is: {tkph:.2f}")
        else:
            print("Failed to calculate TKPH due to invalid input.")

    except ValueError:
        # Handle invalid input format
        print("Error: Please enter valid numeric values for load and speed.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main function
    main()
```
