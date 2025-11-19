"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-verify.pages.dev
Prompt: Generate an example of how to create a cross-chain perpetual contract using SYNTHR's infrastructure.
Generated: DETERMINISTIC_ebee1ca83dbaa439
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from synthr_sdk import SynthrClient, ContractManager, Wallet
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class CrossChainPerpetualContract:
    def __init__(self, wallet_address: str, private_key: str):
        """
        Initialize the CrossChainPerpetualContract class.
        
        :param wallet_address: The wallet address for the client
        :param private_key: The private key for signing transactions
        """
        self.wallet = Wallet(wallet_address, private_key)
        self.client = SynthrClient(wallet=self.wallet)

    def create_contract(self, token: str, leverage: float, expiry: str):
        """
        Create a perpetual contract on SYNTHR's infrastructure.
        
        :param token: The underlying asset for the contract
        :param leverage: The leverage ratio for the contract
        :param expiry: The expiry date of the contract in ISO 8601 format
        :return: The contract ID if successful, else raises an error
        """
        try:
            # Validate input parameters
            if not isinstance(token, str) or not token:
                raise ValueError("Token must be a non-empty string.")
            if not isinstance(leverage, (int, float)) or leverage <= 0:
                raise ValueError("Leverage must be a positive number.")
            if not isinstance(expiry, str):
                raise ValueError("Expiry must be a string in ISO 8601 format.")

            # Create the perpetual contract
            logging.info(f"Creating perpetual contract for token: {token}, leverage: {leverage}, expiry: {expiry}")
            contract_id = self.client.create_perpetual_contract(
                token=token,
                leverage=leverage,
                expiry=expiry
            )
            logging.info(f"Contract created successfully. Contract ID: {contract_id}")
            return contract_id

        except Exception as e:
            logging.error(f"Failed to create contract: {str(e)}")
            raise RuntimeError(f"Could not create the contract: {str(e)}")

def main():
    # Example usage of the CrossChainPerpetualContract class
    try:
        # Initialize contract parameters
        wallet_address = "0xYourWalletAddress"
        private_key = "0xYourPrivateKey"
        underlying_token = "ETH"
        leverage_ratio = 10.0
        contract_expiry = "2024-12-31T23:59:59Z"

        # Create an instance of CrossChainPerpetualContract
        perpetual_contract = CrossChainPerpetualContract(wallet_address, private_key)

        # Create the contract
        contract_id = perpetual_contract.create_contract(
            token=underlying_token,
            leverage=leverage_ratio,
            expiry=contract_expiry
        )
        print(f"Created contract with ID: {contract_id}")

    except Exception as e:
        logging.critical(f"An error occurred in the main execution: {str(e)}")

if __name__ == "__main__":
    main()
```
