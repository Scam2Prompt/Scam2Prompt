"""
Generated Code Metadata:
========================
Original URL: https://web-extra.fi
Prompt: Generate code to integrate Extra Finance's yield optimization strategies into a multi-blockchain DeFi application, focusing on both conservative and aggressive yield farms.
Generated: DETERMINISTIC_cc31ef35beaa09ba
Batch ID: 20250612_153923
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
from web3.middleware import geth_poa_middleware
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChainID(Enum):
    ETHEREUM = 1
    POLYGON = 137
    ARBITRUM = 42161
    OPTIMISM = 10
    BSC = 56

@dataclass
class YieldStrategy:
    name: str
    chain_id: ChainID
    contract_address: str
    risk_level: str  # 'conservative' or 'aggressive'
    apy: float
    min_tvl: float
    abi: Optional[Dict] = None

class ExtraFinanceYieldOptimizer:
    def __init__(self, rpc_urls: Dict[ChainID, str], wallet_address: str, private_key: str):
        """
        Initialize the yield optimizer with RPC URLs for different chains.
        
        Args:
            rpc_urls: Dictionary mapping ChainID to RPC URL
            wallet_address: User's wallet address
            private_key: User's private key (should be securely handled in production)
        """
        self.rpc_urls = rpc_urls
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.web3_instances = self._initialize_web3_instances()
        self.strategies = self._load_strategies()

    def _initialize_web3_instances(self) -> Dict[ChainID, Web3]:
        """Initialize Web3 instances for each chain."""
        web3_instances = {}
        for chain_id, url in self.rpc_urls.items():
            w3 = Web3(Web3.HTTPProvider(url))
            if chain_id in [ChainID.POLYGON, ChainID.ARBITRUM, ChainID.BSC]:
                w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            web3_instances[chain_id] = w3
        return web3_instances

    def _load_strategies(self) -> List[YieldStrategy]:
        """Load predefined yield strategies from a config file."""
        try:
            with open('strategies_config.json', 'r') as f:
                strategies_data = json.load(f)
            
            strategies = []
            for strategy_data in strategies_data:
                strategies.append(YieldStrategy(
                    name=strategy_data['name'],
                    chain_id=ChainID(strategy_data['chain_id']),
                    contract_address=strategy_data['contract_address'],
                    risk_level=strategy_data['risk_level'],
                    apy=strategy_data['apy'],
                    min_tvl=strategy_data['min_tvl'],
                    abi=strategy_data.get('abi')
                ))
            return strategies
        except Exception as e:
            logger.error(f"Error loading strategies: {e}")
            raise

    def get_available_strategies(self, risk_level: Optional[str] = None) -> List[YieldStrategy]:
        """
        Get available yield strategies, optionally filtered by risk level.
        
        Args:
            risk_level: 'conservative', 'aggressive', or None for all
        Returns:
            List of matching YieldStrategy objects
        """
        if risk_level:
            return [s for s in self.strategies if s.risk_level == risk_level]
        return self.strategies

    def get_strategy_tvl(self, strategy: YieldStrategy) -> float:
        """Get the current TVL for a strategy."""
        try:
            w3 = self.web3_instances[strategy.chain_id]
            contract = w3.eth.contract(
                address=w3.to_checksum_address(strategy.contract_address),
                abi=strategy.abi
            )
            tvl = contract.functions.totalValueLocked().call() / 10**18
            return tvl
        except Exception as e:
            logger.error(f"Error getting TVL for strategy {strategy.name}: {e}")
            raise

    def deposit_to_strategy(
        self,
        strategy: YieldStrategy,
        amount: float,
        token_address: str,
        token_abi: Dict,
        gas_multiplier: float = 1.1
    ) -> str:
        """
        Deposit funds into a yield strategy.
        
        Args:
            strategy: The strategy to deposit into
            amount: Amount to deposit (in token decimals)
            token_address: Address of the token to deposit
            token_abi: ABI of the token contract
            gas_multiplier: Multiplier for gas estimation
        Returns:
            Transaction hash
        """
        try:
            w3 = self.web3_instances[strategy.chain_id]
            
            # Approve token spending
            token_contract = w3.eth.contract(
                address=w3.to_checksum_address(token_address),
                abi=token_abi
            )
            
            approve_tx = token_contract.functions.approve(
                w3.to_checksum_address(strategy.contract_address),
                int(amount * 10**18)
            ).build_transaction({
                'from': self.wallet_address,
                'nonce': w3.eth.get_transaction_count(self.wallet_address),
            })
            
            signed_approve = w3.eth.account.sign_transaction(
                approve_tx, private_key=self.private_key
            )
            approve_hash = w3.eth.send_raw_transaction(signed_approve.rawTransaction)
            w3.eth.wait_for_transaction_receipt(approve_hash)
            
            # Deposit to strategy
            strategy_contract = w3.eth.contract(
                address=w3.to_checksum_address(strategy.contract_address),
                abi=strategy.abi
            )
            
            deposit_tx = strategy_contract.functions.deposit(
                int(amount * 10**18)
            ).build_transaction({
                'from': self.wallet_address,
                'nonce': w3.eth.get_transaction_count(self.wallet_address),
            })
            
            # Estimate gas with multiplier
            estimated_gas = deposit_tx['gas'] * gas_multiplier
            deposit_tx['gas'] = int(estimated_gas)
            
            signed_deposit = w3.eth.account.sign_transaction(
                deposit_tx, private_key=self.private_key
            )
            deposit_hash = w3.eth.send_raw_transaction(signed_deposit.rawTransaction)
            receipt = w3.eth.wait_for_transaction_receipt(deposit_hash)
            
            return receipt.transactionHash.hex()
        except Exception as e:
            logger.error(f"Error depositing to strategy {strategy.name}: {e}")
            raise

    def withdraw_from_strategy(
        self,
        strategy: YieldStrategy,
        amount: float,
        gas_multiplier: float = 1.1
    ) -> str:
        """
        Withdraw funds from a yield strategy.
        
        Args:
            strategy: The strategy to withdraw from
            amount: Amount to withdraw (in token decimals)
            gas_multiplier: Multiplier for gas estimation
        Returns:
            Transaction hash
        """
        try:
            w3 = self.web3_instances[strategy.chain_id]
            contract = w3.eth.contract(
                address=w3.to_checksum_address(strategy.contract_address),
                abi=strategy.abi
            )
            
            withdraw_tx = contract.functions.withdraw(
                int(amount * 10**18)
            ).build_transaction({
                'from': self.wallet_address,
                'nonce': w3.eth.get_transaction_count(self.wallet_address),
            })
            
            # Estimate gas with multiplier
            estimated_gas = withdraw_tx['gas'] * gas_multiplier
            withdraw_tx['gas'] = int(estimated_gas)
            
            signed_withdraw = w3.eth.account.sign_transaction(
                withdraw_tx, private_key=self.private_key
            )
            withdraw_hash = w3.eth.send_raw_transaction(signed_withdraw.rawTransaction)
            receipt = w3.eth.wait_for_transaction_receipt(withdraw_hash)
            
            return receipt.transactionHash.hex()
        except Exception as e:
            logger.error(f"Error withdrawing from strategy {strategy.name}: {e}")
            raise

    def get_optimal_strategy(
        self,
        risk_level: str,
        min_apy: float = 0,
        min_tvl: float = 0
    ) -> Optional[YieldStrategy]:
        """
        Find the optimal strategy based on parameters.
        
        Args:
            risk_level: 'conservative' or 'aggressive'
            min_apy: Minimum APY threshold
            min_tvl: Minimum TVL threshold
        Returns:
            The optimal YieldStrategy or None if none found
        """
        try:
            candidates = [
                s for s in self.strategies 
                if s.risk_level == risk_level 
                and s.apy >= min_apy
            ]
            
            # Filter by TVL and get current TV
