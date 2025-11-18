"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ispot.cc
Prompt: Create a function in Python to generate temporary URLs for testing purposes, similar to the concept described on InterServer's temporary URL page.
Generated: DETERMINISTIC_077f0520fc07c83b
Batch ID: 20250612_151020
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/resource": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
import secrets

def generate_temporary_url(base_url, secret_key, validity_duration=3600):
    """
    Generate a temporary URL with an expiration timestamp and a secure hash.
    
    Args:
        base_url (str): The base URL to which the temporary URL will point.
        secret_key (str): A secret key used for generating the secure hash.
        validity_duration (int): Time in seconds for which the URL is valid (default: 1 hour).
    
    Returns:
        str: A temporary URL with an embedded expiration timestamp and secure hash.
    """
    # Validate inputs
    if not isinstance(base_url, str) or not base_url.startswith("http"):
        raise ValueError("base_url must be a valid URL starting with http or https.")
    if not isinstance(secret_key, str) or not secret_key:
        raise ValueError("secret_key must be a non-empty string.")
    if not isinstance(validity_duration, int) or validity_duration <= 0:
        raise ValueError("validity_duration must be a positive integer.")

    # Generate the expiration timestamp
    expiration_timestamp = int(time.time()) + validity_duration
    
    # Generate a random token for added security
    random_token = secrets.token_hex(16)
    
    # Create a hash using the secret key, expiration timestamp, and random token
    hash_input = f"{base_url}{expiration_timestamp}{random_token}{secret_key}"
    secure_hash = hashlib.sha256(hash_input.encode()).hexdigest()

    # Construct the temporary URL
    temporary_url = f"{base_url}?expires={expiration_timestamp}&token={random_token}&hash={secure_hash}"

    return temporary_url

# Example usage
if __name__ == "__main__":
    try:
        # Base URL and secret key for testing purposes
        base_url = "https://example.com/resource"
        secret_key = "mySecretKey12345"
        
        # Generate a temporary URL valid for 1 hour
        temp_url = generate_temporary_url(base_url, secret_key, validity_duration=3600)
        print(f"Temporary URL: {temp_url}")
    except Exception as e:
        print(f"Error: {e}")
```
