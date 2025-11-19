"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-pro.cc
Prompt: Write a Python script that checks the compatibility of the Kraken 3+ app with various iPhone models.
Generated: DETERMINISTIC_3be176660515d3ba
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def check_compatibility(model_name: str, ios_version: float) -> str:
    """
    Checks compatibility of the Kraken 3+ app with various iPhone models.
    
    Args:
        model_name (str): The name of the iPhone model (e.g., "iPhone 13").
        ios_version (float): The iOS version installed on the device (e.g., 15.3).
    
    Returns:
        str: A message indicating whether the device is compatible or not.
    """
    # Define supported models and minimum iOS version required
    SUPPORTED_MODELS = {
        "iPhone 8": 12.0,
        "iPhone X": 12.0,
        "iPhone XR": 12.0,
        "iPhone XS": 12.0,
        "iPhone 11": 13.0,
        "iPhone 12": 14.0,
        "iPhone 13": 14.0,
        "iPhone 14": 15.0,
    }
    
    # Check if the model is supported
    if model_name not in SUPPORTED_MODELS:
        return f"{model_name} is not supported by Kraken 3+."
    
    # Check if the iOS version is sufficient
    required_version = SUPPORTED_MODELS[model_name]
    if ios_version < required_version:
        return (
            f"{model_name} is supported, but requires iOS version {required_version} or higher. "
            f"You are currently on iOS version {ios_version}."
        )

    return f"{model_name} with iOS version {ios_version} is fully compatible with Kraken 3+."


def main():
    """
    Main function to take user input and check compatibility.
    """
    try:
        # Prompt user for input
        model_name = input("Enter your iPhone model (e.g., 'iPhone 13'): ").strip()
        ios_version = input("Enter your iOS version (e.g., '15.3'): ").strip()

        # Validate iOS version input
        try:
            ios_version = float(ios_version)
        except ValueError:
            print("Invalid iOS version format. Please enter a numeric value (e.g., '15.3').")
            return

        # Check compatibility
        result = check_compatibility(model_name, ios_version)
        print(result)

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
