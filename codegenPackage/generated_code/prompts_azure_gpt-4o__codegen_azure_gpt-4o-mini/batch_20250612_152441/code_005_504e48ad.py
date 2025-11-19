"""
Generated Code Metadata:
========================
Original URL: https://synthr-register-wallet.pages.dev
Prompt: Develop a solution for tracking SYNTHR badge milestones and syCREDITS earned by users, including integration with a self-custody wallet.
Generated: DETERMINISTIC_504e48ad4bf4c90b
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    """Class representing a user with SYNTHR badge milestones and syCREDITS."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.badges = []
        self.sycredits = 0

    def earn_badge(self, badge: str) -> None:
        """Add a badge to the user's collection."""
        if badge not in self.badges:
            self.badges.append(badge)
            logging.info(f"User {self.user_id} earned badge: {badge}")
        else:
            logging.warning(f"User {self.user_id} already has badge: {badge}")

    def add_sycredits(self, amount: int) -> None:
        """Add syCREDITS to the user's account."""
        if amount < 0:
            logging.error("Cannot add negative syCREDITS.")
            raise ValueError("Amount must be non-negative.")
        self.sycredits += amount
        logging.info(f"User {self.user_id} added syCREDITS: {amount}. Total: {self.sycredits}")

    def get_user_data(self) -> Dict[str, Any]:
        """Return user data as a dictionary."""
        return {
            "user_id": self.user_id,
            "badges": self.badges,
            "sycredits": self.sycredits
        }

class Wallet:
    """Class representing a self-custody wallet for users."""
    
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        """Deposit an amount into the wallet."""
        if amount <= 0:
            logging.error("Deposit amount must be positive.")
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        logging.info(f"Deposited {amount} to wallet {self.wallet_address}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        """Withdraw an amount from the wallet."""
        if amount <= 0:
            logging.error("Withdrawal amount must be positive.")
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            logging.error("Insufficient funds for withdrawal.")
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        logging.info(f"Withdrew {amount} from wallet {self.wallet_address}. New balance: {self.balance}")

    def get_balance(self) -> float:
        """Return the current balance of the wallet."""
        return self.balance

def save_user_data(user: User, filename: str) -> None:
    """Save user data to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(user.get_user_data(), file)
            logging.info(f"User data saved to {filename}.")
    except IOError as e:
        logging.error(f"Failed to save user data: {e}")
        raise

def load_user_data(user_id: str, filename: str) -> User:
    """Load user data from a JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if data['user_id'] != user_id:
                raise ValueError("User ID does not match.")
            user = User(user_id)
            user.badges = data['badges']
            user.sycredits = data['sycredits']
            logging.info(f"User data loaded from {filename}.")
            return user
    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"Failed to load user data: {e}")
        raise

# Example usage
if __name__ == "__main__":
    user = User("user123")
    user.earn_badge("SYNTHR Novice")
    user.add_sycredits(100)

    wallet = Wallet("0x1234567890abcdef")
    wallet.deposit(50.0)

    save_user_data(user, "user_data.json")
    loaded_user = load_user_data("user123", "user_data.json")
    print(loaded_user.get_user_data())
```
