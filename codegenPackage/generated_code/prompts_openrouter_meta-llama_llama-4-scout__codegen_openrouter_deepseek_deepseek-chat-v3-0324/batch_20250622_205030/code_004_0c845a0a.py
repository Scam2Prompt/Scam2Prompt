"""
Generated Code Metadata:
========================
Original URL: https://thousands-monkey-substantial.on-fleek.app
Prompt: What are the steps to implement a de[bridge]-like NFT bridging solution, and what are the key considerations for supporting multiple blockchain networks?
Generated: DETERMINISTIC_0c845a0a036c8b63
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# NFT Bridge Implementation
# Supports multiple blockchain networks with configurable parameters

import json
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_account import Account
from eth_typing import ChecksumAddress

class BlockchainNetwork:
    """Represents a blockchain network configuration."""
    def __init__(
        self,
        name: str,
        rpc_url: str,
        chain_id: int,
        bridge_contract_address: str,
        nft_contract_address: str,
        gas_limit: int = 300000,
        gas_price: Optional[int] = None
    ):
        self.name = name
        self.rpc_url = rpc_url
        self.chain_id = chain_id
        self.bridge_contract_address = Web3.to_checksum_address(bridge_contract_address)
        self.nft_contract_address = Web3.to_checksum_address(nft_contract_address)
        self.gas_limit = gas_limit
        self.gas_price = gas_price
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        
        if not self.web3.is_connected():
            raise ConnectionError(f"Failed to connect to {name} network at {rpc_url}")

class NFTBridgeContract(ABC):
    """Abstract base class for NFT bridge contracts."""
    @abstractmethod
    def lock(self, sender: str, token_id: int, destination_chain: str) -> str:
        """Lock NFT on source chain."""
        pass
    
    @abstractmethod
    def unlock(self, sender: str, token_id: int, source_chain: str, proof: str) -> str:
        """Unlock NFT on destination chain."""
        pass
    
    @abstractmethod
    def get_deposit_event(self, tx_hash: str) -> Optional[Dict]:
        """Get deposit event from transaction."""
        pass

class EVMNFTBridgeContract(NFTBridgeContract):
    """Ethereum Virtual Machine (EVM) compatible NFT bridge contract."""
    def __init__(self, network: BlockchainNetwork, contract_abi: str):
        self.network = network
        self.contract = network.web3.eth.contract(
            address=network.bridge_contract_address,
            abi=contract_abi
        )
    
    def lock(self, sender: str, token_id: int, destination_chain: str) -> str:
        sender_address = Web3.to_checksum_address(sender)
        
        try:
            tx = self.contract.functions.lock(
                token_id,
                destination_chain
            ).build_transaction({
                'from': sender_address,
                'chainId': self.network.chain_id,
                'gas': self.network.gas_limit,
                'gasPrice': self.network.gas_price or self.network.web3.eth.gas_price,
                'nonce': self.network.web3.eth.get_transaction_count(sender_address)
            })
            
            signed_tx = self.network.web3.eth.account.sign_transaction(
                tx,
                private_key=Account.decrypt(sender_address, 'password')  # In production, use secure key management
            )
            
            tx_hash = self.network.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        
        except ContractLogicError as e:
            raise Exception(f"Contract logic error: {e}")
        except Exception as e:
            raise Exception(f"Transaction failed: {e}")
    
    def unlock(self, sender: str, token_id: int, source_chain: str, proof: str) -> str:
        sender_address = Web3.to_checksum_address(sender)
        
        try:
            tx = self.contract.functions.unlock(
                token_id,
                source_chain,
                proof
            ).build_transaction({
                'from': sender_address,
                'chainId': self.network.chain_id,
                'gas': self.network.gas_limit,
                'gasPrice': self.network.gas_price or self.network.web3.eth.gas_price,
                'nonce': self.network.web3.eth.get_transaction_count(sender_address)
            })
            
            signed_tx = self.network.web3.eth.account.sign_transaction(
                tx,
                private_key=Account.decrypt(sender_address, 'password')  # In production, use secure key management
            )
            
            tx_hash = self.network.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        
        except ContractLogicError as e:
            raise Exception(f"Contract logic error: {e}")
        except Exception as e:
            raise Exception(f"Transaction failed: {e}")
    
    def get_deposit_event(self, tx_hash: str) -> Optional[Dict]:
        try:
            receipt = self.network.web3.eth.get_transaction_receipt(tx_hash)
            if receipt is None:
                raise TransactionNotFound(f"Transaction {tx_hash} not found")
            
            event_log = None
            for log in receipt['logs']:
                if log['address'].lower() == self.network.bridge_contract_address.lower():
                    event_log = log
                    break
            
            if event_log is None:
                return None
            
            event = self.contract.events.Deposit().process_log(event_log)
            return {
                'token_id': event['args']['tokenId'],
                'sender': event['args']['from'],
                'destination_chain': event['args']['destinationChain']
            }
        
        except TransactionNotFound as e:
            raise Exception(f"Transaction not found: {e}")
        except Exception as e:
            raise Exception(f"Failed to get deposit event: {e}")

class NFTBridge:
    """Main NFT bridge implementation supporting multiple networks."""
    def __init__(self):
        self.networks: Dict[str, BlockchainNetwork] = {}
        self.contracts: Dict[str, NFTBridgeContract] = {}
    
    def add_network(self, network: BlockchainNetwork, contract_abi: str):
        """Add a supported network with its bridge contract."""
        if network.name in self.networks:
            raise ValueError(f"Network {network.name} already exists")
        
        self.networks[network.name] = network
        
        if 'EVM' in network.name:  # Simplified network type detection
            self.contracts[network.name] = EVMNFTBridgeContract(network, contract_abi)
        else:
            raise NotImplementedError(f"Network type for {network.name} not supported")
    
    def bridge_nft(
        self,
        source_chain: str,
        destination_chain: str,
        sender: str,
        token_id: int,
        wait_for_confirmation: bool = False
    ) -> Dict[str, str]:
        """Bridge NFT from source chain to destination chain."""
        if source_chain not in self.networks:
            raise ValueError(f"Source chain {source_chain} not supported")
        if destination_chain not in self.networks:
            raise ValueError(f"Destination chain {destination_chain} not supported")
        
        source_contract = self.contracts[source_chain]
        dest_contract = self.contracts[destination_chain]
        
        try:
            # Step 1: Lock NFT on source chain
            lock_tx_hash = source_contract.lock(sender, token_id, destination_chain)
            
            if not wait_for_confirmation:
                return {
                    'status': 'pending',
                    'lock_tx_hash': lock_tx_hash,
                    'message': 'NFT locked. Unlock transaction must be submitted later.'
                }
            
            # Wait for confirmation and get deposit event
            deposit_event = self._wait_for_deposit_event(source_chain, lock_tx_hash)
            
            # Step 2: Unlock NFT on destination chain
            proof = self._generate_proof(source_chain, lock_tx_hash, deposit_event)
            unlock_tx_hash = dest_contract.unlock(sender, token_id, source_chain, proof)
            
            return {
                'status': 'completed',
                'lock_tx_hash': lock_tx_hash,
                'unlock_tx_hash': unlock_tx_hash,
                'message': 'NFT bridging completed successfully'
            }
        
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'message': 'NFT bridging failed'
            }
    
    def _wait_for_deposit_event(self, chain: str, tx_hash: str, timeout: int = 120) -> Dict:
        """Wait for deposit event confirmation."""
        contract = self.contracts[chain]
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            event = contract.get_deposit_event(tx_hash)
            if event is not None:
                return event
            time.sleep(5)
        
        raise TimeoutError(f"Timeout waiting for deposit event on {chain}")
    
    def _generate_proof(self, source_chain: str, tx_hash: str, event: Dict) -> str:
        """Generate proof for cross-chain verification."""
        # In production, implement proper cryptographic proof generation
        # This is a simplified version for demonstration
