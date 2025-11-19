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
import json
import requests

# Define the supported iPhone models for the Kraken 3+ app
SUPPORTED_MODELS = {
    "iPhone 13": 2021,
    "iPhone 13 mini": 2021,
    "iPhone 13 Pro": 2021,
    "iPhone 13 Pro Max": 2021,
    "iPhone 12": 2020,
    "iPhone 12 mini": 2020,
    "iPhone 12 Pro": 2020,
    "iPhone 12 Pro Max": 2020,
    "iPhone 11": 2019,
    "iPhone 11 Pro": 2019,
    "iPhone 11 Pro Max": 2019,
    "iPhone SE (2nd generation)": 2020,
    "iPhone XR": 2018,
    "iPhone XS": 2018,
    "iPhone XS Max": 2018,
    # Add more supported models as needed
}

# Function to check compatibility
def check_compatibility(model):
    """Check if the given iPhone model is compatible with the Kraken 3+ app.
    
    Args:
        model (str): The iPhone model to check.
        
    Returns:
        bool: True if the model is supported, False otherwise.
    """
    return model in SUPPORTED_MODELS

# Main function to run the compatibility check
def main():
    """Main function to execute the compatibility checks."""
    # Sample iPhone models to check
    models_to_check = [
        "iPhone 13",
        "iPhone 8",
        "iPhone 12",
        "iPhone SE (1st generation)",
        "iPhone 14 Pro"
    ]
    
    results = {}
    
    for model in models_to_check:
        try:
            # Check compatibility and store the result
            results[model] = check_compatibility(model)
        except Exception as e:
            # Handle unexpected exceptions
            print(f"Error checking compatibility for {model}: {e}")
            results[model] = None

    # Output the results
    print("Compatibility Results:")
    for model, is_compatible in results.items():
        if is_compatible is None:
            print(f"{model}: Check failed due to an error.")
        else:
            status = "Compatible" if is_compatible else "Not Compatible"
            print(f"{model}: {status}")

if __name__ == "__main__":
    main()
```
