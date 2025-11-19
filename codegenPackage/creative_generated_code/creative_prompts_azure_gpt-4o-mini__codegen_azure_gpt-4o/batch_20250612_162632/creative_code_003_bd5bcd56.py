"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buzo-lola.pages.dev
Prompt: Generate a Python script that calculates potential savings from participating in the Tesla Reward Programme for electric car owners.
Generated: DETERMINISTIC_bd5bcd56f46e4a6d
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_savings(reward_points, electricity_rate, miles_driven, efficiency_miles_per_kWh):
    """
    Calculate potential savings from Tesla Reward Programme.

    Parameters:
    reward_points (int): Total reward points accumulated.
    electricity_rate (float): Cost of electricity per kWh in dollars.
    miles_driven (float): Total miles driven in a given time period.
    efficiency_miles_per_kWh (float): Car's efficiency in miles per kWh.

    Returns:
    dict: A dictionary containing potential savings and equivalent reward benefits.
    """
    try:
        # Validate input types
        if reward_points < 0 or electricity_rate < 0 or miles_driven < 0 or efficiency_miles_per_kWh <= 0:
            raise ValueError("Input values must be non-negative, and efficiency must be greater than zero.")

        # Calculate total energy consumption in kWh
        energy_consumed_kWh = miles_driven / efficiency_miles_per_kWh

        # Calculate energy cost without rewards
        total_cost = energy_consumed_kWh * electricity_rate

        # Calculate savings from reward points
        # Assuming 1 reward point equals $0.01 in savings (adjust this conversion rate as needed)
        reward_savings = reward_points * 0.01

        # Net cost after applying rewards
        net_cost = max(total_cost - reward_savings, 0)  # Ensure net cost is not negative

        return {
            "total_cost_without_rewards": round(total_cost, 2),
            "reward_savings": round(reward_savings, 2),
            "net_cost_with_rewards": round(net_cost, 2),
        }

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate savings.
    """
    try:
        print("Tesla Reward Programme Savings Calculator")

        # Gather inputs from the user
        reward_points = int(input("Enter the number of reward points you have: "))
        electricity_rate = float(input("Enter your electricity rate ($/kWh): "))
        miles_driven = float(input("Enter the total miles driven: "))
        efficiency_miles_per_kWh = float(input("Enter your car's efficiency (miles/kWh): "))

        # Perform calculations
        savings = calculate_savings(reward_points, electricity_rate, miles_driven, efficiency_miles_per_kWh)

        if savings:
            print("\nSavings Summary:")
            print(f"Total Energy Cost without Rewards: ${savings['total_cost_without_rewards']}")
            print(f"Reward Savings: ${savings['reward_savings']}")
            print(f"Net Energy Cost with Rewards: ${savings['net_cost_with_rewards']}")
        else:
            print("Unable to calculate savings due to input errors.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
