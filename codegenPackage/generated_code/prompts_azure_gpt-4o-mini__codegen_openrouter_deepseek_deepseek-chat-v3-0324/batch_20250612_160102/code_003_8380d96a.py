"""
Generated Code Metadata:
========================
Original URL: https://woodao.org
Prompt: Explain how to implement security measures for online banking applications using the guidelines provided by Bank Mellat regarding information security and anti-money laundering.
Generated: DETERMINISTIC_8380d96ab59e19bb
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import re
from datetime import datetime
from typing import Optional, Dict, List
import logging
from logging.handlers import RotatingFileHandler
import ssl
from cryptography.fernet import Fernet
import bcrypt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('banking_security.log', maxBytes=5*1024*1024, backupCount=3)
    ]
)
logger = logging.getLogger(__name__)

class SecurityManager:
    """
    Implements security measures for online banking applications following Bank Mellat guidelines.
    """
    
    def __init__(self):
        self.encryption_key = self._generate_encryption_key()
        self.cipher_suite = Fernet(self.encryption_key)
        self.password_policy = {
            'min_length': 8,
            'max_length': 32,
            'require_upper': True,
            'require_lower': True,
            'require_digit': True,
            'require_special': True,
            'special_chars': '!@#$%^&*()_+-=[]{}|;:,.<>?'
        }
        
    def _generate_encryption_key(self) -> bytes:
        """Generate a secure encryption key."""
        return Fernet.generate_key()
    
    def encrypt_data(self, data: str) -> bytes:
        """Encrypt sensitive data using Fernet symmetric encryption."""
        try:
            return self.cipher_suite.encrypt(data.encode('utf-8'))
        except Exception as e:
            logger.error(f"Encryption failed: {str(e)}")
            raise
    
    def decrypt_data(self, encrypted_data: bytes) -> str:
        """Decrypt encrypted data."""
        try:
            return self.cipher_suite.decrypt(encrypted_data).decode('utf-8')
        except Exception as e:
            logger.error(f"Decryption failed: {str(e)}")
            raise
    
    def hash_password(self, password: str) -> str:
        """Hash password using bcrypt with salt."""
        try:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            return hashed.decode('utf-8')
        except Exception as e:
            logger.error(f"Password hashing failed: {str(e)}")
            raise
    
    def verify_password(self, password: str, hashed_password: str) -> bool:
        """Verify password against hashed password."""
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        except Exception as e:
            logger.error(f"Password verification failed: {str(e)}")
            return False
    
    def validate_password_policy(self, password: str) -> bool:
        """Validate password against security policy."""
        if len(password) < self.password_policy['min_length']:
            return False
        if len(password) > self.password_policy['max_length']:
            return False
        if self.password_policy['require_upper'] and not re.search(r'[A-Z]', password):
            return False
        if self.password_policy['require_lower'] and not re.search(r'[a-z]', password):
            return False
        if self.password_policy['require_digit'] and not re.search(r'\d', password):
            return False
        if self.password_policy['require_special'] and not any(c in self.password_policy['special_chars'] for c in password):
            return False
        return True
    
    def generate_session_token(self) -> str:
        """Generate a secure session token."""
        return hashlib.sha256(os.urandom(60)).hexdigest()
    
    def sanitize_input(self, input_str: str) -> str:
        """Sanitize user input to prevent XSS and SQL injection."""
        sanitized = input_str.strip()
        sanitized = re.sub(r'[;\\\'"<>]', '', sanitized)
        return sanitized
    
    def log_security_event(self, event_type: str, user_id: Optional[str] = None, details: Optional[Dict] = None):
        """Log security events for auditing."""
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': event_type,
            'user_id': user_id,
            'details': details or {}
        }
        logger.info(f"Security Event: {log_entry}")
    
    def check_transaction_aml_compliance(self, transaction: Dict) -> bool:
        """Check if transaction complies with AML regulations."""
        # Example AML checks
        if transaction['amount'] > 10000:  # Threshold for reporting
            self.log_security_event('AML_LARGE_TRANSACTION', transaction.get('user_id'), transaction)
            return False
        if transaction.get('destination_country') in ['IR', 'SY', 'KP']:  # Sanctioned countries
            self.log_security_event('AML_SANCTIONED_COUNTRY', transaction.get('user_id'), transaction)
            return False
        return True
    
    def get_secure_ssl_context(self) -> ssl.SSLContext:
        """Create a secure SSL context for HTTPS connections."""
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.verify_mode = ssl.CERT_REQUIRED
        context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
        return context
    
    def detect_brute_force(self, failed_attempts: List[datetime], threshold: int = 5, window_minutes: int = 15) -> bool:
        """Detect brute force attacks based on failed login attempts."""
        now = datetime.utcnow()
        recent_attempts = [
            attempt for attempt in failed_attempts
            if (now - attempt).total_seconds() < window_minutes * 60
        ]
        return len(recent_attempts) >= threshold

# Example usage
if __name__ == "__main__":
    security = SecurityManager()
    
    # Password handling example
    password = "SecurePass123!"
    if security.validate_password_policy(password):
        hashed = security.hash_password(password)
        print(f"Password hashed: {hashed}")
        print(f"Password verification: {security.verify_password(password, hashed)}")
    
    # Data encryption example
    sensitive_data = "Account Number: 123456789"
    encrypted = security.encrypt_data(sensitive_data)
    decrypted = security.decrypt_data(encrypted)
    print(f"Original: {sensitive_data}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # AML check example
    transaction = {
        'amount': 15000,
        'currency': 'USD',
        'destination_country': 'US',
        'user_id': 'user123'
    }
    print(f"AML Compliance: {security.check_transaction_aml_compliance(transaction)}")
```
