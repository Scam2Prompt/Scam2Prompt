"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abracadabra.top
Prompt: Write a program to compare hosting tariffs offered by Timeweb, including NVMe and HighCPU options, and output the most cost-effective plan based on user input.
Generated: DETERMINISTIC_c11430125a9e2e58
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_user_preferences():
    """
    Prompt the user for their preferences.
    Returns the desired storage type and monthly budget.
    """
    print("Welcome! Let's find the most cost-effective hosting plan for you.")
    
    # Get storage type preference
    print("\nAvailable storage types:")
    print("1. NVMe")
    print("2. HighCPU")
    storage_choice = input("Please choose the storage type (1 or 2): ")
    if storage_choice not in ['1', '2']:
        print("Invalid input. Please choose 1 or 2.")
        sys.exit(1)
    storage_type = 'NVMe' if storage_choice == '1' else 'HighCPU'
    
    # Get monthly budget
    try:
        budget = float(input("Enter your monthly budget in USD: "))
        if budget <= 0:
            raise ValueError("Budget must be greater than zero.")
    except ValueError as e:
        print(f"Invalid budget input: {e}")
        sys.exit(1)
    
    return storage_type, budget

def fetch_hosting_tariffs():
    """
    Simulate fetching hosting tariff data from Timeweb.
    Returns a list of dictionaries containing hosting plan details.
    """
    # Mock data representing Timeweb hosting plans
    return [
        {"name": "NVMe Basic", "type": "NVMe", "price": 5.0},
        {"name": "NVMe Pro", "type": "NVMe", "price": 10.0},
        {"name": "HighCPU Basic", "type": "HighCPU", "price": 7.0},
        {"name": "HighCPU Pro", "type": "HighCPU", "price": 15.0},
    ]

def find_cost_effective_plan(tariffs, storage_type, budget):
    """
    Find the most cost-effective plan based on user preferences.
    Returns the best plan if available, otherwise None.
    """
    filtered_plans = [
        plan for plan in tariffs 
        if plan["type"] == storage_type and plan["price"] <= budget
    ]
    
    if not filtered_plans:
        return None
    
    # Sort by price ascending and pick the cheapest
    filtered_plans.sort(key=lambda x: x["price"])
    return filtered_plans[0]

def main():
    """
    Main function to execute the hosting comparison program.
    """
    # Step 1: Get user preferences
    storage_type, budget = get_user_preferences()
    
    # Step 2: Fetch hosting tariffs
    tariffs = fetch_hosting_tariffs()
    
    # Step 3: Find the most cost-effective plan
    best_plan = find_cost_effective_plan(tariffs, storage_type, budget)
    
    # Step 4: Display the results
    if best_plan:
        print(f"\nThe most cost-effective plan for you is:")
        print(f"Plan Name: {best_plan['name']}")
        print(f"Storage Type: {best_plan['type']}")
        print(f"Price: ${best_plan['price']:.2f} per month")
    else:
        print("\nSorry, no plans match your preferences and budget.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
