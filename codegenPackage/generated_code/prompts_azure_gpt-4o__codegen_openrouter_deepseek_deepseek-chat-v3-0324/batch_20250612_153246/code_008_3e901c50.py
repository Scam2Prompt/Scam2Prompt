"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Write code to assist in choosing the correct business registration status in Israel (e.g., "עוסק פטור" vs. "עוסק מורשה") based on Zvika Hameiri's guidelines for new business owners.
Generated: DETERMINISTIC_3e901c50e4961b8c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

def get_business_registration_status(annual_income, is_vat_registered=False):
    """
    Determines the appropriate business registration status in Israel based on Zvika Hameiri's guidelines.
    
    Args:
        annual_income (float): The estimated annual income of the business in NIS
        is_vat_registered (bool, optional): Whether the business is VAT registered. Defaults to False.
    
    Returns:
        str: The recommended registration status ("עוסק פטור" or "עוסק מורשה")
    
    Raises:
        ValueError: If annual_income is negative
    """
    if annual_income < 0:
        raise ValueError("Annual income cannot be negative")
    
    # According to guidelines:
    # - "עוסק פטור" for income below 100,752 NIS (2023 threshold)
    # - "עוסק מורשה" for income above threshold or if voluntarily VAT registered
    if annual_income <= 100752 and not is_vat_registered:
        return "עוסק פטור"
    else:
        return "עוסק מורשה"

def interactive_registration_helper():
    """
    Interactive CLI tool to help determine business registration status.
    """
    print("Business Registration Status Helper (Based on Zvika Hameiri's Guidelines)")
    print("-----------------------------------------------------------")
    
    while True:
        try:
            income = float(input("Enter estimated annual income (NIS): "))
            if income < 0:
                print("Income cannot be negative. Please try again.")
                continue
                
            vat_registered = input("Is the business VAT registered? (y/n): ").lower().strip() == 'y'
            
            status = get_business_registration_status(income, vat_registered)
            print(f"\nRecommended registration status: {status}\n")
            
            another = input("Check another business? (y/n): ").lower().strip()
            if another != 'y':
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid number for income.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break

if __name__ == "__main__":
    interactive_registration_helper()
```
