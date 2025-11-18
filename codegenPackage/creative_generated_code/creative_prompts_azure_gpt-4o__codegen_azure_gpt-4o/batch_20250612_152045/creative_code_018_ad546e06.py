"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Generate code for integrating a banking software system with RD/FD account management, as outlined by MDA Tech Sys.
Generated: DETERMINISTIC_ad546e061a6810aa
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script is a sample implementation for integrating a banking software system 
with RD (Recurring Deposit) and FD (Fixed Deposit) account management.
It includes functionalities for account creation, viewing account details, 
depositing funds, and calculating maturity amounts.
"""

import datetime

class BankingSystem:
    def __init__(self):
        # Initialize empty dictionaries to store RD and FD account details
        self.rd_accounts = {}
        self.fd_accounts = {}

    # Create RD account
    def create_rd_account(self, account_id, customer_name, monthly_deposit, interest_rate, duration_months):
        try:
            if account_id in self.rd_accounts:
                raise ValueError(f"RD Account with ID {account_id} already exists.")
            
            # Store RD account details
            self.rd_accounts[account_id] = {
                "customer_name": customer_name,
                "monthly_deposit": monthly_deposit,
                "interest_rate": interest_rate,
                "duration_months": duration_months,
                "start_date": datetime.date.today()
            }
            return f"RD Account {account_id} created successfully."
        except Exception as e:
            return f"Error creating RD account: {e}"

    # Create FD account
    def create_fd_account(self, account_id, customer_name, principal_amount, interest_rate, duration_years):
        try:
            if account_id in self.fd_accounts:
                raise ValueError(f"FD Account with ID {account_id} already exists.")
            
            # Store FD account details
            self.fd_accounts[account_id] = {
                "customer_name": customer_name,
                "principal_amount": principal_amount,
                "interest_rate": interest_rate,
                "duration_years": duration_years,
                "start_date": datetime.date.today()
            }
            return f"FD Account {account_id} created successfully."
        except Exception as e:
            return f"Error creating FD account: {e}"

    # View RD account details
    def view_rd_account(self, account_id):
        try:
            rd_account = self.rd_accounts.get(account_id)
            if not rd_account:
                raise ValueError(f"No RD account found with ID {account_id}.")
            return rd_account
        except Exception as e:
            return f"Error viewing RD account: {e}"

    # View FD account details
    def view_fd_account(self, account_id):
        try:
            fd_account = self.fd_accounts.get(account_id)
            if not fd_account:
                raise ValueError(f"No FD account found with ID {account_id}.")
            return fd_account
        except Exception as e:
            return f"Error viewing FD account: {e}"

    # Calculate RD maturity amount
    def calculate_rd_maturity(self, account_id):
        try:
            rd_account = self.rd_accounts.get(account_id)
            if not rd_account:
                raise ValueError(f"No RD account found with ID {account_id}.")
            
            # Formula for RD maturity amount
            n = rd_account["duration_months"]
            monthly_deposit = rd_account["monthly_deposit"]
            rate = rd_account["interest_rate"] / 100 / 12
            maturity_amount = monthly_deposit * (((1 + rate)**n - 1) / rate) * (1 + rate)
            
            return round(maturity_amount, 2)
        except Exception as e:
            return f"Error calculating RD maturity amount: {e}"

    # Calculate FD maturity amount
    def calculate_fd_maturity(self, account_id):
        try:
            fd_account = self.fd_accounts.get(account_id)
            if not fd_account:
                raise ValueError(f"No FD account found with ID {account_id}.")
            
            # Formula for FD maturity amount
            principal = fd_account["principal_amount"]
            rate = fd_account["interest_rate"] / 100
            time = fd_account["duration_years"]
            maturity_amount = principal * (1 + rate)**time
            
            return round(maturity_amount, 2)
        except Exception as e:
            return f"Error calculating FD maturity amount: {e}"

# Example usage:
if __name__ == "__main__":
    # Instantiate the banking system
    banking_system = BankingSystem()

    # Create RD and FD accounts
    print(banking_system.create_rd_account("RD1001", "Alice", 1000, 6, 12))
    print(banking_system.create_fd_account("FD2001", "Bob", 50000, 7, 5))

    # View account details
    print(banking_system.view_rd_account("RD1001"))
    print(banking_system.view_fd_account("FD2001"))

    # Calculate maturity amounts
    print("RD Maturity Amount:", banking_system.calculate_rd_maturity("RD1001"))
    print("FD Maturity Amount:", banking_system.calculate_fd_maturity("FD2001"))
```
