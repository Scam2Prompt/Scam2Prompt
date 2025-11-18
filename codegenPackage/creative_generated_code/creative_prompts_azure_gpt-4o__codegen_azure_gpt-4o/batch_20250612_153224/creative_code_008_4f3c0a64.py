"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Write a Python program to generate a price estimate for title insurance services based on property details, leveraging the consultation process described on the Superior Title Montana website.
Generated: DETERMINISTIC_4f3c0a64edd5dd11
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_property_details():
    """
    Function to collect property details from the user.
    Returns:
        dict: Dictionary containing the user-provided property details.
    """
    print("Enter Property Details:")
    try:
        property_value = float(input("Property Value (in USD): ").strip())
        loan_amount = float(input("Loan Amount (in USD): ").strip())
        property_type = input("Property Type (Residential/Commercial): ").strip().lower()
        
        if property_type not in ['residential', 'commercial']:
            raise ValueError("Invalid property type. Accepted values: Residential, Commercial.")
        
        return {
            "property_value": property_value,
            "loan_amount": loan_amount,
            "property_type": property_type
        }
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def calculate_title_insurance(property_details):
    """
    Function to calculate price estimate for title insurance based on property details.
    Args:
        property_details (dict): Dictionary containing property details.
    Returns:
        float: Estimated price for title insurance.
    """
    try:
        base_rate = 0.005  # Base rate: 0.5%
        loan_rate = 0.004  # Loan rate: 0.4%
        
        # Base calculation for title insurance
        insurance_cost = property_details["property_value"] * base_rate
        
        # Additional cost if there's a loan involved
        if property_details["loan_amount"] > 0:
            insurance_cost += property_details["loan_amount"] * loan_rate
        
        # Adjustments based on property type
        if property_details["property_type"] == "commercial":
            insurance_cost *= 1.2  # Commercial properties incur a 20% surcharge
        
        return insurance_cost
    except Exception as e:
        print(f"Error during calculation: {e}")
        sys.exit(1)

def main():
    """
    Main function to run the program. It collects property details, calculates the 
    estimated price for title insurance, and displays the results.
    """
    print("Welcome to Superior Title Insurance Price Estimator!")
    
    # Step 1: Get property details from the user
    property_details = get_property_details()
    
    # Step 2: Calculate title insurance price
    estimated_cost = calculate_title_insurance(property_details)
    
    # Step 3: Display the estimated cost
    print("\nPrice Estimate:")
    print(f"Estimated Title Insurance Cost: ${estimated_cost:.2f}")
    print("\nThank you for using the Superior Title Insurance Price Estimator!")

if __name__ == "__main__":
    # Entry point of the program
    main()
```
