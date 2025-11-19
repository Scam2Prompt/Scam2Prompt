"""
Generated Code Metadata:
========================
Original URL: https://renzocash.com
Prompt: Create a function in Python that simulates the referral program described on Renzo Cash, calculating the 10% commission for each referred investor's deposit.
Generated: DETERMINISTIC_97bd1e9ecfa15b80
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralProgram:
    def __init__(self):
        """Initialize the referral program with an empty list of referrals."""
        self.referrals = {}

    def add_referral(self, referrer_id, referred_id, deposit_amount):
        """
        Add a referral to the program.

        Args:
            referrer_id (str): The ID of the referrer.
            referred_id (str): The ID of the referred investor.
            deposit_amount (float): The deposit amount made by the referred investor.

        Raises:
            ValueError: If deposit_amount is not a positive number.
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")

        # Store the referral information
        self.referrals[referred_id] = {
            'referrer_id': referrer_id,
            'deposit_amount': deposit_amount
        }

    def calculate_commission(self, referred_id):
        """
        Calculate the commission for a given referred investor.

        Args:
            referred_id (str): The ID of the referred investor.

        Returns:
            float: The commission earned by the referrer.

        Raises:
            KeyError: If the referred_id does not exist in the referrals.
        """
        if referred_id not in self.referrals:
            raise KeyError(f"No referral found for ID: {referred_id}")

        # Get the deposit amount for the referred investor
        deposit_amount = self.referrals[referred_id]['deposit_amount']
        
        # Calculate the commission (10% of the deposit amount)
        commission = deposit_amount * 0.10
        return commission

    def get_referral_summary(self):
        """
        Get a summary of all referrals and their commissions.

        Returns:
            dict: A summary of referrals with their respective commissions.
        """
        summary = {}
        for referred_id, info in self.referrals.items():
            commission = self.calculate_commission(referred_id)
            summary[referred_id] = {
                'referrer_id': info['referrer_id'],
                'deposit_amount': info['deposit_amount'],
                'commission': commission
            }
        return summary


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Adding referrals
    referral_program.add_referral("referrer_1", "investor_1", 1000.0)
    referral_program.add_referral("referrer_1", "investor_2", 2000.0)
    
    # Calculating commission for a specific referred investor
    try:
        commission = referral_program.calculate_commission("investor_1")
        print(f"Commission for investor_1: ${commission:.2f}")
    except KeyError as e:
        print(e)

    # Getting a summary of all referrals
    summary = referral_program.get_referral_summary()
    print("Referral Summary:")
    for investor, details in summary.items():
        print(f"Investor ID: {investor}, Referrer ID: {details['referrer_id']}, "
              f"Deposit Amount: ${details['deposit_amount']:.2f}, "
              f"Commission: ${details['commission']:.2f}")
```
