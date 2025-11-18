"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agfinance-capitals.com
Prompt: Write Python code to calculate affiliate commission earnings based on a 5% rate for direct investors and include a two-level deep referral structure as described in the agfinance-capitals partnership model.
Generated: DETERMINISTIC_49cb3b322494e119
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate affiliate commission earnings based on a 5% rate for direct investors,
# with a two-level deep referral structure as described in the partnership model.

# Affiliate commission rates
DIRECT_INVESTOR_RATE = 0.05  # 5% for direct investors
LEVEL_1_REFERRAL_RATE = 0.03  # 3% for first-level referrals
LEVEL_2_REFERRAL_RATE = 0.02  # 2% for second-level referrals

def calculate_commission(investments, referrals):
    """
    Calculate commission earnings for direct investors and two referral levels.

    Args:
        investments (float): Amount invested by the direct investor.
        referrals (dict): Dictionary containing referral investments at two levels:
                          {
                              "level_1": [amount1, amount2, ...],
                              "level_2": [amount1, amount2, ...]
                          }

    Returns:
        dict: Commission earnings breakdown:
              {
                  "direct_commission": float,
                  "level_1_commission": float,
                  "level_2_commission": float,
                  "total_commission": float
              }
    """
    # Validate inputs
    if investments < 0:
        raise ValueError("Investments cannot be negative.")
    
    direct_commission = investments * DIRECT_INVESTOR_RATE
    
    level_1_commission = sum(referral * LEVEL_1_REFERRAL_RATE for referral in referrals.get("level_1", []))
    level_2_commission = sum(referral * LEVEL_2_REFERRAL_RATE for referral in referrals.get("level_2", []))
    
    total_commission = direct_commission + level_1_commission + level_2_commission

    return {
        "direct_commission": direct_commission,
        "level_1_commission": level_1_commission,
        "level_2_commission": level_2_commission,
        "total_commission": total_commission,
    }

# Example usage
if __name__ == "__main__":
    try:
        # Example direct investor investment
        direct_investment = 1000.0  # $1,000 invested directly

        # Example referral data
        referral_data = {
            "level_1": [500.0, 300.0],  # Two first-level referrals with investments of $500 and $300
            "level_2": [200.0, 150.0]  # Two second-level referrals with investments of $200 and $150
        }

        # Calculate commissions
        commission_result = calculate_commission(direct_investment, referral_data)

        # Print results
        print("Commission Breakdown:")
        print(f"Direct Investor Commission: ${commission_result['direct_commission']:.2f}")
        print(f"Level 1 Referral Commission: ${commission_result['level_1_commission']:.2f}")
        print(f"Level 2 Referral Commission: ${commission_result['level_2_commission']:.2f}")
        print(f"Total Commission: ${commission_result['total_commission']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
