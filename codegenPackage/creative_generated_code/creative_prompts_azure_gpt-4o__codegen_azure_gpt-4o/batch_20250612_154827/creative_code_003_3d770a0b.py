"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibaoinsurance.com
Prompt: Develop a program to calculate group discounts and combined insurance premiums for auto and home insurance, using the discount policies described by Aibao Insurance.
Generated: DETERMINISTIC_3d770a0b47bf2be7
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program Description:
This program calculates group discounts and combined insurance premiums for auto and home insurance, 
based on Aibao Insurance's discount policies. The user provides the auto and home insurance premiums, 
and the program applies the discounts accordingly. Discounts are applied based on eligibility and combined premiums.
"""

def calculate_combined_premium(auto_premium, home_premium, auto_discount_rate, home_discount_rate, combined_discount_rate):
    """
    Calculates the combined insurance premium with applicable discounts.
    
    Parameters:
        auto_premium (float): The premium for auto insurance.
        home_premium (float): The premium for home insurance.
        auto_discount_rate (float): Discount rate for auto insurance.
        home_discount_rate (float): Discount rate for home insurance.
        combined_discount_rate (float): Discount rate for combined auto and home insurance.
    
    Returns:
        dict: Contains details of individual and combined premiums after discounts.
    """
    try:
        # Validate inputs are non-negative
        if auto_premium < 0 or home_premium < 0:
            raise ValueError("Premium values must be non-negative.")
        
        # Calculate individual discounted premiums
        auto_discounted = auto_premium * (1 - auto_discount_rate / 100)
        home_discounted = home_premium * (1 - home_discount_rate / 100)
        
        # Calculate combined premium and apply combined discount
        combined_premium = auto_discounted + home_discounted
        combined_discounted = combined_premium * (1 - combined_discount_rate / 100)
        
        # Return detailed breakdown
        return {
            "auto_premium_after_discount": round(auto_discounted, 2),
            "home_premium_after_discount": round(home_discounted, 2),
            "combined_premium_before_discount": round(combined_premium, 2),
            "combined_premium_after_discount": round(combined_discounted, 2)
        }
    
    except Exception as e:
        return {"error": str(e)}


def main():
    """
    Main function to interact with the user and calculate insurance premiums.
    """
    print("Welcome to Aibao Insurance Premium Calculator!")
    
    try:
        # Gather user inputs
        auto_premium = float(input("Enter the auto insurance premium: "))
        home_premium = float(input("Enter the home insurance premium: "))
        auto_discount_rate = float(input("Enter the auto insurance discount rate (in %): "))
        home_discount_rate = float(input("Enter the home insurance discount rate (in %): "))
        combined_discount_rate = float(input("Enter the combined insurance discount rate (in %): "))
        
        # Calculate the premiums using the function
        result = calculate_combined_premium(auto_premium, home_premium, auto_discount_rate, home_discount_rate, combined_discount_rate)
        
        # Display results
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("\n--- Premium Calculation Results ---")
            print(f"Auto Insurance Premium After Discount: ${result['auto_premium_after_discount']}")
            print(f"Home Insurance Premium After Discount: ${result['home_premium_after_discount']}")
            print(f"Combined Premium Before Discount: ${result['combined_premium_before_discount']}")
            print(f"Combined Premium After Discount: ${result['combined_premium_after_discount']}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
