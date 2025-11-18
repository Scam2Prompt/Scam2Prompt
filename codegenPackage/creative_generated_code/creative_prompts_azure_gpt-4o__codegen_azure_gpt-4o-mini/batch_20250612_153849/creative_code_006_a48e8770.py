"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-disperse.vercel.app
Prompt: Suggest methods for optimizing token dispersal on Starknet, inspired by the Starknet Disperse application.
Generated: DETERMINISTIC_a48e87702091349a
Batch ID: 20250612_153849
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your_starknet_network_url": {
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
# Import necessary libraries
from starknet_py.net import AccountClient
from starknet_py.net.models import InvokeFunction
from starknet_py.contract import Contract
from typing import List, Dict

class TokenDisperser:
    def __init__(self, account_private_key: str, network_url: str):
        """
        Initializes the TokenDisperser with given account private key and network URL.

        Args:
            account_private_key (str): The private key of the Starknet account.
            network_url (str): The URL of the Starknet network.
        """
        self.client = AccountClient(account_private_key, network_url)

    async def disperse_tokens(self, token_contract_address: str, recipients: List[str], amounts: List[int]) -> None:
        """
        Disperses tokens to multiple recipients in a single transaction.

        Args:
            token_contract_address (str): The address of the token contract.
            recipients (List[str]): A list of recipient addresses.
            amounts (List[int]): A list of amounts corresponding to each recipient.

        Raises:
            ValueError: If the length of recipients and amounts do not match.
            Exception: For any errors encountered during token dispersal.
        """
        if len(recipients) != len(amounts):
            raise ValueError("The length of recipients and amounts must match.")

        # Prepare the function call to disperse tokens
        try:
            disperse_function = Contract.from_address(token_contract_address).functions['transfer']
            calls = [InvokeFunction(
                contract_address=token_contract_address,
                function='transfer',
                inputs=[recipients[i], amounts[i]]
            ) for i in range(len(recipients))]

            # Execute the batched transaction
            await self.client.invoke_batch(calls)
            print(f"Successfully dispersed tokens to {len(recipients)} recipients.")
        except Exception as e:
            print(f"An error occurred during the token dispersal: {e}")

# Example Usage
if __name__ == "__main__":
    import asyncio

    async def main():
        # Replace with actual values
        private_key = "YOUR_PRIVATE_KEY"
        network_url = "https://your_starknet_network_url"
        token_address = "0xYourTokenContractAddress"

        # List of recipient addresses and corresponding amounts to send
        recipients = ["0xRecipient1", "0xRecipient2", "0xRecipient3"]
        amounts = [100, 200, 300]

        # Create TokenDisperser instance
        disperser = TokenDisperser(private_key, network_url)
        
        # Disperse tokens
        await disperser.disperse_tokens(token_address, recipients, amounts)

    # Run the async main function
    asyncio.run(main())
```
