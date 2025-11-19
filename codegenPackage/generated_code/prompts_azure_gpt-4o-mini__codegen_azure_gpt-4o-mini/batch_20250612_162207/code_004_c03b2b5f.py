"""
Generated Code Metadata:
========================
Original URL: https://fetch-merge.pages.dev
Prompt: Create an example of an AI agent that can be built using the Fetch.ai developer documentation.
Generated: DETERMINISTIC_c03b2b5fd896888c
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import fetchai.ledger.api as ledger_api
import fetchai.ledger.crypto as crypto
import fetchai.ledger.contract as contract
import fetchai.ledger.models as models
import fetchai.ledger.utils as utils

# Define the AI agent class
class FetchAI_Agent:
    def __init__(self, private_key: str):
        """
        Initialize the Fetch.ai agent with a private key.

        :param private_key: The private key for the agent's wallet.
        """
        self.wallet = crypto.PrivateKey(private_key)
        self.api = ledger_api.FetchAI()
        self.agent_address = self.wallet.get_address()
        self.contract = contract.Contract()

    def create_and_send_transaction(self, recipient: str, amount: float):
        """
        Create and send a transaction to a specified recipient.

        :param recipient: The address of the recipient.
        :param amount: The amount of tokens to send.
        """
        try:
            # Create a transaction
            transaction = self.api.transaction.create_transfer(
                sender=self.agent_address,
                recipient=recipient,
                amount=amount
            )
            # Sign the transaction
            signed_transaction = self.wallet.sign(transaction)
            # Send the transaction
            self.api.transaction.send(signed_transaction)
            print(f"Transaction of {amount} tokens sent to {recipient}.")
        except Exception as e:
            print(f"Error sending transaction: {e}")

    def deploy_contract(self, contract_code: str):
        """
        Deploy a smart contract to the Fetch.ai network.

        :param contract_code: The code of the smart contract to deploy.
        """
        try:
            # Compile the contract code
            compiled_contract = self.contract.compile(contract_code)
            # Deploy the contract
            transaction = self.api.contract.deploy(compiled_contract, self.agent_address)
            signed_transaction = self.wallet.sign(transaction)
            self.api.transaction.send(signed_transaction)
            print("Contract deployed successfully.")
        except Exception as e:
            print(f"Error deploying contract: {e}")

    def query_data(self, query: str):
        """
        Query data from the Fetch.ai network.

        :param query: The query string to execute.
        """
        try:
            result = self.api.query.execute(query)
            print(f"Query result: {result}")
        except Exception as e:
            print(f"Error querying data: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual private key
    PRIVATE_KEY = "your_private_key_here"
    
    # Create an instance of the FetchAI_Agent
    agent = FetchAI_Agent(PRIVATE_KEY)

    # Example transaction
    agent.create_and_send_transaction("recipient_address_here", 10.0)

    # Example contract deployment
    contract_code = """
    contract Example {
        public function greet() {
            return "Hello, Fetch.ai!";
        }
    }
    """
    agent.deploy_contract(contract_code)

    # Example data query
    agent.query_data("SELECT * FROM some_data_source")
```
