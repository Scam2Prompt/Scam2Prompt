"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Write a Python script using web3.py to interact with Tenderize-like staking smart contracts, including depositing tokens and redeeming accrued rewards.
Generated: DETERMINISTIC_d489f2ba5a7e02c5
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from typing import Dict, Any, Optional
from eth_typing import ChecksumAddress
from web3.contract import Contract
from web3.types import TxReceipt, Wei

# Constants
CONFIG_FILE = "config.json"
ERC20_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "_spender", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

class TenderizeStaking:
    def __init__(self, config_path: str = CONFIG_FILE):
        """Initialize the Tenderize staking interaction class."""
        with open(config_path) as f:
            config = json.load(f)
        
        self.w3 = Web3(Web3.HTTPProvider(config["rpc_url"]))
        if config.get("is_poa", False):
            self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        self.private_key = config["private_key"]
        self.account = self.w3.eth.account.from_key(self.private_key)
        self.chain_id = config.get("chain_id", self.w3.eth.chain_id)
        
        # Load contracts
        self.staking_contract = self._load_contract(
            config["staking_contract_address"],
            config["staking_contract_abi"]
        )
        self.token_contract = self._load_contract(
            config["token_contract_address"],
            ERC20_ABI
        )
        self.reward_token_contract = self._load_contract(
            config["reward_token_contract_address"],
            ERC20_ABI
        ) if config.get("reward_token_contract_address") else None

    def _load_contract(self, address: str, abi) -> Contract:
        """Load a contract from its ABI and address."""
        return self.w3.eth.contract(
            address=self.w3.to_checksum_address(address),
            abi=abi
        )

    def _get_nonce(self) -> int:
        """Get the current nonce for the account."""
        return self.w3.eth.get_transaction_count(self.account.address)

    def _send_transaction(self, tx: Dict[str, Any]) -> TxReceipt:
        """Sign and send a transaction."""
        tx.update({
            "chainId": self.chain_id,
            "nonce": self._get_nonce(),
            "from": self.account.address
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def get_token_balance(self, address: Optional[ChecksumAddress] = None) -> int:
        """Get the token balance of an address (defaults to own address)."""
        if address is None:
            address = self.account.address
        return self.token_contract.functions.balanceOf(address).call()

    def get_staked_balance(self, address: Optional[ChecksumAddress] = None) -> int:
        """Get the staked balance of an address (defaults to own address)."""
        if address is None:
            address = self.account.address
        return self.staking_contract.functions.balanceOf(address).call()

    def get_rewards_balance(self, address: Optional[ChecksumAddress] = None) -> int:
        """Get the rewards balance of an address (defaults to own address)."""
        if address is None:
            address = self.account.address
        if not self.reward_token_contract:
            raise ValueError("Reward token contract not configured")
        return self.reward_token_contract.functions.balanceOf(address).call()

    def approve_token_spending(self, amount: int) -> TxReceipt:
        """Approve the staking contract to spend tokens."""
        tx = self.token_contract.functions.approve(
            self.staking_contract.address,
            amount
        ).build_transaction({
            "gasPrice": self.w3.eth.gas_price
        })
        return self._send_transaction(tx)

    def stake_tokens(self, amount: int) -> TxReceipt:
        """Stake tokens into the staking contract."""
        tx = self.staking_contract.functions.deposit(amount).build_transaction({
            "gasPrice": self.w3.eth.gas_price
        })
        return self._send_transaction(tx)

    def unstake_tokens(self, amount: int) -> TxReceipt:
        """Unstake tokens from the staking contract."""
        tx = self.staking_contract.functions.withdraw(amount).build_transaction({
            "gasPrice": self.w3.eth.gas_price
        })
        return self._send_transaction(tx)

    def claim_rewards(self) -> TxReceipt:
        """Claim accrued rewards from the staking contract."""
        if not hasattr(self.staking_contract.functions, "claim"):
            raise ValueError("Claim function not found in staking contract")
        
        tx = self.staking_contract.functions.claim().build_transaction({
            "gasPrice": self.w3.eth.gas_price
        })
        return self._send_transaction(tx)

    def compound_rewards(self) -> TxReceipt:
        """Compound rewards by staking them back into the contract."""
        if not hasattr(self.staking_contract.functions, "compound"):
            raise ValueError("Compound function not found in staking contract")
        
        tx = self.staking_contract.functions.compound().build_transaction({
            "gasPrice": self.w3.eth.gas_price
        })
        return self._send_transaction(tx)

# Example usage
if __name__ == "__main__":
    try:
        tenderize = TenderizeStaking()
        
        # Check balances
        token_balance = tenderize.get_token_balance()
        staked_balance = tenderize.get_staked_balance()
        rewards_balance = tenderize.get_rewards_balance() if tenderize.reward_token_contract else 0
        
        print(f"Token Balance: {token_balance}")
        print(f"Staked Balance: {staked_balance}")
        print(f"Rewards Balance: {rewards_balance}")
        
        # Example stake operation
        if token_balance > 0:
            # Approve first
            approve_receipt = tenderize.approve_token_spending(token_balance)
            print(f"Approval Tx Hash: {approve_receipt.transactionHash.hex()}")
            
            # Then stake
            stake_receipt = tenderize.stake_tokens(token_balance)
            print(f"Stake Tx Hash: {stake_receipt.transactionHash.hex()}")
        
        # Example claim rewards
        if rewards_balance > 0:
            claim_receipt = tenderize.claim_rewards()
            print(f"Claim Rewards Tx Hash: {claim_receipt.transactionHash.hex()}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
