"""
Generated Code Metadata:
========================
Original URL: https://zerion.be
Prompt: Write a function to validate hosting package activation using a unique activation key.
Generated: DETERMINISTIC_2d59f435fb3db832
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac

class HostingPackageValidator:
    def __init__(self, secret_key):
        """
        Initialize the validator with a secret key.

        :param secret_key: The secret key used for HMAC validation.
        """
        self.secret_key = secret_key.encode('utf-8')

    def validate_activation(self, activation_key, package_id):
        """
        Validate a hosting package activation using a unique activation key.

        :param activation_key: The activation key to validate.
        :param package_id: The ID of the hosting package.
        :return: True if the activation key is valid, False otherwise.
        """
        # Create an HMAC object using the secret key and SHA-256 hashing
        hmac_object = hmac.new(self.secret_key, package_id.encode('utf-8'), hashlib.sha256)
        
        # Get the expected activation key
        expected_activation_key = hmac_object.hexdigest()

        # Compare the expected activation key with the provided activation key
        # Use a constant-time comparison to prevent timing attacks
        return hmac.compare_digest(expected_activation_key, activation_key)

    def generate_activation_key(self, package_id):
        """
        Generate a unique activation key for a hosting package.

        :param package_id: The ID of the hosting package.
        :return: A unique activation key.
        """
        # Create an HMAC object using the secret key and SHA-256 hashing
        hmac_object = hmac.new(self.secret_key, package_id.encode('utf-8'), hashlib.sha256)
        
        # Get the activation key
        activation_key = hmac_object.hexdigest()
        return activation_key


def main():
    # Example usage
    secret_key = "my_secret_key"
    validator = HostingPackageValidator(secret_key)

    package_id = "PKG-12345"
    activation_key = validator.generate_activation_key(package_id)

    print(f"Generated Activation Key: {activation_key}")

    is_valid = validator.validate_activation(activation_key, package_id)
    print(f"Is Activation Key Valid? {is_valid}")

    # Test invalid activation key
    is_valid = validator.validate_activation("invalid_key", package_id)
    print(f"Is Invalid Activation Key Valid? {is_valid}")


if __name__ == "__main__":
    main()
```
