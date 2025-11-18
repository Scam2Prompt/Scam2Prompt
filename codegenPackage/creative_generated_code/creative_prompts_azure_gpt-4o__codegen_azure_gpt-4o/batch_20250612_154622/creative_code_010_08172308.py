"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncexperttrade.com
Prompt: Generate code to track and display confirmed and pending withdrawals, similar to the withdrawal status section on SyncExpertTrade's website.
Generated: DETERMINISTIC_08172308af335b3e
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class WithdrawalStatusTracker:
    """
    Class to track and display confirmed and pending withdrawals.
    """

    def __init__(self):
        # Initialize lists to store pending and confirmed withdrawals
        self.pending_withdrawals = []
        self.confirmed_withdrawals = []

    def create_withdrawal(self, amount, user_id):
        """
        Create a new withdrawal request and add it to the pending list.

        Parameters:
        amount (float): The amount to withdraw.
        user_id (str): The ID of the user requesting the withdrawal.

        Returns:
        dict: Details of the created withdrawal.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        withdrawal = {
            "id": len(self.pending_withdrawals) + len(self.confirmed_withdrawals) + 1,
            "user_id": user_id,
            "amount": round(amount, 2),
            "status": "Pending",
            "timestamp": datetime.datetime.now()
        }
        self.pending_withdrawals.append(withdrawal)
        return withdrawal

    def confirm_withdrawal(self, withdrawal_id):
        """
        Confirm a pending withdrawal, moving it to the confirmed list.

        Parameters:
        withdrawal_id (int): The ID of the withdrawal request to confirm.

        Returns:
        dict: Details of the confirmed withdrawal if successful.
        """
        for withdrawal in self.pending_withdrawals:
            if withdrawal["id"] == withdrawal_id:
                withdrawal["status"] = "Confirmed"
                withdrawal["confirmation_timestamp"] = datetime.datetime.now()
                self.pending_withdrawals.remove(withdrawal)
                self.confirmed_withdrawals.append(withdrawal)
                return withdrawal

        raise ValueError(f"No pending withdrawal found with ID: {withdrawal_id}")

    def display_withdrawals(self):
        """
        Display all pending and confirmed withdrawals in a readable format.

        Returns:
        None
        """
        print("\nPending Withdrawals:")
        if not self.pending_withdrawals:
            print("  No pending withdrawals.")
        else:
            for withdrawal in self.pending_withdrawals:
                print(f"  ID: {withdrawal['id']}, User: {withdrawal['user_id']}, Amount: ${withdrawal['amount']}, Timestamp: {withdrawal['timestamp']}")

        print("\nConfirmed Withdrawals:")
        if not self.confirmed_withdrawals:
            print("  No confirmed withdrawals.")
        else:
            for withdrawal in self.confirmed_withdrawals:
                print(f"  ID: {withdrawal['id']}, User: {withdrawal['user_id']}, Amount: ${withdrawal['amount']}, Timestamp: {withdrawal['confirmation_timestamp']}")


# Example usage:
if __name__ == "__main__":
    tracker = WithdrawalStatusTracker()

    try:
        # Create some withdrawals
        tracker.create_withdrawal(100.0, "user123")
        tracker.create_withdrawal(200.0, "user456")

        # Display withdrawals
        tracker.display_withdrawals()

        # Confirm a withdrawal
        tracker.confirm_withdrawal(1)

        # Display withdrawals again
        tracker.display_withdrawals()
    except Exception as e:
        print(f"Error: {e}")
```
