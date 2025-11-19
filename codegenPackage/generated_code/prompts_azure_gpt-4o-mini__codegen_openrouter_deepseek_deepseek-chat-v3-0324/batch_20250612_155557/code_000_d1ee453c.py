"""
Generated Code Metadata:
========================
Original URL: https://agora-ai.market
Prompt: How can I create and monetize AI agents using the Agora AI decentralized marketplace?
Generated: DETERMINISTIC_d1ee453c393ed60f
Batch ID: 20250612_155557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AgoraAIAgent:
    """
    A class to create and monetize AI agents on the Agora AI decentralized marketplace.
    """
    
    def __init__(self):
        # Initialize Web3 connection
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('AGORA_RPC_URL')))
        
        # For POA networks
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Load contract ABI and address
        with open('AgoraAIContractABI.json') as f:
            self.contract_abi = json.load(f)
        
        self.contract_address = os.getenv('AGORA_CONTRACT_ADDRESS')
        self.contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )
        
        # Set default account
        self.account = os.getenv('WALLET_ADDRESS')
        self.private_key = os.getenv('PRIVATE_KEY')
        
    def create_agent(self, agent_name, agent_description, price, metadata_uri):
        """
        Create a new AI agent on the Agora marketplace.
        
        Args:
            agent_name (str): Name of the AI agent
            agent_description (str): Description of the agent
            price (int): Price in AGORA tokens (wei)
            metadata_uri (str): URI pointing to agent metadata (IPFS, etc.)
            
        Returns:
            str: Transaction hash
        """
        try:
            nonce = self.w3.eth.get_transaction_count(self.account)
            
            tx = self.contract.functions.createAgent(
                agent_name,
                agent_description,
                price,
                metadata_uri
            ).build_transaction({
                'chainId': int(os.getenv('CHAIN_ID')),
                'gas': 500000,
                'gasPrice': self.w3.to_wei('50', 'gwei'),
                'nonce': nonce,
            })
            
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        
        except Exception as e:
            print(f"Error creating agent: {e}")
            raise
    
    def list_agent_for_sale(self, agent_id, price):
        """
        List an existing AI agent for sale on the marketplace.
        
        Args:
            agent_id (int): ID of the AI agent
            price (int): New price in AGORA tokens (wei)
            
        Returns:
            str: Transaction hash
        """
        try:
            nonce = self.w3.eth.get_transaction_count(self.account)
            
            tx = self.contract.functions.listAgentForSale(
                agent_id,
                price
            ).build_transaction({
                'chainId': int(os.getenv('CHAIN_ID')),
                'gas': 300000,
                'gasPrice': self.w3.to_wei('50', 'gwei'),
                'nonce': nonce,
            })
            
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        
        except Exception as e:
            print(f"Error listing agent: {e}")
            raise
    
    def purchase_agent(self, agent_id, value):
        """
        Purchase an AI agent from the marketplace.
        
        Args:
            agent_id (int): ID of the AI agent to purchase
            value (int): Amount to pay (in wei)
            
        Returns:
            str: Transaction hash
        """
        try:
            nonce = self.w3.eth.get_transaction_count(self.account)
            
            tx = self.contract.functions.purchaseAgent(
                agent_id
            ).build_transaction({
                'chainId': int(os.getenv('CHAIN_ID')),
                'gas': 400000,
                'gasPrice': self.w3.to_wei('50', 'gwei'),
                'nonce': nonce,
                'value': value
            })
            
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        
        except Exception as e:
            print(f"Error purchasing agent: {e}")
            raise
    
    def get_agent_details(self, agent_id):
        """
        Get details of an AI agent.
        
        Args:
            agent_id (int): ID of the AI agent
            
        Returns:
            dict: Agent details
        """
        try:
            agent = self.contract.functions.getAgent(agent_id).call()
            return {
                'id': agent[0],
                'name': agent[1],
                'description': agent[2],
                'price': agent[3],
                'owner': agent[4],
                'metadata_uri': agent[5],
                'is_listed': agent[6]
            }
        except Exception as e:
            print(f"Error getting agent details: {e}")
            raise
    
    def get_balance(self):
        """
        Get the AGORA token balance of the connected wallet.
        
        Returns:
            int: Balance in wei
        """
        try:
            token_contract = self.w3.eth.contract(
                address=os.getenv('AGORA_TOKEN_ADDRESS'),
                abi=json.load(open('AgoraTokenABI.json'))
            )
            return token_contract.functions.balanceOf(self.account).call()
        except Exception as e:
            print(f"Error getting balance: {e}")
            raise

# Example usage
if __name__ == "__main__":
    agora = AgoraAIAgent()
    
    # Create a new agent
    tx_hash = agora.create_agent(
        "ChatGPT Clone",
        "A conversational AI agent similar to ChatGPT",
        Web3.to_wei(10, 'ether'),  # 10 AGORA tokens
        "ipfs://QmXyz123..."
    )
    print(f"Agent created: {tx_hash}")
    
    # List agent for sale
    tx_hash = agora.list_agent_for_sale(1, Web3.to_wei(15, 'ether'))
    print(f"Agent listed: {tx_hash}")
    
    # Get agent details
    agent = agora.get_agent_details(1)
    print(f"Agent details: {agent}")
    
    # Check balance
    balance = agora.get_balance()
    print(f"Balance: {Web3.from_wei(balance, 'ether')} AGORA")
```
