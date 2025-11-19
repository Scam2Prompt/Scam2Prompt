"""
Generated Code Metadata:
========================
Original URL: https://crtik.cn
Prompt: Generate code to simulate the issuance and market performance of synthetic assets in a decentralized finance ecosystem.
Generated: DETERMINISTIC_15b06c15a836bf3a
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import math
from datetime import datetime, timedelta

class AssetType(Enum):
    STOCK = auto()
    COMMODITY = auto()
    CRYPTO = auto()
    FOREX = auto()
    INDEX = auto()

@dataclass
class SyntheticAsset:
    id: str
    name: str
    asset_type: AssetType
    underlying_assets: List[str]
    collateral_ratio: float
    issuance_date: datetime
    current_price: float = 0.0
    price_history: Dict[datetime, float] = None

    def __post_init__(self):
        if self.price_history is None:
            self.price_history = {}
        self.price_history[self.issuance_date] = self.current_price

class MarketCondition(Enum):
    BULL = auto()
    BEAR = auto()
    STAGNANT = auto()

class SyntheticAssetMarket:
    def __init__(self):
        self.assets: Dict[str, SyntheticAsset] = {}
        self.market_condition = MarketCondition.STAGNANT
        self.last_update = datetime.now()
    
    def issue_asset(
        self,
        name: str,
        asset_type: AssetType,
        underlying_assets: List[str],
        collateral_ratio: float,
        initial_price: float
    ) -> SyntheticAsset:
        asset_id = f"synth_{len(self.assets) + 1}"
        new_asset = SyntheticAsset(
            id=asset_id,
            name=name,
            asset_type=asset_type,
            underlying_assets=underlying_assets,
            collateral_ratio=collateral_ratio,
            issuance_date=datetime.now(),
            current_price=initial_price
        )
        self.assets[asset_id] = new_asset
        return new_asset
    
    def update_market_condition(self):
        conditions = [MarketCondition.BULL, MarketCondition.BEAR, MarketCondition.STAGNANT]
        weights = [0.4, 0.3, 0.3]  # Slightly biased towards bull market
        self.market_condition = random.choices(conditions, weights=weights, k=1)[0]
        self.last_update = datetime.now()
    
    def calculate_price_change(self, base_volatility: float) -> float:
        volatility_multiplier = {
            MarketCondition.BULL: 0.8,
            MarketCondition.BEAR: 1.5,
            MarketCondition.STAGNANT: 0.3
        }[self.market_condition]
        
        # Random walk with market condition influence
        change = random.gauss(0, base_volatility * volatility_multiplier)
        return change
    
    def update_asset_prices(self):
        self.update_market_condition()
        current_time = datetime.now()
        
        for asset in self.assets.values():
            base_volatility = 0.02  # Base 2% daily volatility
            if asset.asset_type == AssetType.CRYPTO:
                base_volatility = 0.05
            elif asset.asset_type == AssetType.COMMODITY:
                base_volatility = 0.03
            
            price_change = self.calculate_price_change(base_volatility)
            new_price = asset.current_price * (1 + price_change)
            
            # Ensure price doesn't go negative
            asset.current_price = max(0.01, new_price)
            asset.price_history[current_time] = asset.current_price
    
    def get_asset_price_history(self, asset_id: str, time_window: Optional[timedelta] = None) -> Dict[datetime, float]:
        if asset_id not in self.assets:
            raise ValueError(f"Asset {asset_id} not found")
        
        asset = self.assets[asset_id]
        if time_window is None:
            return asset.price_history
        
        cutoff = datetime.now() - time_window
        return {t: p for t, p in asset.price_history.items() if t >= cutoff}
    
    def simulate(self, days: int, updates_per_day: int = 1):
        interval = timedelta(days=1/updates_per_day)
        end_time = datetime.now() + timedelta(days=days)
        
        while datetime.now() < end_time:
            self.update_asset_prices()
            time.sleep(0.1)  # Simulate time passing

def main():
    market = SyntheticAssetMarket()
    
    # Issue some synthetic assets
    synth_stock = market.issue_asset(
        name="Synthetic Tech Stock",
        asset_type=AssetType.STOCK,
        underlying_assets=["AAPL", "MSFT", "GOOGL"],
        collateral_ratio=1.5,
        initial_price=100.0
    )
    
    synth_crypto = market.issue_asset(
        name="Synthetic Crypto Index",
        asset_type=AssetType.CRYPTO,
        underlying_assets=["BTC", "ETH", "SOL"],
        collateral_ratio=2.0,
        initial_price=50.0
    )
    
    # Simulate 30 days of market activity with daily updates
    print("Starting simulation...")
    market.simulate(days=30, updates_per_day=1)
    
    # Display results
    print("\nSimulation complete. Final prices:")
    for asset_id, asset in market.assets.items():
        print(f"{asset.name}: ${asset.current_price:.2f}")
        
        # Show price history for the last 7 days
        history = market.get_asset_price_history(asset_id, timedelta(days=7))
        print("Last 7 days price history:")
        for date, price in sorted(history.items()):
            print(f"  {date.strftime('%Y-%m-%d')}: ${price:.2f}")

if __name__ == "__main__":
    main()
```
