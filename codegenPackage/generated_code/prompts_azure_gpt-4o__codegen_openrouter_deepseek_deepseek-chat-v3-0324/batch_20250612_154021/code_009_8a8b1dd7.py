"""
Generated Code Metadata:
========================
Original URL: https://saterdex.com
Prompt: Develop a tool to monitor and execute trades on Aster's decentralized perpetual contracts platform, ensuring full control of assets and leveraging cross-chain liquidity aggregation.
Generated: DETERMINISTIC_8a8b1dd7c1a02d40
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import json
import logging
from typing import Dict, List, Optional, Tuple

import aiohttp
from eth_account import Account
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractLogicError, TransactionNotFound
from web3.middleware import construct_sign_and_send_raw_middleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AsterPerpetualTrader:
    """
    A tool to monitor and execute trades on Aster's decentralized perpetual contracts platform.
    """
    
    def __init__(
        self,
        private_key: str,
        rpc_url: str,
        contract_address: str,
        contract_abi: str,
        cross_chain_aggregator_url: Optional[str] = None
    ):
        """
        Initialize the trader with wallet and contract details.
        
        Args:
            private_key: Private key for the trading wallet
            rpc_url: Ethereum node RPC URL
            contract_address: Aster perpetual contract address
            contract_abi: Aster perpetual contract ABI (as JSON string)
            cross_chain_aggregator_url: Optional URL for cross-chain liquidity aggregator
        """
        self.private_key = private_key
        self.rpc_url = rpc_url
        self.contract_address = contract_address
        self.contract_abi = json.loads(contract_abi)
        self.cross_chain_aggregator_url = cross_chain_aggregator_url
        
        # Initialize Web3
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node")
            
        # Set up account
        self.account = Account.from_key(private_key)
        self.w3.middleware_onion.add(construct_sign_and_send_raw_middleware(self.account))
        self.w3.eth.default_account = self.account.address
        
        # Load contract
        self.contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )
        
        # Initialize session for cross-chain aggregator
        self.session = aiohttp.ClientSession() if cross_chain_aggregator_url else None
        
    async def close(self):
        """Clean up resources."""
        if self.session:
            await self.session.close()
    
    async def get_market_data(self, market_id: str) -> Dict:
        """
        Get market data for a specific market.
        
        Args:
            market_id: ID of the market to query
            
        Returns:
            Dictionary containing market data
        """
        try:
            return self.contract.functions.getMarketData(market_id).call()
        except ContractLogicError as e:
            logger.error(f"Error getting market data: {e}")
            raise
    
    async def get_best_liquidity(
        self,
        market_id: str,
        amount: float,
        is_long: bool
    ) -> Tuple[float, float]:
        """
        Get best available liquidity from cross-chain aggregator.
        
        Args:
            market_id: ID of the market
            amount: Desired trade amount
            is_long: Whether the trade is long
            
        Returns:
            Tuple of (best_price, max_available)
        """
        if not self.cross_chain_aggregator_url:
            raise ValueError("Cross-chain aggregator URL not configured")
            
        try:
            params = {
                "market": market_id,
                "amount": amount,
                "side": "buy" if is_long else "sell"
            }
            
            async with self.session.get(
                f"{self.cross_chain_aggregator_url}/best_price",
                params=params
            ) as resp:
                if resp.status != 200:
                    raise ValueError(f"Aggregator returned status {resp.status}")
                    
                data = await resp.json()
                return float(data["price"]), float(data["max_available"])
                
        except Exception as e:
            logger.error(f"Error getting best liquidity: {e}")
            raise
    
    async def execute_trade(
        self,
        market_id: str,
        amount: float,
        is_long: bool,
        leverage: int = 1,
        price: Optional[float] = None,
        max_slippage: float = 0.005
    ) -> str:
        """
        Execute a trade on Aster perpetual contracts.
        
        Args:
            market_id: ID of the market to trade
            amount: Trade amount in base currency
            is_long: Whether to open a long position
            leverage: Leverage multiplier (default 1)
            price: Optional limit price (None for market)
            max_slippage: Maximum acceptable slippage (default 0.5%)
            
        Returns:
            Transaction hash of the executed trade
        """
        try:
            # Get current market price if not specified
            if price is None:
                market_data = await self.get_market_data(market_id)
                price = market_data["indexPrice"]
                
                # Adjust for slippage
                if is_long:
                    price *= (1 + max_slippage)
                else:
                    price *= (1 - max_slippage)
            
            # Prepare trade parameters
            trade_params = {
                "marketId": market_id,
                "amount": int(amount * 10**18),  # Assuming 18 decimals
                "isLong": is_long,
                "leverage": leverage,
                "price": int(price * 10**18),  # Assuming 18 decimals
                "referralCode": bytes(0)  # No referral by default
            }
            
            # Estimate gas
            gas_estimate = self.contract.functions.openPosition(
                trade_params["marketId"],
                trade_params["amount"],
                trade_params["isLong"],
                trade_params["leverage"],
                trade_params["price"],
                trade_params["referralCode"]
            ).estimate_gas()
            
            # Build transaction
            tx = self.contract.functions.openPosition(
                trade_params["marketId"],
                trade_params["amount"],
                trade_params["isLong"],
                trade_params["leverage"],
                trade_params["price"],
                trade_params["referralCode"]
            ).build_transaction({
                'from': self.account.address,
                'gas': gas_estimate,
                'gasPrice': self.w3.eth.gas_price,
                'nonce': self.w3.eth.get_transaction_count(self.account.address),
            })
            
            # Send transaction
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            logger.info(f"Trade executed with tx hash: {tx_hash.hex()}")
            return tx_hash.hex()
            
        except Exception as e:
            logger.error(f"Error executing trade: {e}")
            raise
    
    async def monitor_positions(self, interval: int = 60) -> List[Dict]:
        """
        Monitor open positions at regular intervals.
        
        Args:
            interval: Monitoring interval in seconds
            
        Returns:
            List of open positions
        """
        while True:
            try:
                positions = self.contract.functions.getPositions(self.account.address).call()
                logger.info(f"Current positions: {positions}")
                await asyncio.sleep(interval)
            except Exception as e:
                logger.error(f"Error monitoring positions: {e}")
                await asyncio.sleep(interval)  # Continue even after error
    
    async def close_position(
        self,
        position_id: str,
        max_slippage: float = 0.005
    ) -> str:
        """
        Close an open position.
        
        Args:
            position_id: ID of the position to close
            max_slippage: Maximum acceptable slippage (default 0.5%)
            
        Returns:
            Transaction hash of the close operation
        """
        try:
            # Get position details
            position = self.contract.functions.getPosition(position_id).call()
            if not position:
                raise ValueError(f"Position {position_id} not found")
                
            # Get current market price
            market_data = await self.get_market_data(position["marketId"])
            price = market_data["indexPrice"]
            
            # Adjust for slippage
            if position["isLong"]:
                price *= (1 - max_slippage)
            else:
                price *= (1 + max_slippage)
            
            # Prepare close parameters
            close_params = {
                "positionId": position_id,
                "price": int(price * 10**18)  # Assuming 18 decimals
            }
            
            # Estimate gas
            gas_estimate = self.contract.functions.closePosition(
                close_params["positionId"],
                close_params["price"]
            ).estimate_gas()
            
            # Build transaction
            tx = self.contract.functions.closePosition(
                close_params["positionId"],
                close_params["price"]
            ).build_transaction({
                'from': self.account.address,
                'gas': gas_estimate,
                'gasPrice': self.w
