"""
Generated Code Metadata:
========================
Original URL: https://91224d72.5bab219c7482a7cd39bd1d22.workers.dev
Prompt: How would you code a "Just a moment" delay with a security check in a web application, considering performance implications?
Generated: DETERMINISTIC_b481119809075bdc
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
import random
import hashlib
import hmac

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_security_token(secret_key):
    """
    Generate a security token.

    Args:
        secret_key (str): The secret key used for HMAC.

    Returns:
        str: A security token.
    """
    # Generate a random token
    token = str(random.randint(100000, 999999))
    # Create an HMAC object using the secret key and the token
    hmac_object = hmac.new(secret_key.encode(), token.encode(), hashlib.sha256)
    # Return the token and the HMAC digest
    return token, hmac_object.hexdigest()

def verify_security_token(token, hmac_digest, secret_key):
    """
    Verify a security token.

    Args:
        token (str): The token to verify.
        hmac_digest (str): The HMAC digest to verify.
        secret_key (str): The secret key used for HMAC.

    Returns:
        bool: True if the token is valid, False otherwise.
    """
    # Create an HMAC object using the secret key and the token
    hmac_object = hmac.new(secret_key.encode(), token.encode(), hashlib.sha256)
    # Compare the HMAC digests
    return hmac.compare_digest(hmac_object.hexdigest(), hmac_digest)

def just_a_moment_delay(max_delay=3):
    """
    Introduce a random delay to prevent brute-force attacks.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 3.

    Returns:
        None
    """
    # Calculate a random delay
    delay = random.randint(1, max_delay)
    logger.info(f"Introducing a delay of {delay} seconds")
    # Sleep for the calculated delay
    time.sleep(delay)

def security_check(token, hmac_digest, secret_key):
    """
    Perform a security check.

    Args:
        token (str): The token to verify.
        hmac_digest (str): The HMAC digest to verify.
        secret_key (str): The secret key used for HMAC.

    Returns:
        bool: True if the security check passes, False otherwise.
    """
    try:
        # Verify the security token
        return verify_security_token(token, hmac_digest, secret_key)
    except Exception as e:
        logger.error(f"Security check failed: {e}")
        return False

def main():
    # Define a secret key
    secret_key = "my_secret_key"

    # Generate a security token
    token, hmac_digest = generate_security_token(secret_key)
    logger.info(f"Generated token: {token}, HMAC digest: {hmac_digest}")

    # Simulate a request with the security token
    request_token = token
    request_hmac_digest = hmac_digest

    # Introduce a delay
    just_a_moment_delay()

    # Perform a security check
    if security_check(request_token, request_hmac_digest, secret_key):
        logger.info("Security check passed")
    else:
        logger.info("Security check failed")

if __name__ == "__main__":
    main()
```
