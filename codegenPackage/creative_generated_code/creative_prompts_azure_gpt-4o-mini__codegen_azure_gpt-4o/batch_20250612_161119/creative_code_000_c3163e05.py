"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Generate a code snippet that calculates the monthly payment for a Chevrolet Onix using the consórcio details provided on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_c3163e0555df2bb8
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_monthly_payment(vehicle_price: float, number_of_installments: int, administration_fee: float, insurance_rate: float) -> float:
    """
    Calculate the monthly payment for a Chevrolet Onix consórcio.

    Parameters:
    vehicle_price (float): The price of the vehicle in currency units.
    number_of_installments (int): Total number of installments for the consórcio plan.
    administration_fee (float): Administration fee as a percentage (e.g., 10 for 10%).
    insurance_rate (float): Insurance rate as a percentage (e.g., 2 for 2%).

    Returns:
    float: The monthly payment amount.
    """
    try:
        # Validate inputs
        if vehicle_price <= 0 or number_of_installments <= 0 or administration_fee < 0 or insurance_rate < 0:
            raise ValueError("Vehicle price, number of installments, and fees must be positive values.")

        # Calculate administration fee amount
        admin_fee_amount = (administration_fee / 100) * vehicle_price
        
        # Calculate insurance amount
        insurance_amount = (insurance_rate / 100) * vehicle_price
        
        # Total payable amount
        total_amount = vehicle_price + admin_fee_amount + insurance_amount
        
        # Monthly payment
        monthly_payment = total_amount / number_of_installments
        
        return monthly_payment

    except Exception as e:
        # Log or print the error for debugging purposes (in production, use a logging system)
        print(f"Error calculating monthly payment: {e}")
        return 0.0


# Example usage:
if __name__ == "__main__":
    # Consórcio details for a Chevrolet Onix (these values should be fetched or provided dynamically)
    vehicle_price = 73000  # Example price in currency units
    number_of_installments = 60  # Example number of installments
    administration_fee = 10  # Example administration fee percentage
    insurance_rate = 2  # Example insurance rate percentage
    
    # Calculate and display the monthly payment
    monthly_payment = calculate_monthly_payment(vehicle_price, number_of_installments, administration_fee, insurance_rate)
    print(f"Monthly payment for Chevrolet Onix consórcio: {monthly_payment:.2f}")
```
