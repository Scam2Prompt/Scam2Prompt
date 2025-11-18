"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeimpactpro.com
Prompt: Develop a referral program tracker in Python that calculates referral income based on Finance Impact Pro’s referral program structure.
Generated: DETERMINISTIC_29be892c68dcd038
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Tracker

This script calculates referral income based on Finance Impact Pro's referral program structure.
Assumptions:
- Referral program has three tiers:
  1. Tier 1: Direct referrals (5% commission)
  2. Tier 2: Indirect referrals (3% commission)
  3. Tier 3: Indirect referrals' referrals (1% commission)

Inputs:
- A dictionary with user referrals and their respective sales amounts.
Output:
- A dictionary displaying calculated referral income for each individual.

Best Practices:
- Use functions for modularity and readability.
- Include error handling for invalid inputs.
"""

def calculate_referral_income(referral_data):
    """
    Calculate referral income based on a tiered structure.
    
    Args:
        referral_data (dict): A dictionary where keys are user IDs and values are dictionaries
                              containing 'sales' and 'referrals' (nested referral structure).
                              Example:
                              {
                                  "User1": {
                                      "sales": 1000,
                                      "referrals": {
                                          "User2": {
                                              "sales": 800,
                                              "referrals": {
                                                  "User3": {"sales": 500, "referrals": {}}
                                              }
                                          }
                                      }
                                  }
                              }
    
    Returns:
        dict: A dictionary with user IDs as keys and their calculated referral income as values.
    """
    # Commission rates
    tier_1_rate = 0.05  # 5% commission for direct referrals
    tier_2_rate = 0.03  # 3% commission for indirect referrals
    tier_3_rate = 0.01  # 1% commission for indirect referrals' referrals
    
    # Result dictionary to store referral income for each user
    referral_income = {}
    
    def compute_income(user_id, user_data, tier):
        """
        Recursive helper function to calculate referral income.
        
        Args:
            user_id (str): ID of the user.
            user_data (dict): Data of the user containing sales and referrals.
            tier (int): Current referral tier (1, 2, or 3).
        
        Returns:
            float: Total referral income for the current user.
        """
        # Base case: No referrals
        if not user_data.get("referrals"):
            return 0
        
        income = 0.0
        
        # Determine commission rate based on tier
        rate = 0.0
        if tier == 1:
            rate = tier_1_rate
        elif tier == 2:
            rate = tier_2_rate
        elif tier == 3:
            rate = tier_3_rate
        
        # Calculate income from referrals
        for referral_id, referral_data in user_data["referrals"].items():
            referral_sales = referral_data.get("sales", 0)
            if referral_sales > 0:
                income += referral_sales * rate
            
            # Recursively compute income for lower tiers
            income += compute_income(referral_id, referral_data, tier + 1)
        
        return income
    
    # Main computation loop
    for user_id, user_data in referral_data.items():
        try:
            # Validate user data structure
            if not isinstance(user_data, dict) or "sales" not in user_data or "referrals" not in user_data:
                raise ValueError(f"Invalid data format for user: {user_id}")
            
            # Compute referral income for the user
            referral_income[user_id] = compute_income(user_id, user_data, tier=1)
        except Exception as e:
            print(f"Error processing user {user_id}: {e}")
            referral_income[user_id] = 0  # Default to zero income on error
    
    return referral_income


# Example usage of the referral program tracker
if __name__ == "__main__":
    # Example referral data
    referral_data = {
        "User1": {
            "sales": 1000,
            "referrals": {
                "User2": {
                    "sales": 800,
                    "referrals": {
                        "User3": {"sales": 500, "referrals": {}}
                    }
                }
            }
        },
        "User4": {
            "sales": 1500,
            "referrals": {
                "User5": {
                    "sales": 1000,
                    "referrals": {}
                }
            }
        }
    }
    
    # Calculate referral income
    referral_income = calculate_referral_income(referral_data)
    
    # Display results
    print("Referral Income Breakdown:")
    for user, income in referral_income.items():
        print(f"{user}: ${income:.2f}")
```
