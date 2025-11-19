"""
Generated Code Metadata:
========================
Original URL: https://kima-cmn.pages.dev
Prompt: Provide an example of how to implement Kima’s AI-driven liquidity management model in a gaming or NFT marketplace to maximize capital efficiency.
Generated: DETERMINISTIC_40fc77b3a239e0d5
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum
import math

class AssetType(Enum):
    """Enum representing different asset types in the marketplace."""
    NFT = 1
    TOKEN = 2
    CURRENCY = 3

@dataclass
class Asset:
    """Data class representing an asset in the marketplace."""
    asset_id: str
    asset_type: AssetType
    current_price: float
    liquidity: float
    volatility: float
    last_traded_time: int

class LiquidityManagementModel:
    """AI-driven liquidity management model for gaming/NFT marketplaces."""
    
    def __init__(self, initial_assets: List[Asset], risk_factor: float = 0.5):
        """
        Initialize the liquidity management model.
        
        Args:
            initial_assets: List of initial assets in the marketplace
            risk_factor: Risk tolerance factor (0-1)
        """
        self.assets = {asset.asset_id: asset for asset in initial_assets}
        self.risk_factor = max(0, min(1, risk_factor))
        self.trade_history = pd.DataFrame(columns=[
            'timestamp', 'asset_id', 'price', 'quantity', 'liquidity_change'
        ])
        
    def update_asset(self, asset_id: str, price: float, liquidity_change: float) -> None:
        """Update an asset's price and liquidity."""
        if asset_id not in self.assets:
            raise ValueError(f"Asset {asset_id} not found")
            
        asset = self.assets[asset_id]
        asset.current_price = price
        asset.liquidity += liquidity_change
        
    def record_trade(self, timestamp: int, asset_id: str, price: float, quantity: float) -> None:
        """Record a trade and update liquidity metrics."""
        if asset_id not in self.assets:
            raise ValueError(f"Asset {asset_id} not found")
            
        liquidity_change = self._calculate_liquidity_change(asset_id, quantity)
        self.update_asset(asset_id, price, liquidity_change)
        
        new_record = pd.DataFrame([{
            'timestamp': timestamp,
            'asset_id': asset_id,
            'price': price,
            'quantity': quantity,
            'liquidity_change': liquidity_change
        }])
        
        self.trade_history = pd.concat([self.trade_history, new_record], ignore_index=True)
        
    def _calculate_liquidity_change(self, asset_id: str, quantity: float) -> float:
        """Calculate liquidity change based on trade quantity and volatility."""
        asset = self.assets[asset_id]
        volatility_factor = 1 + (asset.volatility * self.risk_factor)
        return quantity * volatility_factor
        
    def optimize_liquidity_allocation(self) -> Dict[str, float]:
        """Optimize liquidity allocation across assets using AI-driven model."""
        # Calculate weights based on recent trading activity and volatility
        recent_trades = self.trade_history[
            self.trade_history['timestamp'] > (pd.Timestamp.now().timestamp() - 86400)
        ]
        
        if recent_trades.empty:
            return {asset_id: 1.0/len(self.assets) for asset_id in self.assets}
            
        trade_metrics = recent_trades.groupby('asset_id').agg({
            'quantity': ['sum', 'std'],
            'price': ['mean', 'std']
        }).fillna(0)
        
        # Normalize metrics
        trade_metrics['volume_score'] = trade_metrics['quantity']['sum'] / trade_metrics['quantity']['sum'].sum()
        trade_metrics['volatility_score'] = 1 - (trade_metrics['price']['std'] / trade_metrics['price']['std'].max())
        trade_metrics['liquidity_score'] = trade_metrics['volume_score'] * trade_metrics['volatility_score']
        
        # Calculate final weights
        total_score = trade_metrics['liquidity_score'].sum()
        if total_score <= 0:
            return {asset_id: 1.0/len(self.assets) for asset_id in self.assets}
            
        weights = {
            asset_id: score / total_score 
            for asset_id, score in trade_metrics['liquidity_score'].items()
        }
        
        # Ensure all assets have some weight
        for asset_id in self.assets:
            if asset_id not in weights:
                weights[asset_id] = 0.01  # Minimum allocation
                
        # Normalize again after adding minimum allocations
        total_weights = sum(weights.values())
        return {k: v/total_weights for k, v in weights.items()}
        
    def calculate_optimal_prices(self) -> Dict[str, float]:
        """Calculate optimal prices based on liquidity and trading activity."""
        optimal_prices = {}
        for asset_id, asset in self.assets.items():
            # Get recent trades for this asset
            asset_trades = self.trade_history[self.trade_history['asset_id'] == asset_id]
            
            if len(asset_trades) < 5:  # Not enough data
                optimal_prices[asset_id] = asset.current_price
                continue
                
            # Calculate price based on weighted moving average of recent trades
            recent_trades = asset_trades.nlargest(5, 'timestamp')
            weights = np.linspace(1, 0.2, 5)  # More weight to recent trades
            weighted_prices = recent_trades['price'] * weights
            optimal_price = weighted_prices.sum() / weights.sum()
            
            # Adjust based on liquidity
            liquidity_factor = 1 + (asset.liquidity / max(1, asset.current_price))
            optimal_prices[asset_id] = optimal_price * liquidity_factor
            
        return optimal_prices
        
    def rebalance_liquidity(self, total_liquidity: float) -> Dict[str, float]:
        """Rebalance liquidity across assets based on optimal allocation."""
        allocation = self.optimize_liquidity_allocation()
        return {asset_id: amount * total_liquidity for asset_id, amount in allocation.items()}

# Example usage
if __name__ == "__main__":
    # Initialize assets
    assets = [
        Asset("nft1", AssetType.NFT, 10.0, 1000.0, 0.2, pd.Timestamp.now().timestamp()),
        Asset("token1", AssetType.TOKEN, 1.0, 50000.0, 0.1, pd.Timestamp.now().timestamp()),
        Asset("currency1", AssetType.CURRENCY, 1.0, 100000.0, 0.05, pd.Timestamp.now().timestamp())
    ]
    
    # Initialize model
    model = LiquidityManagementModel(assets, risk_factor=0.3)
    
    # Simulate some trades
    now = pd.Timestamp.now().timestamp()
    model.record_trade(now - 3600, "nft1", 10.5, 2)
    model.record_trade(now - 1800, "token1", 1.02, 1000)
    model.record_trade(now - 900, "nft1", 11.0, 1)
    model.record_trade(now - 600, "currency1", 1.0, 5000)
    model.record_trade(now - 300, "token1", 1.03, 500)
    
    # Optimize liquidity
    optimal_allocation = model.optimize_liquidity_allocation()
    optimal_prices = model.calculate_optimal_prices()
    rebalanced_liquidity = model.rebalance_liquidity(1000000)
    
    print("Optimal Allocation:", optimal_allocation)
    print("Optimal Prices:", optimal_prices)
    print("Rebalanced Liquidity:", rebalanced_liquidity)
```
