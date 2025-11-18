"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Create a script to interact with the DOGE20 token presale contract, allowing users to claim their tokens and check their balances.
Generated: DETERMINISTIC_db3445c6dbe55e3f
Batch ID: 20250612_152620
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
from web3 import Web3
import sys

# Constants
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
CONTRACT_ADDRESS = "0xYourContractAddress"  # Replace with DOGE20 token presale contract address
ABI = """[Contract_ABI_JSON]"""  # Replace with the actual ABI of the contract
PRIVATE_KEY = "0xYourPrivateKey"  # Replace with your private key
WALLET_ADDRESS = "0xYourWalletAddress"  # Replace with your wallet address

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    print("Error: Unable to connect to Ethereum network.")
    sys.exit(1)

# Load contract
contract = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=ABI)

def get_balance(address):
    """
    Fetches the token balance of a given wallet address.
    
    :param address: Wallet address to query
    :return: Token balance (int)
    """
    try:
        balance = contract.functions.balanceOf(Web3.toChecksumAddress(address)).call()
        return balance
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

def claim_tokens():
    """
    Sends a transaction to claim tokens from the presale contract.
    
    :return: Transaction hash
    """
    try:
        # Prepare transaction
        nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
        tx = contract.functions.claimTokens().buildTransaction({
            'nonce': nonce,
            'gas': 200000,  # Adjust gas limit as needed
            'gasPrice': web3.toWei('20', 'gwei'),  # Adjust gas price as needed
            'from': WALLET_ADDRESS
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        print(f"Transaction sent! Hash: {web3.toHex(tx_hash)}")
        return web3.toHex(tx_hash)
    except Exception as e:
        print(f"Error claiming tokens: {e}")
        return None

def main():
    print("DOGE20 Token Presale Script")
    print("===========================")
    print("1. Check Balance")
    print("2. Claim Tokens")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            address = input("Enter wallet address to check balance: ")
            balance = get_balance(address)
            if balance is not None:
                print(f"Balance: {balance} DOGE20")
        elif choice == 2:
            tx_hash = claim_tokens()
            if tx_hash:
                print(f"Tokens claimed successfully! Transaction Hash: {tx_hash}")
        elif choice == 3:
            print("Exiting script.")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace placeholders like `YOUR_INFURA_PROJECT_ID`, `0xYourContractAddress`, `Contract_ABI_JSON`, `0xYourPrivateKey`, and `0xYourWalletAddress` with actual values.
2. Ensure you have installed `web3.py` (`pip install web3`) and have the contract ABI readily available.
3. This script assumes the contract has `balanceOf` and `claimTokens` functions as specified. Adjust as needed for your specific contract implementation.
