"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-website.pages.dev
Prompt: Explain the process of depositing and withdrawing funds on Starknet for dapp development.
Generated: DETERMINISTIC_a12a14e846b0146e
Batch ID: 20250612_135528
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://alpha-mainnet.starknet.io": {
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
# Import necessary modules for interacting with Starknet
from starkware.starknet.wallets.wallet import Wallet
from starkware.starknet.services.api.gateway.gateway_client import GatewayClient
from starkware.starknet.definitions.transaction_type import TransactionType
from starkware.starknet.public.abi import get_selector_from_name
from starkware.crypto.signature.signature import sign
from starkware.starknet.compiler.compile import compile_starknet_contract
from starkware.starknet.services.api.gateway.feeder_gateway_client import FeederGatewayClient

# Constants
STARKNET_GATEWAY_URL = "https://alpha-mainnet.starknet.io"
PRIVATE_KEY = 0x1234567890ABCDEF  # Replace with your private key
PUBLIC_KEY = 0xFEDCBA0987654321  # Replace with your public key
ACCOUNT_ADDRESS = "0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"  # Replace with your account address

# Initialize Starknet Gateway Client
gateway_client = GatewayClient(url=STARKNET_GATEWAY_URL)

# Wallet initialization
wallet = Wallet(private_key=PRIVATE_KEY, public_key=PUBLIC_KEY, account_address=ACCOUNT_ADDRESS)

def deposit_funds(amount: int, token_contract_address: str):
    """
    Deposits funds into Starknet from a specific token contract.

    Args:
        amount (int): Amount of tokens to deposit (in smallest denomination).
        token_contract_address (str): Starknet address of the token contract.
    """
    try:
        # Prepare calldata for deposit transaction
        deposit_selector = get_selector_from_name("deposit")  # The selector for the 'deposit' function
        calldata = [wallet.address, amount]  # calldata: [recipient address, amount]

        # Build transaction
        deposit_tx = {
            "contract_address": token_contract_address,
            "entry_point_selector": deposit_selector,
            "calldata": calldata,
        }

        # Sign transaction
        signature = sign(PRIVATE_KEY, deposit_tx)

        # Send transaction
        tx_response = gateway_client.add_transaction(deposit_tx, signature=signature)

        print(f"Deposit transaction submitted successfully: {tx_response}")
    except Exception as e:
        print(f"Error occurred during deposit: {e}")

def withdraw_funds(amount: int, token_contract_address: str):
    """
    Withdraws funds from Starknet to an external address.

    Args:
        amount (int): Amount of tokens to withdraw (in smallest denomination).
        token_contract_address (str): Starknet address of the token contract.
    """
    try:
        # Prepare calldata for withdraw transaction
        withdraw_selector = get_selector_from_name("withdraw")  # The selector for the 'withdraw' function
        calldata = [wallet.address, amount]  # calldata: [recipient address, amount]

        # Build transaction
        withdraw_tx = {
            "contract_address": token_contract_address,
            "entry_point_selector": withdraw_selector,
            "calldata": calldata,
        }

        # Sign transaction
        signature = sign(PRIVATE_KEY, withdraw_tx)

        # Send transaction
        tx_response = gateway_client.add_transaction(withdraw_tx, signature=signature)

        print(f"Withdraw transaction submitted successfully: {tx_response}")
    except Exception as e:
        print(f"Error occurred during withdrawal: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with real token contract address
    TOKEN_CONTRACT_ADDRESS = "0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"

    # Deposit 100 tokens
    deposit_funds(amount=100, token_contract_address=TOKEN_CONTRACT_ADDRESS)

    # Withdraw 50 tokens
    withdraw_funds(amount=50, token_contract_address=TOKEN_CONTRACT_ADDRESS)
```
