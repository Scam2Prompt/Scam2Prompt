"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write a script to determine the availability and balance of a bank account, including calculations for overdraft limits and available credit, as described in the webpage.
Generated: DETERMINISTIC_73f1e96df441dc61
Batch ID: 20250612_154901
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/accounts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, Optional, Union

class BankAccount:
    """
    A class to represent a bank account and perform balance-related operations.
    
    Attributes:
        account_number (str): The account number.
        account_holder (str): The name of the account holder.
        balance (float): The current balance of the account.
        overdraft_limit (float): The maximum allowed overdraft limit.
        available_credit (float): The available credit (if applicable).
    """
    
    def __init__(
        self,
        account_number: str,
        account_holder: str,
        balance: float = 0.0,
        overdraft_limit: float = 0.0,
        available_credit: float = 0.0
    ):
        """
        Initialize the BankAccount with account details.
        
        Args:
            account_number (str): The account number.
            account_holder (str): The name of the account holder.
            balance (float, optional): The current balance. Defaults to 0.0.
            overdraft_limit (float, optional): The overdraft limit. Defaults to 0.0.
            available_credit (float, optional): The available credit. Defaults to 0.0.
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.overdraft_limit = overdraft_limit
        self.available_credit = available_credit
    
    def get_available_balance(self) -> float:
        """
        Calculate the available balance including overdraft and credit.
        
        Returns:
            float: The available balance (balance + overdraft_limit + available_credit).
        """
        return self.balance + self.overdraft_limit + self.available_credit
    
    def check_overdraft(self) -> bool:
        """
        Check if the account is in overdraft.
        
        Returns:
            bool: True if balance is negative, False otherwise.
        """
        return self.balance < 0
    
    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit.
            
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the account.
        
        Args:
            amount (float): The amount to withdraw.
            
        Raises:
            ValueError: If the amount is negative or exceeds available balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        available_balance = self.get_available_balance()
        if amount > available_balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
    
    def __str__(self) -> str:
        """
        Return a string representation of the account.
        
        Returns:
            str: Account details.
        """
        return (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance: {self.balance:.2f}\n"
            f"Overdraft Limit: {self.overdraft_limit:.2f}\n"
            f"Available Credit: {self.available_credit:.2f}\n"
            f"Available Balance: {self.get_available_balance():.2f}\n"
            f"In Overdraft: {'Yes' if self.check_overdraft() else 'No'}"
        )


def fetch_account_data(api_url: str, account_id: str) -> Optional[Dict[str, Union[str, float]]]:
    """
    Fetch account data from a given API endpoint.
    
    Args:
        api_url (str): The API endpoint URL.
        account_id (str): The account ID to fetch data for.
        
    Returns:
        Optional[Dict[str, Union[str, float]]]: The account data if successful, None otherwise.
    """
    try:
        response = requests.get(f"{api_url}/{account_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching account data: {e}")
        return None


def create_account_from_api(api_url: str, account_id: str) -> Optional[BankAccount]:
    """
    Create a BankAccount instance from API data.
    
    Args:
        api_url (str): The API endpoint URL.
        account_id (str): The account ID to fetch data for.
        
    Returns:
        Optional[BankAccount]: The BankAccount instance if successful, None otherwise.
    """
    account_data = fetch_account_data(api_url, account_id)
    if not account_data:
        return None
    
    try:
        return BankAccount(
            account_number=account_data.get("account_number", ""),
            account_holder=account_data.get("account_holder", ""),
            balance=float(account_data.get("balance", 0.0)),
            overdraft_limit=float(account_data.get("overdraft_limit", 0.0)),
            available_credit=float(account_data.get("available_credit", 0.0))
        )
    except (ValueError, TypeError) as e:
        print(f"Error creating account: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Example with manual account creation
    account = BankAccount(
        account_number="123456789",
        account_holder="John Doe",
        balance=1000.0,
        overdraft_limit=500.0,
        available_credit=2000.0
    )
    print(account)
    
    # Example with API data
    API_URL = "https://api.example.com/accounts"
    account_id = "123456789"
    api_account = create_account_from_api(API_URL, account_id)
    if api_account:
        print(api_account)
```
