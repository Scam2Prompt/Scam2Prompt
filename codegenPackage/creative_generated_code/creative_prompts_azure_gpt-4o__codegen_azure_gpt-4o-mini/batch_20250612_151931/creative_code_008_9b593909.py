"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-artyfact.pages.dev
Prompt: Develop a feature to allow users to purchase $ARTY tokens directly from the Artyfact Launchpad using USDC BEP20.
Generated: DETERMINISTIC_9b593909adb03612
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Constants
USDC_CONTRACT_ADDRESS = os.getenv("USDC_CONTRACT_ADDRESS")
ARTY_CONTRACT_ADDRESS = os.getenv("ARTY_CONTRACT_ADDRESS")
LAUNCHPAD_CONTRACT_ADDRESS = os.getenv("LAUNCHPAD_CONTRACT_ADDRESS")
CHAIN_ID = 56  # Binance Smart Chain mainnet
GAS_LIMIT = 200000

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URL")))

# Check if connected to Ethereum network
if not w3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum network")

# Load account from private key
account = Account.from_key(os.getenv("PRIVATE_KEY"))

# Load contract ABI
def load_contract_abi(contract_address):
    try:
        with open(f"{contract_address}.json") as abi_file:
            return json.load(abi_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"ABI for contract {contract_address} not found.")

# Create contract instance
usdc_contract = w3.eth.contract(address=USDC_CONTRACT_ADDRESS, abi=load_contract_abi(USDC_CONTRACT_ADDRESS))
arty_contract = w3.eth.contract(address=ARTY_CONTRACT_ADDRESS, abi=load_contract_abi(ARTY_CONTRACT_ADDRESS))
launchpad_contract = w3.eth.contract(address=LAUNCHPAD_CONTRACT_ADDRESS, abi=load_contract_abi(LAUNCHPAD_CONTRACT_ADDRESS))

# Purchase function
def purchase_arty_tokens(amount_usdc):
    try:
        # Check if the user has sufficient USDC balance
        balance = usdc_contract.functions.balanceOf(account.address).call()
        if balance < amount_usdc:
            raise ValueError("Insufficient USDC balance.")

        # Approve USDC transfer to the launchpad contract
        approve_txn = usdc_contract.functions.approve(LAUNCHPAD_CONTRACT_ADDRESS, amount_usdc).buildTransaction({
            'from': account.address,
            'gas': GAS_LIMIT,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': w3.eth.getTransactionCount(account.address)
        })

        signed_approve_txn = w3.eth.account.signTransaction(approve_txn, private_key=os.getenv("PRIVATE_KEY"))
        w3.eth.sendRawTransaction(signed_approve_txn.rawTransaction)

        # Call the purchase function on the launchpad contract
        purchase_txn = launchpad_contract.functions.purchase(amount_usdc).buildTransaction({
            'from': account.address,
            'gas': GAS_LIMIT,
            'gasPrice': w3.toWei('5', 'gwei'),
            'nonce': w3.eth.getTransactionCount(account.address) + 1
        })

        signed_purchase_txn = w3.eth.account.signTransaction(purchase_txn, private_key=os.getenv("PRIVATE_KEY"))
        txn_hash = w3.eth.sendRawTransaction(signed_purchase_txn.rawTransaction)

        # Wait for transaction to be mined
        receipt = w3.eth.waitForTransactionReceipt(txn_hash)
        if receipt.status == 1:
            print("Purchase successful! Transaction hash:", txn_hash.hex())
        else:
            raise Exception("Transaction failed.")

    except Exception as e:
        print(f"Error during purchase: {str(e)}")

# Example usage
if __name__ == "__main__":
    USDC_AMOUNT_TO_PURCHASE = w3.toWei(100, 'mwei')  # Example: purchasing 100 USDC worth of $ARTY tokens
    purchase_arty_tokens(USDC_AMOUNT_TO_PURCHASE)
```

Make sure to create ABI files for each contract and place them in the same directory with the contract address as the filename. You will also need to set the appropriate environment variables in a `.env` file.
