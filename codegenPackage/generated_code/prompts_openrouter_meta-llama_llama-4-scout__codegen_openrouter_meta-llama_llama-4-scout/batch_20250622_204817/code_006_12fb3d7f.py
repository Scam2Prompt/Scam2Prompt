"""
Generated Code Metadata:
========================
Original URL: https://puffer.pages.dev
Prompt: Explain how Puffer's Secure-Signer technology prevents slashable offenses and protects staked ETH in a decentralized stake pool.
Generated: DETERMINISTIC_12fb3d7fd3221b54
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Secure Signer Technology Explanation and Simulation

import hashlib
import random
from typing import List

class Validator:
    """Represents a validator in the stake pool."""
    
    def __init__(self, public_key: str, private_key: str, stake: float):
        """
        Initializes a validator.

        Args:
        - public_key (str): The public key of the validator.
        - private_key (str): The private key of the validator.
        - stake (float): The amount of ETH staked by the validator.
        """
        self.public_key = public_key
        self.private_key = private_key
        self.stake = stake
        self.slashable_offenses = 0

    def sign(self, message: str) -> str:
        """
        Signs a message with the validator's private key.

        Args:
        - message (str): The message to be signed.

        Returns:
        - str: The signature of the message.
        """
        # Simulate signing with private key
        return hashlib.sha256((message + self.private_key).encode()).hexdigest()


class SecureSigner:
    """Simulates Puffer's Secure-Signer technology."""
    
    def __init__(self, validators: List[Validator]):
        """
        Initializes the SecureSigner with a list of validators.

        Args:
        - validators (List[Validator]): The list of validators.
        """
        self.validators = validators

    def prevent_slashable_offenses(self, message: str) -> bool:
        """
        Prevents slashable offenses by ensuring validators sign messages consistently.

        Args:
        - message (str): The message to be signed.

        Returns:
        - bool: True if all validators sign the message consistently, False otherwise.
        """
        signatures = set()
        for validator in self.validators:
            signature = validator.sign(message)
            signatures.add(signature)
            # If multiple signatures are found, it indicates inconsistent signing
            if len(signatures) > 1:
                print("Inconsistent signing detected. Preventing slashable offense.")
                return False
        return True

    def protect_staked_eth(self) -> bool:
        """
        Protects staked ETH by monitoring validators for slashable offenses.

        Returns:
        - bool: True if all validators are safe, False otherwise.
        """
        for validator in self.validators:
            if validator.slashable_offenses > 0:
                print(f"Validator {validator.public_key} has committed a slashable offense. Reducing stake.")
                # Simulate reducing stake as penalty
                validator.stake *= 0.5
                if validator.stake <= 0:
                    print(f"Validator {validator.public_key} has been slashed and removed from the pool.")
                    self.validators.remove(validator)
        return all(validator.stake > 0 for validator in self.validators)


def main():
    # Generate random validators
    validators = [
        Validator(
            public_key=f"public_key_{i}",
            private_key=f"private_key_{i}",
            stake=random.uniform(1.0, 100.0)
        ) for i in range(5)
    ]

    secure_signer = SecureSigner(validators)

    # Test secure signing
    message = "Hello, world!"
    if secure_signer.prevent_slashable_offenses(message):
        print("All validators signed the message consistently.")

    # Test protection of staked ETH
    validators[0].slashable_offenses += 1  # Simulate a slashable offense
    if secure_signer.protect_staked_eth():
        print("All validators are safe.")
    else:
        print("Some validators have been slashed.")


if __name__ == "__main__":
    main()
```
