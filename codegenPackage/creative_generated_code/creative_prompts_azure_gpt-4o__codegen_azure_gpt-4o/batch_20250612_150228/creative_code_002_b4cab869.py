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
import hashlib
import json
import time
from typing import Tuple

class TokenClaimValidator:
    """
    A class to validate the token claim process as outlined in the MultiChain protocol.
    """

    def __init__(self, secret_key: str):
        """
        Initialize the validator with a secret key.

        :param secret_key: A unique secret key for token claim validation.
        """
        self.secret_key = secret_key

    def generate_claim_token(self, user_id: str, expiration_seconds: int) -> str:
        """
        Generate a claim token for a user.

        :param user_id: The ID of the user claiming the token.
        :param expiration_seconds: How long the token is valid (in seconds).
        :return: A generated token string.
        """
        current_timestamp = int(time.time())
        expiration_timestamp = current_timestamp + expiration_seconds

        token_data = {
            "user_id": user_id,
            "expiration_timestamp": expiration_timestamp,
            "secret_key": self.secret_key
        }

        # Generate a hash using SHA-256 for the token
        token_hash = hashlib.sha256(json.dumps(token_data).encode()).hexdigest()

        # Return the token string
        return json.dumps({
            "user_id": user_id,
            "expiration_timestamp": expiration_timestamp,
            "token_hash": token_hash
        })

    def validate_claim_token(self, token_string: str) -> Tuple[bool, str]:
        """
        Validate the claim token.

        :param token_string: The token string to validate.
        :return: A tuple containing a boolean (validation status) and a message.
        """
        try:
            # Parse the token string
            token_data = json.loads(token_string)

            user_id = token_data["user_id"]
            expiration_timestamp = token_data["expiration_timestamp"]
            received_token_hash = token_data["token_hash"]

            # Check if the token has expired
            current_timestamp = int(time.time())
            if current_timestamp > expiration_timestamp:
                return False, "Token has expired."

            # Recreate the token hash to verify integrity
            expected_token_hash = hashlib.sha256(json.dumps({
                "user_id": user_id,
                "expiration_timestamp": expiration_timestamp,
                "secret_key": self.secret_key
            }).encode()).hexdigest()

            if received_token_hash != expected_token_hash:
                return False, "Token hash mismatch. Invalid token."

            return True, "Token is valid."

        except (json.JSONDecodeError, KeyError) as e:
            # Handle errors when parsing or validating the token
            return False, f"Invalid token format: {str(e)}"
        except Exception as e:
            # Catch unexpected errors
            return False, f"An error occurred during validation: {str(e)}"


# Example usage
if __name__ == "__main__":
    SECRET_KEY = "my_super_secret_key"

    validator = TokenClaimValidator(secret_key=SECRET_KEY)

    # Generate a token for user 'user123'
    token = validator.generate_claim_token(user_id="user123", expiration_seconds=300)
    print("Generated Token:", token)

    # Validate the token
    is_valid, message = validator.validate_claim_token(token_string=token)
    print("Validation Result:", is_valid)
    print("Validation Message:", message)
```
