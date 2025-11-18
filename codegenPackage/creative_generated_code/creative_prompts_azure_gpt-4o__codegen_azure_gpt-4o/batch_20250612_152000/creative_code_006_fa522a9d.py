"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiofibers.com
Prompt: Write code to simulate a user selecting a JioFiber plan and calculate the total cost for annual prepaid broadband plans in 2025.
Generated: DETERMINISTIC_fa522a9dad5f6803
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to simulate a user selecting a JioFiber broadband plan and calculate the total cost for annual prepaid plans.
# Written in Python

# Define the available JioFiber plans
class JioFiberPlan:
    def __init__(self, name, speed_mbps, monthly_cost):
        """
        Initialize the JioFiber plan details
        :param name: Name of the plan
        :param speed_mbps: Internet speed in Mbps
        :param monthly_cost: Monthly cost in INR
        """
        self.name = name
        self.speed_mbps = speed_mbps
        self.monthly_cost = monthly_cost

# List of available JioFiber plans for 2025
available_plans = [
    JioFiberPlan("Bronze", 30, 399), 
    JioFiberPlan("Silver", 100, 699), 
    JioFiberPlan("Gold", 300, 999),
    JioFiberPlan("Diamond", 500, 1499),
    JioFiberPlan("Platinum", 1000, 2499)
]

def display_plans():
    """
    Display available JioFiber plans to the user.
    """
    print("Available JioFiber Broadband Plans for 2025:")
    for idx, plan in enumerate(available_plans):
        print(f"{idx + 1}. {plan.name} Plan - {plan.speed_mbps} Mbps - ₹{plan.monthly_cost} per month")

def calculate_annual_cost(selected_plan):
    """
    Calculate the total annual cost for the selected plan.
    Includes a 10% discount for annual prepaid subscriptions.
    :param selected_plan: The JioFiberPlan object selected by the user
    :return: Annual cost after discount
    """
    annual_cost_without_discount = selected_plan.monthly_cost * 12
    discount = annual_cost_without_discount * 0.10
    annual_cost_with_discount = annual_cost_without_discount - discount
    return annual_cost_with_discount

def main():
    """
    Main function to simulate selecting a JioFiber plan and calculating the annual cost.
    """
    try:
        # Display available plans
        display_plans()
        
        # Prompt the user to select a plan
        user_choice = int(input("Enter the number corresponding to the plan you want to select: "))
        
        # Validate user choice
        if user_choice < 1 or user_choice > len(available_plans):
            print("Invalid choice. Please run the program again and select a valid plan.")
            return
        
        # Get the selected plan
        selected_plan = available_plans[user_choice - 1]
        
        # Calculate the annual cost
        annual_cost = calculate_annual_cost(selected_plan)
        
        # Display the result
        print(f"\nYou selected the {selected_plan.name} Plan.")
        print(f"Monthly Cost: ₹{selected_plan.monthly_cost}")
        print(f"Annual Cost (after 10% discount): ₹{annual_cost:.2f}")
    
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a number corresponding to the plan.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
