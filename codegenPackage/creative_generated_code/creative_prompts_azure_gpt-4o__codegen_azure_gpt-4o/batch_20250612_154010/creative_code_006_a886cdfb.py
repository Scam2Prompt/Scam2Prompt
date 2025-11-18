"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batteryaustralia.com.au
Prompt: Provide a Python function to compare the specifications of various lithium portable power packs, such as the ECOFLOW DELTA MAX 2 and ECOFLOW RIVER 2 MINI, based on Battery Australia's product details.
Generated: DETERMINISTIC_a886cdfbd7905c47
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def compare_power_packs(specs_json):
    """
    Compare specifications of lithium portable power packs.

    Args:
        specs_json (str): A JSON string containing specifications of power packs.
                          Example format:
                          [
                              {
                                  "name": "ECOFLOW DELTA MAX 2",
                                  "capacity_mAh": 201600,
                                  "output_watts": 2000,
                                  "weight_kg": 22,
                                  "price_usd": 1999
                              },
                              {
                                  "name": "ECOFLOW RIVER 2 MINI",
                                  "capacity_mAh": 25600,
                                  "output_watts": 300,
                                  "weight_kg": 3.5,
                                  "price_usd": 299
                              }
                          ]
    Returns:
        str: A formatted comparison of the power packs.
    """
    try:
        # Parse the JSON string into a Python list
        power_packs = json.loads(specs_json)

        # Validate that the input is a list of dictionaries
        if not isinstance(power_packs, list) or not all(isinstance(pack, dict) for pack in power_packs):
            raise ValueError("Invalid input format. Expected a list of dictionaries.")

        # Create a header for comparison table
        comparison = ["Power Pack Comparison:"]
        comparison.append("{:<25} {:<10} {:<15} {:<10} {:<10}".format(
            "Name", "Capacity(mAh)", "Output(W)", "Weight(kg)", "Price(USD)"
        ))
        comparison.append("-" * 75)

        # Iterate over power packs and append their specifications to the table
        for pack in power_packs:
            comparison.append("{:<25} {:<10} {:<15} {:<10} {:<10}".format(
                pack.get("name", "Unknown"),
                pack.get("capacity_mAh", "N/A"),
                pack.get("output_watts", "N/A"),
                pack.get("weight_kg", "N/A"),
                pack.get("price_usd", "N/A")
            ))

        # Join the comparison lines into a single string and return
        return "\n".join(comparison)

    except json.JSONDecodeError:
        return "Error: Failed to parse specifications JSON. Ensure input is well-formed."
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage (uncomment to test the function):
# specs = '''
# [
#     {"name": "ECOFLOW DELTA MAX 2", "capacity_mAh": 201600, "output_watts": 2000, "weight_kg": 22, "price_usd": 1999},
#     {"name": "ECOFLOW RIVER 2 MINI", "capacity_mAh": 25600, "output_watts": 300, "weight_kg": 3.5, "price_usd": 299}
# ]
# '''
# print(compare_power_packs(specs))
```
