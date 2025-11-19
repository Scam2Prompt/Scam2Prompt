"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-evista-software.com
Prompt: Generate code to simulate a demo account for cryptocurrency trading, incorporating features like enhanced security with cryptography and borderless transactions as described on Bitcoin Evista.
Generated: DETERMINISTIC_a5fab408b6073e61
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import json
import os
import random
import string
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Union

# Constants
CURRENCIES = ["BTC", "ETH", "LTC", "XRP", "USDT"]
INITIAL_BALANCE = 10000.0  # USD
API_KEY_LENGTH = 32
SECRET_KEY_LENGTH = 64
HASH_ALGORITHM = "sha256"
TOKEN_EXPIRY_HOURS = 24


class CryptoTradingAccount:
    """
    A demo cryptocurrency trading account with enhanced security features.
    """

    def __init__(self, username: str, email: str):
        """
        Initialize a new trading account.
        
        Args:
            username: Account username
            email: Account email address
        """
        self.username = username
        self.email = email
        self.balances = {"USD": INITIAL_BALANCE}
        self.transactions = []
        self.api_key = self._generate_random_key(API_KEY_LENGTH)
        self.secret_key = self._generate_random_key(SECRET_KEY_LENGTH)
        self.session_tokens = {}
        self._initialize_balances()

    def _initialize_balances(self) -> None:
        """Initialize cryptocurrency balances with zero amounts."""
        for currency in CURRENCIES:
            self.balances[currency] = 0.0

    def _generate_random_key(self, length: int) -> str:
        """Generate a random cryptographic key."""
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    def _hash_data(self, data: str) -> str:
        """Hash data using HMAC with the account's secret key."""
        return hmac.new(
            self.secret_key.encode(),
            data.encode(),
            hashlib.sha256
        ).hexdigest()

    def generate_session_token(self) -> str:
        """Generate a new session token with expiry."""
        token = self._generate_random_key(64)
        expiry = datetime.now() + timedelta(hours=TOKEN_EXPIRY_HOURS)
        self.session_tokens[token] = expiry
        return token

    def validate_token(self, token: str) -> bool:
        """Validate a session token."""
        if token not in self.session_tokens:
            return False
        if datetime.now() > self.session_tokens[token]:
            del self.session_tokens[token]
            return False
        return True

    def get_balances(self) -> Dict[str, float]:
        """Return current account balances."""
        return self.balances

    def deposit(self, amount: float, currency: str = "USD") -> bool:
        """
        Deposit funds into the account.
        
        Args:
            amount: Amount to deposit
            currency: Currency to deposit (default: USD)
        
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            return False
        
        currency = currency.upper()
        if currency not in self.balances:
            return False
            
        self.balances[currency] += amount
        self._record_transaction("deposit", amount, currency)
        return True

    def withdraw(self, amount: float, currency: str = "USD") -> bool:
        """
        Withdraw funds from the account.
        
        Args:
            amount: Amount to withdraw
            currency: Currency to withdraw (default: USD)
        
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            return False
            
        currency = currency.upper()
        if currency not in self.balances or self.balances[currency] < amount:
            return False
            
        self.balances[currency] -= amount
        self._record_transaction("withdrawal", amount, currency)
        return True

    def buy(self, base_currency: str, quote_currency: str, amount: float, price: float) -> bool:
        """
        Buy cryptocurrency.
        
        Args:
            base_currency: Currency to buy (e.g., BTC)
            quote_currency: Currency to spend (e.g., USD)
            amount: Amount of base currency to buy
            price: Price per unit of base currency
        
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0 or price <= 0:
            return False
            
        base_currency = base_currency.upper()
        quote_currency = quote_currency.upper()
        
        total_cost = amount * price
        
        if (quote_currency not in self.balances or 
            base_currency not in self.balances or 
            self.balances[quote_currency] < total_cost):
            return False
            
        self.balances[quote_currency] -= total_cost
        self.balances[base_currency] += amount
        self._record_transaction(
            "buy", 
            amount, 
            base_currency,
            {"quote_currency": quote_currency, "price": price, "total_cost": total_cost}
        )
        return True

    def sell(self, base_currency: str, quote_currency: str, amount: float, price: float) -> bool:
        """
        Sell cryptocurrency.
        
        Args:
            base_currency: Currency to sell (e.g., BTC)
            quote_currency: Currency to receive (e.g., USD)
            amount: Amount of base currency to sell
            price: Price per unit of base currency
        
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0 or price <= 0:
            return False
            
        base_currency = base_currency.upper()
        quote_currency = quote_currency.upper()
        
        total_value = amount * price
        
        if (base_currency not in self.balances or 
            quote_currency not in self.balances or 
            self.balances[base_currency] < amount):
            return False
            
        self.balances[base_currency] -= amount
        self.balances[quote_currency] += total_value
        self._record_transaction(
            "sell", 
            amount, 
            base_currency,
            {"quote_currency": quote_currency, "price": price, "total_value": total_value}
        )
        return True

    def _record_transaction(self, 
                          tx_type: str, 
                          amount: float, 
                          currency: str,
                          metadata: Optional[Dict] = None) -> None:
        """
        Record a transaction in the account history.
        
        Args:
            tx_type: Type of transaction (deposit, withdrawal, buy, sell)
            amount: Transaction amount
            currency: Transaction currency
            metadata: Additional transaction details
        """
        tx = {
            "timestamp": datetime.now().isoformat(),
            "type": tx_type,
            "amount": amount,
            "currency": currency,
            "metadata": metadata or {}
        }
        self.transactions.append(tx)

    def get_transaction_history(self, limit: int = 10) -> List[Dict]:
        """
        Get transaction history.
        
        Args:
            limit: Maximum number of transactions to return
        
        Returns:
            List of transaction records
        """
        return self.transactions[-limit:]

    def generate_api_signature(self, data: Dict) -> str:
        """
        Generate an API request signature.
        
        Args:
            data: Request data to sign
        
        Returns:
            str: HMAC signature
        """
        sorted_data = json.dumps(data, sort_keys=True)
        return self._hash_data(sorted_data)

    def verify_api_signature(self, data: Dict, signature: str) -> bool:
        """
        Verify an API request signature.
        
        Args:
            data: Request data
            signature: Signature to verify
        
        Returns:
            bool: True if signature is valid, False otherwise
        """
        expected_signature = self.generate_api_signature(data)
        return hmac.compare_digest(expected_signature, signature)


class BorderlessPaymentProcessor:
    """
    Simulate borderless cryptocurrency payments.
    """

    @staticmethod
    def generate_payment_request(
        sender_account: CryptoTradingAccount,
        recipient_address: str,
        amount: float,
        currency: str
    ) -> Dict:
        """
        Generate a borderless payment request.
        
        Args:
            sender_account: Sender's account
            recipient_address: Recipient's wallet address
            amount: Amount to send
            currency: Currency to send
        
        Returns:
            Dict: Payment request details
        """
        payment_id = hashlib.sha256(
            f"{sender_account.username}{recipient_address}{datetime.now().timestamp()}".encode()
        ).hexdigest()
        
        return {
            "payment_id": payment_id,
            "sender": sender_account.username,
            "recipient": recipient_address,
            "amount": amount,
            "currency": currency.upper(),
            "timestamp": datetime.now().isoformat(),
            "status": "pending"
        }

    @staticmethod
    def process_payment(
        sender_account: CryptoTradingAccount,
        payment_request: Dict
    ) -> bool:
        """
