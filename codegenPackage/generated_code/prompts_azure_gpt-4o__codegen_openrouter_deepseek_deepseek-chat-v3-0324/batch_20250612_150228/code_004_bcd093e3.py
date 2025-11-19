"""
Generated Code Metadata:
========================
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: Write a script to automate trading on Kwenta using Synthetix Perps. Include functionality for setting leverage levels and monitoring market conditions.
Generated: DETERMINISTIC_bcd093e3b998de6e
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
from typing import Dict, Optional, Tuple

# Load environment variables
load_dotenv()

# Constants
KWENTA_RPC_URL = os.getenv("KWENTA_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
PERPS_V2_MARKET_ADDRESS = os.getenv("PERPS_V2_MARKET_ADDRESS")
PERPS_V2_MARKET_ABI = json.load(open("abis/PerpsV2Market.json"))
SYNTHETIX_ADDRESS = os.getenv("SYNTHETIX_ADDRESS")
SYNTHETIX_ABI = json.load(open("abis/Synthetix.json"))

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(KWENTA_RPC_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Contracts
perps_v2_market = web3.eth.contract(address=PERPS_V2_MARKET_ADDRESS, abi=PERPS_V2_MARKET_ABI)
synthetix = web3.eth.contract(address=SYNTHETIX_ADDRESS, abi=SYNTHETIX_ABI)

class KwentaPerpsTrader:
    def __init__(self):
        self.account = web3.eth.account.from_key(PRIVATE_KEY)
        self.leverage = 10  # Default leverage
        self.max_slippage = 0.5  # 0.5% max slippage
        self.position_check_interval = 60  # seconds

    def _get_nonce(self) -> int:
        return web3.eth.get_transaction_count(self.account.address)

    def _send_transaction(self, tx: Dict) -> str:
        tx.update({
            'nonce': self._get_nonce(),
            'from': self.account.address,
            'gasPrice': web3.eth.gas_price
        })
        signed_tx = self.account.sign_transaction(tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def set_leverage(self, leverage: int) -> None:
        """Set the leverage for future trades."""
        if leverage < 1 or leverage > 25:
            raise ValueError("Leverage must be between 1 and 25")
        self.leverage = leverage

    def get_market_data(self, market_id: int) -> Dict:
        """Get market data including price and skew."""
        market_summary = perps_v2_market.functions.marketSummaries(market_id).call()
        return {
            'price': market_summary[0],
            'skew': market_summary[1],
            'size': market_summary[2]
        }

    def get_position(self, market_id: int) -> Optional[Dict]:
        """Get current position details for a market."""
        position = perps_v2_market.functions.positions(market_id, self.account.address).call()
        if position[0] == 0:  # No position exists
            return None
        return {
            'id': position[0],
            'last_price': position[1],
            'size': position[2],
            'margin': position[3],
            'last_funding_rate': position[4]
        }

    def open_position(
        self,
        market_id: int,
        size: float,
        is_long: bool,
        desired_price: Optional[float] = None
    ) -> str:
        """Open a new position with specified size and direction."""
        if desired_price is None:
            desired_price = self.get_market_data(market_id)['price']

        size_d18 = int(size * 1e18)
        desired_price_d18 = int(desired_price * 1e18)
        
        tx = perps_v2_market.functions.modifyPositionWithTracking(
            market_id,
            size_d18 if is_long else -size_d18,
            desired_price_d18,
            int(self.max_slippage * 1e18),
            self.leverage * 1e18,
            bytes(0)  # No tracking code
        ).build_transaction({
            'from': self.account.address
        })
        
        return self._send_transaction(tx)

    def close_position(self, market_id: int) -> str:
        """Close an existing position."""
        position = self.get_position(market_id)
        if not position:
            raise ValueError("No position exists to close")
        
        current_price = self.get_market_data(market_id)['price']
        size_d18 = int(position['size'] * 1e18)
        desired_price_d18 = int(current_price * 1e18)
        
        tx = perps_v2_market.functions.modifyPositionWithTracking(
            market_id,
            -size_d18 if position['size'] > 0 else size_d18,
            desired_price_d18,
            int(self.max_slippage * 1e18),
            0,  # No leverage when closing
            bytes(0)
        ).build_transaction({
            'from': self.account.address
        })
        
        return self._send_transaction(tx)

    def adjust_leverage(self, market_id: int, new_leverage: int) -> str:
        """Adjust leverage of an existing position."""
        position = self.get_position(market_id)
        if not position:
            raise ValueError("No position exists to adjust")
        
        current_price = self.get_market_data(market_id)['price']
        size_d18 = int(position['size'] * 1e18)
        desired_price_d18 = int(current_price * 1e18)
        
        tx = perps_v2_market.functions.modifyPositionWithTracking(
            market_id,
            size_d18 if position['size'] > 0 else -size_d18,
            desired_price_d18,
            int(self.max_slippage * 1e18),
            new_leverage * 1e18,
            bytes(0)
        ).build_transaction({
            'from': self.account.address
        })
        
        return self._send_transaction(tx)

    def monitor_and_trade(
        self,
        market_id: int,
        strategy_func,
        check_interval: Optional[int] = None
    ) -> None:
        """Monitor market conditions and execute trades based on strategy."""
        interval = check_interval or self.position_check_interval
        
        while True:
            try:
                market_data = self.get_market_data(market_id)
                position = self.get_position(market_id)
                
                action = strategy_func(market_data, position)
                
                if action == 'open_long':
                    self.open_position(market_id, 1, True)
                elif action == 'open_short':
                    self.open_position(market_id, 1, False)
                elif action == 'close':
                    self.close_position(market_id)
                elif action == 'adjust_leverage':
                    self.adjust_leverage(market_id, self.leverage)
                
                time.sleep(interval)
                
            except Exception as e:
                print(f"Error in monitoring loop: {e}")
                time.sleep(60)  # Wait before retrying

# Example strategy function
def example_strategy(market_data: Dict, position: Optional[Dict]) -> str:
    """Example strategy: Open long if price is below threshold, close if above."""
    price_threshold = 1000.0
    current_price = market_data['price'] / 1e18
    
    if position:
        if current_price > price_threshold * 1.05:
            return 'close'
    else:
        if current_price < price_threshold:
            return 'open_long'
    
    return 'hold'

if __name__ == "__main__":
    trader = KwentaPerpsTrader()
    trader.set_leverage(5)  # Set leverage to 5x
    
    # Start monitoring ETH market (market_id=1) with example strategy
    trader.monitor_and_trade(1, example_strategy)
```
