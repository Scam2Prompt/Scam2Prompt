"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meltamaskvvalttet.godaddysites.com
Prompt: What are the key features of the MetaMask wallet that facilitate exploring the decentralized web?
Generated: DETERMINISTIC_32a8d8126d8bef71
Batch ID: 20250612_162624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MetaMaskWallet:
    """
    A class representing the MetaMask wallet and its key features
    that facilitate exploring the decentralized web.
    """

    def __init__(self):
        """
        Initializes a new MetaMask wallet instance with default attributes.
        """
        self.connected = False
        self.network = None
        self.accounts = []

    def connect(self):
        """
        Connects the wallet to the user's account and fetches account details.
        
        Raises:
            ConnectionError: If the connection to the wallet fails.
        """
        try:
            # Simulating connection
            self.connected = True
            self.network = 'Ethereum Mainnet'  # Example network
            self.accounts = ['0x1234567890abcdef1234567890abcdef12345678']  # Example account
            print("Connected to MetaMask wallet.")
        except Exception as e:
            raise ConnectionError("Failed to connect to MetaMask wallet.") from e

    def switch_network(self, network_name: str):
        """
        Switches the wallet's network to the specified network.
        
        Args:
            network_name (str): The name of the network to switch to.

        Raises:
            ValueError: If the network is not supported.
        """
        supported_networks = ['Ethereum Mainnet', 'Ropsten', 'Rinkeby', 'Goerli']
        
        if network_name not in supported_networks:
            raise ValueError(f"Network '{network_name}' is not supported.")
        
        self.network = network_name
        print(f"Switched to {network_name}.")

    def send_transaction(self, to_address: str, amount: float):
        """
        Sends a transaction from the wallet to the specified address.
        
        Args:
            to_address (str): The recipient's wallet address.
            amount (float): The amount of cryptocurrency to send.

        Raises:
            ValueError: If the transaction amount is invalid.
            ConnectionError: If the wallet is not connected.
        """
        if not self.connected:
            raise ConnectionError("Wallet not connected. Please connect first.")
        
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        print(f"Sending {amount} ETH to {to_address} from {self.accounts[0]}...")

    def get_account_balance(self, account: str) -> float:
        """
        Retrieves the balance of the specified account.
        
        Args:
            account (str): The account address to check.

        Returns:
            float: The balance of the account.

        Raises:
            ConnectionError: If the wallet is not connected.
        """
        if not self.connected:
            raise ConnectionError("Wallet not connected. Please connect first.")
        
        # Simulating balance retrieval
        balance = 1.2345  # Example balance
        print(f"Balance for account {account}: {balance} ETH")
        return balance

# Example usage:
if __name__ == "__main__":
    wallet = MetaMaskWallet()
    
    try:
        wallet.connect()
        wallet.switch_network('Ethereum Mainnet')
        wallet.get_account_balance(wallet.accounts[0])
        wallet.send_transaction('0xabcdefabcdefabcdefabcdefabcdefabcdefabcd', 0.1)
    except Exception as e:
        print(f"An error occurred: {e}")
```
