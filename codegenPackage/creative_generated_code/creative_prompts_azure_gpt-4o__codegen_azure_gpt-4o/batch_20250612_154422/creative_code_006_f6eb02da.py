"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securecash.info
Prompt: Create a function to calculate funding amounts ranging from $10k to $5M, factoring in business revenue and credit score, as specified by New York Savings.
Generated: DETERMINISTIC_f6eb02da878ffaff
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_funding_amount(revenue: float, credit_score: int) -> float:
    """
    Calculates funding amount based on business revenue and credit score.
    
    Parameters:
    revenue (float): Annual revenue of the business (positive number).
    credit_score (int): Credit score of the business (integer between 300 and 850).
    
    Returns:
    float: Funding amount in dollars, ranging between $10,000 and $5,000,000.

    Raises:
    ValueError: If revenue is not positive or credit_score is out of range.
    """
    
    # Constants for minimum and maximum funding limits
    MIN_FUNDING = 10_000
    MAX_FUNDING = 5_000_000
    
    # Validate inputs
    if revenue <= 0:
        raise ValueError("Revenue must be a positive number.")
    if credit_score < 300 or credit_score > 850:
        raise ValueError("Credit score must be between 300 and 850.")
    
    # Base funding amount as a percentage of revenue
    # Higher credit scores increase the percentage
    base_percentage = 0.10  # Default 10% of revenue
    credit_multiplier = (credit_score - 300) / 550  # Scales credit score from 0 to 1
    funding_percentage = base_percentage + (0.15 * credit_multiplier)  # Up to 25% of revenue
    
    # Calculate funding amount
    funding_amount = revenue * funding_percentage
    
    # Ensure funding amount stays within limits
    funding_amount = max(MIN_FUNDING, min(funding_amount, MAX_FUNDING))
    
    return funding_amount


# Example usage:
if __name__ == "__main__":
    try:
        # Example inputs
        example_revenue = 1_000_000  # $1,000,000 revenue
        example_credit_score = 750   # Credit score of 750
        
        # Calculate funding amount
        result = calculate_funding_amount(example_revenue, example_credit_score)
        
        # Output the result
        print(f"Eligible funding amount: ${result:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
