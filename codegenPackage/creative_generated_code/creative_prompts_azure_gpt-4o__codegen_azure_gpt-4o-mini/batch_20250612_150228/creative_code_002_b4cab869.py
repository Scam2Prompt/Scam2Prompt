"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://home--txnets.pages.dev
Prompt: Generate code to validate a token claim process as outlined in the "Claim Token" section of the MultiChain protocol.
Generated: DETERMINISTIC_b4cab86945380588
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import jwt  # Importing the PyJWT library for handling JSON Web Tokens
from datetime import datetime, timedelta

class TokenValidator:
    def __init__(self, secret_key: str):
        """
        Initializes the TokenValidator with a secret key.
        
        :param secret_key: The secret key used for encoding and decoding tokens.
        """
        self.secret_key = secret_key

    def validate_token(self, token: str) -> dict:
        """
        Validates the provided JWT token.
        
        :param token: The JWT token to validate.
        :return: Decoded token claims if validation is successful.
        :raises ValueError: If the token is expired or invalid.
        """
        try:
            # Decode the token using the secret key
            claims = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            
            # Check for expiration
            if 'exp' in claims:
                expiration_time = datetime.fromtimestamp(claims['exp'])
                if expiration_time < datetime.utcnow():
                    raise ValueError("Token has expired.")
            
            return claims
        
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired.")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token.")

    def create_token(self, claims: dict, expiration_minutes: int = 60) -> str:
        """
        Creates a new JWT token with the specified claims.
        
        :param claims: The claims to include in the token.
        :param expiration_minutes: The number of minutes until the token expires.
        :return: The encoded JWT token.
        """
        # Set expiration time
        expiration = datetime.utcnow() + timedelta(minutes=expiration_minutes)
        claims['exp'] = expiration.timestamp()
        
        # Create the token
        token = jwt.encode(claims, self.secret_key, algorithm="HS256")
        
        return token


# Example usage
if __name__ == "__main__":
    # Secret key for signing tokens (should be kept safe)
    SECRET_KEY = "your_secret_key_here"

    # Initialize the TokenValidator
    validator = TokenValidator(SECRET_KEY)

    # Example claims
    claims = {
        "sub": "user123",
        "name": "John Doe",
        "role": "admin"
    }

    # Create a token
    token = validator.create_token(claims)
    print("Generated Token:", token)

    # Validate the token
    try:
        validated_claims = validator.validate_token(token)
        print("Validated Claims:", validated_claims)
    except ValueError as e:
        print("Token validation error:", e)
```
