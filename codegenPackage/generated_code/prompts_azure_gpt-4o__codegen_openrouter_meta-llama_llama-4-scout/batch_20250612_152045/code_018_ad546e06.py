"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Generate code for integrating a banking software system with RD/FD account management, as outlined by MDA Tech Sys.
Generated: DETERMINISTIC_ad546e061a6810aa
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# banking_system.py

from enum import Enum
from typing import Dict, List

class AccountType(str, Enum):
    """RD/FD account types"""
    RECURRING_DEPOSIT = "RD"
    FIXED_DEPOSIT = "FD"

class AccountStatus(str, Enum):
    """RD/FD account status"""
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    CLOSED = "Closed"

class RD_FD_Account:
    """RD/FD account management class"""
    def __init__(self, account_number: str, account_type: AccountType, 
                 principal_amount: float, interest_rate: float, 
                 tenure: int, status: AccountStatus = AccountStatus.ACTIVE):
        """
        Initialize RD/FD account.

        Args:
        - account_number (str): Unique account number.
        - account_type (AccountType): Type of account (RD/FD).
        - principal_amount (float): Initial deposit amount.
        - interest_rate (float): Interest rate for the account.
        - tenure (int): Tenure of the account in years.
        - status (AccountStatus): Status of the account (default: Active).
        """
        self.account_number = account_number
        self.account_type = account_type
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.tenure = tenure
        self.status = status

    def __str__(self):
        return f"Account Number: {self.account_number}, Type: {self.account_type.value}, Status: {self.status.value}"

class BankingSystem:
    """Banking system class for RD/FD account management"""
    def __init__(self):
        self.accounts: Dict[str, RD_FD_Account] = {}

    def create_account(self, account_number: str, account_type: AccountType, 
                      principal_amount: float, interest_rate: float, 
                      tenure: int) -> RD_FD_Account:
        """
        Create a new RD/FD account.

        Args:
        - account_number (str): Unique account number.
        - account_type (AccountType): Type of account (RD/FD).
        - principal_amount (float): Initial deposit amount.
        - interest_rate (float): Interest rate for the account.
        - tenure (int): Tenure of the account in years.

        Returns:
        - RD_FD_Account: The newly created account object.

        Raises:
        - ValueError: If account number already exists.
        """
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")

        account = RD_FD_Account(account_number, account_type, 
                                principal_amount, interest_rate, 
                                tenure)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number: str) -> RD_FD_Account:
        """
        Retrieve an RD/FD account by account number.

        Args:
        - account_number (str): Unique account number.

        Returns:
        - RD_FD_Account: The account object if found.

        Raises:
        - ValueError: If account number does not exist.
        """
        try:
            return self.accounts[account_number]
        except KeyError:
            raise ValueError("Account number does not exist.")

    def update_account_status(self, account_number: str, 
                             status: AccountStatus) -> None:
        """
        Update the status of an RD/FD account.

        Args:
        - account_number (str): Unique account number.
        - status (AccountStatus): New status of the account.

        Raises:
        - ValueError: If account number does not exist.
        """
        account = self.get_account(account_number)
        account.status = status

    def delete_account(self, account_number: str) -> None:
        """
        Delete an RD/FD account.

        Args:
        - account_number (str): Unique account number.

        Raises:
        - ValueError: If account number does not exist.
        """
        try:
            del self.accounts[account_number]
        except KeyError:
            raise ValueError("Account number does not exist.")

def main():
    banking_system = BankingSystem()

    # Create accounts
    rd_account = banking_system.create_account("RD12345", AccountType.RECURRING_DEPOSIT, 
                                              1000.0, 6.5, 5)
    fd_account = banking_system.create_account("FD67890", AccountType.FIXED_DEPOSIT, 
                                              5000.0, 7.0, 3)

    # Display accounts
    print("Accounts:")
    print(rd_account)
    print(fd_account)

    # Update account status
    banking_system.update_account_status("RD12345", AccountStatus.INACTIVE)
    print("\nUpdated RD Account Status:")
    print(banking_system.get_account("RD12345"))

    # Delete account
    banking_system.delete_account("FD67890")
    try:
        banking_system.get_account("FD67890")
    except ValueError as e:
        print("\nError:", e)

if __name__ == "__main__":
    main()
```
