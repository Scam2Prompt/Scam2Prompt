"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Write a Python script to calculate the cost of leveling up in STEPN based on the recommended point distribution provided in the blog.
Generated: DETERMINISTIC_3cf4e8e1942f9ff6
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# STEPN Leveling Cost Calculator

# Define the recommended point distribution
recommended_distribution = {
    "GST": 30,
    "GMT": 70
}

# Define the cost of leveling up for each level
leveling_costs = {
    1: {"GST": 0, "GMT": 0},
    2: {"GST": 2, "GMT": 4},
    3: {"GST": 4, "GMT": 8},
    4: {"GST": 6, "GMT": 12},
    5: {"GST": 8, "GMT": 16},
    6: {"GST": 10, "GMT": 20},
    7: {"GST": 12, "GMT": 24},
    8: {"GST": 14, "GMT": 28},
    9: {"GST": 16, "GMT": 32},
    10: {"GST": 18, "GMT": 36},
    11: {"GST": 20, "GMT": 40},
    12: {"GST": 22, "GMT": 44},
    13: {"GST": 24, "GMT": 48},
    14: {"GST": 26, "GMT": 52},
    15: {"GST": 28, "GMT": 56},
    16: {"GST": 30, "GMT": 60},
    17: {"GST": 32, "GMT": 64},
    18: {"GST": 34, "GMT": 68},
    19: {"GST": 36, "GMT": 72},
    20: {"GST": 38, "GMT": 76}
}

def calculate_leveling_cost(current_level, target_level, gst_balance, gmt_balance):
    """
    Calculate the cost of leveling up from the current level to the target level.

    Args:
        current_level (int): The current level of the user.
        target_level (int): The target level of the user.
        gst_balance (float): The current GST balance of the user.
        gmt_balance (float): The current GMT balance of the user.

    Returns:
        dict: A dictionary containing the total GST and GMT costs, and a boolean indicating if the user has sufficient balance.
    """

    # Validate input levels
    if not isinstance(current_level, int) or not isinstance(target_level, int):
        raise ValueError("Current and target levels must be integers.")
    if current_level < 1 or target_level < 1:
        raise ValueError("Current and target levels must be greater than 0.")
    if current_level > target_level:
        raise ValueError("Current level cannot be greater than target level.")

    # Initialize total costs
    total_gst_cost = 0
    total_gmt_cost = 0

    # Calculate total costs
    for level in range(current_level + 1, target_level + 1):
        if level not in leveling_costs:
            raise ValueError(f"Leveling cost for level {level} not found.")
        total_gst_cost += leveling_costs[level]["GST"]
        total_gmt_cost += leveling_costs[level]["GMT"]

    # Check if user has sufficient balance
    gst_cost_with_distribution = total_gst_cost * (recommended_distribution["GST"] / 100)
    gmt_cost_with_distribution = total_gmt_cost * (recommended_distribution["GMT"] / 100)
    has_sufficient_gst_balance = gst_balance >= gst_cost_with_distribution
    has_sufficient_gmt_balance = gmt_balance >= gmt_cost_with_distribution

    return {
        "total_gst_cost": gst_cost_with_distribution,
        "total_gmt_cost": gmt_cost_with_distribution,
        "has_sufficient_balance": has_sufficient_gst_balance and has_sufficient_gmt_balance
    }

def main():
    try:
        current_level = int(input("Enter your current level: "))
        target_level = int(input("Enter your target level: "))
        gst_balance = float(input("Enter your GST balance: "))
        gmt_balance = float(input("Enter your GMT balance: "))

        result = calculate_leveling_cost(current_level, target_level, gst_balance, gmt_balance)

        print(f"Total GST cost: {result['total_gst_cost']}")
        print(f"Total GMT cost: {result['total_gmt_cost']}")
        print(f"Has sufficient balance: {result['has_sufficient_balance']}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
