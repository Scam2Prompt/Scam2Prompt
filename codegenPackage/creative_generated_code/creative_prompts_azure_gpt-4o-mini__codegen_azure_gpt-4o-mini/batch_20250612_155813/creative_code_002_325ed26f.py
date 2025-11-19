"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://keplr-extension.com
Prompt: Explain the features of the Keplr Wallet as an interchain gateway.
Generated: DETERMINISTIC_325ed26f8976bac2
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class KeplrWallet:
    """
    A class to represent the Keplr Wallet as an interchain gateway.

    Attributes:
        networks (list): A list of supported blockchain networks.
        current_network (str): The currently active network.
    """

    def __init__(self):
        """
        Initializes the KeplrWallet with default settings.
        """
        self.networks = []
        self.current_network = None

    def add_network(self, network_name):
        """
        Adds a new blockchain network to the wallet.

        Args:
            network_name (str): The name of the blockchain network to add.
        
        Raises:
            ValueError: If the network already exists in the wallet.
        """
        if network_name in self.networks:
            raise ValueError(f"Network '{network_name}' already exists.")
        
        self.networks.append(network_name)

    def switch_network(self, network_name):
        """
        Switches the currently active blockchain network.

        Args:
            network_name (str): The name of the blockchain network to switch to.
        
        Raises:
            ValueError: If the network is not supported or does not exist.
        """
        if network_name not in self.networks:
            raise ValueError(f"Network '{network_name}' is not supported.")
        
        self.current_network = network_name

    def get_supported_networks(self):
        """
        Returns a list of supported blockchain networks.

        Returns:
            list: A list of network names supported by the wallet.
        """
        return self.networks

    def is_connected(self):
        """
        Checks if the wallet is connected to a network.

        Returns:
            bool: True if connected to a network, False otherwise.
        """
        return self.current_network is not None

    def send_transaction(self, to_address, amount):
        """
        Sends a transaction from the wallet to a specified address.

        Args:
            to_address (str): The address to send the transaction to.
            amount (float): The amount of currency to send.

        Raises:
            ValueError: If not connected to a network or if the amount is invalid.
            Exception: For any other errors during transaction processing.

        Returns:
            str: A success message indicating the transaction was sent.
        """
        if not self.is_connected():
            raise ValueError("Cannot send transaction: wallet is not connected to any network.")
        
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        # Simulate sending a transaction (this would be replaced with actual logic)
        try:
            # Transaction logic would go here
            return f"Transaction of {amount} sent to {to_address} on {self.current_network}."
        except Exception as e:
            raise Exception("An error occurred while sending the transaction: " + str(e))

# Example usage
if __name__ == "__main__":
    wallet = KeplrWallet()

    # Adding supported networks
    wallet.add_network("Cosmos")
    wallet.add_network("Osmosis")

    # Switching to a network
    wallet.switch_network("Cosmos")

    # Sending a transaction
    try:
        response = wallet.send_transaction("cosmos1xyz...", 10.5)
        print(response)
    except Exception as e:
        print("Error:", e)
```
