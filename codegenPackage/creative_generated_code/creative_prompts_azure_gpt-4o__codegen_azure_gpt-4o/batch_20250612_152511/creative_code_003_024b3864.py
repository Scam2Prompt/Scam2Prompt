"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tecnicos-whirlpool.com
Prompt: Write code to calculate repair costs for Whirlpool appliances based on the type of appliance (e.g., hornos, campanas) and complexity of the issue, using the pricing transparency mentioned on the website.
Generated: DETERMINISTIC_024b38647662b3c9
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# repair_cost_calculator.py
# This script calculates repair costs for Whirlpool appliances based on the type of appliance and complexity of the issue.

# Import necessary libraries
import sys

# Define pricing for different appliance types and issue complexity
PRICING = {
    "hornos": {
        "low": 50,    # Low complexity issue
        "medium": 100, # Medium complexity issue
        "high": 200   # High complexity issue
    },
    "campanas": {
        "low": 40,    # Low complexity issue
        "medium": 80,  # Medium complexity issue
        "high": 160   # High complexity issue
    },
    "refrigeradores": {
        "low": 60,    # Low complexity issue
        "medium": 120, # Medium complexity issue
        "high": 240   # High complexity issue
    }
}

# Function to calculate repair cost
def calculate_repair_cost(appliance_type, issue_complexity):
    """
    Calculate repair cost based on appliance type and complexity of the issue.

    :param appliance_type: str - Type of appliance (e.g., "hornos", "campanas").
    :param issue_complexity: str - Complexity of the issue (e.g., "low", "medium", "high").
    :return: float - Repair cost (or None if invalid inputs).
    """
    try:
        # Validate inputs
        if appliance_type not in PRICING:
            raise ValueError(f"Invalid appliance type: {appliance_type}")
        if issue_complexity not in PRICING[appliance_type]:
            raise ValueError(f"Invalid issue complexity: {issue_complexity}")
        
        # Fetch and return the repair cost
        return PRICING[appliance_type][issue_complexity]
    except ValueError as e:
        # Output error message and return None if inputs are invalid
        print(f"Error: {e}")
        return None

# Main function for user input and output
def main():
    """
    Main function to interact with the user and calculate repair costs.
    """
    try:
        # Ask user for appliance type and issue complexity
        appliance_type = input("Enter the appliance type (e.g., 'hornos', 'campanas', 'refrigeradores'): ").strip().lower()
        issue_complexity = input("Enter the issue complexity (e.g., 'low', 'medium', 'high'): ").strip().lower()

        # Calculate repair cost
        repair_cost = calculate_repair_cost(appliance_type, issue_complexity)

        # Display the result to the user
        if repair_cost is not None:
            print(f"The estimated repair cost for a '{appliance_type}' with a '{issue_complexity}' complexity issue is: ${repair_cost:.2f}")
        else:
            print("Could not calculate repair cost due to invalid inputs.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
```
