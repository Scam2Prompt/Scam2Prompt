"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidfgwggshi5syqnklufswynx2u6rumuvgp4jl6n4lbqsolbeshdga.ipfs.dweb.link
Prompt: Generate code in Python to interact with the Usual protocol's smart contracts, specifically for minting USD0 by depositing RWA or USDC.
Generated: DETERMINISTIC_6fb166e9658843e8
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import json
from web3 import Web3, exceptions

class UsualProtocolInteraction:
    """
    A class to interact with Usual protocol's smart contracts for minting USD0 
    by depositing RWA or USDC.
    """
    
    def __init__(self, rpc_url: str, contract_address: str, abi: str, private_key: str):
        """
        Initializes the connection to the blockchain and the contract.

        :param rpc_url: The RPC URL of the blockchain network (e.g., Ethereum).
        :param contract_address: The address of the Usual protocol smart contract.
        :param abi: The ABI of the contract, as a JSON string or object.
        :param private_key: The private key of the wallet to interact with the contract.
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.isConnected():
            raise ConnectionError("Unable to connect to RPC URL.")
        
        self.contract_address = Web3.toChecksumAddress(contract_address)
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=abi)
        self.private_key = private_key
        self.wallet_address = self.web3.eth.account.privateKeyToAccount(private_key).address

    def deposit_and_mint(self, asset_address: str, amount: int) -> str:
        """
        Deposits RWA or USDC and mints USD0.

        :param asset_address: The address of the asset being deposited (e.g., USDC or RWA).
        :param amount: The amount of the asset to deposit (in smallest denomination, e.g., wei for USDC).
        :return: Transaction hash of the deposit and mint operation.
        """
        try:
            asset_address = Web3.toChecksumAddress(asset_address)
            
            # Build the transaction payload to interact with the "depositAndMint" function
            txn = self.contract.functions.depositAndMint(asset_address, amount).buildTransaction({
                'chainId': self.web3.eth.chain_id,
                'gas': 200000,  # Adjust as per gas estimation
                'gasPrice': self.web3.eth.gas_price,
                'nonce': self.web3.eth.getTransactionCount(self.wallet_address),
            })

            # Sign the transaction with the private key
            signed_txn = self.web3.eth.account.sign_transaction(txn, self.private_key)

            # Send the signed transaction
            txn_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)

            return self.web3.toHex(txn_hash)

        except exceptions.SmartContractLogicError as e:
            raise RuntimeError(f"Smart contract logic error: {str(e)}")
        except ValueError as ve:
            raise RuntimeError(f"Transaction failed: {str(ve)}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {str(e)}")

    def check_balance(self, token_address: str) -> int:
        """
        Checks the balance of a specific token for the connected wallet.

        :param token_address: The address of the token contract (e.g., USDC or USD0).
        :return: Balance of the token (in smallest denomination, e.g., wei for USDC).
        """
        try:
            token_address = Web3.toChecksumAddress(token_address)
            
            # ABI for ERC20 tokens
            erc20_abi = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
            
            token_contract = self.web3.eth.contract(address=token_address, abi=erc20_abi)

            # Query balance for the wallet
            balance = token_contract.functions.balanceOf(self.wallet_address).call()

            return balance

        except exceptions.SmartContractLogicError as e:
            raise RuntimeError(f"Smart contract logic error: {str(e)}")
        except ValueError as ve:
            raise RuntimeError(f"Failed to query balance: {str(ve)}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Replace with your actual parameters
    RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    CONTRACT_ADDRESS = "0xYourContractAddressHere"
    CONTRACT_ABI = '[...]'  # Replace with the actual ABI JSON string
    PRIVATE_KEY = "0xYourPrivateKeyHere"
    ASSET_ADDRESS = "0xAssetContractAddressHere"  # Address of USDC or RWA
    DEPOSIT_AMOUNT = 1000000  # Example: Deposit 1 USDC (considering 6 decimals)

    try:
        # Initialize the interaction class
        protocol = UsualProtocolInteraction(RPC_URL, CONTRACT_ADDRESS, CONTRACT_ABI, PRIVATE_KEY)
        
        # Deposit and mint USD0
        txn_hash = protocol.deposit_and_mint(ASSET_ADDRESS, DEPOSIT_AMOUNT)
        print(f"Transaction successful! Hash: {txn_hash}")

        # Check USD0 balance
        usd0_balance = protocol.check_balance(CONTRACT_ADDRESS)
        print(f"USD0 Balance: {usd0_balance}")

    except Exception as e:
        print(f"Error: {str(e)}")
```
