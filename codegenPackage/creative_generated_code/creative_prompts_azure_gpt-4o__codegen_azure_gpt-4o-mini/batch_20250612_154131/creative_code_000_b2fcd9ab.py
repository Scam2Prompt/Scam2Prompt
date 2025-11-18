"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.com
Prompt: Write a Python script to interact with Morpho's smart contracts for depositing crypto assets into non-custodial vaults optimized for yield. Include steps for selecting a tailored strategy based on risk level.
Generated: DETERMINISTIC_b2fcd9abf0cb3280
Batch ID: 20250612_154131
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import json
import requests
from web3 import Web3
from web3.exceptions import ContractLogicError

# Constants for the Infura endpoint and Morpho contract details
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
MORPHO_CONTRACT_ADDRESS = "0xYourMorphoContractAddress"
MORPHO_ABI = json.loads('[{"constant":true,"inputs":[...],"name":"...","outputs":[...],"payable":false,"stateMutability":"view","type":"function"}, ...]')  # Replace with actual ABI

# Risk strategy mappings
RISK_STRATEGIES = {
    "low": "0xLowRiskStrategyAddress",
    "medium": "0xMediumRiskStrategyAddress",
    "high": "0xHighRiskStrategyAddress"
}

class MorphoVault:
    def __init__(self, wallet_address: str, private_key: str):
        self.web3 = Web3(Web3.HTTPProvider(INFURA_URL))
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.contract = self.web3.eth.contract(address=MORPHO_CONTRACT_ADDRESS, abi=MORPHO_ABI)

    def deposit(self, amount: float, risk_level: str):
        """Deposit crypto assets into the vault based on the selected risk strategy."""
        if risk_level not in RISK_STRATEGIES:
            raise ValueError("Invalid risk level. Choose from 'low', 'medium', or 'high'.")

        strategy_address = RISK_STRATEGIES[risk_level]
        nonce = self.web3.eth.getTransactionCount(self.wallet_address)

        # Create a transaction for depositing assets
        transaction = {
            'to': strategy_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': nonce,
        }

        # Sign the transaction
        signed_txn = self.web3.eth.account.sign_transaction(transaction, self.private_key)

        try:
            # Send the transaction
            txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            print(f"Transaction successful with hash: {self.web3.toHex(txn_hash)}")
        except ContractLogicError as e:
            print(f"Contract logic error occurred: {str(e)}")
        except ValueError as e:
            print(f"Value error occurred: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    wallet_address = "0xYourWalletAddress"  # Replace with your wallet address
    private_key = "YourPrivateKey"  # Replace with your private key

    vault = MorphoVault(wallet_address, private_key)
    
    # Deposit 0.1 ETH into the vault with a medium risk strategy
    try:
        vault.deposit(amount=0.1, risk_level="medium")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

**Note:** Replace the placeholders (`YOUR_INFURA_PROJECT_ID`, `0xYourMorphoContractAddress`, etc.) with actual values before running the script. The ABI should be filled in with the actual ABI of the Morpho contract. Adjust gas prices and limits as necessary based on network conditions.
