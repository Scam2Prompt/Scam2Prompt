"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullport.net
Prompt: Create a function that calculates the total cost of purchasing multiple types of HDMI cables from FullPort, considering different lengths and brands.
Generated: DETERMINISTIC_752a601f266334fa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for error handling
from typing import List, Dict

def calculate_total_cost(hdmi_cables: List[Dict[str, str]]) -> float:
    """
    Calculates the total cost of purchasing HDMI cables based on their length, brand, and quantity.

    Parameters:
        hdmi_cables (List[Dict[str, str]]): A list of dictionaries, where each dictionary represents
        a type of HDMI cable with keys:
            - 'brand' (str): The brand of the HDMI cable.
            - 'length' (str): The length of the HDMI cable (e.g., "1m", "2m").
            - 'quantity' (int): The number of units being purchased.

    Returns:
        float: The total cost of all HDMI cables purchased.

    Raises:
        ValueError: If any required key is missing or has an invalid value.
    """
    # Pricing for different lengths and brands
    pricing = {
        "FullPort": {
            "1m": 5.99,
            "2m": 7.99,
            "5m": 12.99,
            "10m": 19.99
        },
        "UltraHD": {
            "1m": 8.49,
            "2m": 11.49,
            "5m": 16.49,
            "10m": 24.49
        },
        "PremiumConnect": {
            "1m": 10.99,
            "2m": 14.99,
            "5m": 20.99,
            "10m": 31.99
        }
    }

    # Initialize total cost
    total_cost = 0.0

    # Loop through each HDMI cable entry in the input list
    for cable in hdmi_cables:
        try:
            # Extract required values
            brand = cable['brand']
            length = cable['length']
            quantity = int(cable['quantity'])  # Ensure quantity is an integer

            # Validate brand and length
            if brand not in pricing:
                raise ValueError(f"Invalid brand '{brand}' provided.")
            if length not in pricing[brand]:
                raise ValueError(f"Invalid length '{length}' provided for brand '{brand}'.")

            # Calculate cost for this type of HDMI cable
            cost_per_unit = pricing[brand][length]
            total_cost += cost_per_unit * quantity
        except KeyError as e:
            raise ValueError(f"Missing required key: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid value: {e}")
        except Exception as e:
            # Catch any unexpected errors
            raise RuntimeError(f"An unexpected error occurred: {e}")

    return round(total_cost, 2)  # Round to 2 decimal places for currency formatting


# Example usage
if __name__ == "__main__":
    # Input: List of HDMI cables purchased
    hdmi_cables = [
        {"brand": "FullPort", "length": "2m", "quantity": 3},
        {"brand": "UltraHD", "length": "5m", "quantity": 1},
        {"brand": "PremiumConnect", "length": "1m", "quantity": 2}
    ]

    try:
        total = calculate_total_cost(hdmi_cables)
        print(f"Total cost: ${total}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
```
