"""
Generated Code Metadata:
========================
Original URL: https://app.extra-fl.io
Prompt: Generate code to simulate leveraged yield farming strategies using Extra Finance's yield farming simulation tool, incorporating risk analysis and liquidation thresholds.
Generated: DETERMINISTIC_76f71912d2c70bff
Batch ID: 20250612_154131
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
from typing import Dict, Tuple, Optional, List
from dataclasses import dataclass
from enum import Enum

class AssetType(Enum):
    STABLE = "STABLE"
    VOLATILE = "VOLATILE"

@dataclass
class Asset:
    symbol: str
    price: float
    volatility: float
    type: AssetType
    apy: float

@dataclass
class Position:
    asset: Asset
    amount: float
    is_collateral: bool

@dataclass
class SimulationResult:
    total_value: float
    liquidation_events: int
    returns: List[float]
    max_drawdown: float

class YieldFarmingSimulator:
    """
    Simulates leveraged yield farming strategies with risk analysis.
    """
    
    def __init__(self, assets: Dict[str, Asset], liquidation_threshold: float = 0.8):
        """
        Initialize the simulator with assets and liquidation threshold.
        
        Args:
            assets: Dictionary of available assets (symbol: Asset)
            liquidation_threshold: Collateral ratio threshold for liquidation (0-1)
        """
        self.assets = assets
        self.liquidation_threshold = liquidation_threshold
        self.positions = []
        self.historical_prices = {}
        
    def add_position(self, asset_symbol: str, amount: float, is_collateral: bool = False) -> None:
        """
        Add a position to the simulation.
        
        Args:
            asset_symbol: Symbol of the asset
            amount: Amount of the asset
            is_collateral: Whether this position is used as collateral
        """
        if asset_symbol not in self.assets:
            raise ValueError(f"Asset {asset_symbol} not found")
            
        asset = self.assets[asset_symbol]
        self.positions.append(Position(asset=asset, amount=amount, is_collateral=is_collateral))
        
    def _calculate_collateral_ratio(self, current_prices: Dict[str, float]) -> float:
        """
        Calculate current collateral ratio.
        
        Args:
            current_prices: Current prices of all assets
            
        Returns:
            Collateral ratio (collateral value / debt value)
        """
        collateral_value = 0.0
        debt_value = 0.0
        
        for position in self.positions:
            current_price = current_prices[position.asset.symbol]
            position_value = position.amount * current_price
            
            if position.is_collateral:
                collateral_value += position_value
            else:
                debt_value += position_value
                
        if debt_value == 0:
            return float('inf')
            
        return collateral_value / debt_value
    
    def _simulate_price_movement(self, days: int) -> Dict[str, List[float]]:
        """
        Simulate price movements for all assets using geometric Brownian motion.
        
        Args:
            days: Number of days to simulate
            
        Returns:
            Dictionary of price paths (symbol: list of prices)
        """
        price_paths = {}
        dt = 1 / 365  # Daily time step
        
        for symbol, asset in self.assets.items():
            prices = [asset.price]
            for _ in range(1, days):
                drift = (asset.apy - 0.5 * asset.volatility**2) * dt
                shock = asset.volatility * np.random.normal(0, np.sqrt(dt))
                new_price = prices[-1] * np.exp(drift + shock)
                prices.append(new_price)
            price_paths[symbol] = prices
            
        return price_paths
    
    def _calculate_daily_returns(self, price_paths: Dict[str, List[float]]) -> List[float]:
        """
        Calculate daily portfolio returns based on price movements.
        
        Args:
            price_paths: Simulated price paths for all assets
            
        Returns:
            List of daily returns
        """
        daily_values = []
        days = len(next(iter(price_paths.values())))
        
        for day in range(days):
            current_prices = {symbol: prices[day] for symbol, prices in price_paths.items()}
            total_value = 0.0
            
            for position in self.positions:
                current_price = current_prices[position.asset.symbol]
                total_value += position.amount * current_price
                
            daily_values.append(total_value)
            
        returns = []
        for i in range(1, len(daily_values)):
            returns.append((daily_values[i] - daily_values[i-1]) / daily_values[i-1])
            
        return returns
    
    def run_simulation(self, days: int = 365, simulations: int = 1000) -> SimulationResult:
        """
        Run Monte Carlo simulation of the yield farming strategy.
        
        Args:
            days: Number of days to simulate
            simulations: Number of simulation runs
            
        Returns:
            SimulationResult containing aggregated statistics
        """
        all_returns = []
        liquidation_counts = []
        final_values = []
        max_drawdowns = []
        
        for _ in range(simulations):
            price_paths = self._simulate_price_movement(days)
            returns = self._calculate_daily_returns(price_paths)
            all_returns.extend(returns)
            
            # Track liquidation events
            liquidation_events = 0
            for day in range(days):
                current_prices = {symbol: prices[day] for symbol, prices in price_paths.items()}
                ratio = self._calculate_collateral_ratio(current_prices)
                if ratio < self.liquidation_threshold:
                    liquidation_events += 1
            liquidation_counts.append(liquidation_events)
            
            # Calculate final value and max drawdown
            final_price = {symbol: prices[-1] for symbol, prices in price_paths.items()}
            final_value = sum(pos.amount * final_price[pos.asset.symbol] for pos in self.positions)
            final_values.append(final_value)
            
            # Calculate max drawdown
            daily_values = [sum(pos.amount * price_paths[pos.asset.symbol][day] 
                              for pos in self.positions) 
                          for day in range(days)]
            peak = daily_values[0]
            max_dd = 0.0
            for value in daily_values:
                if value > peak:
                    peak = value
                dd = (peak - value) / peak
                if dd > max_dd:
                    max_dd = dd
            max_drawdowns.append(max_dd)
            
        avg_final_value = np.mean(final_values)
        avg_liquidation_events = np.mean(liquidation_counts)
        avg_max_drawdown = np.mean(max_drawdowns)
        
        return SimulationResult(
            total_value=avg_final_value,
            liquidation_events=avg_liquidation_events,
            returns=all_returns,
            max_drawdown=avg_max_drawdown
        )

def example_usage():
    # Define assets
    assets = {
        "USDC": Asset(symbol="USDC", price=1.0, volatility=0.01, type=AssetType.STABLE, apy=0.05),
        "ETH": Asset(symbol="ETH", price=3000, volatility=0.5, type=AssetType.VOLATILE, apy=0.15),
        "WBTC": Asset(symbol="WBTC", price=40000, volatility=0.4, type=AssetType.VOLATILE, apy=0.12)
    }
    
    # Initialize simulator
    simulator = YieldFarmingSimulator(assets, liquidation_threshold=1.5)
    
    # Add positions (collateral and debt)
    simulator.add_position("USDC", 10000, is_collateral=True)
    simulator.add_position("ETH", 5)  # Borrowed ETH
    
    # Run simulation
    result = simulator.run_simulation(days=90, simulations=1000)
    
    # Print results
    print(f"Average Portfolio Value: ${result.total_value:,.2f}")
    print(f"Average Liquidation Events: {result.liquidation_events:.2f}")
    print(f"Average Max Drawdown: {result.max_drawdown:.2%}")
    print(f"Average Daily Return: {np.mean(result.returns):.4%}")

if __name__ == "__main__":
    example_usage()
```
