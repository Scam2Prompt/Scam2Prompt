"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://expressfinsbk.com
Prompt: Provide a Python implementation to handle beneficiary listing and fund transfers within the Express Finance Banking system, including support for transfers to external banks.
Generated: DETERMINISTIC_920dc7562ccb37c2
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List, Dict, Union

class Beneficiary:
    """Class representing a bank account beneficiary."""
    
    def __init__(self, name: str, account_number: str, bank_name: str):
        self.name = name
        self.account_number = account_number
        self.bank_name = bank_name
        self.id = uuid.uuid4()  # Unique ID for each beneficiary

class Account:
    """Class representing a bank account."""
    
    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance
        self.beneficiaries: List[Beneficiary] = []

    def add_beneficiary(self, name: str, account_number: str, bank_name: str) -> None:
        """Adds a new beneficiary to the account."""
        new_beneficiary = Beneficiary(name, account_number, bank_name)
        self.beneficiaries.append(new_beneficiary)

    def transfer_funds(self, beneficiary_id: uuid.UUID, amount: float, external: bool = False) -> Union[str, None]:
        """Transfers funds to a beneficiary or an external bank account.
        
        Args:
            beneficiary_id (uuid.UUID): ID of the beneficiary to transfer funds to.
            amount (float): Amount to transfer.
            external (bool): If True, transfer to an external account.

        Returns:
            str or None: Error message if the transfer fails, otherwise None.
        """
        if amount <= 0:
            return "Transfer amount must be greater than zero."
        if amount > self.balance:
            return "Insufficient funds."

        beneficiary = next((b for b in self.beneficiaries if b.id == beneficiary_id), None)
        
        if external:
            # Logic for transferring to an external account
            self.balance -= amount
            return f"Transferred ${amount:.2f} to external account {beneficiary.account_number} at {beneficiary.bank_name}."
        
        if beneficiary:
            self.balance -= amount
            return f"Transferred ${amount:.2f} to {beneficiary.name}'s account {beneficiary.account_number}."
        
        return "Beneficiary not found."

class BankingSystem:
    """Class representing the Express Finance Banking System."""
    
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def create_account(self, account_number: str) -> None:
        """Creates a new bank account."""
        if account_number in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[account_number] = Account(account_number)

    def get_account(self, account_number: str) -> Union[Account, None]:
        """Retrieves an account by its account number."""
        return self.accounts.get(account_number)

# Example usage:
if __name__ == "__main__":
    banking_system = BankingSystem()
    
    # Create a new account
    banking_system.create_account("123456789")
    account = banking_system.get_account("123456789")

    # Add beneficiaries
    account.add_beneficiary("John Doe", "987654321", "Some Bank")
    account.add_beneficiary("Jane Smith", "123123123", "Another Bank")

    # Transfer funds
    beneficiary = account.beneficiaries[0]  # John Doe
    result = account.transfer_funds(beneficiary.id, 50.0)
    print(result)  # Output: Transferred $50.00 to John Doe's account 987654321.
    
    # Attempt an external transfer
    result_external = account.transfer_funds(beneficiary.id, 20.0, external=True)
    print(result_external)  # Output: Transferred $20.00 to external account 987654321 at Some Bank.
```
