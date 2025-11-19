"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiofibers.com
Prompt: Develop a function that compares JioFiber's broadband plans in different cities like Bhubaneswar and Guwahati based on speed and price.
Generated: DETERMINISTIC_1ff305670018bc54
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def compare_jiofiber_plans(city1, city2):
    """
    Compare JioFiber broadband plans between two cities based on speed and price.

    Parameters:
    city1 (str): Name of the first city to compare (e.g., "Bhubaneswar").
    city2 (str): Name of the second city to compare (e.g., "Guwahati").

    Returns:
    dict: A comparison result containing the best plans for each speed tier.
    """

    # Mock data for broadband plans in two cities
    # In production, this data would be fetched from a reliable API or database
    broadband_data = {
        "Bhubaneswar": [
            {"plan_name": "Basic", "speed": 100, "price": 399},
            {"plan_name": "Silver", "speed": 300, "price": 699},
            {"plan_name": "Gold", "speed": 500, "price": 999},
        ],
        "Guwahati": [
            {"plan_name": "Basic", "speed": 100, "price": 349},
            {"plan_name": "Silver", "speed": 300, "price": 749},
            {"plan_name": "Gold", "speed": 500, "price": 949},
        ],
    }

    # Error handling: Check if cities exist in the mock data
    if city1 not in broadband_data:
        raise ValueError(f"City '{city1}' not found in broadband data.")
    if city2 not in broadband_data:
        raise ValueError(f"City '{city2}' not found in broadband data.")

    # Extract plans for the given cities
    city1_plans = broadband_data[city1]
    city2_plans = broadband_data[city2]

    # Create a dictionary to store the comparison result
    comparison_result = {}

    # Compare plans based on speed tiers
    for plan1 in city1_plans:
        for plan2 in city2_plans:
            if plan1['speed'] == plan2['speed']:
                # Determine the better plan based on price
                if plan1['price'] < plan2['price']:
                    comparison_result[plan1['speed']] = {
                        "better_plan": plan1,
                        "city": city1
                    }
                else:
                    comparison_result[plan2['speed']] = {
                        "better_plan": plan2,
                        "city": city2
                    }

    # Return the comparison result
    return comparison_result


# Example usage
if __name__ == "__main__":
    try:
        city1 = "Bhubaneswar"
        city2 = "Guwahati"
        result = compare_jiofiber_plans(city1, city2)
        print(json.dumps(result, indent=4))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
