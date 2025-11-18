"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicbffa3pntrrd6o7gbifdctk2ingttjnunx3qdqyzr27guaqcdgbi.ipfs.dweb.link
Prompt: Create a program to calculate monthly costs for renting AI nodes from NodeAI, based on GPU types and pricing provided (e.g., $0.85/hr for A100).
Generated: DETERMINISTIC_69b08ae00d57ce41
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate monthly costs for renting AI nodes from NodeAI

from datetime import timedelta

def calculate_monthly_cost(gpu_type, hours_per_day, days_per_month=30):
    """
    Calculate the monthly cost for renting AI nodes based on GPU type and hours used per day.

    Args:
        gpu_type (str): The type of GPU (e.g., 'A100').
        hours_per_day (float): Number of hours the GPU nodes are used per day.
        days_per_month (int, optional): Number of days in the month. Defaults to 30.

    Returns:
        float: Monthly cost for renting the GPU nodes.
    """
    # Pricing dictionary for GPU hourly rates
    gpu_pricing = {
        'A100': 0.85,  # $0.85/hour
        'V100': 0.60,  # $0.60/hour
        'T4': 0.35,    # $0.35/hour
    }

    # Check if the GPU type exists in pricing dictionary
    if gpu_type not in gpu_pricing:
        raise ValueError(f"Invalid GPU type '{gpu_type}'. Available types: {', '.join(gpu_pricing.keys())}")

    # Calculate monthly cost
    hourly_rate = gpu_pricing[gpu_type]
    total_hours = hours_per_day * days_per_month
    monthly_cost = total_hours * hourly_rate

    return monthly_cost


def main():
    """
    Main function to interact with the user and calculate costs.
    """
    print("Welcome to the NodeAI Monthly Cost Calculator!")
    print("Available GPU types: A100, V100, T4")
    
    try:
        # Get user input for GPU type and hours usage
        gpu_type = input("Enter GPU type (e.g., A100): ").strip()
        hours_per_day = float(input("Enter hours per day the GPU nodes are used: ").strip())

        if hours_per_day < 0 or hours_per_day > 24:
            raise ValueError("Hours per day must be between 0 and 24.")

        # Calculate and display the cost
        monthly_cost = calculate_monthly_cost(gpu_type, hours_per_day)
        print(f"Monthly cost for renting {gpu_type} nodes: ${monthly_cost:.2f}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the program
    main()
```
