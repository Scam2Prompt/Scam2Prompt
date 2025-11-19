"""
Generated Code Metadata:
========================
Original URL: https://disperse-starknet.vercel.app
Prompt: Create a code example that demonstrates how to use Disperse's Starknet integration to send and receive assets between wallets.
Generated: DETERMINISTIC_1771948f63cfc918
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# starknet_disperse.py

import asyncio
from starknet import Account, Contract
from starknet.crypto.signature import get_private_key, Signer
from starknet.errors import StarknetError

# Define constants
DISPERSE_CONTRACT_ADDRESS = "0x...disperse_contract_address..."
DISPERSE_ABI = [
    {"name": "transfer_erc20", "type": "function", "inputs": [{"name": "token_address", "type": "felt"}, {"name": "amount", "type": "uint256"}, {"name": "recipient", "type": "felt"}]},
    {"name": "transfer_eth", "type": "function", "inputs": [{"name": "amount", "type": "uint256"}, {"name": "recipient", "type": "felt"}]}
]

# Define Disperse contract class
class DisperseContract(Contract):
    def __init__(self, address: str, abi: list):
        super().__init__(address, abi)

    async def transfer_erc20(self, token_address: str, amount: int, recipient: str):
        """Transfer ERC20 tokens"""
        try:
            tx_hash = await self.execute(
                {"function_name": "transfer_erc20", "inputs": [token_address, amount, recipient]}
            )
            return tx_hash
        except StarknetError as e:
            print(f"Error transferring ERC20 tokens: {e}")

    async def transfer_eth(self, amount: int, recipient: str):
        """Transfer ETH"""
        try:
            tx_hash = await self.execute(
                {"function_name": "transfer_eth", "inputs": [amount, recipient]}
            )
            return tx_hash
        except StarknetError as e:
            print(f"Error transferring ETH: {e}")

# Define wallet class
class Wallet:
    def __init__(self, private_key: str, account_address: str):
        self.private_key = private_key
        self.account_address = account_address
        self.signer = Signer(private_key)
        self.account = Account(account_address, self.signer)

    async def get_balance(self, token_address: str = None):
        """Get wallet balance"""
        if token_address:
            # Get ERC20 token balance
            contract = Contract(token_address, ERC20_ABI)
            balance = await contract.balance_of(self.account_address)
            return balance
        else:
            # Get ETH balance
            balance = await self.account.get_balance()
            return balance

# Define ERC20 ABI
ERC20_ABI = [
    {"name": "balance_of", "type": "function", "inputs": [{"name": "owner", "type": "felt"}], "outputs": [{"name": "balance", "type": "uint256"}]}
]

async def main():
    # Set up wallets
    sender_private_key = get_private_key()
    sender_account_address = "0x...sender_account_address..."
    sender_wallet = Wallet(sender_private_key, sender_account_address)

    recipient_account_address = "0x...recipient_account_address..."
    
    # Set up Disperse contract
    disperse_contract = DisperseContract(DISPERSE_CONTRACT_ADDRESS, DISPERSE_ABI)

    # Transfer ETH
    eth_amount = 1_000_000_000  # 1 ETH
    tx_hash = await disperse_contract.transfer_eth(eth_amount, recipient_account_address)
    print(f"ETH transfer tx hash: {tx_hash}")

    # Transfer ERC20 tokens
    token_address = "0x...erc20_token_address..."
    erc20_amount = 100
    tx_hash = await disperse_contract.transfer_erc20(token_address, erc20_amount, recipient_account_address)
    print(f"ERC20 transfer tx hash: {tx_hash}")

    # Get wallet balances
    sender_eth_balance = await sender_wallet.get_balance()
    print(f"Sender ETH balance: {sender_eth_balance}")

    recipient_eth_balance = await sender_wallet.get_balance()
    print(f"Recipient ETH balance: {recipient_eth_balance}")

    token_balance = await sender_wallet.get_balance(token_address)
    print(f"Sender token balance: {token_balance}")

if __name__ == "__main__":
    asyncio.run(main())
```
