"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Develop a script that automates the process of calculating notary fees for property transactions using the guidelines provided by Inmobiliaria Nueva Ciudad.
Generated: DETERMINISTIC_43beab7c2e2f31c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_notary_fees(property_value):
    """
    Calculate notary fees for property transactions based on the guidelines provided by Inmobiliaria Nueva Ciudad.

    Args:
        property_value (float): The value of the property in monetary units.

    Returns:
        float: The calculated notary fees.
    """
    try:
        # Validate input
        if property_value <= 0:
            raise ValueError("Property value must be greater than zero.")

        # Fee calculation guidelines (example rules, replace with actual guidelines)
        if property_value <= 100_000:
            fee = property_value * 0.01  # 1% fee for properties <= 100,000
        elif property_value <= 500_000:
            fee = property_value * 0.008  # 0.8% fee for properties <= 500,000
        else:
            fee = property_value * 0.005  # 0.5% fee for properties > 500,000

        # Minimum fee threshold
        minimum_fee = 500
        return max(fee, minimum_fee)

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the notary fee calculation script.
    """
    try:
        print("Welcome to the Notary Fee Calculator!")
        property_value = float(input("Enter the property value: "))

        # Calculate fees
        notary_fee = calculate_notary_fees(property_value)

        # Display the result
        print(f"The notary fee for a property valued at {property_value} is: {notary_fee:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the property.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
