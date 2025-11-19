"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mining-equipment.vercel.app
Prompt: Generate a script that calculates the cost of mining equipment based on the minting of machines for Bitcoin on SOL.
Generated: DETERMINISTIC_76b75a2d866f6539
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_mining_cost(machine_cost, power_cost_per_kw, power_usage_kw_per_machine, hours_per_day, days_per_month):
    """
    Calculates the monthly cost of running a Bitcoin mining machine.
    
    Parameters:
        machine_cost (float): Cost of one mining machine in USD.
        power_cost_per_kw (float): Cost of power per kilowatt-hour (kWh) in USD.
        power_usage_kw_per_machine (float): Power usage of one machine in kilowatts (kW).
        hours_per_day (int): Number of hours the machine runs per day.
        days_per_month (int): Number of days the machine runs per month.
    
    Returns:
        total_monthly_cost (float): Total monthly cost of running the machine.
    """
    try:
        # Calculate power cost per machine per month
        monthly_power_cost = power_cost_per_kw * power_usage_kw_per_machine * hours_per_day * days_per_month
        
        # Total monthly cost = upfront machine cost + monthly power cost
        total_monthly_cost = machine_cost + monthly_power_cost
        
        return total_monthly_cost
    except Exception as e:
        print(f"An error occurred during calculation: {e}")
        sys.exit(1)

def main():
    """
    Main function to take input from the user and calculate the cost of mining equipment.
    """
    try:
        print("Bitcoin Mining Equipment Cost Calculator")
        
        # Gather input from the user
        machine_cost = float(input("Enter the cost of one mining machine (USD): "))
        power_cost_per_kw = float(input("Enter the cost of power per kilowatt-hour (USD): "))
        power_usage_kw_per_machine = float(input("Enter the power usage of one machine (kW): "))
        hours_per_day = int(input("Enter the number of hours per day the machine runs: "))
        days_per_month = int(input("Enter the number of days per month the machine runs: "))
        
        # Calculate total monthly cost
        total_cost = calculate_mining_cost(machine_cost, power_cost_per_kw, power_usage_kw_per_machine, hours_per_day, days_per_month)
        
        print(f"\nThe total monthly cost of running one mining machine is: ${total_cost:.2f}")
    except ValueError:
        print("Invalid input provided. Please ensure you enter numbers for all fields.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
