"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: Generate code to interact with NAVI Protocol's liquidity pool system, allowing users to borrow cryptocurrency assets while enforcing supply limits and debt ceilings for risk management.
Generated: DETERMINISTIC_5e5ea927c767fab0
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from web3.exceptions import ContractLogicError
from typing import Dict, List, Optional, Tuple

class NAVILiquidityPool:
    """
    Interact with NAVI Protocol's liquidity pool system for borrowing assets.
    Handles supply limits and debt ceilings for risk management.
    """
    
    def __init__(self, web3_provider: str, pool_contract_address: str, abi_file: str):
        """
        Initialize the NAVI liquidity pool interaction.
        
        Args:
            web3_provider: URL of the Ethereum node provider
            pool_contract_address: Address of the NAVI pool contract
            abi_file: Path to the contract ABI JSON file
        """
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.pool_address = pool_contract_address
        
        with open(abi_file) as f:
            abi = json.load(f)
        
        self.contract = self.web3.eth.contract(
            address=self.pool_address,
            abi=abi
        )
    
    def get_asset_config(self, asset_address: str) -> Dict:
        """
        Get configuration details for a specific asset in the pool.
        
        Args:
            asset_address: Address of the asset to query
            
        Returns:
            Dictionary containing asset configuration
        """
        try:
            config = self.contract.functions.getAssetConfig(asset_address).call()
            return {
                'is_active': config[0],
                'supply_cap': config[1],
                'borrow_cap': config[2],
                'collateral_enabled': config[3],
                'collateral_factor': config[4],
                'liquidation_threshold': config[5],
                'liquidation_bonus': config[6],
                'reserve_factor': config[7]
            }
        except ContractLogicError as e:
            raise ValueError(f"Error fetching asset config: {str(e)}")
    
    def get_user_position(self, user_address: str) -> Dict:
        """
        Get a user's current position including supplied and borrowed assets.
        
        Args:
            user_address: Address of the user to query
            
        Returns:
            Dictionary containing user's position details
        """
        try:
            position = self.contract.functions.getUserPosition(user_address).call()
            return {
                'total_collateral': position[0],
                'total_debt': position[1],
                'available_borrow': position[2],
                'health_factor': position[3],
                'liquidation_threshold': position[4]
            }
        except ContractLogicError as e:
            raise ValueError(f"Error fetching user position: {str(e)}")
    
    def borrow_asset(
        self,
        asset_address: str,
        amount: float,
        private_key: str,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ) -> str:
        """
        Borrow an asset from the pool with risk management checks.
        
        Args:
            asset_address: Address of the asset to borrow
            amount: Amount to borrow (in asset decimals)
            private_key: Private key for signing transaction
            gas_limit: Gas limit for transaction
            gas_price: Gas price in wei (optional)
            
        Returns:
            Transaction hash of the borrow operation
            
        Raises:
            ValueError: If borrow would exceed limits or other constraints
        """
        # Convert amount to integer based on asset decimals
        decimals = self.contract.functions.getAssetDecimals(asset_address).call()
        amount_wei = int(amount * (10 ** decimals))
        
        # Check borrow limits
        asset_config = self.get_asset_config(asset_address)
        if not asset_config['is_active']:
            raise ValueError("Asset is not active for borrowing")
        
        if asset_config['borrow_cap'] > 0:
            current_borrows = self.contract.functions.getAssetBorrows(asset_address).call()
            if current_borrows + amount_wei > asset_config['borrow_cap']:
                raise ValueError("Borrow would exceed asset borrow cap")
        
        # Check user position
        account = self.web3.eth.account.from_key(private_key)
        user_position = self.get_user_position(account.address)
        
        if amount_wei > user_position['available_borrow']:
            raise ValueError("Borrow amount exceeds available borrow limit")
        
        # Prepare transaction
        nonce = self.web3.eth.get_transaction_count(account.address)
        
        tx_params = {
            'chainId': self.web3.eth.chain_id,
            'gas': gas_limit,
            'nonce': nonce,
            'from': account.address
        }
        
        if gas_price:
            tx_params['gasPrice'] = gas_price
        else:
            tx_params['maxFeePerGas'] = self.web3.eth.gas_price
            tx_params['maxPriorityFeePerGas'] = self.web3.eth.max_priority_fee
        
        try:
            tx = self.contract.functions.borrow(
                asset_address,
                amount_wei
            ).build_transaction(tx_params)
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        except ContractLogicError as e:
            raise ValueError(f"Borrow transaction failed: {str(e)}")
        except Exception as e:
            raise ValueError(f"Transaction error: {str(e)}")
    
    def repay_asset(
        self,
        asset_address: str,
        amount: float,
        private_key: str,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ) -> str:
        """
        Repay a borrowed asset to the pool.
        
        Args:
            asset_address: Address of the asset to repay
            amount: Amount to repay (in asset decimals)
            private_key: Private key for signing transaction
            gas_limit: Gas limit for transaction
            gas_price: Gas price in wei (optional)
            
        Returns:
            Transaction hash of the repay operation
        """
        decimals = self.contract.functions.getAssetDecimals(asset_address).call()
        amount_wei = int(amount * (10 ** decimals))
        
        account = self.web3.eth.account.from_key(private_key)
        nonce = self.web3.eth.get_transaction_count(account.address)
        
        tx_params = {
            'chainId': self.web3.eth.chain_id,
            'gas': gas_limit,
            'nonce': nonce,
            'from': account.address
        }
        
        if gas_price:
            tx_params['gasPrice'] = gas_price
        else:
            tx_params['maxFeePerGas'] = self.web3.eth.gas_price
            tx_params['maxPriorityFeePerGas'] = self.web3.eth.max_priority_fee
        
        try:
            tx = self.contract.functions.repay(
                asset_address,
                amount_wei
            ).build_transaction(tx_params)
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        except ContractLogicError as e:
            raise ValueError(f"Repay transaction failed: {str(e)}")
        except Exception as e:
            raise ValueError(f"Transaction error: {str(e)}")
    
    def get_available_assets(self) -> List[Dict]:
        """
        Get list of all available assets in the pool with their configurations.
        
        Returns:
            List of dictionaries containing asset details
        """
        try:
            assets = self.contract.functions.getAvailableAssets().call()
            asset_details = []
            
            for asset in assets:
                config = self.get_asset_config(asset)
                asset_details.append({
                    'address': asset,
                    'symbol': self.contract.functions.getAssetSymbol(asset).call(),
                    'decimals': self.contract.functions.getAssetDecimals(asset).call(),
                    'config': config
                })
            
            return asset_details
        except ContractLogicError as e:
            raise ValueError(f"Error fetching available assets: {str(e)}")
```
