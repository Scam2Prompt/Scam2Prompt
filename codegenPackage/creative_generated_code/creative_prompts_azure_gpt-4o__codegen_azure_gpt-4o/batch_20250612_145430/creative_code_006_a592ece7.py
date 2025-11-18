"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-update-doc-419labs.vercel.app
Prompt: Write code to bridge assets between StarkNet Layer 2 and another blockchain, using a bridge tool mentioned in the StarkNet ecosystem.
Generated: DETERMINISTIC_a592ece787b8399d
Batch ID: 20250612_145430
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://alpha4.starknet.io": {
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
import asyncio
from starkware.starknet.public.abi import get_selector_from_name
from starkware.starknet.services.api.gateway.gateway_client import GatewayClient
from web3 import Web3

# Constants
STARKNET_TESTNET_URL = "https://alpha4.starknet.io"
ETHEREUM_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"

# Configuration
BRIDGE_CONTRACT_ADDRESS = "0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"  # StarkNet bridge contract
ETHEREUM_TOKEN_CONTRACT = "0xYourEthereumTokenContractAddressHere"  # Replace with your token contract
STARKNET_RECEIVER_ADDRESS = "0xYourStarkNetReceiverAddressHere"  # StarkNet L2 address

class AssetBridge:
    def __init__(self, starknet_url, ethereum_rpc_url):
        # Initialize StarkNet and Ethereum clients
        self.starknet_client = GatewayClient(starknet_url)
        self.web3 = Web3(Web3.HTTPProvider(ethereum_rpc_url))

    async def deposit_to_starknet(self, amount, sender_private_key):
        """
        Deposit assets from Ethereum L1 to StarkNet L2 using the bridge contract.
        """
        try:
            # Create Ethereum contract instance
            eth_bridge_contract = self.web3.eth.contract(
                address=Web3.to_checksum_address(BRIDGE_CONTRACT_ADDRESS),
                abi=[
                    # Add the ABI of the bridge contract here
                    # Example only: Replace with the actual ABI
                    {
                        "constant": False,
                        "inputs": [
                            {"name": "starknetAddress", "type": "bytes32"},
                            {"name": "amount", "type": "uint256"}
                        ],
                        "name": "deposit",
                        "outputs": [],
                        "type": "function"
                    }
                ],
            )

            # Prepare transaction data
            starknet_receiver_bytes = Web3.to_bytes(hexstr=STARKNET_RECEIVER_ADDRESS)
            transaction = eth_bridge_contract.functions.deposit(
                starknet_receiver_bytes, amount
            ).build_transaction({
                'from': self.web3.eth.account.from_key(sender_private_key).address,
                'nonce': self.web3.eth.get_transaction_count(self.web3.eth.account.from_key(sender_private_key).address),
                'gas': 300000,  # Adjust as needed
                'gasPrice': self.web3.eth.gas_price,
            })

            # Sign transaction
            signed_tx = self.web3.eth.account.sign_transaction(transaction, sender_private_key)

            # Send transaction
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(f"Transaction sent! Hash: {tx_hash.hex()}")

            # Wait for the transaction receipt
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status == 1:
                print("Deposit successful!")
            else:
                print("Deposit failed!")
        except Exception as e:
            print(f"An error occurred during deposit: {e}")

    async def withdraw_to_ethereum(self, amount, starknet_sender_address):
        """
        Withdraw assets from StarkNet L2 back to Ethereum L1.
        """
        try:
            # Call the StarkNet bridge contract to initiate a withdrawal
            selector = get_selector_from_name("withdraw")
            calldata = [starknet_sender_address, amount]

            # Build and send the StarkNet transaction
            withdrawal_tx = await self.starknet_client.add_transaction(
                {
                    "type": "INVOKE_FUNCTION",
                    "contract_address": BRIDGE_CONTRACT_ADDRESS,
                    "entry_point_selector": selector,
                    "calldata": calldata,
                }
            )
            print(f"Withdrawal transaction sent! Transaction hash: {withdrawal_tx['transaction_hash']}")
        except Exception as e:
            print(f"An error occurred during withdrawal: {e}")


async def main():
    # Create the AssetBridge instance
    bridge = AssetBridge(STARKNET_TESTNET_URL, ETHEREUM_RPC_URL)

    # Example usage
    sender_private_key = "0xYourEthereumPrivateKeyHere"  # Replace with your Ethereum private key
    amount = 1000  # Replace with the amount to transfer

    # Deposit assets from Ethereum to StarkNet
    await bridge.deposit_to_starknet(amount, sender_private_key)

    # Withdraw assets from StarkNet to Ethereum
    await bridge.withdraw_to_ethereum(amount, STARKNET_RECEIVER_ADDRESS)


# Entry point
if __name__ == "__main__":
    asyncio.run(main())
```
