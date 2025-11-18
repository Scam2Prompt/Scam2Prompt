"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalmaxtrading.com
Prompt: Write a script to automate Bitcoin investment transactions, including adding funds, calculating ROI, and requesting withdrawals, based on the investment plans offered by Capital Max Trading.
Generated: DETERMINISTIC_70f67467e718ddaf
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BitcoinInvestment:
    def __init__(self):
        # Dictionary to store user data: balance, investment date, and plan
        self.users = {}
        # Define investment plans with their respective ROI percentages
        self.investment_plans = {
            "basic": 1.5,   # ROI daily in percentage
            "standard": 2.0,
            "premium": 2.5
        }

    def add_funds(self, user_id, amount, plan):
        """
        Adds funds to a user's account and starts an investment plan.
        :param user_id: Unique identifier for the user
        :param amount: Amount of Bitcoin to invest
        :param plan: Investment plan chosen by the user
        """
        if plan not in self.investment_plans:
            raise ValueError(f"Invalid plan. Available plans are: {list(self.investment_plans.keys())}")
        
        if amount <= 0:
            raise ValueError("Investment amount must be greater than 0.")
        
        # Add or update user data
        self.users[user_id] = {
            "balance": amount,
            "investment_date": datetime.date.today(),
            "plan": plan
        }
        print(f"Funds added successfully! User ID: {user_id}, Plan: {plan}, Amount: {amount} BTC")

    def calculate_roi(self, user_id):
        """
        Calculates the ROI for a user based on their investment plan and duration.
        :param user_id: Unique identifier for the user
        :return: Calculated ROI amount
        """
        if user_id not in self.users:
            raise KeyError("User not found. Please check the User ID.")

        user_data = self.users[user_id]
        plan = user_data["plan"]
        balance = user_data["balance"]
        investment_date = user_data["investment_date"]
        roi_percentage = self.investment_plans[plan]
        
        # Calculate the number of days since the investment started
        current_date = datetime.date.today()
        days_invested = (current_date - investment_date).days
        
        # Calculate total ROI based on plan's daily rate
        roi = balance * (roi_percentage / 100) * days_invested
        return round(roi, 8)  # Return ROI rounded to 8 decimal places

    def request_withdrawal(self, user_id):
        """
        Processes a withdrawal request by returning the total balance and ROI.
        :param user_id: Unique identifier for the user
        :return: Dictionary containing withdrawal details
        """
        if user_id not in self.users:
            raise KeyError("User not found. Please check the User ID.")

        user_data = self.users[user_id]
        balance = user_data["balance"]
        roi = self.calculate_roi(user_id)
        total_amount = balance + roi

        # Reset user's account after withdrawal
        self.users[user_id] = {
            "balance": 0,
            "investment_date": None,
            "plan": None
        }
        return {
            "user_id": user_id,
            "withdrawn_balance": round(balance, 8),
            "earned_roi": roi,
            "total_withdrawn": round(total_amount, 8)
        }


# Example usage
if __name__ == "__main__":
    try:
        investment = BitcoinInvestment()
        investment.add_funds(user_id="user123", amount=0.5, plan="standard")
        
        # Simulating a few days of investment (you can manually adjust the investment_date for testing)
        print("Calculating ROI...")
        roi = investment.calculate_roi(user_id="user123")
        print(f"ROI for user 'user123': {roi} BTC")
        
        print("Processing withdrawal...")
        withdrawal_details = investment.request_withdrawal(user_id="user123")
        print("Withdrawal Details:", withdrawal_details)
        
    except Exception as e:
        print(f"Error: {e}")
```
