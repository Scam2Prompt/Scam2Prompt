"""
Generated Code Metadata:
========================
Original URL: https://atocha.io
Prompt: Provide a step-by-step guide to deploying an appchain on the Octopus Network for a puzzle-solving dApp similar to Atocha.
Generated: DETERMINISTIC_a47e984d078c9edf
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
import os
import json
import subprocess
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class OctopusNetworkDeployer:
    """
    A class to handle the deployment of an appchain on Octopus Network for a puzzle-solving dApp.
    """
    
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('OCTOPUS_RPC_URL')))
        self.owner_address = os.getenv('OWNER_ADDRESS')
        self.owner_private_key = os.getenv('OWNER_PRIVATE_KEY')
        self.chain_id = int(os.getenv('CHAIN_ID'))
        self.gas_price = int(os.getenv('GAS_PRICE', 1000000000))
        self.gas_limit = int(os.getenv('GAS_LIMIT', 3000000))
        
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to Octopus Network RPC")
    
    def check_balance(self):
        """Check the balance of the owner account."""
        balance = self.w3.eth.get_balance(self.owner_address)
        return self.w3.from_wei(balance, 'ether')
    
    def deploy_contract(self, contract_name, *args):
        """
        Deploy a smart contract to the Octopus Network.
        
        Args:
            contract_name (str): Name of the contract to deploy
            *args: Constructor arguments for the contract
            
        Returns:
            str: Address of the deployed contract
        """
        # Load contract ABI and bytecode
        with open(f'build/contracts/{contract_name}.json') as f:
            contract_data = json.load(f)
        
        abi = contract_data['abi']
        bytecode = contract_data['bytecode']
        
        # Create contract instance
        contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        
        # Build transaction
        transaction = contract.constructor(*args).build_transaction({
            'chainId': self.chain_id,
            'gas': self.gas_limit,
            'gasPrice': self.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.owner_address),
        })
        
        # Sign and send transaction
        signed_txn = self.w3.eth.account.sign_transaction(
            transaction, private_key=self.owner_private_key
        )
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        # Wait for transaction receipt
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        
        return tx_receipt.contractAddress
    
    def register_appchain(self, contract_address):
        """
        Register the appchain with Octopus Network.
        
        Args:
            contract_address (str): Address of the deployed appchain contract
            
        Returns:
            str: Transaction hash of the registration
        """
        # Load Octopus Registry contract
        with open('build/contracts/OctopusRegistry.json') as f:
            registry_data = json.load(f)
        
        registry = self.w3.eth.contract(
            address=os.getenv('OCTOPUS_REGISTRY_ADDRESS'),
            abi=registry_data['abi']
        )
        
        # Build transaction
        transaction = registry.functions.registerAppchain(
            contract_address,
            os.getenv('APPCHAIN_NAME'),
            os.getenv('APPCHAIN_DESC'),
            os.getenv('APPCHAIN_WEBSITE'),
            os.getenv('APPCHAIN_LOGO')
        ).build_transaction({
            'chainId': self.chain_id,
            'gas': self.gas_limit,
            'gasPrice': self.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.owner_address),
        })
        
        # Sign and send transaction
        signed_txn = self.w3.eth.account.sign_transaction(
            transaction, private_key=self.owner_private_key
        )
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        return tx_hash.hex()
    
    def compile_contracts(self):
        """Compile smart contracts using Hardhat."""
        try:
            subprocess.run(
                ['npx', 'hardhat', 'compile'],
                check=True,
                cwd=os.getcwd()
            )
            print("Contracts compiled successfully")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Contract compilation failed: {e}")

def main():
    try:
        # Initialize deployer
        deployer = OctopusNetworkDeployer()
        
        # Check balance
        balance = deployer.check_balance()
        print(f"Owner balance: {balance} OCT")
        
        if balance < 1:
            raise ValueError("Insufficient balance for deployment")
        
        # Compile contracts
        deployer.compile_contracts()
        
        # Deploy puzzle contract
        puzzle_contract_address = deployer.deploy_contract(
            'PuzzleGame',
            os.getenv('REWARD_TOKEN_ADDRESS'),
            int(os.getenv('PUZZLE_REWARD_AMOUNT'))
        )
        print(f"Puzzle contract deployed at: {puzzle_contract_address}")
        
        # Register appchain
        tx_hash = deployer.register_appchain(puzzle_contract_address)
        print(f"Appchain registration tx hash: {tx_hash}")
        
        print("Deployment completed successfully!")
        
    except Exception as e:
        print(f"Deployment failed: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
```
