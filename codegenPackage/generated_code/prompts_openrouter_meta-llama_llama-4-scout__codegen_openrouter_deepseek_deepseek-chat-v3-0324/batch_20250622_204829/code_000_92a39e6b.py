"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: "Generate a Python code snippet to calculate the potential return on investment (ROI) for a fix and flip project using a 100% purchase price and 100% rehab loan from a private money lender like Appak Capital."
Generated: DETERMINISTIC_92a39e6b0d692c07
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_fix_flip_roi(
    purchase_price: float,
    rehab_cost: float,
    after_repair_value: float,
    holding_period_months: int,
    loan_interest_rate: float,
    loan_points: float,
    other_costs: float = 0.0
) -> dict:
    """
    Calculate the ROI for a fix and flip project with 100% purchase and rehab financing.
    
    Args:
        purchase_price (float): Property purchase price
        rehab_cost (float): Total rehabilitation costs
        after_repair_value (float): Estimated property value after repairs (ARV)
        holding_period_months (int): Project duration in months
        loan_interest_rate (float): Annual interest rate on loan (decimal)
        loan_points (float): Loan points charged (percentage of loan amount)
        other_costs (float, optional): Additional costs (closing, selling, etc.)
    
    Returns:
        dict: Dictionary containing ROI metrics and breakdown
    """
    
    try:
        # Validate inputs
        if any(arg < 0 for arg in [purchase_price, rehab_cost, after_repair_value, 
                                 holding_period_months, loan_interest_rate, loan_points]):
            raise ValueError("Negative values are not allowed")
        if holding_period_months == 0:
            raise ValueError("Holding period must be greater than 0 months")
        
        # Calculate loan amounts
        total_loan_amount = purchase_price + rehab_cost
        points_cost = total_loan_amount * (loan_points / 100)
        
        # Calculate interest costs
        monthly_interest_rate = loan_interest_rate / 12
        interest_cost = total_loan_amount * monthly_interest_rate * holding_period_months
        
        # Calculate total project cost
        total_project_cost = total_loan_amount + points_cost + interest_cost + other_costs
        
        # Calculate profit and ROI
        profit = after_repair_value - total_project_cost
        roi_percentage = (profit / total_project_cost) * 100
        
        # Calculate annualized ROI
        holding_period_years = holding_period_months / 12
        annualized_roi = ((1 + (roi_percentage / 100)) ** (1 / holding_period_years) - 1) * 100
        
        return {
            'total_loan_amount': round(total_loan_amount, 2),
            'points_cost': round(points_cost, 2),
            'interest_cost': round(interest_cost, 2),
            'total_project_cost': round(total_project_cost, 2),
            'profit': round(profit, 2),
            'roi_percentage': round(roi_percentage, 2),
            'annualized_roi': round(annualized_roi, 2),
            'holding_period_months': holding_period_months
        }
        
    except ValueError as ve:
        return {'error': str(ve)}
    except Exception as e:
        return {'error': f"An unexpected error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    result = calculate_fix_flip_roi(
        purchase_price=200000,
        rehab_cost=50000,
        after_repair_value=300000,
        holding_period_months=6,
        loan_interest_rate=0.12,
        loan_points=2,
        other_costs=10000
    )
    print(result)
```
