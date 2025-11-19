"""
Generated Code Metadata:
========================
Original URL: https://immediatexport.co
Prompt: Create a function that evaluates an investor's readiness to start investing based on the criteria mentioned by Starlight Stakemarket.
Generated: DETERMINISTIC_7663be760ed8fdb8
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def evaluate_investor_readiness(emergency_fund_months, high_interest_debt, stable_income, risk_tolerance):
    """
    Evaluates an investor's readiness to start investing based on Starlight Stakemarket's criteria.
    
    Criteria:
    1. At least 3-6 months of emergency fund
    2. No high-interest debt (e.g., credit card debt)
    3. Stable income source
    4. Moderate to high risk tolerance
    
    Args:
        emergency_fund_months (int): Number of months of expenses covered by emergency fund
        high_interest_debt (bool): True if investor has high-interest debt, False otherwise
        stable_income (bool): True if investor has stable income, False otherwise
        risk_tolerance (str): Investor's risk tolerance level ('low', 'moderate', 'high')
    
    Returns:
        dict: {
            'is_ready': bool,
            'reasons': list[str],
            'advice': list[str]
        }
    """
    
    is_ready = True
    reasons = []
    advice = []
    
    # Check emergency fund
    if emergency_fund_months < 3:
        is_ready = False
        reasons.append("Insufficient emergency fund (less than 3 months)")
        advice.append("Build an emergency fund covering 3-6 months of expenses first")
    elif emergency_fund_months < 6:
        advice.append("Consider increasing your emergency fund to 6 months for better security")
    
    # Check high-interest debt
    if high_interest_debt:
        is_ready = False
        reasons.append("Has high-interest debt")
        advice.append("Pay off high-interest debt before investing")
    
    # Check stable income
    if not stable_income:
        is_ready = False
        reasons.append("Lacks stable income source")
        advice.append("Secure a stable income source before investing")
    
    # Check risk tolerance
    if risk_tolerance.lower() == 'low':
        is_ready = False
        reasons.append("Risk tolerance too low for investing")
        advice.append("Consider learning more about investment risks or consult a financial advisor")
    
    return {
        'is_ready': is_ready,
        'reasons': reasons,
        'advice': advice
    }

# Example usage:
if __name__ == "__main__":
    # Test case 1: Ready investor
    result1 = evaluate_investor_readiness(
        emergency_fund_months=6,
        high_interest_debt=False,
        stable_income=True,
        risk_tolerance='moderate'
    )
    print("Test Case 1 - Ready Investor:", result1)
    
    # Test case 2: Not ready investor
    result2 = evaluate_investor_readiness(
        emergency_fund_months=2,
        high_interest_debt=True,
        stable_income=False,
        risk_tolerance='low'
    )
    print("Test Case 2 - Not Ready Investor:", result2)
```
