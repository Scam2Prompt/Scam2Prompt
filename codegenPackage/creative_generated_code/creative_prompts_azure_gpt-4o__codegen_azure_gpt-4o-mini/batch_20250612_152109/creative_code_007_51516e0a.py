"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-shibabudz.web.app
Prompt: Generate a function to calculate referral income based on the SHIBABUDZ referral program, where users earn up to 5% from their referrals' first token purchase.
Generated: DETERMINISTIC_51516e0a0edd2d13
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    """
    This class handles the calculation of referral income based on the SHIBABUDZ referral program.
    Users earn up to 5% from their referrals' first token purchase.
    """
    
    def __init__(self):
        self.referral_earnings = {}
    
    def calculate_referral_income(self, referral_id, token_purchase_amount):
        """
        Calculate the referral income for a given referral ID based on the token purchase amount.

        Parameters:
        referral_id (str): The ID of the user who referred another user.
        token_purchase_amount (float): The amount of the first token purchase made by the referral.

        Returns:
        float: The income earned from the referral.

        Raises:
        ValueError: If the token purchase amount is negative or not a number.
        """
        
        # Validate input
        if not isinstance(referral_id, str) or not referral_id:
            raise ValueError("Referral ID must be a non-empty string.")
        if not isinstance(token_purchase_amount, (int, float)) or token_purchase_amount < 0:
            raise ValueError("Token purchase amount must be a non-negative number.")
        
        # Define the referral commission rate
        referral_commission_rate = 0.05  # 5%
        
        # Calculate referral income
        referral_income = token_purchase_amount * referral_commission_rate
        
        # Store the earnings per referral ID if not already present
        if referral_id not in self.referral_earnings:
            self.referral_earnings[referral_id] = 0.0
            
        self.referral_earnings[referral_id] += referral_income
        
        return referral_income

    def get_total_earnings(self, referral_id):
        """
        Retrieve the total earnings for a specific referral ID.

        Parameters:
        referral_id (str): The ID of the user to check total earnings for.

        Returns:
        float: The total earnings for the specified referral ID.

        Raises:
        ValueError: If the referral ID is invalid.
        """
        
        if not isinstance(referral_id, str) or not referral_id:
            raise ValueError("Referral ID must be a non-empty string.")
        
        return self.referral_earnings.get(referral_id, 0.0)

# Example usage:
if __name__ == "__main__":
    # Create an instance of the ReferralProgram
    referral_program = ReferralProgram()
    
    # Simulate a referral earning
    try:
        referral_income = referral_program.calculate_referral_income("user123", 100.0)
        print(f"Referral income earned: ${referral_income:.2f}")
        
        # Check total earnings for the user
        total_earnings = referral_program.get_total_earnings("user123")
        print(f"Total earnings for user123: ${total_earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
