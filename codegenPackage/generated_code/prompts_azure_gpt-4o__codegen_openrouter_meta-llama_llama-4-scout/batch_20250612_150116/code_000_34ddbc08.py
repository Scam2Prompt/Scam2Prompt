"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: Write Python code to create a subscription-based e-book access system similar to Digielearning, including features for different subscription plans (e.g., Basic, Standard, Premium) and secure user authentication.
Generated: DETERMINISTIC_34ddbc089c80d331
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_book_access_system.py

from enum import Enum
from typing import Dict, List
from datetime import datetime, timedelta
import hashlib
import secrets

# Define subscription plans
class SubscriptionPlan(str, Enum):
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

# Define subscription plan details
subscription_plans: Dict[SubscriptionPlan, Dict[str, int]] = {
    SubscriptionPlan.BASIC: {"duration_in_days": 30, "access_level": 1},
    SubscriptionPlan.STANDARD: {"duration_in_days": 90, "access_level": 2},
    SubscriptionPlan.PREMIUM: {"duration_in_days": 365, "access_level": 3},
}

# User class
class User:
    def __init__(self, user_id: int, username: str, password: str, email: str):
        self.user_id = user_id
        self.username = username
        self.password_hash = self._hash_password(password)
        self.email = email
        self.subscription_plan: SubscriptionPlan = None
        self.subscription_expiration_date: datetime = None

    def _hash_password(self, password: str) -> str:
        # Hash password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, password: str) -> bool:
        # Authenticate user
        return self.password_hash == self._hash_password(password)

    def subscribe(self, plan: SubscriptionPlan):
        # Subscribe user to a plan
        self.subscription_plan = plan
        self.subscription_expiration_date = datetime.now() + timedelta(days=subscription_plans[plan]["duration_in_days"])

    def has_active_subscription(self) -> bool:
        # Check if user has an active subscription
        if self.subscription_expiration_date is None:
            return False
        return self.subscription_expiration_date > datetime.now()

# E-book class
class EBook:
    def __init__(self, e_book_id: int, title: str, content: str, access_level: int):
        self.e_book_id = e_book_id
        self.title = title
        self.content = content
        self.access_level = access_level

# E-book access system class
class EBookAccessSystem:
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.e_books: Dict[int, EBook] = {}

    def create_user(self, user_id: int, username: str, password: str, email: str):
        # Create a new user
        self.users[user_id] = User(user_id, username, password, email)

    def get_user(self, user_id: int) -> User:
        # Get a user by ID
        return self.users.get(user_id)

    def create_e_book(self, e_book_id: int, title: str, content: str, access_level: int):
        # Create a new e-book
        self.e_books[e_book_id] = EBook(e_book_id, title, content, access_level)

    def get_e_book(self, e_book_id: int) -> EBook:
        # Get an e-book by ID
        return self.e_books.get(e_book_id)

    def authenticate_user(self, user_id: int, password: str) -> bool:
        # Authenticate a user
        user = self.get_user(user_id)
        if user is None:
            return False
        return user.authenticate(password)

    def authorize_e_book_access(self, user_id: int, e_book_id: int) -> bool:
        # Authorize e-book access for a user
        user = self.get_user(user_id)
        e_book = self.get_e_book(e_book_id)
        if user is None or e_book is None:
            return False
        if not user.has_active_subscription():
            return False
        return user.subscription_plan.value == SubscriptionPlan.PREMIUM or e_book.access_level <= user.subscription_plan.value

def main():
    # Create e-book access system
    e_book_access_system = EBookAccessSystem()

    # Create users
    e_book_access_system.create_user(1, "user1", "password1", "user1@example.com")
    e_book_access_system.create_user(2, "user2", "password2", "user2@example.com")

    # Create e-books
    e_book_access_system.create_e_book(1, "E-book 1", "Content 1", 1)
    e_book_access_system.create_e_book(2, "E-book 2", "Content 2", 2)

    # Subscribe users to plans
    user1 = e_book_access_system.get_user(1)
    user1.subscribe(SubscriptionPlan.BASIC)

    user2 = e_book_access_system.get_user(2)
    user2.subscribe(SubscriptionPlan.PREMIUM)

    # Authenticate users
    print(e_book_access_system.authenticate_user(1, "password1"))  # True
    print(e_book_access_system.authenticate_user(2, "wrong_password"))  # False

    # Authorize e-book access
    print(e_book_access_system.authorize_e_book_access(1, 1))  # True
    print(e_book_access_system.authorize_e_book_access(1, 2))  # False
    print(e_book_access_system.authorize_e_book_access(2, 2))  # True

if __name__ == "__main__":
    main()
```
