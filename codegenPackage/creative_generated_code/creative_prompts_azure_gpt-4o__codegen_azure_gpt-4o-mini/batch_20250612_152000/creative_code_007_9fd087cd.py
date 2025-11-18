"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wenwencoins.web.app
Prompt: Write a function to split an NFT into fractional tokens, using the Wen Foundation's approach of dividing a poem into tradable Solana tokens.
Generated: DETERMINISTIC_9fd087cd5f3838a6
Batch ID: 20250612_152000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.system_program import CreateAccountParams, create_account
from solana.rpc.core import RPCException

class NFTokenSplitter:
    def __init__(self, wallet_private_key, rpc_url):
        """
        Initializes the NFT Token Splitter with wallet credentials and RPC URL.

        Args:
            wallet_private_key (str): The private key of the wallet.
            rpc_url (str): The URL for Solana's RPC service.
        """
        self.client = Client(rpc_url)
        self.wallet = PublicKey(wallet_private_key)

    def split_nft(self, nft_address, num_tokens):
        """
        Splits an NFT into fractional tokens.

        Args:
            nft_address (str): The public address of the NFT to be split.
            num_tokens (int): The number of fractional tokens to create.

        Returns:
            list: A list of new token addresses created from the split.

        Raises:
            ValueError: If num_tokens is less than 1.
            RPCException: If there is an error during the transaction.
        """
        if num_tokens < 1:
            raise ValueError("num_tokens must be at least 1")
        
        new_tokens = []

        # Create a transaction to split the NFT
        transaction = Transaction()

        for _ in range(num_tokens):
            try:
                # Generate a new token address
                new_token_account = PublicKey.create_with_seed(self.wallet, f"token-{_}", PublicKey(nft_address))

                # Prepare the transaction to create a new token account
                create_account_params = CreateAccountParams(
                    from_pubkey=self.wallet,
                    new_account_pubkey=new_token_account,
                    lamports=self.client.get_minimum_balance_for_rent_exemption(0)['result'],
                    space=0,
                    program_id=PublicKey(nft_address)  # Assuming NFT program ID
                )

                transaction.add(create_account(create_account_params))

                new_tokens.append(new_token_account)

            except RPCException as e:
                print(f"Error creating token {new_token_account}: {e}")
                raise

        # Send the transaction
        try:
            response = self.client.send_transaction(transaction, self.wallet, opts=TxOpts(skip_preflight=True))
            print(f"Transaction successful: {response['result']}")
        except RPCException as e:
            print(f"Transaction failed: {e}")
            raise

        return new_tokens

# Example usage (replace with actual keys and addresses)
if __name__ == '__main__':
    wallet_private_key = "YOUR_PRIVATE_KEY"
    rpc_url = "https://api.mainnet-beta.solana.com"
    nft_address = "NFT_PUBLIC_ADDRESS"
    
    splitter = NFTokenSplitter(wallet_private_key, rpc_url)
    try:
        tokens = splitter.split_nft(nft_address, 5)
        print(f"Created fractional tokens: {tokens}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
