"""
Generated Code Metadata:
========================
Original URL: https://earnifi.co
Prompt: How can I design an interest-free spending model for a financial app, taking cues from Earnifi's Visa Card offering?
Generated: DETERMINISTIC_5864cbd37b69b143
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Interest-Free Spending Model for Financial App
Inspired by Earnifi's Visa Card offering
"""

from datetime import datetime, timedelta
from typing import Optional, List, Dict
import uuid

class InterestFreeSpendingModel:
    """
    A class to model interest-free spending with features like:
    - Spending limits
    - Repayment periods
    - Payment scheduling
    - Late payment handling
    """
    
    def __init__(self, user_id: str, credit_limit: float, interest_free_period_days: int = 30):
        """
        Initialize the spending model for a user.
        
        Args:
            user_id: Unique identifier for the user
            credit_limit: Maximum amount user can spend interest-free
            interest_free_period_days: Number of days before interest starts accruing
        """
        self.user_id = user_id
        self.credit_limit = credit_limit
        self.available_credit = credit_limit
        self.interest_free_period = interest_free_period_days
        self.transactions: List[Dict] = []
        self.payment_schedule: List[Dict] = []
        
    def make_purchase(self, amount: float, description: str = "") -> Optional[Dict]:
        """
        Record a purchase if within available credit.
        
        Args:
            amount: Purchase amount
            description: Optional description of purchase
            
        Returns:
            Transaction record if successful, None otherwise
        """
        if amount <= 0:
            raise ValueError("Purchase amount must be positive")
            
        if amount > self.available_credit:
            return None
            
        transaction = {
            "id": str(uuid.uuid4()),
            "date": datetime.now(),
            "amount": amount,
            "description": description,
            "due_date": datetime.now() + timedelta(days=self.interest_free_period),
            "paid": False
        }
        
        self.transactions.append(transaction)
        self.available_credit -= amount
        self._update_payment_schedule()
        
        return transaction
    
    def make_payment(self, amount: float) -> Dict:
        """
        Apply payment to outstanding balance.
        
        Args:
            amount: Payment amount
            
        Returns:
            Payment summary with new balance
        """
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
            
        unpaid_transactions = [t for t in self.transactions if not t["paid"]]
        unpaid_transactions.sort(key=lambda x: x["due_date"])
        
        remaining_payment = amount
        for transaction in unpaid_transactions:
            if remaining_payment <= 0:
                break
                
            payment_amount = min(remaining_payment, transaction["amount"])
            transaction["amount"] -= payment_amount
            remaining_payment -= payment_amount
            
            if transaction["amount"] <= 0:
                transaction["paid"] = True
                
        self.available_credit += (amount - remaining_payment)
        self._update_payment_schedule()
        
        return {
            "payment_amount": amount,
            "remaining_balance": self.get_outstanding_balance(),
            "available_credit": self.available_credit
        }
    
    def get_outstanding_balance(self) -> float:
        """Return the total unpaid balance."""
        return sum(t["amount"] for t in self.transactions if not t["paid"])
    
    def get_payment_schedule(self) -> List[Dict]:
        """Get the current payment schedule."""
        return self.payment_schedule
    
    def _update_payment_schedule(self):
        """Update the payment schedule based on current transactions."""
        unpaid_transactions = [t for t in self.transactions if not t["paid"]]
        unpaid_transactions.sort(key=lambda x: x["due_date"])
        
        self.payment_schedule = [
            {
                "due_date": t["due_date"],
                "amount": t["amount"],
                "description": t["description"]
            }
            for t in unpaid_transactions
        ]
    
    def check_late_payments(self) -> List[Dict]:
        """
        Check for any transactions past their due date.
        
        Returns:
            List of late transactions with days overdue
        """
        now = datetime.now()
        late_payments = []
        
        for t in self.transactions:
            if not t["paid"] and now > t["due_date"]:
                days_overdue = (now - t["due_date"]).days
                late_payments.append({
                    "transaction_id": t["id"],
                    "days_overdue": days_overdue,
                    "amount": t["amount"],
                    "original_due_date": t["due_date"]
                })
                
        return late_payments

# Example usage
if __name__ == "__main__":
    # Initialize for a user with $1000 credit limit and 30-day interest-free period
    user_spending = InterestFreeSpendingModel(
        user_id="user_123",
        credit_limit=1000.00,
        interest_free_period_days=30
    )
    
    # Make some purchases
    user_spending.make_purchase(200.00, "Groceries")
    user_spending.make_purchase(150.00, "Electronics")
    
    # Check payment schedule
    print("Payment Schedule:")
    for payment in user_spending.get_payment_schedule():
        print(f"Due {payment['due_date']}: ${payment['amount']} for {payment['description']}")
    
    # Make a payment
    payment_result = user_spending.make_payment(300.00)
    print(f"\nPayment applied. New balance: ${payment_result['remaining_balance']}")
    
    # Check for late payments (none expected in this example)
    late_payments = user_spending.check_late_payments()
    if late_payments:
        print("\nLate Payments:")
        for late in late_payments:
            print(f"Transaction {late['transaction_id']} is {late['days_overdue']} days late")
    else:
        print("\nNo late payments")
```
