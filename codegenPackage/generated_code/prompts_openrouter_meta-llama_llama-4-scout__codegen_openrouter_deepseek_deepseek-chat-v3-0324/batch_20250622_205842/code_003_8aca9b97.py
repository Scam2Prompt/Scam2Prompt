"""
Generated Code Metadata:
========================
Original URL: https://liquideth-hub.org
Prompt: What are the benefits and requirements for opening a Livret A savings account with Crédit Agricole, and how does it differ from other savings accounts like the LDDS and LEP?
Generated: DETERMINISTIC_8aca9b972649dc40
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SavingsAccount:
    """
    Base class for savings accounts in France.
    Contains common attributes and methods for all savings account types.
    """
    
    def __init__(self, name: str, interest_rate: float, tax_status: str):
        """
        Initialize a savings account with basic parameters.
        
        Args:
            name (str): Name of the savings account
            interest_rate (float): Annual interest rate (as decimal)
            tax_status (str): Tax status ('taxable' or 'tax-free')
        """
        self.name = name
        self.interest_rate = interest_rate
        self.tax_status = tax_status
        self.balance = 0.0
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            bool: True if deposit was successful, False otherwise
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        self.balance += amount
        return True
    
    def calculate_interest(self) -> float:
        """
        Calculate annual interest based on current balance.
        
        Returns:
            float: Amount of interest earned
        """
        return self.balance * self.interest_rate
    
    def get_details(self) -> dict:
        """
        Get account details as a dictionary.
        
        Returns:
            dict: Dictionary containing account details
        """
        return {
            'name': self.name,
            'interest_rate': self.interest_rate,
            'tax_status': self.tax_status,
            'balance': self.balance
        }


class LivretA(SavingsAccount):
    """
    Livret A savings account implementation.
    Specific to Crédit Agricole requirements and benefits.
    """
    
    def __init__(self):
        super().__init__(
            name="Livret A",
            interest_rate=0.03,  # Example rate, changes periodically
            tax_status="tax-free"
        )
        self.max_balance = 22950.0  # Maximum balance as of 2023
        self.min_opening_amount = 10.0  # Minimum to open account
    
    def deposit(self, amount: float) -> bool:
        """
        Override deposit method to include Livret A specific rules.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            bool: True if deposit was successful, False otherwise
        """
        if amount < self.min_opening_amount and self.balance == 0:
            print(f"Error: Minimum opening deposit is {self.min_opening_amount}€")
            return False
        
        if self.balance + amount > self.max_balance:
            print(f"Error: Cannot exceed maximum balance of {self.max_balance}€")
            return False
        
        return super().deposit(amount)


class LDDS(SavingsAccount):
    """
    Livret de Développement Durable et Solidaire implementation.
    """
    
    def __init__(self):
        super().__init__(
            name="LDDS",
            interest_rate=0.03,  # Same as Livret A
            tax_status="tax-free"
        )
        self.max_balance = 12000.0
        self.min_opening_amount = 15.0


class LEP(SavingsAccount):
    """
    Livret d'Épargne Populaire implementation.
    For low-income earners.
    """
    
    def __init__(self):
        super().__init__(
            name="LEP",
            interest_rate=0.06,  # Higher than Livret A
            tax_status="tax-free"
        )
        self.max_balance = 10000.0
        self.min_opening_amount = 30.0
        self.income_requirement = 21393.0  # Annual income limit for 2023
    
    def can_open(self, annual_income: float) -> bool:
        """
        Check if user meets income requirements to open LEP account.
        
        Args:
            annual_income (float): User's annual income
            
        Returns:
            bool: True if eligible, False otherwise
        """
        return annual_income <= self.income_requirement


def compare_accounts() -> dict:
    """
    Compare different French savings accounts.
    
    Returns:
        dict: Dictionary with comparison of account features
    """
    livret_a = LivretA()
    ldds = LDDS()
    lep = LEP()
    
    return {
        'accounts': [
            {
                'name': livret_a.name,
                'interest_rate': livret_a.interest_rate,
                'max_balance': livret_a.max_balance,
                'tax_status': livret_a.tax_status,
                'requirements': "Available to everyone, no income restrictions"
            },
            {
                'name': ldds.name,
                'interest_rate': ldds.interest_rate,
                'max_balance': ldds.max_balance,
                'tax_status': ldds.tax_status,
                'requirements': "Available to everyone, no income restrictions"
            },
            {
                'name': lep.name,
                'interest_rate': lep.interest_rate,
                'max_balance': lep.max_balance,
                'tax_status': lep.tax_status,
                'requirements': f"Annual income below {lep.income_requirement}€"
            }
        ],
        'notes': [
            "All accounts are tax-free (no income tax or social contributions)",
            "Interest rates are set by the government and change periodically",
            "Maximum balances are periodically adjusted for inflation"
        ]
    }


# Example usage
if __name__ == "__main__":
    # Create accounts
    my_livret_a = LivretA()
    my_ldds = LDDS()
    my_lep = LEP()
    
    # Try deposits
    my_livret_a.deposit(1000)
    my_ldds.deposit(500)
    
    # Check LEP eligibility
    user_income = 20000.0
    if my_lep.can_open(user_income):
        my_lep.deposit(300)
    
    # Compare accounts
    comparison = compare_accounts()
    print("Account Comparison:")
    for account in comparison['accounts']:
        print(f"\n{account['name']}:")
        print(f"  Interest Rate: {account['interest_rate']*100}%")
        print(f"  Max Balance: {account['max_balance']}€")
        print(f"  Requirements: {account['requirements']}")
```
