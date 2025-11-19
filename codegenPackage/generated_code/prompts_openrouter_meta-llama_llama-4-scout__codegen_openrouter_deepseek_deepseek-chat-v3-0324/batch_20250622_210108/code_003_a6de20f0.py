"""
Generated Code Metadata:
========================
Original URL: https://waltztechsec.com
Prompt: Develop a secure wallet recovery system for cryptocurrency and hardware wallets, incorporating multi-factor authentication and secure key storage, based on WaltzTech Security's wallet recovery services.
Generated: DETERMINISTIC_a6de20f06bc4faac
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import hmac
import base64
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from typing import Optional, Dict, Tuple
import pyotp
import qrcode
from getpass import getpass
import secrets
import string
import bcrypt

class WalletRecoverySystem:
    """
    Secure wallet recovery system with multi-factor authentication and encrypted key storage.
    """
    
    def __init__(self):
        self.users_db = "users.json"  # Simulated user database
        self.salt = os.urandom(16)    # For key derivation
        self._initialize_db()
        
    def _initialize_db(self) -> None:
        """Initialize the user database if it doesn't exist."""
        if not os.path.exists(self.users_db):
            with open(self.users_db, 'w') as f:
                json.dump({}, f)
    
    def _generate_key(self, password: str) -> bytes:
        """Derive a cryptographic key from a password."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    def _encrypt_data(self, data: str, key: bytes) -> str:
        """Encrypt data using Fernet symmetric encryption."""
        f = Fernet(key)
        return f.encrypt(data.encode()).decode()
    
    def _decrypt_data(self, encrypted_data: str, key: bytes) -> str:
        """Decrypt data using Fernet symmetric encryption."""
        f = Fernet(key)
        return f.decrypt(encrypted_data.encode()).decode()
    
    def _hash_password(self, password: str) -> str:
        """Hash a password using bcrypt."""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    def _verify_password(self, password: str, hashed_password: str) -> bool:
        """Verify a password against its bcrypt hash."""
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
    
    def _generate_2fa_secret(self) -> str:
        """Generate a new TOTP secret for 2FA."""
        return pyotp.random_base32()
    
    def _generate_recovery_code(self) -> str:
        """Generate a secure recovery code."""
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(24))
    
    def register_user(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Register a new user with password and 2FA setup.
        Returns (success, message) tuple.
        """
        try:
            with open(self.users_db, 'r') as f:
                users = json.load(f)
            
            if username in users:
                return False, "Username already exists"
            
            # Generate user data
            hashed_pw = self._hash_password(password)
            recovery_code = self._generate_recovery_code()
            totp_secret = self._generate_2fa_secret()
            
            # Encrypt recovery code with password-derived key
            key = self._generate_key(password)
            encrypted_recovery_code = self._encrypt_data(recovery_code, key)
            
            users[username] = {
                'password_hash': hashed_pw,
                'recovery_code': encrypted_recovery_code,
                'totp_secret': totp_secret,
                'wallet_data': None,
                'failed_attempts': 0,
                'locked': False
            }
            
            with open(self.users_db, 'w') as f:
                json.dump(users, f)
            
            # Generate QR code for 2FA setup
            totp_uri = pyotp.totp.TOTP(totp_secret).provisioning_uri(username, issuer_name="WaltzTech Wallet Recovery")
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(totp_uri)
            qr.make(fit=True)
            qr_img = qr.make_image(fill='black', back_color='white')
            qr_img.save(f"{username}_2fa.png")
            
            return True, f"User registered successfully. Recovery code: {recovery_code}. Scan the QR code for 2FA setup."
        
        except Exception as e:
            return False, f"Registration failed: {str(e)}"
    
    def authenticate_user(self, username: str, password: str, totp_code: str) -> Tuple[bool, str]:
        """
        Authenticate a user with password and 2FA.
        Returns (success, message) tuple.
        """
        try:
            with open(self.users_db, 'r') as f:
                users = json.load(f)
            
            if username not in users:
                return False, "User not found"
            
            user = users[username]
            
            if user['locked']:
                return False, "Account locked due to too many failed attempts"
            
            if not self._verify_password(password, user['password_hash']):
                user['failed_attempts'] += 1
                if user['failed_attempts'] >= 5:
                    user['locked'] = True
                with open(self.users_db, 'w') as f:
                    json.dump(users, f)
                return False, "Invalid password"
            
            totp = pyotp.TOTP(user['totp_secret'])
            if not totp.verify(totp_code):
                return False, "Invalid 2FA code"
            
            # Reset failed attempts on successful login
            user['failed_attempts'] = 0
            with open(self.users_db, 'w') as f:
                json.dump(users, f)
            
            return True, "Authentication successful"
        
        except Exception as e:
            return False, f"Authentication failed: {str(e)}"
    
    def store_wallet_data(self, username: str, password: str, wallet_data: str) -> Tuple[bool, str]:
        """
        Securely store encrypted wallet data for a user.
        Returns (success, message) tuple.
        """
        try:
            with open(self.users_db, 'r') as f:
                users = json.load(f)
            
            if username not in users:
                return False, "User not found"
            
            key = self._generate_key(password)
            encrypted_wallet = self._encrypt_data(wallet_data, key)
            
            users[username]['wallet_data'] = encrypted_wallet
            with open(self.users_db, 'w') as f:
                json.dump(users, f)
            
            return True, "Wallet data stored successfully"
        
        except Exception as e:
            return False, f"Failed to store wallet data: {str(e)}"
    
    def recover_wallet(self, username: str, recovery_code: str) -> Tuple[bool, str]:
        """
        Recover wallet data using the recovery code.
        Returns (success, decrypted_wallet_data) tuple.
        """
        try:
            with open(self.users_db, 'r') as f:
                users = json.load(f)
            
            if username not in users:
                return False, "User not found"
            
            user = users[username]
            
            # Temporarily unlock account for recovery
            user['locked'] = False
            with open(self.users_db, 'w') as f:
                json.dump(users, f)
            
            # Prompt for new password to derive key
            new_password = getpass("Enter a new password for recovery: ")
            key = self._generate_key(new_password)
            
            try:
                decrypted_recovery_code = self._decrypt_data(user['recovery_code'], key)
            except:
                return False, "Invalid recovery code or password"
            
            if not hmac.compare_digest(recovery_code, decrypted_recovery_code):
                return False, "Invalid recovery code"
            
            if not user['wallet_data']:
                return False, "No wallet data found"
            
            decrypted_wallet = self._decrypt_data(user['wallet_data'], key)
            
            # Update password hash with new password
            user['password_hash'] = self._hash_password(new_password)
            user['failed_attempts'] = 0
            with open(self.users_db, 'w') as f:
                json.dump(users, f)
            
            return True, decrypted_wallet
        
        except Exception as e:
            return False, f"Recovery failed: {str(e)}"
    
    def generate_backup_export(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Generate an encrypted backup export of wallet data.
        Returns (success, encrypted_export) tuple.
        """
        try:
            with open(self.users_db, 'r') as f:
                users = json.load(f)
            
            if
