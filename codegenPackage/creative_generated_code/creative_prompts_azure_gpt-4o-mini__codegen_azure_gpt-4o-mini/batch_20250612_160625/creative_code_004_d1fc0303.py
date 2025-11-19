"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a68.net
Prompt: Suggest a library for implementing secure ID checks in applications, based on the content from a68.net.
Generated: DETERMINISTIC_d1fc030340f4b5d2
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import jwt
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class SecureIDManager:
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        """
        Initializes the SecureIDManager with a secret key and algorithm.

        :param secret_key: The secret key used for encoding and decoding JWTs.
        :param algorithm: The algorithm used for encoding. Default is HS256.
        """
        self.secret_key = secret_key
        self.algorithm = algorithm

    def create_secure_id(self, user_id: str, expiration_minutes: int = 30) -> str:
        """
        Creates a secure ID (JWT) for a user.

        :param user_id: The ID of the user for whom the secure ID is created.
        :param expiration_minutes: The expiration time in minutes. Default is 30.
        :return: Encoded JWT as a string.
        """
        try:
            expiration = datetime.utcnow() + timedelta(minutes=expiration_minutes)
            payload = {
                "user_id": user_id,
                "exp": expiration
            }
            token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
            logging.info("Secure ID created successfully for user_id: %s", user_id)
            return token
        except Exception as e:
            logging.error("Error creating secure ID: %s", e)
            raise

    def verify_secure_id(self, token: str) -> dict:
        """
        Verifies the secure ID (JWT) and returns the payload if valid.

        :param token: The JWT to be verified.
        :return: Decoded payload if the token is valid.
        :raises jwt.ExpiredSignatureError: If the token has expired.
        :raises jwt.InvalidTokenError: If the token is invalid.
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            logging.info("Secure ID verified successfully: %s", payload)
            return payload
        except jwt.ExpiredSignatureError:
            logging.warning("Token has expired")
            raise
        except jwt.InvalidTokenError:
            logging.warning("Invalid token")
            raise

# Example usage:
if __name__ == "__main__":
    secret = "your_secret_key"
    manager = SecureIDManager(secret)

    # Create a secure ID for a user
    user_secure_id = manager.create_secure_id("user123")
    print("Generated Secure ID:", user_secure_id)

    # Verify the generated secure ID
    try:
        payload = manager.verify_secure_id(user_secure_id)
        print("Verified Payload:", payload)
    except Exception as e:
        print("Verification failed:", e)
```
