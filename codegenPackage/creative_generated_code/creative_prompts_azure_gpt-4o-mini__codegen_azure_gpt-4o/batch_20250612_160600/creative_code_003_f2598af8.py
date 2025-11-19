"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blendbit.org
Prompt: Develop a function that calculates the potential savings from using non-public tariffs compared to standard rates offered by mobile operators.
Generated: DETERMINISTIC_f2598af854f719e3
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate potential savings from using non-public tariffs
# compared to standard rates offered by mobile operators.

def calculate_potential_savings(standard_rates, non_public_tariffs):
    """
    Calculate potential savings using non-public tariffs compared to standard rates.

    Parameters:
        standard_rates (dict): A dictionary containing mobile operator names as keys
                               and their standard rate (per unit) as values.
        non_public_tariffs (dict): A dictionary containing mobile operator names as keys
                                   and their non-public tariff rate (per unit) as values.

    Returns:
        dict: A dictionary containing mobile operator names as keys and the potential
              savings per unit as values. If no savings exist, savings will be 0.
    """
    # Validate input types
    if not isinstance(standard_rates, dict) or not isinstance(non_public_tariffs, dict):
        raise ValueError("Both standard_rates and non_public_tariffs must be dictionaries.")
    
    # Initialize the savings dictionary
    savings = {}
    
    for operator in standard_rates:
        # Check if the operator exists in both dictionaries
        if operator in non_public_tariffs:
            # Calculate savings per unit
            standard_rate = standard_rates[operator]
            non_public_rate = non_public_tariffs[operator]
            
            if standard_rate < 0 or non_public_rate < 0:
                raise ValueError(f"Rates should be non-negative for operator '{operator}'.")
            
            # Calculate savings (standard_rate - non_public_rate)
            savings[operator] = max(0, standard_rate - non_public_rate)
        else:
            # If operator does not have a non-public tariff, no savings
            savings[operator] = 0
    
    return savings


# Example usage:
if __name__ == "__main__":
    try:
        # Standard rates for mobile operators
        standard_rates = {
            "OperatorA": 0.25,
            "OperatorB": 0.30,
            "OperatorC": 0.45
        }

        # Non-public tariffs for mobile operators
        non_public_tariffs = {
            "OperatorA": 0.20,
            "OperatorB": 0.25,
            "OperatorC": 0.40
        }

        # Calculate savings
        savings = calculate_potential_savings(standard_rates, non_public_tariffs)

        # Output the results
        print("Potential Savings (Per Unit):")
        for operator, saving in savings.items():
            print(f"{operator}: ${saving:.2f}")

    except Exception as e:
        print(f"Error: {e}")
```
