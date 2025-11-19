"""
Generated Code Metadata:
========================
Original URL: https://learnatcheap.com
Prompt: Write a code snippet that implements a trading algorithm based on the "Order Flow/Market Profile Trader Dale – Order Flow Pack" course content.
Generated: DETERMINISTIC_e3e98972efb94fc1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Optional, Tuple, Dict, List

class OrderFlowTrader:
    """
    Implements a trading algorithm based on Order Flow and Market Profile concepts.
    Key features:
        - Volume Profile Analysis
        - Order Flow Imbalance Detection
        - Market Profile (Value Area, POC)
    """
    
    def __init__(self, tick_data: pd.DataFrame, tick_size: float = 0.25, volume_threshold: int = 1000):
        """
        Initialize the OrderFlowTrader with market data.
        
        Args:
            tick_data: DataFrame containing tick data with columns ['price', 'volume', 'bid', 'ask']
            tick_size: Minimum price movement increment
            volume_threshold: Minimum volume to consider for significant levels
        """
        self.tick_data = tick_data
        self.tick_size = tick_size
        self.volume_threshold = volume_threshold
        self._validate_input_data()
        
        # Preprocess data
        self.volume_profile = self._calculate_volume_profile()
        self.value_area, self.poc = self._calculate_value_area_and_poc()
        self.order_flow_imbalance = self._calculate_order_flow_imbalance()
    
    def _validate_input_data(self) -> None:
        """Validate input data structure and contents."""
        required_columns = {'price', 'volume', 'bid', 'ask'}
        if not required_columns.issubset(self.tick_data.columns):
            raise ValueError(f"Input data must contain columns: {required_columns}")
        if len(self.tick_data) == 0:
            raise ValueError("Input data cannot be empty")
    
    def _calculate_volume_profile(self) -> pd.DataFrame:
        """Calculate volume at each price level."""
        volume_profile = self.tick_data.groupby('price')['volume'].sum().reset_index()
        volume_profile.columns = ['price', 'total_volume']
        return volume_profile.sort_values('price')
    
    def _calculate_value_area_and_poc(self) -> Tuple[Tuple[float, float], float]:
        """
        Calculate Value Area (70% of volume) and Point of Control (POC).
        
        Returns:
            ((value_area_low, value_area_high), poc_price)
        """
        sorted_profile = self.volume_profile.sort_values('total_volume', ascending=False)
        total_volume = sorted_profile['total_volume'].sum()
        
        # Calculate POC (price with highest volume)
        poc = sorted_profile.iloc[0]['price']
        
        # Calculate Value Area (70% of volume around POC)
        cumulative_volume = 0
        value_area_prices = []
        
        for _, row in sorted_profile.iterrows():
            if cumulative_volume < 0.7 * total_volume:
                value_area_prices.append(row['price'])
                cumulative_volume += row['total_volume']
            else:
                break
        
        value_area_low = min(value_area_prices)
        value_area_high = max(value_area_prices)
        
        return (value_area_low, value_area_high), poc
    
    def _calculate_order_flow_imbalance(self) -> pd.DataFrame:
        """
        Calculate order flow imbalance at each price level.
        
        Returns:
            DataFrame with columns ['price', 'bid_volume', 'ask_volume', 'imbalance']
        """
        bid_mask = self.tick_data['price'] <= self.tick_data['bid']
        ask_mask = self.tick_data['price'] >= self.tick_data['ask']
        
        bid_volume = self.tick_data[bid_mask].groupby('price')['volume'].sum()
        ask_volume = self.tick_data[ask_mask].groupby('price')['volume'].sum()
        
        imbalance = pd.DataFrame({
            'bid_volume': bid_volume,
            'ask_volume': ask_volume
        }).fillna(0)
        
        imbalance['imbalance'] = imbalance['bid_volume'] - imbalance['ask_volume']
        return imbalance.reset_index()
    
    def find_significant_levels(self) -> Dict[str, List[float]]:
        """
        Identify significant support/resistance levels based on volume and order flow.
        
        Returns:
            Dictionary with 'support' and 'resistance' keys containing price levels
        """
        # Find high volume nodes
        high_volume_nodes = self.volume_profile[
            self.volume_profile['total_volume'] > self.volume_threshold
        ]['price'].values
        
        # Find order flow imbalance extremes
        significant_imbalance = self.order_flow_imbalance[
            abs(self.order_flow_imbalance['imbalance']) > self.volume_threshold
        ]
        
        support = []
        resistance = []
        
        for price in high_volume_nodes:
            # Check if price is in value area
            in_value_area = (self.value_area[0] <= price <= self.value_area[1])
            
            # Get imbalance at this price
            imbalance = self.order_flow_imbalance[
                self.order_flow_imbalance['price'] == price
            ]['imbalance'].values
            
            if len(imbalance) > 0:
                if imbalance[0] > 0 and not in_value_area:
                    support.append(price)
                elif imbalance[0] < 0 and not in_value_area:
                    resistance.append(price)
        
        return {
            'support': sorted(support),
            'resistance': sorted(resistance, reverse=True)
        }
    
    def generate_signals(self) -> pd.DataFrame:
        """
        Generate trading signals based on order flow and market profile analysis.
        
        Returns:
            DataFrame with signals: 1 (buy), -1 (sell), 0 (no signal)
        """
        signals = pd.DataFrame(index=self.tick_data.index, columns=['signal'])
        signals['signal'] = 0
        
        significant_levels = self.find_significant_levels()
        current_price = self.tick_data['price'].iloc[-1]
        
        # Check for breakout above resistance with volume confirmation
        for level in significant_levels['resistance']:
            if (current_price > level and 
                self.tick_data['price'].iloc[-1] > self.tick_data['price'].iloc[-2] and
                self.tick_data['volume'].iloc[-1] > self.tick_data['volume'].rolling(5).mean().iloc[-1]):
                signals['signal'].iloc[-1] = 1  # Buy signal
        
        # Check for breakdown below support with volume confirmation
        for level in significant_levels['support']:
            if (current_price < level and 
                self.tick_data['price'].iloc[-1] < self.tick_data['price'].iloc[-2] and
                self.tick_data['volume'].iloc[-1] > self.tick_data['volume'].rolling(5).mean().iloc[-1]):
                signals['signal'].iloc[-1] = -1  # Sell signal
        
        return signals

# Example usage
if __name__ == "__main__":
    # Sample tick data (in a real scenario, this would come from a data feed)
    data = {
        'price': [100.0, 100.25, 100.5, 100.25, 100.0, 99.75, 100.0, 100.25],
        'volume': [500, 800, 1200, 600, 400, 1500, 700, 900],
        'bid': [99.75, 100.0, 100.25, 100.0, 99.75, 99.5, 99.75, 100.0],
        'ask': [100.25, 100.5, 100.75, 100.5, 100.25, 100.0, 100.25, 100.5]
    }
    tick_df = pd.DataFrame(data)
    
    # Initialize and run strategy
    trader = OrderFlowTrader(tick_df)
    signals = trader.generate_signals()
    
    print("Signals Generated:")
    print(signals)
```
