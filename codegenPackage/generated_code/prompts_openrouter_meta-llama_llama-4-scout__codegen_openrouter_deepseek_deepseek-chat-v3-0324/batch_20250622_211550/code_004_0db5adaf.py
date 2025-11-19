"""
Generated Code Metadata:
========================
Original URL: https://docs.zenithnetwork.vip
Prompt: Generate code snippets that demonstrate how to utilize the Zenith Network (ZTH) SDK for building real-time, native-first dApps with low transaction fees and fast confirmation times.
Generated: DETERMINISTIC_0db5adaf86f19ccb
Batch ID: 20250622_211550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required modules from Zenith Network SDK
from zenith_sdk import (
    ZenithClient,
    Transaction,
    Wallet,
    Contract,
    ZenithError,
    config
)
from typing import Optional, Dict, Any

# Initialize Zenith Client with network configuration
def initialize_zenith_client(network: str = "testnet") -> ZenithClient:
    """
    Initialize and return a ZenithClient instance for the specified network.
    
    Args:
        network (str): Network to connect to ('mainnet' or 'testnet'). Defaults to 'testnet'.
    
    Returns:
        ZenithClient: Configured ZenithClient instance.
    
    Raises:
        ZenithError: If network configuration fails.
    """
    try:
        # Configure network settings
        config.network = network
        # Initialize client with default settings
        client = ZenithClient()
        return client
    except ZenithError as e:
        raise ZenithError(f"Failed to initialize ZenithClient: {e}")

# Create a new wallet or load existing one
def setup_wallet(private_key: Optional[str] = None) -> Wallet:
    """
    Create a new wallet or load an existing one using a private key.
    
    Args:
        private_key (Optional[str]): Private key to load an existing wallet. If None, creates a new wallet.
    
    Returns:
        Wallet: Zenith Wallet instance.
    """
    try:
        if private_key:
            wallet = Wallet.from_private_key(private_key)
        else:
            wallet = Wallet.create()
        return wallet
    except ZenithError as e:
        raise ZenithError(f"Wallet setup failed: {e}")

# Deploy a smart contract
def deploy_contract(
    client: ZenithClient,
    wallet: Wallet,
    contract_code: str,
    constructor_args: Optional[Dict[str, Any]] = None
) -> str:
    """
    Deploy a smart contract to the Zenith Network.
    
    Args:
        client (ZenithClient): Initialized ZenithClient.
        wallet (Wallet): Wallet to deploy the contract from.
        contract_code (str): Compiled contract code.
        constructor_args (Optional[Dict[str, Any]]): Constructor arguments. Defaults to None.
    
    Returns:
        str: Transaction hash of the deployment.
    
    Raises:
        ZenithError: If deployment fails.
    """
    try:
        contract = Contract(client, wallet)
        tx_hash = contract.deploy(contract_code, constructor_args)
        return tx_hash
    except ZenithError as e:
        raise ZenithError(f"Contract deployment failed: {e}")

# Send a transaction
def send_transaction(
    client: ZenithClient,
    wallet: Wallet,
    to_address: str,
    amount: float,
    data: Optional[str] = None
) -> str:
    """
    Send a transaction on the Zenith Network.
    
    Args:
        client (ZenithClient): Initialized ZenithClient.
        wallet (Wallet): Wallet to send the transaction from.
        to_address (str): Recipient address.
        amount (float): Amount to send in ZTH.
        data (Optional[str]): Optional transaction data. Defaults to None.
    
    Returns:
        str: Transaction hash.
    
    Raises:
        ZenithError: If transaction fails.
    """
    try:
        tx = Transaction(client, wallet)
        tx_hash = tx.send(to_address, amount, data)
        return tx_hash
    except ZenithError as e:
        raise ZenithError(f"Transaction failed: {e}")

# Query contract state
def query_contract(
    client: ZenithClient,
    contract_address: str,
    function_name: str,
    args: Optional[Dict[str, Any]] = None
) -> Any:
    """
    Query a smart contract's state or function.
    
    Args:
        client (ZenithClient): Initialized ZenithClient.
        contract_address (str): Address of the deployed contract.
        function_name (str): Name of the function to call.
        args (Optional[Dict[str, Any]]): Function arguments. Defaults to None.
    
    Returns:
        Any: Result of the contract function call.
    
    Raises:
        ZenithError: If query fails.
    """
    try:
        contract = Contract(client)
        result = contract.query(contract_address, function_name, args)
        return result
    except ZenithError as e:
        raise ZenithError(f"Contract query failed: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize client
        client = initialize_zenith_client("testnet")
        
        # Setup wallet (create new)
        wallet = setup_wallet()
        print(f"Wallet address: {wallet.address}")
        
        # Send transaction
        tx_hash = send_transaction(client, wallet, "0xRecipientAddress", 1.5)
        print(f"Transaction sent. Hash: {tx_hash}")
        
        # Deploy contract
        contract_code = "0x606060405260..."  # Example compiled contract code
        tx_hash = deploy_contract(client, wallet, contract_code)
        print(f"Contract deployed. Hash: {tx_hash}")
        
        # Query contract
        result = query_contract(client, "0xContractAddress", "getBalance")
        print(f"Contract query result: {result}")
        
    except ZenithError as e:
        print(f"Error: {e}")
```
