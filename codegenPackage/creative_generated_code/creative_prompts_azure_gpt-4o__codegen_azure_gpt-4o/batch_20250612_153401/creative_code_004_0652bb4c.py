"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mileimoneda.pages.dev
Prompt: Write a Python script using web3.py to interact with a smart contract for purchasing tokens and updating balances, referencing the transaction completion process described for $MEDA tokens.
Generated: DETERMINISTIC_0652bb4cf47a297d
Batch ID: 20250612_153401
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
from web3 import Web3
from web3.exceptions import ContractLogicError

# Configuration
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your private key
WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"  # Replace with your wallet address
CONTRACT_ADDRESS = "SMART_CONTRACT_ADDRESS"  # Replace with the token's smart contract address
ABI_FILE_PATH = "path/to/contract_abi.json"  # Replace with the file path to the contract ABI
TOKEN_PURCHASE_AMOUNT = 100  # Number of tokens to purchase
GAS_LIMIT = 200000  # Adjust based on the contract requirements
GAS_PRICE_GWEI = 50  # Gas price in Gwei

def main():
    try:
        # Connect to Ethereum network
        web3 = Web3(Web3.HTTPProvider(INFURA_URL))
        
        if not web3.isConnected():
            raise ConnectionError("Unable to connect to Ethereum network")

        # Load the contract ABI
        with open(ABI_FILE_PATH, 'r') as abi_file:
            contract_abi = json.load(abi_file)

        # Load the contract
        contract = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=contract_abi)

        # Calculate gas price in Wei
        gas_price = web3.toWei(GAS_PRICE_GWEI, 'gwei')

        # Prepare transaction for purchasing tokens
        nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)
        transaction = contract.functions.purchaseTokens(TOKEN_PURCHASE_AMOUNT).buildTransaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': GAS_LIMIT,
            'gasPrice': gas_price,
            'nonce': nonce
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Transaction sent successfully. TX Hash: {web3.toHex(tx_hash)}")

        # Wait for the transaction receipt
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        if receipt.status == 1:
            print("Transaction completed successfully!")
        else:
            print("Transaction failed!")
    
        # Fetch updated balance
        balance = contract.functions.balanceOf(WALLET_ADDRESS).call()
        print(f"Updated balance: {balance} tokens")
    
    except FileNotFoundError:
        print("ABI file not found. Please check the ABI file path.")
    except ConnectionError as ce:
        print(f"Connection error: {ce}")
    except ContractLogicError as cle:
        print(f"Contract logic error: {cle}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
