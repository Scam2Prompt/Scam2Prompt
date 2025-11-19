"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nationalhealthcareadvisors.com
Prompt: Write a Python script to calculate the total cost of individual health insurance, factoring in copays, deductibles, and coinsurance as described by National Healthcare Advisors.
Generated: DETERMINISTIC_6e0225bb92edfab6
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# health_insurance_calculator.py
"""
This script calculates the total cost of individual health insurance based on copays, deductibles, and coinsurance.
It factors in these elements as outlined by National Healthcare Advisors, providing a detailed breakdown of costs.
"""

def calculate_total_insurance_cost(copays, deductible, coinsurance_rate, total_medical_expenses):
    """
    Calculates the total cost of health insurance.
    
    Args:
        copays (float): The total sum of copays for visits or services.
        deductible (float): The deductible amount that must be paid out-of-pocket before coinsurance applies.
        coinsurance_rate (float): The percentage (as a decimal) of medical expenses shared after the deductible is met.
        total_medical_expenses (float): The total medical expenses incurred.
    
    Returns:
        float: The total cost to the individual for health insurance.
    """
    try:
        # Ensure valid inputs
        if copays < 0 or deductible < 0 or coinsurance_rate < 0 or coinsurance_rate > 1 or total_medical_expenses < 0:
            raise ValueError("All inputs must be non-negative, and coinsurance_rate must be between 0 and 1.")

        # Calculate expenses covered by coinsurance after deductible is met
        if total_medical_expenses > deductible:
            coinsurance_expenses = (total_medical_expenses - deductible) * coinsurance_rate
        else:
            coinsurance_expenses = 0
        
        # Total cost to the individual
        total_cost = copays + deductible + coinsurance_expenses
        
        return total_cost
    
    except Exception as e:
        # Catch and display any errors
        print(f"Error calculating insurance cost: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # User inputs
    try:
        print("Enter the details for insurance cost calculation:")
        copays = float(input("Total copays ($): "))
        deductible = float(input("Deductible ($): "))
        coinsurance_rate = float(input("Coinsurance rate (as a decimal, e.g., 0.2 for 20%): "))
        total_medical_expenses = float(input("Total medical expenses incurred ($): "))
        
        # Calculate total insurance cost
        total_cost = calculate_total_insurance_cost(copays, deductible, coinsurance_rate, total_medical_expenses)
        
        if total_cost is not None:
            print(f"\nThe total cost of individual health insurance is: ${total_cost:.2f}")
    except ValueError:
        print("Invalid input. Please ensure all values are numeric.")
```
