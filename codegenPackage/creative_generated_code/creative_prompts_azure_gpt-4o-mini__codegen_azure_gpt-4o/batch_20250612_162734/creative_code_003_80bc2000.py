"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.com
Prompt: Provide a code example for implementing a secure password storage mechanism for user accounts, referencing best practices that might be applicable to gmvci.com.
Generated: DETERMINISTIC_80bc2000adfa5fe8
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import os

# Secure Password Storage Mechanism - Production Ready Code

class PasswordManager:
    """
    A class to manage secure password hashing and verification.
    """
    
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes a password using bcrypt.
        
        Args:
            password (str): The plaintext password to be hashed.
            
        Returns:
            str: The hashed password in a format safe for storage.
        """
        try:
            # Generate a secure salt
            salt = bcrypt.gensalt()
            
            # Hash the password with the generated salt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            
            return hashed_password.decode('utf-8')  # Convert bytes to string for storage
        except Exception as e:
            # Log the error or handle it appropriately
            raise RuntimeError("Error while hashing password") from e

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """
        Verifies a plaintext password against its hashed counterpart.
        
        Args:
            password (str): The plaintext password.
            hashed_password (str): The hashed password stored in the database.
            
        Returns:
            bool: True if the password matches the hash, False otherwise.
        """
        try:
            # Check if the password matches the hash
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        except Exception as e:
            # Log the error or handle it appropriately
            raise RuntimeError("Error while verifying password") from e

# Example usage of PasswordManager
if __name__ == "__main__":
    # Input from user (this would typically come from a form in a web app)
    plaintext_password = "SecurePassword123"
    
    # Hash the password for storage
    hashed = PasswordManager.hash_password(plaintext_password)
    print(f"Hashed Password: {hashed}")
    
    # Verify the password during login
    is_verified = PasswordManager.verify_password("SecurePassword123", hashed)
    print(f"Password Verified: {is_verified}")
```

### Key Notes in the Code
1. **bcrypt Usage**: The bcrypt library is used for hashing and verifying passwords. It is designed for secure password handling and follows industry best practices.
2. **Error Handling**: Proper error handling is implemented to ensure robustness in case of unexpected failures.
3. **Salting**: A unique salt is generated for every password hash, ensuring that even identical passwords produce different hashes.
4. **Encoding**: The `encode` and `decode` methods are used to handle string-to-byte conversion, which is required by bcrypt.
