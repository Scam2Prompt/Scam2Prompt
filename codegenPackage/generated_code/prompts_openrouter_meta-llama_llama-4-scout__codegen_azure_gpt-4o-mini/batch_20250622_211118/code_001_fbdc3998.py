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
class SmartContractStorage:
    """
    A class to represent the storage mechanism of smart contracts on blockchain networks.
    
    Attributes:
        contract_address (str): The unique address of the smart contract on the blockchain.
        storage (dict): A dictionary to simulate the storage of contract data.
    """

    def __init__(self, contract_address):
        """
        Initializes the SmartContractStorage with a contract address.
        
        Args:
            contract_address (str): The unique address of the smart contract.
        
        Raises:
            ValueError: If the contract address is not a valid string.
        """
        if not isinstance(contract_address, str) or not contract_address:
            raise ValueError("Contract address must be a non-empty string.")
        
        self.contract_address = contract_address
        self.storage = {}

    def set_value(self, key, value):
        """
        Stores a value in the smart contract's storage.
        
        Args:
            key (str): The key under which the value is stored.
            value (any): The value to be stored.
        
        Raises:
            ValueError: If the key is not a valid string.
        """
        if not isinstance(key, str) or not key:
            raise ValueError("Key must be a non-empty string.")
        
        self.storage[key] = value

    def get_value(self, key):
        """
        Retrieves a value from the smart contract's storage.
        
        Args:
            key (str): The key for which the value is to be retrieved.
        
        Returns:
            any: The value associated with the key, or None if the key does not exist.
        
        Raises:
            ValueError: If the key is not a valid string.
        """
        if not isinstance(key, str) or not key:
            raise ValueError("Key must be a non-empty string.")
        
        return self.storage.get(key)

    def delete_value(self, key):
        """
        Deletes a value from the smart contract's storage.
        
        Args:
            key (str): The key of the value to be deleted.
        
        Raises:
            ValueError: If the key is not a valid string.
        """
        if not isinstance(key, str) or not key:
            raise ValueError("Key must be a non-empty string.")
        
        if key in self.storage:
            del self.storage[key]

    def get_all_storage(self):
        """
        Returns all key-value pairs stored in the smart contract's storage.
        
        Returns:
            dict: A dictionary containing all stored key-value pairs.
        """
        return self.storage.copy()

# Example usage
if __name__ == "__main__":
    try:
        # Create a new smart contract storage instance
        contract_storage = SmartContractStorage("0x1234567890abcdef")

        # Set values in the storage
        contract_storage.set_value("owner", "Alice")
        contract_storage.set_value("balance", 100)

        # Retrieve a value
        print("Owner:", contract_storage.get_value("owner"))  # Output: Owner: Alice

        # Delete a value
        contract_storage.delete_value("balance")

        # Get all storage
        print("Current Storage:", contract_storage.get_all_storage())  # Output: Current Storage: {'owner': 'Alice'}

    except ValueError as e:
        print(f"Error: {e}")
```
