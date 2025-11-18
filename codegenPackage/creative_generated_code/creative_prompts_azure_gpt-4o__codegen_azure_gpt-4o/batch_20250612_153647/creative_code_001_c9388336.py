"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mining-equipment.vercel.app
Prompt: Generate a script to calculate hashpower for a mining pool on the Solana blockchain, factoring in the increasing cost of mining equipment every 385 machines minted.
Generated: DETERMINISTIC_c93883366c40b6c3
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_hashpower(machine_count, base_hashpower, equipment_cost_increase_factor=1.2, cost_increase_interval=385):
    """
    Calculate the total hashpower of a mining pool on the Solana blockchain.

    Parameters:
    - machine_count (int): Total number of mining machines in the pool.
    - base_hashpower (float): Hashpower provided by each machine in H/s.
    - equipment_cost_increase_factor (float): Factor by which equipment cost increases every interval. Default is 1.2.
    - cost_increase_interval (int): Number of machines after which equipment cost increases. Default is 385.

    Returns:
    - total_hashpower (float): Total hashpower of the mining pool.
    """
    if machine_count <= 0:
        raise ValueError("Machine count must be greater than zero.")
    if base_hashpower <= 0:
        raise ValueError("Base hashpower must be greater than zero.")
    if equipment_cost_increase_factor <= 0:
        raise ValueError("Equipment cost increase factor must be greater than zero.")
    if cost_increase_interval <= 0:
        raise ValueError("Cost increase interval must be greater than zero.")

    total_hashpower = 0.0
    remaining_machines = machine_count
    interval_start_cost = base_hashpower

    # Loop through intervals of machines minted
    while remaining_machines > 0:
        current_interval_machines = min(remaining_machines, cost_increase_interval)
        total_hashpower += current_interval_machines * interval_start_cost

        # Update remaining machines and hashpower cost for the next interval
        remaining_machines -= current_interval_machines
        interval_start_cost *= equipment_cost_increase_factor

    return total_hashpower


def main():
    """
    Main function to calculate the hashpower for a given mining pool configuration.
    Modify the values below to test different configurations.
    """
    try:
        # Example configuration
        machine_count = 1000  # Total number of machines in the mining pool
        base_hashpower = 50.0  # Base hashpower per machine in H/s

        # Calculate total hashpower
        total_hashpower = calculate_hashpower(machine_count, base_hashpower)

        # Display the result
        print(f"Total Hashpower for {machine_count} machines: {total_hashpower:.2f} H/s")
    except Exception as e:
        # Handle errors and display appropriate messages
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
