"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gngm.clck.hk
Prompt: Generate a script that simulates the GMGN login process by validating a device ID, confirming a seed phrase, and implementing two-factor authentication.
Generated: DETERMINISTIC_8e50047d3c954ee3
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import random
import string

# Constants for simulation
VALID_DEVICE_IDS = {"device123", "device456", "device789"}  # Example valid device IDs
SEED_PHRASE = "correct horse battery staple"  # Example seed phrase for validation
TWO_FACTOR_CODE_LENGTH = 6


def validate_device_id(device_id):
    """
    Validate the provided device ID against a list of valid device IDs.

    :param device_id: str, the device ID to validate
    :return: bool, True if the device ID is valid, False otherwise
    """
    return device_id in VALID_DEVICE_IDS


def confirm_seed_phrase(provided_seed_phrase):
    """
    Validate the provided seed phrase against the stored seed phrase.

    :param provided_seed_phrase: str, the seed phrase to validate
    :return: bool, True if the seed phrase matches, False otherwise
    """
    return provided_seed_phrase == SEED_PHRASE


def generate_two_factor_code():
    """
    Generate a random numeric two-factor authentication code.

    :return: str, the generated two-factor code
    """
    return ''.join(random.choices(string.digits, k=TWO_FACTOR_CODE_LENGTH))


def validate_two_factor_code(provided_code, actual_code):
    """
    Validate the provided two-factor authentication code.

    :param provided_code: str, the code entered by the user
    :param actual_code: str, the actual code generated
    :return: bool, True if the codes match, False otherwise
    """
    return provided_code == actual_code


def simulate_login(device_id, seed_phrase, two_factor_code):
    """
    Simulate the GMGN login process by validating the device ID,
    confirming the seed phrase, and performing two-factor authentication.

    :param device_id: str, the device ID provided by the user
    :param seed_phrase: str, the seed phrase provided by the user
    :param two_factor_code: str, the two-factor code provided by the user
    :return: str, login status message
    """
    try:
        # Step 1: Validate the device ID
        if not validate_device_id(device_id):
            return "Login failed: Invalid device ID."

        # Step 2: Confirm the seed phrase
        if not confirm_seed_phrase(seed_phrase):
            return "Login failed: Incorrect seed phrase."

        # Step 3: Generate a two-factor authentication code
        actual_code = generate_two_factor_code()
        # Simulate sending the code (e.g., via SMS or email)
        print(f"Two-factor code sent: {actual_code}")  # For demonstration purposes

        # Step 4: Validate the two-factor code
        if not validate_two_factor_code(two_factor_code, actual_code):
            return "Login failed: Incorrect two-factor authentication code."

        # If all validations pass, login is successful
        return "Login successful."
    except Exception as e:
        # Catch any unexpected errors and return a generic failure message
        return f"Login failed due to an error: {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Sample input for simulation (replace with actual user input in production)
    input_device_id = "device123"
    input_seed_phrase = "correct horse battery staple"
    input_two_factor_code = input("Enter the two-factor code sent to your device: ")

    # Simulate login process
    result = simulate_login(
        device_id=input_device_id,
        seed_phrase=input_seed_phrase,
        two_factor_code=input_two_factor_code
    )
    print(result)
```
