"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script to simulate notarial expenses for property sales in Bogotá, Colombia, using the parameters provided by Inmobiliaria Capri's simulator tool.
Generated: DETERMINISTIC_44cdc3f92bd86b6d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_notarial_expenses(property_value, is_new_property, buyer_is_first_time, notary_fee_percentage=0.3):
    """
    Calculate notarial expenses for property sales in Bogotá, Colombia.

    Parameters:
    - property_value (float): The value of the property in COP.
    - is_new_property (bool): Flag indicating whether the property is new or not.
    - buyer_is_first_time (bool): Flag indicating whether the buyer is a first-time buyer.
    - notary_fee_percentage (float): Notary fee percentage (default is 0.3% of property value).

    Returns:
    - dict: A dictionary containing detailed breakdown of expenses.
    """

    try:
        if property_value <= 0:
            raise ValueError("Property value must be greater than zero.")
        
        # Base notary fee calculation
        notary_fee = property_value * (notary_fee_percentage / 100)
        
        # Apply discount for first-time buyers
        first_time_discount = 0.1 if buyer_is_first_time else 0  # 10% discount for first-time buyers
        notary_fee_discounted = notary_fee * (1 - first_time_discount)
        
        # Additional costs for new properties
        new_property_surcharge = 0.02 if is_new_property else 0  # 2% surcharge for new properties
        new_property_cost = property_value * new_property_surcharge
        
        # Total expenses
        total_expenses = notary_fee_discounted + new_property_cost
        
        # Detailed breakdown
        return {
            "Property Value (COP)": property_value,
            "Notary Base Fee (COP)": round(notary_fee, 2),
            "First Time Buyer Discount (%)": first_time_discount * 100,
            "Notary Fee After Discount (COP)": round(notary_fee_discounted, 2),
            "New Property Surcharge (COP)": round(new_property_cost, 2),
            "Total Expenses (COP)": round(total_expenses, 2)
        }
    
    except ValueError as ve:
        # Error handling for invalid input
        return {"error": str(ve)}
    except Exception as e:
        # Catch-all for unexpected errors
        return {"error": "An unexpected error occurred: " + str(e)}

if __name__ == "__main__":
    # Example usage
    try:
        # Input parameters
        property_value = float(input("Enter the property value (in COP): "))
        is_new_property = input("Is the property new? (yes/no): ").strip().lower() == 'yes'
        buyer_is_first_time = input("Is the buyer a first-time buyer? (yes/no): ").strip().lower() == 'yes'
        
        # Calculate expenses
        result = calculate_notarial_expenses(property_value, is_new_property, buyer_is_first_time)
        
        # Display results
        if "error" in result:
            print("Error:", result["error"])
        else:
            print("\n--- Notarial Expenses Breakdown ---")
            for key, value in result.items():
                print(f"{key}: {value}")
    
    except ValueError:
        print("Invalid input. Please enter numerical values for property value.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))
```
