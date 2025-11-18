"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fundfa.com
Prompt: Create a function to simulate the account purchasing process and trading exam participation for SDF Prop Firm, referencing the steps outlined on Fundfa.
Generated: DETERMINISTIC_e6ea6e221fdafdca
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountPurchaseError(Exception):
    """Custom exception for account purchase errors."""
    pass


class TradingExamError(Exception):
    """Custom exception for trading exam participation errors."""
    pass


class SDFPropFirm:
    """Class to simulate the account purchasing process and trading exam participation for SDF Prop Firm."""
    
    def __init__(self, user_id):
        """Initialize the SDF Prop Firm with a user ID."""
        self.user_id = user_id
        self.account_active = False
        self.exam_passed = False

    def purchase_account(self, payment_info):
        """
        Simulate the account purchasing process.

        :param payment_info: dict, contains payment details like card number, amount, etc.
        :raises AccountPurchaseError: if payment is unsuccessful or invalid details provided
        """
        try:
            if not self.validate_payment(payment_info):
                raise AccountPurchaseError("Invalid payment details.")
            
            # Simulate payment processing
            print(f"Processing payment for user {self.user_id}...")
            # Here, implement actual payment logic
            self.account_active = True
            print("Account purchased successfully.")
        
        except Exception as e:
            raise AccountPurchaseError(f"Failed to purchase account: {str(e)}")

    def validate_payment(self, payment_info):
        """
        Validate the payment information.

        :param payment_info: dict, contains payment details
        :return: bool, True if payment info is valid, False otherwise
        """
        # Basic validation checks
        if 'card_number' not in payment_info or 'amount' not in payment_info:
            return False
        if len(payment_info['card_number']) != 16:
            return False
        if payment_info['amount'] <= 0:
            return False
        return True

    def participate_in_exam(self):
        """
        Simulate participation in a trading exam.

        :raises TradingExamError: if user does not have an active account or exam fails
        """
        if not self.account_active:
            raise TradingExamError("Account is not active. Please purchase an account first.")

        # Simulate exam participation
        print(f"User {self.user_id} is participating in the trading exam...")
        # Here, implement actual exam logic
        self.exam_passed = True  # Simulate passing the exam
        print("Trading exam completed successfully. User passed.")

    def run_process(self, payment_info):
        """
        Run the full account purchasing and exam participation process.

        :param payment_info: dict, contains payment details for account purchase
        """
        try:
            self.purchase_account(payment_info)
            self.participate_in_exam()
        except (AccountPurchaseError, TradingExamError) as e:
            print(f"Error: {str(e)}")


# Example usage
if __name__ == "__main__":
    user_payment_info = {
        'card_number': '1234567812345678',
        'amount': 100
    }

    sdf_firm = SDFPropFirm(user_id='user123')
    sdf_firm.run_process(user_payment_info)
```
