"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Generate code using a blockchain-based solution to ensure transparency in donation tracking, similar to Dysnix's transparent reporting of funds used for vehicle purchases.
Generated: DETERMINISTIC_fb7288c07226bce6
Batch ID: 20250612_154322
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
import json

# Blockchain configuration
BLOCKCHAIN_PROVIDER = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura project ID
CONTRACT_ABI = '[...]'  # Replace with the ABI of your smart contract
CONTRACT_ADDRESS = '0xYourContractAddressHere'  # Replace with your deployed contract address

# Connect to the blockchain
try:
    web3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_PROVIDER))
    if not web3.isConnected():
        raise ConnectionError("Unable to connect to the blockchain provider.")
except Exception as e:
    print(f"Error connecting to the blockchain: {e}")
    exit()

# Load the contract
try:
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=json.loads(CONTRACT_ABI))
except Exception as e:
    print(f"Error loading the contract: {e}")
    exit()

# Function to log donation details on the blockchain
def log_donation(donor_address, amount, message):
    """
    Logs donation details (donor address, amount, and a message) on the blockchain.

    Args:
        donor_address (str): The Ethereum address of the donor.
        amount (float): The amount donated (in Ether).
        message (str): A message or note associated with the donation.

    Returns:
        str: Transaction hash if successful, or error message otherwise.
    """
    try:
        if not web3.isAddress(donor_address):
            return "Invalid donor address."

        # Convert Ether amount to Wei
        amount_in_wei = web3.toWei(amount, 'ether')

        # Prepare the transaction (assuming a `logDonation` function exists in your smart contract)
        txn = contract.functions.logDonation(
            donor_address,
            amount_in_wei,
            message
        ).buildTransaction({
            'from': donor_address,
            'gas': 2000000,  # Set an appropriate gas limit
            'gasPrice': web3.toWei('20', 'gwei')  # Set an appropriate gas price
        })

        # Sign and send the transaction (requires donor's private key)
        # In production, handle private keys securely (e.g., via a secure wallet system)
        private_key = "YourPrivateKeyHere"  # Replace with the donor's private key
        signed_txn = web3.eth.account.sign_transaction(txn, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return web3.toHex(tx_hash)
    except Exception as e:
        return f"Error logging donation: {e}"

# Function to retrieve donation details
def get_donation_history(donor_address):
    """
    Retrieves donation history for a given donor address.

    Args:
        donor_address (str): The Ethereum address of the donor.

    Returns:
        list: A list of donation records (if any), or an error message otherwise.
    """
    try:
        if not web3.isAddress(donor_address):
            return "Invalid donor address."

        # Assuming `getDonationsByAddress` function exists in your smart contract
        donations = contract.functions.getDonationsByAddress(donor_address).call()
        return donations
    except Exception as e:
        return f"Error retrieving donation history: {e}"

# Example usage of the functions
if __name__ == "__main__":
    donor_address = "0xSampleDonorAddressHere"  # Replace with an actual donor address
    donation_amount = 0.5  # Example donation amount in Ether
    donation_message = "For vehicle purchase transparency"

    # Log a donation
    transaction_result = log_donation(donor_address, donation_amount, donation_message)
    print(f"Transaction Result: {transaction_result}")

    # Retrieve donation history
    donation_history = get_donation_history(donor_address)
    print(f"Donation History: {donation_history}")
```

Note: This is a template code assuming your smart contract contains methods like `logDonation` and `getDonationsByAddress`. Modify the contract interaction as per your specific implementation. Ensure you have deployed the smart contract to the blockchain and have the correct ABI and address. Test thoroughly before deploying in a production environment.
