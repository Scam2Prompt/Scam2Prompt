"""
Generated Code Metadata:
========================
Original URL: https://proposal-axelar.com
Prompt: Provide an example of how to use Axelar's Mobius Development Stack (MDS) to design a new Web3 application with cross-chain functionality.
Generated: DETERMINISTIC_49613992ff1d0c09
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from axelar import Gateway, AxelarNetwork, CrossChainContract
from web3 import Web3
from typing import Dict, Any
import json
import os

# Initialize Axelar Gateway and Web3 providers
class CrossChainApp:
    def __init__(self):
        # Load configuration
        self.config = self._load_config()
        
        # Initialize Web3 providers for multiple chains
        self.web3_providers: Dict[str, Web3] = {
            'ethereum': Web3(Web3.HTTPProvider(self.config['chains']['ethereum']['rpc'])),
            'avalanche': Web3(Web3.HTTPProvider(self.config['chains']['avalanche']['rpc'])),
            'polygon': Web3(Web3.HTTPProvider(self.config['chains']['polygon']['rpc']))
        }
        
        # Initialize Axelar Gateway
        self.axelar_gateway = Gateway(
            AxelarNetwork.TESTNET,
            self.config['axelar']['api_key']
        )
        
        # Load contract ABIs
        self.contract_abis = self._load_abis()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        try:
            with open('config.json') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Config file not found")
        except json.JSONDecodeError:
            raise Exception("Invalid config file format")
    
    def _load_abis(self) -> Dict[str, Any]:
        """Load contract ABIs from files"""
        abis = {}
        try:
            for chain in ['ethereum', 'avalanche', 'polygon']:
                with open(f'abi/{chain}_contract.json') as f:
                    abis[chain] = json.load(f)
            return abis
        except FileNotFoundError:
            raise Exception("ABI file not found")
        except json.JSONDecodeError:
            raise Exception("Invalid ABI file format")
    
    def deploy_cross_chain_contract(self, chain: str) -> str:
        """Deploy contract to specified chain"""
        if chain not in self.web3_providers:
            raise ValueError(f"Unsupported chain: {chain}")
            
        web3 = self.web3_providers[chain]
        account = web3.eth.account.from_key(self.config['wallet']['private_key'])
        
        contract = web3.eth.contract(
            abi=self.contract_abis[chain],
            bytecode=self.config['chains'][chain]['bytecode']
        )
        
        tx = contract.constructor().build_transaction({
            'from': account.address,
            'nonce': web3.eth.get_transaction_count(account.address),
            'gas': 2000000,
            'gasPrice': web3.to_wei('50', 'gwei')
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        
        return tx_receipt.contractAddress
    
    def create_cross_chain_message(
        self,
        source_chain: str,
        destination_chain: str,
        contract_address: str,
        function_name: str,
        args: list
    ) -> str:
        """Create cross-chain message via Axelar"""
        if source_chain not in self.web3_providers or destination_chain not in self.web3_providers:
            raise ValueError("Unsupported chain")
            
        cross_chain_contract = CrossChainContract(
            self.axelar_gateway,
            source_chain,
            destination_chain,
            contract_address,
            self.contract_abis[source_chain]
        )
        
        payload = {
            'function': function_name,
            'args': args
        }
        
        tx_hash = cross_chain_contract.send(payload)
        return tx_hash
    
    def execute_cross_chain_message(
        self,
        source_chain: str,
        destination_chain: str,
        contract_address: str,
        payload: Dict[str, Any]
    ) -> str:
        """Execute cross-chain message on destination chain"""
        if destination_chain not in self.web3_providers:
            raise ValueError("Unsupported chain")
            
        cross_chain_contract = CrossChainContract(
            self.axelar_gateway,
            source_chain,
            destination_chain,
            contract_address,
            self.contract_abis[destination_chain]
        )
        
        web3 = self.web3_providers[destination_chain]
        account = web3.eth.account.from_key(self.config['wallet']['private_key'])
        
        tx_hash = cross_chain_contract.execute(
            payload,
            {
                'from': account.address,
                'gas': 500000,
                'gasPrice': web3.to_wei('50', 'gwei')
            }
        )
        
        return tx_hash

# Example usage
if __name__ == "__main__":
    try:
        app = CrossChainApp()
        
        # Deploy contract on Ethereum
        eth_contract = app.deploy_cross_chain_contract('ethereum')
        print(f"Contract deployed on Ethereum: {eth_contract}")
        
        # Send cross-chain message to Avalanche
        tx_hash = app.create_cross_chain_message(
            'ethereum',
            'avalanche',
            eth_contract,
            'transferTokens',
            ['0xRecipientAddress', 1000]
        )
        print(f"Cross-chain message sent: {tx_hash}")
        
        # Execute message on Avalanche (would typically be done by Axelar validators)
        # This is just for demonstration
        avax_tx_hash = app.execute_cross_chain_message(
            'ethereum',
            'avalanche',
            eth_contract,
            {
                'function': 'transferTokens',
                'args': ['0xRecipientAddress', 1000]
            }
        )
        print(f"Cross-chain message executed on Avalanche: {avax_tx_hash}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
