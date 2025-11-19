"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakestoneclaim.pages.dev
Prompt: Write a code example for a lending protocol that utilizes STONE as collateral, ensuring it aligns with the features outlined in the StakeStone documentation.
Generated: DETERMINISTIC_8703726fce5bd0a7
Batch ID: 20250612_163443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class StoneLendingProtocol:
    def __init__(self):
        self.loans = {}
        self.collateral = {}
    
    def lend(self, borrower, amount, stone_amount):
        """
        Lends a certain amount to the borrower using STONE as collateral.
        
        :param borrower: The address of the borrower
        :param amount: The amount of currency to lend
        :param stone_amount: The amount of STONE used as collateral
        :raises ValueError: If the collateral is insufficient or amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Loan amount must be greater than 0.")
        
        if not self.is_collateral_sufficient(borrower, stone_amount):
            raise ValueError("Insufficient STONE collateral.")
        
        # Register the loan
        loan_id = self.generate_loan_id()
        self.loans[loan_id] = {
            'borrower': borrower,
            'amount': amount,
            'stone_amount': stone_amount,
            'timestamp': time.time(),
            'active': True
        }
        
        # Deduct collateral
        self.collateral[borrower] = self.collateral.get(borrower, 0) - stone_amount
        
        print(f"Loan granted: {loan_id} | Amount: {amount} | Collateral: {stone_amount} STONE")
        return loan_id

    def repay(self, loan_id):
        """
        Repays a loan and releases the collateral.
        
        :param loan_id: The identifier of the loan to repay
        :raises ValueError: If loan_id is invalid or loan is already repaid
        """
        if loan_id not in self.loans:
            raise ValueError("Invalid loan ID.")
        
        loan = self.loans[loan_id]
        if not loan['active']:
            raise ValueError("Loan has already been repaid.")
        
        # Mark loan as repaid
        loan['active'] = False
        
        # Return collateral
        self.collateral[loan['borrower']] = self.collateral.get(loan['borrower'], 0) + loan['stone_amount']
        
        print(f"Loan repaid: {loan_id} | Collateral returned: {loan['stone_amount']} STONE")
    
    def is_collateral_sufficient(self, borrower, stone_amount):
        """
        Checks if the given borrower has sufficient STONE as collateral.
        
        :param borrower: The address of the borrower
        :param stone_amount: The amount of STONE needed as collateral
        :return: True if sufficient, False otherwise
        """
        return self.collateral.get(borrower, 0) >= stone_amount
    
    def generate_loan_id(self):
        """
        Generates a unique loan identifier.
        
        :return: A unique loan ID
        """
        return f"loan-{random.randint(1000, 9999)}"

# Example Usage
if __name__ == "__main__":
    protocol = StoneLendingProtocol()
    
    # Adding collateral for a borrower
    protocol.collateral['0x123456789'] = 100  # Assume this address has 100 STONE
    
    try:
        loan_id = protocol.lend('0x123456789', 50, 20)  # Borrow 50 with 20 STONE as collateral
        protocol.repay(loan_id)  # Repay the loan
    except ValueError as e:
        print(f"Error: {e}")
```
