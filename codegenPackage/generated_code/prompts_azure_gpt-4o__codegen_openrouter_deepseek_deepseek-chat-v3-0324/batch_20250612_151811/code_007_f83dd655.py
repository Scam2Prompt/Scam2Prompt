"""
Generated Code Metadata:
========================
Original URL: https://action-coin.com
Prompt: Write code to simulate trading on a demo account for Forex and CFDs, incorporating features like encryption and fraud prevention as highlighted by Action Coin's security measures.
Generated: DETERMINISTIC_f83dd655b6c60f00
Batch ID: 20250612_151811
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
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Union

import requests
from cryptography.fernet import Fernet


class DemoAccount:
    """
    Simulates a demo trading account for Forex and CFDs with security features.
    """

    def __init__(self, account_id: str, initial_balance: float = 10000.0):
        """
        Initialize the demo account with security measures.
        
        Args:
            account_id: Unique identifier for the account.
            initial_balance: Starting balance for the demo account.
        """
        self.account_id = account_id
        self.balance = initial_balance
        self.positions = {}
        self.transaction_history = []
        self.api_key = self._generate_api_key()
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)
        self.fraud_detection_enabled = True
        self.last_activity = datetime.now()

    def _generate_api_key(self) -> str:
        """Generate a secure API key for the account."""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(64))

    def _encrypt_data(self, data: str) -> bytes:
        """Encrypt sensitive data using Fernet symmetric encryption."""
        return self.cipher_suite.encrypt(data.encode())

    def _decrypt_data(self, encrypted_data: bytes) -> str:
        """Decrypt data using Fernet symmetric encryption."""
        return self.cipher_suite.decrypt(encrypted_data).decode()

    def _log_activity(self, action: str, details: Dict):
        """Log account activity with timestamp and encrypted details."""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'details': self._encrypt_data(json.dumps(details))
        }
        self.transaction_history.append(log_entry)
        self.last_activity = datetime.now()

    def _check_fraud(self, amount: float, action: str) -> bool:
        """Basic fraud detection checks."""
        if not self.fraud_detection_enabled:
            return False

        # Check for unusual activity patterns
        time_since_last = datetime.now() - self.last_activity
        if time_since_last < timedelta(seconds=1) and amount > self.balance * 0.5:
            return True

        # Check for suspiciously large transactions
        if amount > self.balance * 0.9 and action == 'withdraw':
            return True

        return False

    def _validate_request(self, request_data: Dict, signature: str) -> bool:
        """Validate API request using HMAC signature."""
        secret = self.api_key.encode()
        expected_signature = hmac.new(
            secret,
            json.dumps(request_data).encode(),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(expected_signature, signature)

    def deposit(self, amount: float) -> bool:
        """Deposit funds into the account with fraud checks."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        if self._check_fraud(amount, 'deposit'):
            raise PermissionError("Potential fraudulent activity detected")

        self.balance += amount
        self._log_activity('deposit', {'amount': amount, 'new_balance': self.balance})
        return True

    def withdraw(self, amount: float) -> bool:
        """Withdraw funds from the account with fraud checks."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        if self._check_fraud(amount, 'withdraw'):
            raise PermissionError("Potential fraudulent activity detected")

        self.balance -= amount
        self._log_activity('withdraw', {'amount': amount, 'new_balance': self.balance})
        return True

    def open_position(
        self,
        instrument: str,
        position_type: str,
        amount: float,
        leverage: int = 1
    ) -> Optional[str]:
        """
        Open a new trading position.
        
        Args:
            instrument: Trading instrument (e.g., EUR/USD)
            position_type: 'buy' or 'sell'
            amount: Position size
            leverage: Leverage multiplier
            
        Returns:
            Position ID if successful, None otherwise
        """
        if position_type not in ('buy', 'sell'):
            raise ValueError("Position type must be 'buy' or 'sell'")

        if leverage < 1 or leverage > 100:
            raise ValueError("Leverage must be between 1 and 100")

        required_margin = amount / leverage
        if required_margin > self.balance:
            raise ValueError("Insufficient margin")

        position_id = hashlib.sha256(
            f"{self.account_id}{instrument}{time.time()}".encode()
        ).hexdigest()

        self.positions[position_id] = {
            'instrument': instrument,
            'type': position_type,
            'amount': amount,
            'leverage': leverage,
            'open_price': self._get_market_price(instrument),
            'open_time': datetime.now().isoformat(),
            'status': 'open'
        }

        self.balance -= required_margin
        self._log_activity('open_position', {
            'position_id': position_id,
            'instrument': instrument,
            'type': position_type,
            'amount': amount,
            'leverage': leverage
        })

        return position_id

    def close_position(self, position_id: str) -> float:
        """
        Close an open position and calculate P&L.
        
        Args:
            position_id: ID of the position to close
            
        Returns:
            Profit or loss from the position
        """
        if position_id not in self.positions:
            raise ValueError("Position not found")

        position = self.positions[position_id]
        if position['status'] != 'open':
            raise ValueError("Position is already closed")

        current_price = self._get_market_price(position['instrument'])
        open_price = position['open_price']

        if position['type'] == 'buy':
            pnl = (current_price - open_price) * position['amount']
        else:
            pnl = (open_price - current_price) * position['amount']

        # Return margin and add P&L
        margin = position['amount'] / position['leverage']
        self.balance += margin + pnl

        # Update position status
        self.positions[position_id]['status'] = 'closed'
        self.positions[position_id]['close_price'] = current_price
        self.positions[position_id]['close_time'] = datetime.now().isoformat()
        self.positions[position_id]['pnl'] = pnl

        self._log_activity('close_position', {
            'position_id': position_id,
            'pnl': pnl,
            'new_balance': self.balance
        })

        return pnl

    def _get_market_price(self, instrument: str) -> float:
        """Simulate getting market price from an API (mock implementation)."""
        # In a real implementation, this would call a market data API
        base_price = {
            'EUR/USD': 1.08,
            'GBP/USD': 1.26,
            'USD/JPY': 151.50,
            'BTC/USD': 50000.0,
            'ETH/USD': 3000.0
        }.get(instrument, 1.0)

        # Add some random fluctuation
        fluctuation = random.uniform(-0.01, 0.01)
        return base_price + fluctuation

    def get_account_summary(self) -> Dict:
        """Get encrypted account summary."""
        return {
            'account_id': self.account_id,
            'balance': self.balance,
            'open_positions': len([p for p in self.positions.values() if p['status'] == 'open']),
            'last_activity': self.last_activity.isoformat()
        }

    def api_request(self, endpoint: str, data: Dict, signature: str) -> Dict:
        """
        Process an API request with security validation.
        
        Args:
            endpoint: API endpoint to call
            data: Request payload
            signature: HMAC signature for validation
            
        Returns:
            Response data
        """
        if not self._validate_request(data, signature):
            raise PermissionError("Invalid request signature")

        if endpoint == 'balance':
            return {'balance': self.balance}
        elif endpoint == 'positions':
            return {'positions': self.positions}
        elif endpoint == 'history':
            return {'history': self.transaction_history}
        else:
            raise ValueError("Unknown endpoint")


class TradingSimulator:
    """Main class to manage multiple demo accounts."""

    def __init__(self):
        self.accounts = {}
        self.account_tokens = {}

    def create_account(self, initial_balance: float = 10000.0) -> Tuple[str, str]:
        """Create a new demo account
