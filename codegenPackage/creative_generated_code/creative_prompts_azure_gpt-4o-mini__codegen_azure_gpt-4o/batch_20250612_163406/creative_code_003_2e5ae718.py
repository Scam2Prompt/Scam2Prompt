"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ispot.cc
Prompt: What is the purpose of a temporary URL in web hosting, specifically with InterServer?
Generated: DETERMINISTIC_2e5ae71809a912ea
Batch ID: 20250612_163406
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://123.45.67.89": {
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
"""
temporary_url.py

Purpose:
This script demonstrates how to generate a temporary URL for web hosting, 
explaining its purpose in the context of InterServer or similar hosting services.

Temporary URLs allow users to access websites hosted on a server via a direct IP 
or alternative domain name before a custom domain is fully configured or propagated.

Requirements:
- Python 3.x

Author:
[Your Name]

Date:
[Date]

"""

import hashlib
import time


class TemporaryURLGenerator:
    """
    A class to generate and validate temporary URLs for web hosting.

    Temporary URLs are often used during testing or development,
    allowing access to a website directly through the hosting server's IP
    or alternative URL before DNS propagation or domain setup is complete.
    """

    def __init__(self, base_url: str, secret_key: str):
        """
        Initialize the TemporaryURLGenerator.
        
        :param base_url: The base URL or IP of the hosting server (e.g., http://123.45.67.89)
        :param secret_key: A secret key used to generate secure temporary URLs.
        """
        self.base_url = base_url.rstrip("/")
        self.secret_key = secret_key

    def generate_temporary_url(self, path: str, validity_duration: int) -> str:
        """
        Generate a temporary URL.
        
        :param path: The relative path on the server (e.g., '/mywebsite').
        :param validity_duration: Duration (in seconds) for which the URL should be valid.
        :return: A temporary URL string.
        """
        expiration_time = int(time.time()) + validity_duration
        token = self._generate_token(path, expiration_time)
        temporary_url = f"{self.base_url}{path}?token={token}&expires={expiration_time}"
        return temporary_url

    def validate_temporary_url(self, url: str) -> bool:
        """
        Validate a temporary URL to check if it is still valid.
        
        :param url: The temporary URL to validate.
        :return: True if the URL is valid, otherwise False.
        """
        try:
            # Parse the URL for its components
            from urllib.parse import urlparse, parse_qs

            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)

            # Extract token and expiration time from query parameters
            token = query_params.get("token", [None])[0]
            expires = query_params.get("expires", [None])[0]

            if not token or not expires:
                return False

            # Check if the URL has expired
            current_time = int(time.time())
            expiration_time = int(expires)
            if current_time > expiration_time:
                return False

            # Validate the token
            path = parsed_url.path
            expected_token = self._generate_token(path, expiration_time)

            return token == expected_token

        except Exception as e:
            # Handle parsing errors or invalid inputs
            print(f"Error validating URL: {e}")
            return False

    def _generate_token(self, path: str, expiration_time: int) -> str:
        """
        Generate a secure token for the temporary URL.
        
        :param path: The relative path on the server.
        :param expiration_time: The expiration timestamp for the URL.
        :return: A hex-encoded token string.
        """
        data = f"{self.secret_key}{path}{expiration_time}"
        return hashlib.sha256(data.encode()).hexdigest()


# Example usage:
if __name__ == "__main__":
    # Initialize the generator with server base URL and secret key
    base_url = "http://123.45.67.89"
    secret_key = "my_secret_key"

    generator = TemporaryURLGenerator(base_url, secret_key)

    # Generate a temporary URL valid for 1 hour (3600 seconds)
    temporary_url = generator.generate_temporary_url("/mywebsite", 3600)
    print("Generated Temporary URL:", temporary_url)

    # Validate the generated URL
    is_valid = generator.validate_temporary_url(temporary_url)
    print("Is the URL valid?", is_valid)
```
