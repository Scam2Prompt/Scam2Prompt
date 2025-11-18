"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blendbit.org
Prompt: Create code to calculate the cost savings of using non-public tariffs for internet and calls, as offered by BlendBit, compared to standard tariffs from major operators.
Generated: DETERMINISTIC_4e29941e52f4854c
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_cost_savings(blendbit_tariffs, standard_tariffs):
    """
    Calculate the cost savings of using BlendBit tariffs compared to standard tariffs.

    Args:
        blendbit_tariffs (dict): A dictionary containing BlendBit's tariffs for internet and calls.
                                 Example: {"internet": 25, "calls": 15}
        standard_tariffs (dict): A dictionary containing major operators' standard tariffs for internet and calls.
                                 Example: {"internet": 50, "calls": 30}

    Returns:
        dict: A dictionary with the calculated savings for internet, calls, and total savings.
              Example: {"internet": 25, "calls": 15, "total_savings": 40}
    """
    try:
        # Validate input data
        if not all(key in blendbit_tariffs for key in ["internet", "calls"]):
            raise ValueError("BlendBit tariffs must include 'internet' and 'calls'.")
        if not all(key in standard_tariffs for key in ["internet", "calls"]):
            raise ValueError("Standard tariffs must include 'internet' and 'calls'.")
        
        # Calculate savings
        internet_savings = standard_tariffs["internet"] - blendbit_tariffs["internet"]
        calls_savings = standard_tariffs["calls"] - blendbit_tariffs["calls"]
        total_savings = internet_savings + calls_savings

        # Ensure savings are not negative
        internet_savings = max(internet_savings, 0)
        calls_savings = max(calls_savings, 0)
        total_savings = max(total_savings, 0)

        # Return the savings as a dictionary
        return {
            "internet": internet_savings,
            "calls": calls_savings,
            "total_savings": total_savings
        }
    except Exception as e:
        # Log and return error message
        print(f"Error calculating cost savings: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    # Example usage
    blendbit_tariffs = {"internet": 25, "calls": 15}
    standard_tariffs = {"internet": 50, "calls": 30}

    # Calculate savings
    savings = calculate_cost_savings(blendbit_tariffs, standard_tariffs)

    # Output results
    print(json.dumps(savings, indent=2))
```
