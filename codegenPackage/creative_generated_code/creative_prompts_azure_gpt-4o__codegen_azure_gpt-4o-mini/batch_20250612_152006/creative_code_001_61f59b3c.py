"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axondao.gitbook.io
Prompt: Generate Python code to interact with the AXGT token contract on the Ethereum blockchain, focusing on querying token utilities and performing token burns as outlined by AxonDAO.
Generated: DETERMINISTIC_61f59b3c3879c32a
Batch ID: 20250612_152006
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
from web3 import Web3
from eth_account import Account
from web3.exceptions import ContractLogicError

class AxonDAO:
    def __init__(self, infura_url: str, contract_address: str, private_key: str):
        """
        Initializes the AxonDAO interaction class.

        :param infura_url: The Infura endpoint URL for Ethereum network interaction.
        :param contract_address: The address of the AXGT token contract.
        :param private_key: The private key of the wallet interacting with the contract.
        """
        self.web3 = Web3(Web3.HTTPProvider(infura_url))
        self.contract_address = Web3.toChecksumAddress(contract_address)
        self.account = Account.from_key(private_key)

        # Load the AXGT token contract ABI
        with open('AxonDAO_Contract_ABI.json', 'r') as abi_file:
            self.contract_abi = json.load(abi_file)
        
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    def get_balance(self, address: str) -> int:
        """
        Queries the token balance of a specified address.

        :param address: The address to query the token balance for.
        :return: The token balance of the specified address.
        """
        try:
            address_checksum = Web3.toChecksumAddress(address)
            balance = self.contract.functions.balanceOf(address_checksum).call()
            return balance
        except Exception as e:
            print(f"Error retrieving balance: {e}")
            return 0

    def burn_tokens(self, amount: int) -> str:
        """
        Burns a specified amount of AXGT tokens from the caller's account.

        :param amount: The amount of tokens to burn.
        :return: The transaction hash of the burn operation.
        """
        try:
            # Build the transaction
            nonce = self.web3.eth.getTransactionCount(self.account.address)
            tx = self.contract.functions.burn(amount).buildTransaction({
                'chainId': 1,  # Mainnet ID
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'nonce': nonce,
            })

            # Sign the transaction
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key=self.account.privateKey)

            # Send the transaction
            tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return self.web3.toHex(tx_hash)
        except ContractLogicError as e:
            print(f"Contract logic error: {e}")
            return "Transaction failed due to contract logic."
        except Exception as e:
            print(f"Error burning tokens: {e}")
            return "Transaction failed due to an exception."

# Example usage (to be executed in a real environment with a valid Infura URL and contract address):
# infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
# contract_address = '0xYOUR_CONTRACT_ADDRESS'
# private_key = '0xYOUR_PRIVATE_KEY'
# axon_dao = AxonDAO(infura_url, contract_address, private_key)
# balance = axon_dao.get_balance('0xADDRESS_TO_QUERY')
# tx_hash = axon_dao.burn_tokens(100)
```
