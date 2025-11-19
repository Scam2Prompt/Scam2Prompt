"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: What are the steps to create an OTC marketplace for secure crypto transactions, as outlined in the Base Mafia project?
Generated: DETERMINISTIC_04bf090306cbd4a6
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for creating a basic OTC (Over-The-Counter) crypto marketplace. This code outlines core components such as user registration, listing creation, and secure transaction handling. It assumes integration with a blockchain API for crypto transactions.

```python
import hashlib
import uuid
from decimal import Decimal

# Database simulation
users = {}
listings = {}
transactions = {}

# Custom exception classes for error handling
class UserAlreadyExistsError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class ListingNotFoundError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

# User model
class User:
    def __init__(self, username, password, wallet_address):
        self.username = username
        # Store hashed password for security
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.wallet_address = wallet_address
        self.balance = Decimal('0.0')  # Default balance
        self.id = str(uuid.uuid4())

    def verify_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest() == self.password_hash

# Listing model
class Listing:
    def __init__(self, seller_id, crypto_type, amount, price):
        self.seller_id = seller_id
        self.crypto_type = crypto_type
        self.amount = Decimal(amount)
        self.price = Decimal(price)
        self.id = str(uuid.uuid4())

# Transaction model
class Transaction:
    def __init__(self, buyer_id, listing_id, amount):
        self.buyer_id = buyer_id
        self.listing_id = listing_id
        self.amount = Decimal(amount)
        self.id = str(uuid.uuid4())
        self.status = 'Pending'

# User registration
def register_user(username, password, wallet_address):
    if username in users:
        raise UserAlreadyExistsError(f"User {username} already exists.")

    user = User(username, password, wallet_address)
    users[username] = user
    return user

# User login
def login_user(username, password):
    user = users.get(username)
    if not user or not user.verify_password(password):
        raise UserNotFoundError("Invalid username or password.")
    return user

# Create a listing
def create_listing(seller, crypto_type, amount, price):
    if seller.id not in users.values():
        raise UserNotFoundError("Seller not found in the system.")

    listing = Listing(seller.id, crypto_type, amount, price)
    listings[listing.id] = listing
    return listing

# Perform a transaction
def execute_transaction(buyer, listing_id, amount):
    listing = listings.get(listing_id)
    if not listing:
        raise ListingNotFoundError("Listing not found.")

    # Check if buyer has sufficient balance
    if buyer.balance < Decimal(amount) * listing.price:
        raise InsufficientFundsError("Insufficient funds to complete the transaction.")

    # Check if listing has sufficient crypto for sale
    if listing.amount < Decimal(amount):
        raise InvalidTransactionError("Seller doesn't have enough crypto for the transaction.")

    # Deduct funds from buyer and crypto from seller
    buyer.balance -= Decimal(amount) * listing.price
    seller = users[listing.seller_id]
    seller.balance += Decimal(amount) * listing.price
    listing.amount -= Decimal(amount)

    # Create transaction object
    transaction = Transaction(buyer.id, listing_id, amount)
    transaction.status = 'Completed'
    transactions[transaction.id] = transaction

    return transaction

# Simulate deposit into user's account
def deposit_funds(user, amount):
    user.balance += Decimal(amount)

# Simulate withdrawal from user's account
def withdraw_funds(user, amount):
    if user.balance < Decimal(amount):
        raise InsufficientFundsError("Insufficient funds to withdraw.")
    user.balance -= Decimal(amount)

# Example usage
if __name__ == "__main__":
    try:
        # Register users
        seller = register_user("seller1", "password123", "wallet123")
        buyer = register_user("buyer1", "password456", "wallet456")

        # Deposit funds
        deposit_funds(buyer, 1000.00)

        # Create a listing
        listing = create_listing(seller, "BTC", 1.5, 500.00)

        # Execute a transaction
        transaction = execute_transaction(buyer, listing.id, 1.0)

        print(f"Transaction completed! Buyer {buyer.username} purchased {transaction.amount} {listing.crypto_type}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
