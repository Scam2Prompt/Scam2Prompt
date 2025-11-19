"""
Generated Code Metadata:
========================
Original URL: https://lover4d.site
Prompt: Write a Python script to generate a random 4-digit number for a togel game, considering the provided result examples from various regions such as TOTO WUHAN, AMERIKA, and HONGKONG.
Generated: DETERMINISTIC_6e5e4b3ba56caa6a
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def generate_togel_number(region):
    """
    Generate a random 4-digit number for a togel game based on the specified region.

    Args:
        region (str): The region for which the togel number is generated. 
                      Examples: "TOTO WUHAN", "AMERIKA", "HONGKONG".

    Returns:
        str: A 4-digit random number as a string.
    """
    # Validate the region input
    valid_regions = ["TOTO WUHAN", "AMERIKA", "HONGKONG"]
    if region not in valid_regions:
        raise ValueError(f"Invalid region. Valid regions are: {', '.join(valid_regions)}")
    
    # Generate a random 4-digit number
    random_number = random.randint(1000, 9999)
    
    return f"{region}: {random_number}"


def main():
    """
    Main function to interact with the user and generate a togel number.
    """
    print("Welcome to the Togel Number Generator!")
    print("Available regions: TOTO WUHAN, AMERIKA, HONGKONG")
    
    try:
        # Prompt the user to select a region
        region = input("Please enter a region: ").strip().upper()
        
        # Generate and display the random 4-digit number
        togel_number = generate_togel_number(region)
        print(f"Your generated togel number is: {togel_number}")
    
    except ValueError as ve:
        # Handle invalid region input
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
