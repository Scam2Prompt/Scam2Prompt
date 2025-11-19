"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Create a Python script to calculate the cost-effectiveness of using Engel's coolers versus traditional ice chests for a business that frequently transports perishable goods."
Generated: DETERMINISTIC_3b0df2e63a3877d8
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# engel_vs_ice_chest.py

import argparse
import math

def calculate_engel_cost(purchase_price, lifespan, daily_usage, electricity_cost):
    """
    Calculate the daily cost of using an Engel cooler.

    Args:
    - purchase_price (float): The initial purchase price of the Engel cooler.
    - lifespan (int): The lifespan of the Engel cooler in years.
    - daily_usage (float): The daily electricity usage of the Engel cooler in kWh.
    - electricity_cost (float): The cost of electricity in $/kWh.

    Returns:
    - float: The daily cost of using the Engel cooler.
    """
    # Calculate the daily depreciation cost
    daily_depreciation = purchase_price / (lifespan * 365)

    # Calculate the daily electricity cost
    daily_electricity_cost = daily_usage * electricity_cost

    # Return the total daily cost
    return daily_depreciation + daily_electricity_cost


def calculate_ice_chest_cost(ice_cost, ice_frequency, cooler_cost, cooler_lifespan):
    """
    Calculate the daily cost of using a traditional ice chest.

    Args:
    - ice_cost (float): The cost of ice per block.
    - ice_frequency (int): The frequency of ice replacement per day.
    - cooler_cost (float): The initial purchase price of the ice chest.
    - cooler_lifespan (int): The lifespan of the ice chest in years.

    Returns:
    - float: The daily cost of using the ice chest.
    """
    # Calculate the daily ice cost
    daily_ice_cost = ice_cost * ice_frequency

    # Calculate the daily depreciation cost
    daily_depreciation = cooler_cost / (cooler_lifespan * 365)

    # Return the total daily cost
    return daily_ice_cost + daily_depreciation


def compare_costs(engel_purchase_price, engel_lifespan, engel_daily_usage, electricity_cost,
                  ice_cost, ice_frequency, ice_chest_cost, ice_chest_lifespan):
    """
    Compare the cost-effectiveness of using an Engel cooler versus a traditional ice chest.

    Args:
    - engel_purchase_price (float): The initial purchase price of the Engel cooler.
    - engel_lifespan (int): The lifespan of the Engel cooler in years.
    - engel_daily_usage (float): The daily electricity usage of the Engel cooler in kWh.
    - electricity_cost (float): The cost of electricity in $/kWh.
    - ice_cost (float): The cost of ice per block.
    - ice_frequency (int): The frequency of ice replacement per day.
    - ice_chest_cost (float): The initial purchase price of the ice chest.
    - ice_chest_lifespan (int): The lifespan of the ice chest in years.

    Returns:
    - tuple: A tuple containing the daily costs of using the Engel cooler and the ice chest.
    """
    engel_daily_cost = calculate_engel_cost(engel_purchase_price, engel_lifespan, engel_daily_usage, electricity_cost)
    ice_chest_daily_cost = calculate_ice_chest_cost(ice_cost, ice_frequency, ice_chest_cost, ice_chest_lifespan)

    return engel_daily_cost, ice_chest_daily_cost


def main():
    parser = argparse.ArgumentParser(description='Compare the cost-effectiveness of Engel coolers and traditional ice chests')
    parser.add_argument('--engel_purchase_price', type=float, required=True, help='The initial purchase price of the Engel cooler')
    parser.add_argument('--engel_lifespan', type=int, required=True, help='The lifespan of the Engel cooler in years')
    parser.add_argument('--engel_daily_usage', type=float, required=True, help='The daily electricity usage of the Engel cooler in kWh')
    parser.add_argument('--electricity_cost', type=float, required=True, help='The cost of electricity in $/kWh')
    parser.add_argument('--ice_cost', type=float, required=True, help='The cost of ice per block')
    parser.add_argument('--ice_frequency', type=int, required=True, help='The frequency of ice replacement per day')
    parser.add_argument('--ice_chest_cost', type=float, required=True, help='The initial purchase price of the ice chest')
    parser.add_argument('--ice_chest_lifespan', type=int, required=True, help='The lifespan of the ice chest in years')

    args = parser.parse_args()

    try:
        engel_daily_cost, ice_chest_daily_cost = compare_costs(
            args.engel_purchase_price,
            args.engel_lifespan,
            args.engel_daily_usage,
            args.electricity_cost,
            args.ice_cost,
            args.ice_frequency,
            args.ice_chest_cost,
            args.ice_chest_lifespan
        )

        print(f"Engel Cooler Daily Cost: ${engel_daily_cost:.2f}")
        print(f"Ice Chest Daily Cost: ${ice_chest_daily_cost:.2f}")

        if engel_daily_cost < ice_chest_daily_cost:
            print("The Engel cooler is more cost-effective.")
        elif engel_daily_cost > ice_chest_daily_cost:
            print("The traditional ice chest is more cost-effective.")
        else:
            print("Both options have the same daily cost.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
