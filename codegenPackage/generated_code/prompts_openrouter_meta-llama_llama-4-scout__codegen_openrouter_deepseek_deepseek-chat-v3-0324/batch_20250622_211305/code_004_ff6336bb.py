"""
Generated Code Metadata:
========================
Original URL: https://quantumfbc6.com
Prompt: Create a demo account script for Quantum FBC 6.0, allowing users to test the software's performance with virtual money before committing real funds.
Generated: DETERMINISTIC_ff6336bbc7da21a5
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Quantum FBC 6.0 Demo Account Script

This script creates demo accounts for Quantum FBC 6.0, allowing users to test
the software with virtual money before committing real funds.

Features:
- Generates unique demo accounts with virtual balance
- Secure account creation with validation
- Persists accounts to database
- Provides account cleanup functionality
"""

import uuid
import random
import sqlite3
from datetime import datetime, timedelta
from typing import Optional, Dict

# Configuration
DATABASE_FILE = "quantum_fbc_demo.db"
DEFAULT_VIRTUAL_BALANCE = 10000.00  # Starting virtual balance
ACCOUNT_EXPIRY_DAYS = 30  # Accounts expire after 30 days


class DemoAccountManager:
    """Manages creation and maintenance of demo accounts."""

    def __init__(self):
        """Initialize the account manager and ensure database setup."""
        self._initialize_database()

    def _initialize_database(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS demo_accounts (
                    account_id TEXT PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    balance REAL NOT NULL,
                    created_at TEXT NOT NULL,
                    expires_at TEXT NOT NULL,
                    is_active INTEGER DEFAULT 1
                )
            """)
            conn.commit()

    def _generate_credentials(self) -> Dict[str, str]:
        """Generate random username and password for demo account."""
        username = f"demo_{uuid.uuid4().hex[:8]}"
        password = uuid.uuid4().hex[:12]
        return {"username": username, "password": password}

    def create_demo_account(self) -> Dict[str, str]:
        """
        Create a new demo account with virtual funds.
        
        Returns:
            Dictionary containing account details including:
            - account_id: Unique account identifier
            - username: Generated username
            - password: Generated password
            - balance: Virtual starting balance
            - expires_at: Account expiration date
        """
        credentials = self._generate_credentials()
        account_id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()
        expires_at = (datetime.now() + timedelta(days=ACCOUNT_EXPIRY_DAYS)).isoformat()

        try:
            with sqlite3.connect(DATABASE_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO demo_accounts
                    (account_id, username, password, balance, created_at, expires_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    account_id,
                    credentials["username"],
                    credentials["password"],
                    DEFAULT_VIRTUAL_BALANCE,
                    created_at,
                    expires_at
                ))
                conn.commit()

            return {
                "account_id": account_id,
                "username": credentials["username"],
                "password": credentials["password"],
                "balance": DEFAULT_VIRTUAL_BALANCE,
                "expires_at": expires_at
            }

        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to create demo account: {str(e)}")

    def validate_account(self, username: str, password: str) -> Optional[Dict[str, str]]:
        """
        Validate demo account credentials and check if account is active.
        
        Args:
            username: Demo account username
            password: Demo account password
            
        Returns:
            Account details if valid, None otherwise
        """
        try:
            with sqlite3.connect(DATABASE_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT account_id, username, balance, expires_at
                    FROM demo_accounts
                    WHERE username = ? AND password = ? AND is_active = 1
                """, (username, password))
                result = cursor.fetchone()

                if result:
                    return {
                        "account_id": result[0],
                        "username": result[1],
                        "balance": result[2],
                        "expires_at": result[3]
                    }
                return None

        except sqlite3.Error as e:
            raise RuntimeError(f"Account validation failed: {str(e)}")

    def cleanup_expired_accounts(self) -> int:
        """
        Mark expired accounts as inactive.
        
        Returns:
            Number of accounts deactivated
        """
        try:
            with sqlite3.connect(DATABASE_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE demo_accounts
                    SET is_active = 0
                    WHERE expires_at < ? AND is_active = 1
                """, (datetime.now().isoformat(),))
                count = cursor.rowcount
                conn.commit()
                return count

        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to cleanup expired accounts: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        manager = DemoAccountManager()
        
        # Create a demo account
        new_account = manager.create_demo_account()
        print("Demo account created successfully:")
        print(f"Username: {new_account['username']}")
        print(f"Password: {new_account['password']}")
        print(f"Balance: ${new_account['balance']:,.2f}")
        print(f"Expires on: {new_account['expires_at']}")
        
        # Cleanup expired accounts
        cleaned = manager.cleanup_expired_accounts()
        print(f"\nCleaned up {cleaned} expired accounts")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
