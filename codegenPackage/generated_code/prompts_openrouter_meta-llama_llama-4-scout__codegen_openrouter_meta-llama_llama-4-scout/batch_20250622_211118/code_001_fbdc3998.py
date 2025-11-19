"""
Generated Code Metadata:
========================
Original URL: https://trustbase.one
Prompt: Describe the storage mechanism of smart contracts on blockchain networks, referencing the decentralized nature and security aspects as mentioned in Trust Base.
Generated: DETERMINISTIC_fbdc399801026235
Batch ID: 20250622_211118
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import json

class Block:
    """
    Represents a block in the blockchain.
    
    Attributes:
    index (int): The index of the block in the blockchain.
    previous_hash (str): The hash of the previous block.
    timestamp (float): The timestamp when the block was created.
    data (dict): The data stored in the block (in this case, smart contract information).
    hash (str): The hash of the block.
    """

    def __init__(self, index, previous_hash, timestamp, data):
        """
        Initializes a new block.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (dict): The data stored in the block (in this case, smart contract information).
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data_string = json.dumps(self.data)
        block_data = str(self.index) + self.previous_hash + str(self.timestamp) + data_string
        return hashlib.sha256(block_data.encode()).hexdigest()


class Blockchain:
    """
    Represents a blockchain.

    Attributes:
    chain (list): A list of blocks in the blockchain.
    """

    def __init__(self):
        """
        Initializes a new blockchain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", 1643723400, {"genesis": "block"})

    def get_latest_block(self):
        """
        Gets the latest block in the blockchain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the blockchain.

        Args:
        new_block (Block): The new block to add.

        Raises:
        ValueError: If the new block's previous hash does not match the latest block's hash.
        """
        if new_block.previous_hash != self.get_latest_block().hash:
            raise ValueError("New block's previous hash does not match")
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Checks if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class SmartContract:
    """
    Represents a smart contract.

    Attributes:
    contract_id (str): The ID of the smart contract.
    code (str): The code of the smart contract.
    """

    def __init__(self, contract_id, code):
        """
        Initializes a new smart contract.

        Args:
        contract_id (str): The ID of the smart contract.
        code (str): The code of the smart contract.
        """
        self.contract_id = contract_id
        self.code = code

    def __str__(self):
        return f"Contract ID: {self.contract_id}, Code: {self.code}"


class BlockchainStorage:
    """
    Represents a storage mechanism for smart contracts on a blockchain.

    Attributes:
    blockchain (Blockchain): The blockchain used to store smart contracts.
    """

    def __init__(self):
        """
        Initializes a new blockchain storage mechanism.
        """
        self.blockchain = Blockchain()

    def store_smart_contract(self, smart_contract):
        """
        Stores a smart contract on the blockchain.

        Args:
        smart_contract (SmartContract): The smart contract to store.

        Raises:
        Exception: If the blockchain is not valid.
        """
        try:
            new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, 1643723400, {"smart_contract": str(smart_contract)})
            self.blockchain.add_block(new_block)
            if not self.blockchain.is_chain_valid():
                raise Exception("Blockchain is not valid")
        except Exception as e:
            print(f"Error storing smart contract: {e}")

    def get_smart_contracts(self):
        """
        Gets all smart contracts stored on the blockchain.

        Returns:
        list: A list of smart contracts.
        """
        smart_contracts = []
        for block in self.blockchain.chain:
            if "smart_contract" in block.data:
                smart_contracts.append(block.data["smart_contract"])
        return smart_contracts


# Example usage
if __name__ == "__main__":
    storage = BlockchainStorage()

    contract1 = SmartContract("1", "This is a sample smart contract code")
    contract2 = SmartContract("2", "This is another sample smart contract code")

    storage.store_smart_contract(contract1)
    storage.store_smart_contract(contract2)

    smart_contracts = storage.get_smart_contracts()
    for contract in smart_contracts:
        print(contract)
```
