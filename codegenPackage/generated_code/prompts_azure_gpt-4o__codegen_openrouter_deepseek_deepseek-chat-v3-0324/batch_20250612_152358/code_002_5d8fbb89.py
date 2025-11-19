"""
Generated Code Metadata:
========================
Original URL: https://bafybeicc34wxgmwfldpiehsmb6azuurx52lonvbu63phtv6fto7rbacmja.ipfs.dweb.link
Prompt: Recommend an open-source stack for interchain communication that supports permissionless expansion and customizable security. Use Hyperlane as the example and explain its deployment process.
Generated: DETERMINISTIC_5d8fbb8988263e3c
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hyperlane_deployment.py
# Example deployment script for Hyperlane interchain communication stack

import os
import json
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class HyperlaneDeployer:
    """
    A class to handle Hyperlane deployment and configuration.
    Supports permissionless expansion and customizable security.
    """
    
    def __init__(self, rpc_urls: dict, deployer_key: str):
        """
        Initialize the deployer with RPC URLs for different chains and deployer private key.
        
        Args:
            rpc_urls (dict): Dictionary mapping chain names to their RPC URLs
            deployer_key (str): Private key of the deployer account
        """
        self.rpc_urls = rpc_urls
        self.deployer_key = deployer_key
        self.contracts = {}
        self.abis = self._load_abis()
        
    def _load_abis(self) -> dict:
        """Load ABIs for Hyperlane contracts from JSON files"""
        abis = {}
        contract_names = [
            'Mailbox', 'InterchainGasPaymaster', 
            'ValidatorAnnounce', 'MultisigIsm'
        ]
        
        for name in contract_names:
            with open(f'abi/{name}.json') as f:
                abis[name] = json.load(f)
        return abis
    
    def _get_web3_instance(self, chain: str) -> Web3:
        """Get Web3 instance for a specific chain"""
        if chain not in self.rpc_urls:
            raise ValueError(f"RPC URL not configured for chain: {chain}")
        return Web3(Web3.HTTPProvider(self.rpc_urls[chain]))
    
    def _get_deployer_account(self, w3: Web3):
        """Get deployer account from private key"""
        return w3.eth.account.from_key(self.deployer_key)
    
    def deploy_mailbox(self, chain: str, local_domain: int) -> str:
        """
        Deploy Mailbox contract on specified chain.
        
        Args:
            chain (str): Chain identifier
            local_domain (int): Domain ID for the chain
            
        Returns:
            str: Deployed contract address
        """
        w3 = self._get_web3_instance(chain)
        account = self._get_deployer_account(w3)
        
        contract = w3.eth.contract(
            abi=self.abis['Mailbox'],
            bytecode=self.abis['Mailbox']['bytecode']
        )
        
        tx = contract.constructor(local_domain).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 5000000,
            'gasPrice': w3.eth.gas_price
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        self.contracts[chain] = {
            'mailbox': receipt.contractAddress
        }
        return receipt.contractAddress
    
    def deploy_igp(self, chain: str, mailbox_address: str) -> str:
        """
        Deploy Interchain Gas Paymaster contract.
        
        Args:
            chain (str): Chain identifier
            mailbox_address (str): Address of Mailbox contract
            
        Returns:
            str: Deployed contract address
        """
        w3 = self._get_web3_instance(chain)
        account = self._get_deployer_account(w3)
        
        contract = w3.eth.contract(
            abi=self.abis['InterchainGasPaymaster'],
            bytecode=self.abis['InterchainGasPaymaster']['bytecode']
        )
        
        tx = contract.constructor(mailbox_address).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 5000000,
            'gasPrice': w3.eth.gas_price
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        self.contracts[chain]['igp'] = receipt.contractAddress
        return receipt.contractAddress
    
    def deploy_validator_announce(self, chain: str, mailbox_address: str) -> str:
        """
        Deploy Validator Announce contract.
        
        Args:
            chain (str): Chain identifier
            mailbox_address (str): Address of Mailbox contract
            
        Returns:
            str: Deployed contract address
        """
        w3 = self._get_web3_instance(chain)
        account = self._get_deployer_account(w3)
        
        contract = w3.eth.contract(
            abi=self.abis['ValidatorAnnounce'],
            bytecode=self.abis['ValidatorAnnounce']['bytecode']
        )
        
        tx = contract.constructor(mailbox_address).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 5000000,
            'gasPrice': w3.eth.gas_price
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        self.contracts[chain]['validator_announce'] = receipt.contractAddress
        return receipt.contractAddress
    
    def deploy_multisig_ism(self, chain: str, validators: list, threshold: int) -> str:
        """
        Deploy Multisig ISM contract with custom security parameters.
        
        Args:
            chain (str): Chain identifier
            validators (list): List of validator addresses
            threshold (int): Minimum number of signatures required
            
        Returns:
            str: Deployed contract address
        """
        w3 = self._get_web3_instance(chain)
        account = self._get_deployer_account(w3)
        
        contract = w3.eth.contract(
            abi=self.abis['MultisigIsm'],
            bytecode=self.abis['MultisigIsm']['bytecode']
        )
        
        tx = contract.constructor(validators, threshold).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 5000000,
            'gasPrice': w3.eth.gas_price
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        self.contracts[chain]['multisig_ism'] = receipt.contractAddress
        return receipt.contractAddress
    
    def configure_connection(
        self, 
        source_chain: str, 
        destination_chain: str, 
        ism_address: str
    ) -> bool:
        """
        Configure connection between two chains with custom ISM.
        
        Args:
            source_chain (str): Source chain identifier
            destination_chain (str): Destination chain identifier
            ism_address (str): Address of ISM contract
            
        Returns:
            bool: True if configuration was successful
        """
        w3 = self._get_web3_instance(source_chain)
        account = self._get_deployer_account(w3)
        
        mailbox = w3.eth.contract(
            address=self.contracts[source_chain]['mailbox'],
            abi=self.abis['Mailbox']
        )
        
        domain_map = {
            'ethereum': 1,
            'polygon': 2,
            'avalanche': 3,
            'optimism': 4,
            'arbitrum': 5
        }
        
        tx = mailbox.functions.setInterchainSecurityModule(
            domain_map[destination_chain],
            ism_address
        ).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 5000000,
            'gasPrice': w3.eth.gas_price
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        return receipt.status == 1

if __name__ == "__main__":
    # Example configuration
    rpc_urls = {
        'ethereum': os.getenv('ETHEREUM_RPC'),
        'polygon': os.getenv('POLYGON_RPC'),
        'avalanche': os.getenv('AVALANCHE_RPC')
    }
    
    deployer = HyperlaneDeployer(
        r
