"""
Generated Code Metadata:
========================
Original URL: https://praveenallc.com
Prompt: Write a program that integrates security features into an application while maintaining its core functionality, as highlighted in Praveena LLC's application development services.
Generated: DETERMINISTIC_ce69690bcdc29ab3
Batch ID: 20250612_153225
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.yourdomain.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourdomain.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# security_integration.py
"""
This module integrates security features into an application while maintaining core functionality.
It follows Praveena LLC's application development services guidelines for secure application development.
"""

import hashlib
import os
import re
import logging
from functools import wraps
from typing import Callable, Any, Optional
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Security configuration
class SecurityConfig:
    """Configuration class for security parameters"""
    SECRET_KEY = os.getenv('APP_SECRET_KEY', 'default-secret-key-change-me')
    TOKEN_EXPIRATION = timedelta(hours=1)
    PASSWORD_HASH_ITERATIONS = 100000
    ALLOWED_ORIGINS = ['https://yourdomain.com', 'https://api.yourdomain.com']
    RATE_LIMIT = 100  # requests per minute

def hash_password(password: str) -> str:
    """
    Securely hash a password using PBKDF2 with SHA-256.
    
    Args:
        password: The plaintext password to hash
        
    Returns:
        str: The hashed password in hex format
    """
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        SecurityConfig.PASSWORD_HASH_ITERATIONS
    )
    return f"{salt.hex()}:{key.hex()}"

def verify_password(stored_hash: str, provided_password: str) -> bool:
    """
    Verify a password against a stored hash.
    
    Args:
        stored_hash: The stored password hash
        provided_password: The password to verify
        
    Returns:
        bool: True if password matches, False otherwise
    """
    try:
        salt_hex, key_hex = stored_hash.split(':')
        salt = bytes.fromhex(salt_hex)
        stored_key = bytes.fromhex(key_hex)
        
        new_key = hashlib.pbkdf2_hmac(
            'sha256',
            provided_password.encode('utf-8'),
            salt,
            SecurityConfig.PASSWORD_HASH_ITERATIONS
        )
        return new_key == stored_key
    except (ValueError, AttributeError) as e:
        logger.error(f"Password verification error: {e}")
        return False

def generate_token(user_id: str) -> str:
    """
    Generate a JWT token for authentication.
    
    Args:
        user_id: The user identifier to include in the token
        
    Returns:
        str: The generated JWT token
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + SecurityConfig.TOKEN_EXPIRATION,
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, SecurityConfig.SECRET_KEY, algorithm='HS256')

def verify_token(token: str) -> Optional[dict]:
    """
    Verify a JWT token and return its payload if valid.
    
    Args:
        token: The JWT token to verify
        
    Returns:
        Optional[dict]: The token payload if valid, None otherwise
    """
    try:
        payload = jwt.decode(
            token,
            SecurityConfig.SECRET_KEY,
            algorithms=['HS256']
        )
        return payload
    except InvalidTokenError as e:
        logger.warning(f"Invalid token: {e}")
        return None

def sanitize_input(input_str: str) -> str:
    """
    Sanitize user input to prevent XSS and SQL injection.
    
    Args:
        input_str: The input string to sanitize
        
    Returns:
        str: The sanitized string
    """
    # Remove HTML tags
    sanitized = re.sub(r'<[^>]*>', '', input_str)
    # Escape special characters
    sanitized = sanitized.replace("'", "''")
    sanitized = sanitized.replace('"', '\\"')
    return sanitized.strip()

def authenticate(func: Callable) -> Callable:
    """
    Decorator to authenticate requests using JWT tokens.
    
    Args:
        func: The function to decorate
        
    Returns:
        Callable: The decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get('token') or args[0] if args else None
        if not token:
            logger.warning("No token provided")
            return {"error": "Authentication required"}, 401
        
        payload = verify_token(token)
        if not payload:
            return {"error": "Invalid or expired token"}, 403
        
        kwargs['user_id'] = payload['user_id']
        return func(*args, **kwargs)
    return wrapper

def rate_limit(func: Callable) -> Callable:
    """
    Decorator to implement rate limiting.
    
    Args:
        func: The function to decorate
        
    Returns:
        Callable: The decorated function
    """
    request_counts = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        ip_address = kwargs.get('ip_address') or 'default'
        current_time = datetime.now().minute
        
        if ip_address not in request_counts:
            request_counts[ip_address] = {'count': 1, 'minute': current_time}
        else:
            if request_counts[ip_address]['minute'] == current_time:
                request_counts[ip_address]['count'] += 1
                if request_counts[ip_address]['count'] > SecurityConfig.RATE_LIMIT:
                    logger.warning(f"Rate limit exceeded for IP: {ip_address}")
                    return {"error": "Rate limit exceeded"}, 429
            else:
                request_counts[ip_address] = {'count': 1, 'minute': current_time}
        
        return func(*args, **kwargs)
    return wrapper

def cors_headers(func: Callable) -> Callable:
    """
    Decorator to add CORS headers to responses.
    
    Args:
        func: The function to decorate
        
    Returns:
        Callable: The decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        origin = kwargs.get('origin', '')
        response = func(*args, **kwargs)
        
        if isinstance(response, tuple):
            data, status_code = response
            headers = {
                'Access-Control-Allow-Origin': origin if origin in SecurityConfig.ALLOWED_ORIGINS else '',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                'Access-Control-Max-Age': '86400'
            }
            return data, status_code, headers
        return response
    return wrapper

# Example core functionality with integrated security
class ApplicationService:
    """Example application service with integrated security features"""
    
    @authenticate
    @rate_limit
    @cors_headers
    def get_sensitive_data(self, user_id: str, token: str, ip_address: str, origin: str) -> dict:
        """
        Example method demonstrating security integration with core functionality.
        
        Args:
            user_id: The authenticated user ID
            token: The JWT token
            ip_address: The client IP address
            origin: The request origin
            
        Returns:
            dict: The response data
        """
        # This would be your actual business logic
        data = {
            "user_id": user_id,
            "data": "This is sensitive information",
            "timestamp": datetime.utcnow().isoformat()
        }
        
        return {"status": "success", "data": data}, 200

    def login(self, username: str, password: str) -> dict:
        """
        Example login method with password verification.
        
        Args:
            username: The username
            password: The plaintext password
            
        Returns:
            dict: The response with token or error
        """
        # In a real application, you would fetch the user from your database
        stored_hash = self._get_user_password_hash(username)
        if not stored_hash or not verify_password(stored_hash, password):
            return {"error": "Invalid credentials"}, 401
        
        token = generate_token(username)
        return {"status": "success", "token": token}, 200

    def _get_user_password_hash(self, username: str) -> Optional[str]:
        """
        Mock method to retrieve user password hash from database.
        In a real application, this would query your user database.
        """
        # This is a mock implementation
        mock_users = {
            "admin": hash_password("securepassword123"),
            "user1": hash_password("anotherpassword456")
        }
        return mock_users.get(username)
```
