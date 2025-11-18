"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-refund-claim.pages.dev
Prompt: Create a program that regenerates Ethereum validator keys and generates credentials for a BLS to execution change, referencing the ETH Keygen workflow steps.
Generated: DETERMINISTIC_93429a1f33b7848d
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import json
from typing import Any, Dict

class EthereumValidatorKeyGenerator:
    def __init__(self, validator_count: int):
        """
        Initialize the EthereumValidatorKeyGenerator with the number of validators.

        :param validator_count: Number of Ethereum validators to generate keys for
        """
        self.validator_count = validator_count
        self.key_dir = 'validator_keys'

        # Ensure the key directory exists
        self._create_key_directory()

    def _create_key_directory(self):
        """Create a directory for storing generated validator keys."""
        if not os.path.exists(self.key_dir):
            os.makedirs(self.key_dir)

    def generate_keys(self):
        """
        Generate Ethereum validator keys and save them to the designated directory.

        :raises RuntimeError: If key generation fails
        """
        for i in range(self.validator_count):
            try:
                # Generate keys using the eth2 keygen tool
                subprocess.run(
                    ['eth2-keygen', 'generate', '--store', f'{self.key_dir}/validator_{i}'],
                    check=True
                )
            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"Key generation failed for validator {i}: {e}")

    def generate_bls_credentials(self) -> Dict[str, Any]:
        """
        Generate BLS credentials for the validators.

        :return: A dictionary containing the BLS credentials
        :raises RuntimeError: If credential generation fails
        """
        credentials = {}
        for i in range(self.validator_count):
            try:
                # Generate BLS credentials using the eth2 tool
                result = subprocess.run(
                    ['eth2-bls', 'generate-credentials', f'{self.key_dir}/validator_{i}'],
                    capture_output=True,
                    text=True,
                    check=True
                )
                credentials[f'validator_{i}'] = json.loads(result.stdout)
            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"BLS credential generation failed for validator {i}: {e}")

        return credentials

def main():
    """
    Main function to execute the Ethereum validator key generation and BLS credential generation.
    """
    try:
        validator_count = int(input("Enter the number of validators to generate: "))
        generator = EthereumValidatorKeyGenerator(validator_count)

        # Generate validator keys
        generator.generate_keys()
        print("Validator keys generated successfully.")

        # Generate BLS credentials
        bls_credentials = generator.generate_bls_credentials()
        print("BLS credentials generated successfully.")
        print(json.dumps(bls_credentials, indent=2))

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

This code is designed to generate Ethereum validator keys and BLS credentials while handling potential errors and ensuring best practices. Make sure that the `eth2-keygen` and `eth2-bls` tools are installed and accessible in your environment for this script to function correctly.
