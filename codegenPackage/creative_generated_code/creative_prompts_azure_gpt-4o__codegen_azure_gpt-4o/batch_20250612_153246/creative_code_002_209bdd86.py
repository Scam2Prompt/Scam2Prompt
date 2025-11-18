"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pahubel.com
Prompt: Create a Python script to calculate the cost estimation for healthcare facility renovations, factoring in design, construction, and legal requirements as outlined by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_209bdd86377bc353
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def input_positive_float(prompt):
    """
    Get a positive floating-point number from user input.
    
    Args:
        prompt (str): Input prompt message.

    Returns:
        float: A positive floating-point number.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def calculate_total_cost(design_cost, construction_cost, legal_cost):
    """
    Calculate the total estimated cost for healthcare facility renovations.

    Args:
        design_cost (float): Cost of design phase.
        construction_cost (float): Cost of construction phase.
        legal_cost (float): Cost of handling legal requirements.

    Returns:
        float: The total estimated cost.
    """
    return design_cost + construction_cost + legal_cost

def main():
    """
    Main function to calculate healthcare facility renovation cost.
    Includes design, construction, and legal requirements.
    """
    print("Healthcare Facility Renovation Cost Estimation")
    print("------------------------------------------------")

    # Input costs for each component of the renovation project
    try:
        design_cost = input_positive_float("Enter the estimated cost for design phase (€): ")
        construction_cost = input_positive_float("Enter the estimated cost for construction phase (€): ")
        legal_cost = input_positive_float("Enter the estimated cost for legal requirements (€): ")
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
        sys.exit(1)

    # Calculate total cost
    total_cost = calculate_total_cost(design_cost, construction_cost, legal_cost)

    # Display total cost
    print("\n------------------------------------------------")
    print(f"Total Estimated Renovation Cost: €{total_cost:.2f}")
    print("------------------------------------------------")

if __name__ == "__main__":
    main()
```
