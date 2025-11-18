"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Write Python code to calculate the cost-effectiveness of using Calmar Transport's trailer drop service, factoring in reduced downtime and labor costs as described on their website.
Generated: DETERMINISTIC_ff9ed084d7683f22
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cost_effectiveness(downtime_hours_saved, labor_rate_per_hour, trailer_drop_service_cost):
    """
    Calculate the cost-effectiveness of using Calmar Transport's trailer drop service.

    Args:
        downtime_hours_saved (float): Number of hours saved by reducing downtime.
        labor_rate_per_hour (float): Labor cost per hour.
        trailer_drop_service_cost (float): Cost of the trailer drop service.

    Returns:
        float: Net savings or cost-effectiveness.
    """
    try:
        # Calculate the monetary value of downtime saved
        cost_saved_from_downtime = downtime_hours_saved * labor_rate_per_hour
        
        # Calculate the net savings
        net_savings = cost_saved_from_downtime - trailer_drop_service_cost
        
        return net_savings
    except TypeError as e:
        raise ValueError("Invalid input type. Please ensure all inputs are numeric.") from e


def main():
    """
    Main function to collect user input and calculate the cost-effectiveness.
    """
    print("Calmar Transport Trailer Drop Service Cost-Effectiveness Calculator\n")
    
    try:
        # Collect user input
        downtime_hours_saved = float(input("Enter the downtime hours saved (e.g., 8): "))
        labor_rate_per_hour = float(input("Enter the labor rate per hour (e.g., 50): "))
        trailer_drop_service_cost = float(input("Enter the cost of the trailer drop service (e.g., 200): "))
        
        # Calculate the cost-effectiveness
        net_savings = calculate_cost_effectiveness(downtime_hours_saved, labor_rate_per_hour, trailer_drop_service_cost)
        
        # Display the result
        if net_savings > 0:
            print(f"\nThe service is cost-effective! Net savings: ${net_savings:.2f}")
        elif net_savings == 0:
            print("\nThe service breaks even. No net savings or loss.")
        else:
            print(f"\nThe service is not cost-effective. Net loss: ${abs(net_savings):.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


# Entry point for the script
if __name__ == "__main__":
    main()
```
