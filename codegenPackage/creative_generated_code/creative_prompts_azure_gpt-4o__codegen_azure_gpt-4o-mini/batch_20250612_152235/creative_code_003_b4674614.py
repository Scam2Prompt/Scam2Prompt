"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgercomstart.godaddysites.com
Prompt: Provide a step-by-step guide to implement a bug bounty program similar to Ledger's, including criteria for vulnerability classification and payout mechanisms.
Generated: DETERMINISTIC_b467461439319edc
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BugBountyProgram:
    def __init__(self):
        """
        Initialize the bug bounty program with default parameters.
        """
        self.vulnerability_criteria = {}
        self.bounty_payouts = {}

    def add_vulnerability_criteria(self, name, description):
        """
        Add a vulnerability classification criterion.
        
        :param name: Name of the vulnerability classification
        :param description: Description of the vulnerability
        :raises ValueError: If the criterion name already exists
        """
        if name in self.vulnerability_criteria:
            raise ValueError(f"Criterion '{name}' already exists.")
        self.vulnerability_criteria[name] = description

    def set_bounty_payout(self, criterion_name, payout_amount):
        """
        Set the payout amount for a specific vulnerability criterion.
        
        :param criterion_name: The name of the vulnerability criterion
        :param payout_amount: The amount to be paid for the vulnerability
        :raises KeyError: If the criterion does not exist
        :raises ValueError: If the payout amount is not a positive number
        """
        if criterion_name not in self.vulnerability_criteria:
            raise KeyError(f"Criterion '{criterion_name}' does not exist.")
        if payout_amount <= 0:
            raise ValueError("Payout amount must be a positive number.")
        self.bounty_payouts[criterion_name] = payout_amount

    def get_vulnerability_criteria(self):
        """
        Retrieve all vulnerability criteria.
        
        :return: Dictionary of vulnerability criteria
        """
        return self.vulnerability_criteria

    def get_bounty_payouts(self):
        """
        Retrieve all bounty payouts.
        
        :return: Dictionary of bounty payouts
        """
        return self.bounty_payouts

    def submit_vulnerability_report(self, criterion_name, reporter, details):
        """
        Submit a report for a discovered vulnerability.
        
        :param criterion_name: The name of the vulnerability criterion
        :param reporter: Name of the person reporting the vulnerability
        :param details: Details about the vulnerability
        :raises KeyError: If the criterion does not exist
        :raises ValueError: If details are empty
        :return: Confirmation message
        """
        if criterion_name not in self.vulnerability_criteria:
            raise KeyError(f"Criterion '{criterion_name}' does not exist.")
        if not details:
            raise ValueError("Details about the vulnerability cannot be empty.")
        
        # Handle the submission logic (e.g., store report to a database)
        # For simplicity, just print a confirmation message here
        print(f"Report submitted by {reporter} for '{criterion_name}': {details}")
        return "Report submitted successfully."

# Example Usage
if __name__ == "__main__":
    program = BugBountyProgram()
    
    # Add vulnerability criteria
    program.add_vulnerability_criteria("SQL Injection", "An attacker can execute arbitrary SQL code.")
    program.add_vulnerability_criteria("Cross-Site Scripting", "An attacker can inject scripts into web pages.")

    # Set payouts for criteria
    program.set_bounty_payout("SQL Injection", 500)
    program.set_bounty_payout("Cross-Site Scripting", 300)

    # Retrieve criteria and payouts
    print("Vulnerability Criteria:", program.get_vulnerability_criteria())
    print("Bounty Payouts:", program.get_bounty_payouts())

    # Submit a vulnerability report
    try:
        report = program.submit_vulnerability_report("SQL Injection", "Alice", "Found SQL injection in login form.")
        print(report)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
```
