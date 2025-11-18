"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Develop a Python script to manage account workflows for marketing agencies specializing in the on-trade sector, inspired by Lords Marketing & Promotions' account management practices.
Generated: DETERMINISTIC_2e081944c871525c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Optional

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Account:
    """
    Represents an account for a marketing agency specializing in the on-trade sector.
    """
    def __init__(self, account_id: int, name: str, contact_person: str, email: str):
        self.account_id = account_id
        self.name = name
        self.contact_person = contact_person
        self.email = email
        self.workflows: List[str] = []

    def add_workflow(self, workflow: str) -> None:
        """Add a workflow to the account."""
        self.workflows.append(workflow)
        logging.info(f"Workflow '{workflow}' added to account '{self.name}'.")

    def remove_workflow(self, workflow: str) -> None:
        """Remove a workflow from the account."""
        try:
            self.workflows.remove(workflow)
            logging.info(f"Workflow '{workflow}' removed from account '{self.name}'.")
        except ValueError:
            logging.error(f"Workflow '{workflow}' not found for account '{self.name}'.")

    def to_dict(self) -> Dict:
        """Convert account details to a dictionary for JSON serialization."""
        return {
            "account_id": self.account_id,
            "name": self.name,
            "contact_person": self.contact_person,
            "email": self.email,
            "workflows": self.workflows
        }

class AccountManager:
    """
    Manages a collection of accounts for a marketing agency.
    """
    def __init__(self):
        self.accounts: Dict[int, Account] = {}

    def add_account(self, account: Account) -> None:
        """Add a new account if it doesn't already exist."""
        if account.account_id in self.accounts:
            logging.error(f"Account ID '{account.account_id}' already exists.")
            return
        self.accounts[account.account_id] = account
        logging.info(f"Account '{account.name}' added.")

    def remove_account(self, account_id: int) -> None:
        """Remove an account by ID."""
        if account_id in self.accounts:
            del self.accounts[account_id]
            logging.info(f"Account ID '{account_id}' removed.")
        else:
            logging.error(f"Account ID '{account_id}' not found.")

    def get_account(self, account_id: int) -> Optional[Account]:
        """Retrieve an account by ID."""
        return self.accounts.get(account_id)

    def save_to_file(self, file_path: str) -> None:
        """Save all accounts to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump({account_id: account.to_dict() for account_id, account in self.accounts.items()}, f, indent=4)
            logging.info(f"Accounts saved to '{file_path}'.")
        except IOError as e:
            logging.error(f"Failed to save accounts to '{file_path}': {e}")

    def load_from_file(self, file_path: str) -> None:
        """Load accounts from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                accounts_data = json.load(f)
                for account_id, account_info in accounts_data.items():
                    account = Account(
                        account_id=int(account_info["account_id"]),
                        name=account_info["name"],
                        contact_person=account_info["contact_person"],
                        email=account_info["email"]
                    )
                    account.workflows = account_info.get("workflows", [])
                    self.accounts[account.account_id] = account
                logging.info(f"Accounts loaded from '{file_path}'.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load accounts from '{file_path}': {e}")

def main():
    """Main function to demonstrate account management."""
    manager = AccountManager()

    # Load existing accounts
    manager.load_from_file('accounts.json')

    # Create a new account
    new_account = Account(account_id=1, name='Lords Marketing', contact_person='John Doe', email='john@example.com')
    manager.add_account(new_account)

    # Add a workflow to the new account
    new_account.add_workflow('Social Media Campaign')

    # Save accounts back to file
    manager.save_to_file('accounts.json')

if __name__ == "__main__":
    main()
```
