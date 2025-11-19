"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: What is the role of Fully Homomorphic Encryption (FHE) in PrivateAI's data-as-a-service model, and how does it ensure data privacy?
Generated: DETERMINISTIC_3b84a788db50eef2
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, Any
import json
from phe import paillier  # Using PyPaillier for Homomorphic Encryption

class PrivateAIDataService:
    """
    A class representing PrivateAI's Data-as-a-Service model using Fully Homomorphic Encryption (FHE).
    This ensures data privacy by allowing computations on encrypted data without decryption.
    """

    def __init__(self):
        """
        Initialize the service with a public-private key pair for Paillier encryption.
        """
        self.public_key, self.private_key = paillier.generate_paillier_keypair()

    def encrypt_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Encrypt sensitive data fields using FHE (Paillier scheme).

        Args:
            data (Dict[str, Any]): Raw data to be encrypted.

        Returns:
            Dict[str, Any]: Encrypted data with sensitive fields replaced by ciphertexts.
        """
        encrypted_data = {}
        for key, value in data.items():
            if isinstance(value, (int, float)):
                encrypted_data[key] = self.public_key.encrypt(value)
            else:
                encrypted_data[key] = value  # Non-numeric fields remain as-is
        return encrypted_data

    def perform_secure_computation(self, encrypted_data: Dict[str, Any], operation: str) -> Any:
        """
        Perform computations on encrypted data without decryption.

        Args:
            encrypted_data (Dict[str, Any]): Encrypted data.
            operation (str): Operation to perform (e.g., 'sum', 'average').

        Returns:
            Any: Result of the computation (still encrypted if numeric).

        Raises:
            ValueError: If operation is not supported or data is invalid.
        """
        if not encrypted_data:
            raise ValueError("No encrypted data provided")

        numeric_values = [
            val for val in encrypted_data.values() if isinstance(val, paillier.EncryptedNumber)
        ]

        if not numeric_values:
            raise ValueError("No numeric data to compute")

        if operation == 'sum':
            result = sum(numeric_values, self.public_key.encrypt(0))
        elif operation == 'average':
            total = sum(numeric_values, self.public_key.encrypt(0))
            count = self.public_key.encrypt(len(numeric_values))
            result = total / count.ciphertext()
        else:
            raise ValueError(f"Unsupported operation: {operation}")

        return result

    def decrypt_result(self, encrypted_result: paillier.EncryptedNumber) -> float:
        """
        Decrypt the result of a computation using the private key.

        Args:
            encrypted_result (paillier.EncryptedNumber): Encrypted result to decrypt.

        Returns:
            float: Decrypted result.
        """
        return self.private_key.decrypt(encrypted_result)

    def serialize_encrypted_data(self, encrypted_data: Dict[str, Any]) -> str:
        """
        Serialize encrypted data to JSON for storage/transmission.

        Args:
            encrypted_data (Dict[str, Any]): Encrypted data.

        Returns:
            str: JSON string representation of the encrypted data.
        """
        serializable_data = {}
        for key, value in encrypted_data.items():
            if isinstance(value, paillier.EncryptedNumber):
                serializable_data[key] = {
                    'ciphertext': str(value.ciphertext()),
                    'exponent': value.exponent
                }
            else:
                serializable_data[key] = value
        return json.dumps(serializable_data)

    def deserialize_encrypted_data(self, json_str: str) -> Dict[str, Any]:
        """
        Deserialize JSON-encoded encrypted data back into EncryptedNumber objects.

        Args:
            json_str (str): JSON string containing serialized encrypted data.

        Returns:
            Dict[str, Any]: Deserialized encrypted data.
        """
        data = json.loads(json_str)
        deserialized_data = {}
        for key, value in data.items():
            if isinstance(value, dict) and 'ciphertext' in value:
                ciphertext = int(value['ciphertext'])
                exponent = int(value['exponent'])
                deserialized_data[key] = paillier.EncryptedNumber(
                    self.public_key, ciphertext, exponent
                )
            else:
                deserialized_data[key] = value
        return deserialized_data

# Example usage
if __name__ == "__main__":
    # Initialize the service
    private_ai = PrivateAIDataService()

    # Sample data to encrypt
    sample_data = {
        "user_id": "user123",
        "age": 30,
        "income": 75000,
        "credit_score": 720
    }

    # Encrypt the data
    encrypted_data = private_ai.encrypt_data(sample_data)
    print("Encrypted data:", private_ai.serialize_encrypted_data(encrypted_data))

    # Perform secure computation (sum of numeric fields)
    try:
        encrypted_sum = private_ai.perform_secure_computation(encrypted_data, 'sum')
        decrypted_sum = private_ai.decrypt_result(encrypted_sum)
        print(f"Sum of numeric fields: {decrypted_sum}")
    except ValueError as e:
        print(f"Error during computation: {e}")
```
