"""
Generated Code Metadata:
========================
Original URL: https://armaalacak.com.tr
Prompt: What is the typical process that Arma Alacak Yönetim A.Ş. follows for managing and collecting debts, and what are the key steps involved?
Generated: DETERMINISTIC_d785c49bafa1847a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DebtManagement:
    """
    A class to represent the debt management process for Arma Alacak Yönetim A.Ş.
    """

    def __init__(self):
        """
        Initializes the debt management system with an empty list of debts.
        """
        self.debts = []

    def add_debt(self, debtor_name, amount):
        """
        Adds a new debt to the system.

        Parameters:
        debtor_name (str): The name of the debtor.
        amount (float): The amount of the debt.

        Raises:
        ValueError: If the amount is negative or debtor_name is empty.
        """
        if amount < 0:
            raise ValueError("Debt amount cannot be negative.")
        if not debtor_name:
            raise ValueError("Debtor name cannot be empty.")
        
        self.debts.append({'debtor_name': debtor_name, 'amount': amount})
        print(f"Debt added: {debtor_name} owes {amount}.")

    def collect_debt(self, debtor_name, amount):
        """
        Collects a specified amount from a debtor.

        Parameters:
        debtor_name (str): The name of the debtor.
        amount (float): The amount to collect.

        Raises:
        ValueError: If the amount is negative or debtor_name is not found.
        """
        if amount < 0:
            raise ValueError("Collection amount cannot be negative.")
        
        for debt in self.debts:
            if debt['debtor_name'] == debtor_name:
                if debt['amount'] < amount:
                    raise ValueError("Cannot collect more than the owed amount.")
                debt['amount'] -= amount
                print(f"Collected {amount} from {debtor_name}. Remaining debt: {debt['amount']}.")
                return
        
        raise ValueError("Debtor not found.")

    def list_debts(self):
        """
        Lists all debts in the system.
        """
        if not self.debts:
            print("No debts to display.")
            return
        
        print("Current debts:")
        for debt in self.debts:
            print(f"{debt['debtor_name']} owes {debt['amount']}.")

    def clear_debt(self, debtor_name):
        """
        Clears the debt for a specific debtor.

        Parameters:
        debtor_name (str): The name of the debtor.

        Raises:
        ValueError: If debtor_name is not found.
        """
        for i, debt in enumerate(self.debts):
            if debt['debtor_name'] == debtor_name:
                del self.debts[i]
                print(f"Debt cleared for {debtor_name}.")
                return
        
        raise ValueError("Debtor not found.")

# Example usage
if __name__ == "__main__":
    try:
        debt_manager = DebtManagement()
        debt_manager.add_debt("John Doe", 1000)
        debt_manager.add_debt("Jane Smith", 500)
        debt_manager.list_debts()
        debt_manager.collect_debt("John Doe", 300)
        debt_manager.clear_debt("Jane Smith")
        debt_manager.list_debts()
    except ValueError as e:
        print(f"Error: {e}")
```
