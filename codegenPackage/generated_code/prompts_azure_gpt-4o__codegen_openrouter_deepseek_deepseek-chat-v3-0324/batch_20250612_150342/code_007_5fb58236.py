"""
Generated Code Metadata:
========================
Original URL: https://starkware.eu
Prompt: Recommend best practices for integrating StarkWare's Layer 2 solutions into an NFT marketplace to reduce transaction costs and improve scalability.
Generated: DETERMINISTIC_5fb58236326356d2
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from web3 import Web3
from starkware.starknet.compiler.compile import compile_starknet_files
from starkware.starknet.testing.starknet import Starknet
from starkware.starknet.services.api.contract_definition import ContractDefinition
from starkware.starknet.services.api.gateway.transaction import InvokeFunction
from starkware.starknet.services.api.gateway.gateway_client import GatewayClient
from starkware.starknet.services.api.feeder_gateway.feeder_gateway_client import FeederGatewayClient
from starkware.starknet.services.api.feeder_gateway.response_objects import TransactionStatus
from starkware.starknet.business_logic.state.state import BlockInfo
from starkware.starknet.business_logic.execution.objects import Event
from starkware.starknet.public.abi import get_selector_from_name
import asyncio
import json
import os
from typing import Dict, List, Optional, Tuple

# Constants
STARKNET_NETWORK = "testnet"  # or "mainnet"
CONTRACT_SOURCE = "nft_marketplace.cairo"
MAX_FEE = int(1e18)  # Maximum fee in wei
GAS_PRICE = int(1e9)  # Gas price in wei

class StarkNetNFTMarketplace:
    """
    A class to handle StarkNet NFT Marketplace integration with StarkWare's Layer 2.
    """
    
    def __init__(self, network: str = STARKNET_NETWORK):
        """
        Initialize the StarkNet NFT Marketplace with network configuration.
        
        Args:
            network: StarkNet network to connect to (testnet/mainnet)
        """
        self.network = network
        self.gateway_client = GatewayClient(network=self.network)
        self.feeder_gateway_client = FeederGatewayClient(network=self.network)
        self.contract_definition = None
        self.contract_address = None
        self.account_address = None
        self.private_key = None
        
    async def deploy_contract(self, contract_source: str = CONTRACT_SOURCE) -> str:
        """
        Deploy the NFT Marketplace contract to StarkNet.
        
        Args:
            contract_source: Path to the Cairo contract source file
            
        Returns:
            Contract address
        """
        try:
            # Compile the contract
            contract_definition = compile_starknet_files(
                files=[contract_source],
                debug_info=True
            )
            
            # Deploy the contract
            starknet = await Starknet.empty()
            contract = await starknet.deploy(
                contract_definition=contract_definition
            )
            
            self.contract_definition = contract_definition
            self.contract_address = contract.contract_address
            
            return contract.contract_address
        except Exception as e:
            raise Exception(f"Failed to deploy contract: {str(e)}")
    
    async def initialize_marketplace(self, admin_address: str, fee_percentage: int):
        """
        Initialize the NFT Marketplace contract with admin and fee settings.
        
        Args:
            admin_address: Admin address for the marketplace
            fee_percentage: Percentage fee for marketplace transactions (0-100)
        """
        if not self.contract_address:
            raise Exception("Contract not deployed")
            
        try:
            selector = get_selector_from_name("initialize")
            calldata = [
                int(admin_address, 16),  # Admin address
                fee_percentage           # Fee percentage
            ]
            
            transaction = InvokeFunction(
                contract_address=self.contract_address,
                entry_point_selector=selector,
                calldata=calldata,
                max_fee=MAX_FEE
            )
            
            await self.gateway_client.add_transaction(transaction)
        except Exception as e:
            raise Exception(f"Failed to initialize marketplace: {str(e)}")
    
    async def list_nft(
        self, 
        seller_address: str,
        nft_contract_address: str,
        token_id: int,
        price: int,
        expiration_timestamp: int
    ) -> str:
        """
        List an NFT for sale on the marketplace.
        
        Args:
            seller_address: Address of the NFT seller
            nft_contract_address: Address of the NFT contract
            token_id: ID of the NFT token
            price: Price in wei
            expiration_timestamp: Unix timestamp when listing expires
            
        Returns:
            Transaction hash
        """
        try:
            selector = get_selector_from_name("list_nft")
            calldata = [
                int(seller_address, 16),
                int(nft_contract_address, 16),
                token_id,
                price,
                expiration_timestamp
            ]
            
            transaction = InvokeFunction(
                contract_address=self.contract_address,
                entry_point_selector=selector,
                calldata=calldata,
                max_fee=MAX_FEE
            )
            
            response = await self.gateway_client.add_transaction(transaction)
            return response["transaction_hash"]
        except Exception as e:
            raise Exception(f"Failed to list NFT: {str(e)}")
    
    async def buy_nft(
        self,
        buyer_address: str,
        listing_id: int,
        amount: int
    ) -> str:
        """
        Purchase an NFT listed on the marketplace.
        
        Args:
            buyer_address: Address of the buyer
            listing_id: ID of the NFT listing
            amount: Amount to pay (should match listing price)
            
        Returns:
            Transaction hash
        """
        try:
            selector = get_selector_from_name("buy_nft")
            calldata = [
                int(buyer_address, 16),
                listing_id,
                amount
            ]
            
            transaction = InvokeFunction(
                contract_address=self.contract_address,
                entry_point_selector=selector,
                calldata=calldata,
                max_fee=MAX_FEE
            )
            
            response = await self.gateway_client.add_transaction(transaction)
            return response["transaction_hash"]
        except Exception as e:
            raise Exception(f"Failed to buy NFT: {str(e)}")
    
    async def get_transaction_status(self, tx_hash: str) -> TransactionStatus:
        """
        Get the status of a transaction.
        
        Args:
            tx_hash: Transaction hash
            
        Returns:
            Transaction status
        """
        try:
            return await self.feeder_gateway_client.get_transaction_status(tx_hash)
        except Exception as e:
            raise Exception(f"Failed to get transaction status: {str(e)}")
    
    async def get_contract_state(self) -> Dict:
        """
        Get the current state of the marketplace contract.
        
        Returns:
            Dictionary containing contract state
        """
        try:
            return await self.feeder_gateway_client.get_contract_state(
                self.contract_address
            )
        except Exception as e:
            raise Exception(f"Failed to get contract state: {str(e)}")

# Example usage
async def main():
    try:
        # Initialize marketplace
        marketplace = StarkNetNFTMarketplace()
        
        # Deploy contract
        contract_address = await marketplace.deploy_contract()
        print(f"Contract deployed at: {contract_address}")
        
        # Initialize marketplace settings
        admin_address = "0x123..."  # Replace with actual admin address
        await marketplace.initialize_marketplace(admin_address, 5)  # 5% fee
        
        # Example NFT listing
        seller_address = "0x456..."  # Replace with actual seller address
        nft_contract_address = "0x789..."  # Replace with actual NFT contract address
        tx_hash = await marketplace.list_nft(
            seller_address,
            nft_contract_address,
            token_id=1,
            price=1000000000000000000,  # 1 ETH in wei
            expiration_timestamp=1234567890
        )
        print(f"NFT listed with tx hash: {tx_hash}")
        
        # Check transaction status
        status = await marketplace.get_transaction_status(tx_hash)
        print(f"Transaction status: {status}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
```
