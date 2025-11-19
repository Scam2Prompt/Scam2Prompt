"""
Generated Code Metadata:
========================
Original URL: https://optimisenow.net
Prompt: Write a code snippet that automates the tracking and reimbursement of expenses using a Digitised Expense Claims System (DECS).
Generated: DETERMINISTIC_7aa859c9be256796
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from datetime import datetime

class ExpenseClaim:
    """Class to represent an individual expense claim."""
    
    def __init__(self, user_id, amount, description, date):
        self.claim_id = str(uuid.uuid4())  # Unique identifier for the claim
        self.user_id = user_id  # ID of the user making the claim
        self.amount = amount  # Amount of the expense
        self.description = description  # Description of the expense
        self.date = date  # Date of the expense
        self.status = 'Pending'  # Initial status of the claim

    def approve(self):
        """Approve the expense claim."""
        self.status = 'Approved'

    def reject(self):
        """Reject the expense claim."""
        self.status = 'Rejected'


class ExpenseClaimsSystem:
    """Class to manage the expense claims system."""
    
    def __init__(self):
        self.claims = []  # List to store expense claims

    def add_claim(self, user_id, amount, description, date):
        """Add a new expense claim to the system."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if not isinstance(date, datetime):
            raise TypeError("Date must be a datetime object.")
        
        claim = ExpenseClaim(user_id, amount, description, date)
        self.claims.append(claim)
        return claim.claim_id

    def approve_claim(self, claim_id):
        """Approve an expense claim by its ID."""
        claim = self._find_claim(claim_id)
        if claim:
            claim.approve()
            return claim
        else:
            raise LookupError("Claim ID not found.")

    def reject_claim(self, claim_id):
        """Reject an expense claim by its ID."""
        claim = self._find_claim(claim_id)
        if claim:
            claim.reject()
            return claim
        else:
            raise LookupError("Claim ID not found.")

    def _find_claim(self, claim_id):
        """Private method to find a claim by its ID."""
        for claim in self.claims:
            if claim.claim_id == claim_id:
                return claim
        return None

    def get_claims(self, user_id=None):
        """Retrieve all claims, optionally filtered by user ID."""
        if user_id:
            return [claim for claim in self.claims if claim.user_id == user_id]
        return self.claims

    def export_claims(self, file_path):
        """Export claims to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump([claim.__dict__ for claim in self.claims], file, default=str)
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        expense_system = ExpenseClaimsSystem()
        claim_id = expense_system.add_claim("user123", 150.00, "Business lunch", datetime.now())
        print(f"Claim added with ID: {claim_id}")

        # Approve the claim
        approved_claim = expense_system.approve_claim(claim_id)
        print(f"Claim approved: {approved_claim.__dict__}")

        # Export claims to a file
        expense_system.export_claims("claims.json")
        print("Claims exported successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
