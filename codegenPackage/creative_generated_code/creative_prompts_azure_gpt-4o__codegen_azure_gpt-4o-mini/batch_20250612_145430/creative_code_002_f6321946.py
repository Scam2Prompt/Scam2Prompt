"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-update-doc-419labs.vercel.app
Prompt: Generate code to integrate NFT payments functionality into a StarkNet Layer 2 application, using tools described in the StarkNet ecosystem.
Generated: DETERMINISTIC_f6321946690799c9
Batch ID: 20250612_145430
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.starknet.io": {
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
# Import necessary libraries from the StarkNet ecosystem
from starkware.starknet.business_logic.execution.objects import TransactionExecutionInfo
from starkware.starknet.services.api.contract_class import ContractClass
from starkware.starknet.services.api.gateway import GatewayClient
from starkware.starknet.services.api.gateway.gateway_client import GatewayClientError
from starkware.starknet.services.api.gateway.response import InvokeFunctionResponse

class NFTPaymentIntegration:
    def __init__(self, rpc_url: str, contract_address: str):
        """
        Initialize the NFTPaymentIntegration with RPC URL and contract address.

        :param rpc_url: The RPC URL of the StarkNet node.
        :param contract_address: The address of the NFT contract.
        """
        self.rpc_url = rpc_url
        self.contract_address = contract_address
        self.client = GatewayClient(self.rpc_url)

    async def get_nft_details(self, token_id: str):
        """
        Fetch the details of the NFT based on the token ID.

        :param token_id: The unique identifier for the NFT.
        :return: Details of the NFT.
        """
        try:
            # Assuming we have a method to fetch NFT details from the contract
            nft_details = await self.client.call_contract(method='get_nft_details', 
                                                           contract_address=self.contract_address, 
                                                           inputs=[token_id])
            return nft_details
        except GatewayClientError as e:
            print(f"Error fetching NFT details: {e}")
            return None

    async def make_payment(self, user_address: str, token_id: str, amount: int):
        """
        Trigger a payment transaction for the NFT.

        :param user_address: The address of the user making the payment.
        :param token_id: The unique identifier for the NFT.
        :param amount: The amount to be paid for the NFT.
        :return: Transaction execution information or error message.
        """
        try:
            # Prepare the transaction for invoking payment function
            invoke_response: InvokeFunctionResponse = await self.client.invoke_function(
                contract_address=self.contract_address,
                function_name='buy_nft',
                inputs=[user_address, token_id, amount]
            )
            return invoke_response
        except GatewayClientError as e:
            print(f"Error making payment for NFT: {e}")
            return None

    async def confirm_payment(self, tx_hash: str):
        """
        Confirm the payment transaction status based on transaction hash.

        :param tx_hash: The hash of the transaction.
        :return: Transaction execution info or error message.
        """
        try:
            # Poll for transaction execution info
            tx_info: TransactionExecutionInfo = await self.client.get_transaction_status(tx_hash)
            return tx_info
        except GatewayClientError as e:
            print(f"Error confirming payment transaction: {e}")
            return None

# Example usage (Uncomment to use in an async context where appropriate)
# async def main():
#     nft_payment = NFTPaymentIntegration(rpc_url="https://rpc.starknet.io", 
#                                          contract_address="0xYourNFTContractAddress")
#     nft_details = await nft_payment.get_nft_details(token_id="1")
#     print(f"NFT Details: {nft_details}")

#     payment_response = await nft_payment.make_payment(user_address="0xUserAddress", 
#                                                        token_id="1", 
#                                                        amount=100)
#     print(f"Payment Response: {payment_response}")

#     tx_info = await nft_payment.confirm_payment(tx_hash=payment_response.tx_hash)
#     print(f"Transaction Info: {tx_info}")

# asyncio.run(main())
```
