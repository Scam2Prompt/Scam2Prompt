"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Write a Python script to calculate dumpster rental pricing based on the service areas listed on the Purple Dumpster website, including specific regions like Milton, Oakville, and Mississauga.
Generated: DETERMINISTIC_bab7fd67f00bdec9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_dumpster_price(region, dumpster_size):
    """
    Calculate the price for dumpster rental based on region and dumpster size.

    Args:
        region (str): The service area (e.g., Milton, Oakville, Mississauga).
        dumpster_size (str): The size of the dumpster (e.g., 'small', 'medium', 'large').

    Returns:
        float: The price of the dumpster rental.
    """
    # Define pricing details for dumpsters by region and size
    pricing = {
        "Milton": {"small": 200, "medium": 300, "large": 400},
        "Oakville": {"small": 220, "medium": 320, "large": 420},
        "Mississauga": {"small": 250, "medium": 350, "large": 450}
    }

    # Ensure region is valid
    if region not in pricing:
        raise ValueError(f"Invalid region: '{region}'. Available regions are: {', '.join(pricing.keys())}")

    # Ensure dumpster size is valid
    if dumpster_size not in pricing[region]:
        raise ValueError(
            f"Invalid dumpster size: '{dumpster_size}'. Available sizes are: {', '.join(pricing[region].keys())}"
        )

    # Return the price for the region and dumpster size
    return pricing[region][dumpster_size]


def main():
    """
    Main function to run the script. Prompts user for region and dumpster size,
    then calculates and displays the pricing.
    """
    print("Welcome to Purple Dumpster Rental Pricing Calculator!")
    print("Available regions: Milton, Oakville, Mississauga")
    print("Available dumpster sizes: small, medium, large")

    try:
        # Get user input for region and size
        region = input("Enter your region: ").strip()
        dumpster_size = input("Enter dumpster size: ").strip().lower()

        # Calculate the price
        price = calculate_dumpster_price(region, dumpster_size)

        # Display the result
        print(f"The price for a {dumpster_size} dumpster in {region} is: ${price:.2f}")
    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by the user.")
        sys.exit()
```
