"""
Generated Code Metadata:
========================
Original URL: https://kima-cmn.pages.dev
Prompt: What are the best practices for using Kima's SDK in a gaming application that requires cross-chain asset transfers?
Generated: DETERMINISTIC_96f4ceee04cb5d01
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import kima_sdk  # Import Kima's SDK for blockchain interactions
from kima_sdk.exceptions import KimaError  # Import custom exceptions for error handling

class CrossChainAssetTransfer:
    """
    A class to handle cross-chain asset transfers using Kima's SDK.
    """

    def __init__(self, api_key: str):
        """
        Initializes the CrossChainAssetTransfer with the provided API key.

        :param api_key: The API key for authenticating with Kima's SDK.
        """
        self.api_key = api_key
        self.kima_client = self.initialize_kima_client()

    def initialize_kima_client(self):
        """
        Initializes the Kima client with the provided API key.

        :return: Kima client instance.
        """
        try:
            client = kima_sdk.Client(api_key=self.api_key)
            return client
        except KimaError as e:
            raise RuntimeError(f"Failed to initialize Kima client: {e}")

    def transfer_asset(self, asset_id: str, amount: float, from_chain: str, to_chain: str):
        """
        Transfers an asset from one blockchain to another.

        :param asset_id: The ID of the asset to transfer.
        :param amount: The amount of the asset to transfer.
        :param from_chain: The blockchain to transfer the asset from.
        :param to_chain: The blockchain to transfer the asset to.
        :raises ValueError: If the amount is non-positive.
        :raises RuntimeError: If the transfer fails.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        try:
            # Initiate the asset transfer
            transfer_response = self.kima_client.transfer(
                asset_id=asset_id,
                amount=amount,
                from_chain=from_chain,
                to_chain=to_chain
            )
            return transfer_response
        except KimaError as e:
            raise RuntimeError(f"Asset transfer failed: {e}")

    def check_transfer_status(self, transfer_id: str):
        """
        Checks the status of a transfer.

        :param transfer_id: The ID of the transfer to check.
        :return: The status of the transfer.
        :raises RuntimeError: If the status check fails.
        """
        try:
            status_response = self.kima_client.get_transfer_status(transfer_id)
            return status_response
        except KimaError as e:
            raise RuntimeError(f"Failed to check transfer status: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the cross-chain asset transfer handler
        transfer_handler = CrossChainAssetTransfer(api_key="your_api_key_here")

        # Perform a transfer
        response = transfer_handler.transfer_asset(
            asset_id="asset123",
            amount=10.0,
            from_chain="Ethereum",
            to_chain="BinanceSmartChain"
        )
        print("Transfer initiated:", response)

        # Check the status of the transfer
        transfer_id = response.get("transfer_id")
        status = transfer_handler.check_transfer_status(transfer_id)
        print("Transfer status:", status)

    except Exception as e:
        print(f"An error occurred: {e}")
```
