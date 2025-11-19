"""
Generated Code Metadata:
========================
Original URL: https://hemi.host
Prompt: Can you provide code examples for creating decentralized applications that utilize the Hemi Virtual Machine (hVM)?
Generated: DETERMINISTIC_f6e060f73efb4440
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Example 1: Basic hVM Smart Contract
from hemi import hVM, Contract

class SimpleStorage(Contract):
    def __init__(self):
        super().__init__()
        self.storage = {}

    @hVM.payable
    def set(self, key: str, value: str):
        """
        Stores a key-value pair in the contract storage
        """
        self.storage[key] = value
        self.emit("ValueSet", {"key": key, "value": value})

    def get(self, key: str) -> str:
        """
        Retrieves a value from the contract storage
        """
        return self.storage.get(key, "")

# Example 2: Token Contract
class HemiToken(Contract):
    def __init__(self):
        super().__init__()
        self.balances = {}
        self.total_supply = 0

    @hVM.payable
    def mint(self, amount: int):
        """
        Mints new tokens to the sender's address
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        sender = self.msg.sender
        self.balances[sender] = self.balances.get(sender, 0) + amount
        self.total_supply += amount
        self.emit("Minted", {"to": sender, "amount": amount})

    def transfer(self, to: str, amount: int) -> bool:
        """
        Transfers tokens to another address
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        sender = self.msg.sender
        if self.balances.get(sender, 0) < amount:
            raise ValueError("Insufficient balance")
        
        self.balances[sender] -= amount
        self.balances[to] = self.balances.get(to, 0) + amount
        self.emit("Transfer", {"from": sender, "to": to, "amount": amount})
        return True

    def balance_of(self, address: str) -> int:
        """
        Returns the token balance of an address
        """
        return self.balances.get(address, 0)

# Example 3: Interacting with hVM from a DApp
from hemi import Web3Provider, Account

class DAppClient:
    def __init__(self, provider_url: str, private_key: str):
        self.web3 = Web3Provider(provider_url)
        self.account = Account.from_key(private_key)
        self.web3.set_default_account(self.account)

    def deploy_contract(self, contract_class, *args):
        """
        Deploys a contract to the hVM network
        """
        contract = contract_class(*args)
        tx_hash = self.web3.deploy(contract)
        receipt = self.web3.wait_for_transaction(tx_hash)
        return receipt.contract_address

    def call_contract(self, address: str, abi: dict, function_name: str, *args):
        """
        Calls a contract function
        """
        contract = self.web3.get_contract(address, abi)
        return contract.functions[function_name](*args).call()

    def send_transaction(self, address: str, abi: dict, function_name: str, *args, value=0):
        """
        Sends a transaction to a contract function
        """
        contract = self.web3.get_contract(address, abi)
        tx = contract.functions[function_name](*args).build_transaction({
            'value': value,
            'gas': 1000000
        })
        signed_tx = self.account.sign_transaction(tx)
        tx_hash = self.web3.send_raw_transaction(signed_tx.raw_transaction)
        return self.web3.wait_for_transaction(tx_hash)

# Example 4: Event Listener
from hemi import EventListener

class StorageEventListener(EventListener):
    def on_ValueSet(self, event):
        print(f"New value set: {event.args['key']} = {event.args['value']}")

    def start_listening(self, contract_address: str, abi: dict):
        contract = self.web3.get_contract(contract_address, abi)
        contract.events.ValueSet.create_listener(self.on_ValueSet)
```
