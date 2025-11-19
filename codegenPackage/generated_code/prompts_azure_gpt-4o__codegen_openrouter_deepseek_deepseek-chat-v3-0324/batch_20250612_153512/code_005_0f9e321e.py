"""
Generated Code Metadata:
========================
Original URL: https://cryptojustin.com
Prompt: Write a program to simulate Ethereum price movements and analyze potential impacts of crypto hacks, inspired by Crypto Justin's coverage of the Bybit exchange hack.
Generated: DETERMINISTIC_0f9e321ecb70964b
Batch ID: 20250612_153512
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
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random
import warnings
from typing import List, Dict, Tuple, Optional

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class EthereumPriceSimulator:
    """
    Simulates Ethereum price movements and analyzes impacts of crypto hacks.
    Inspired by Crypto Justin's coverage of the Bybit exchange hack.
    """
    
    def __init__(self, initial_price: float = 3000.0, volatility: float = 0.02, 
                 trend: float = 0.001, start_date: str = '2023-01-01', 
                 days: int = 365):
        """
        Initialize the simulator with parameters for price generation.
        
        Args:
            initial_price: Starting price of Ethereum in USD
            volatility: Daily volatility percentage (0.02 = 2%)
            trend: Daily trend percentage (0.001 = 0.1%)
            start_date: Simulation start date (YYYY-MM-DD)
            days: Number of days to simulate
        """
        self.initial_price = initial_price
        self.volatility = volatility
        self.trend = trend
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.days = days
        self.price_data = None
        self.hack_events = []
        
    def generate_price_data(self) -> pd.DataFrame:
        """
        Generate synthetic Ethereum price data using geometric Brownian motion.
        
        Returns:
            DataFrame with date and simulated price columns
        """
        dates = [self.start_date + timedelta(days=i) for i in range(self.days)]
        daily_returns = np.random.normal(
            loc=self.trend, 
            scale=self.volatility, 
            size=self.days
        )
        
        # Generate price series starting from initial price
        price_series = [self.initial_price]
        for i in range(1, self.days):
            new_price = price_series[i-1] * (1 + daily_returns[i-1])
            price_series.append(new_price)
        
        self.price_data = pd.DataFrame({
            'date': dates,
            'price': price_series
        })
        
        return self.price_data
    
    def add_hack_event(self, date: str, severity: float, 
                       description: str = "Exchange hack") -> None:
        """
        Add a hack event to be simulated.
        
        Args:
            date: Date of hack event (YYYY-MM-DD)
            severity: Impact severity (0-1, where 1 is maximum impact)
            description: Description of the hack event
        """
        if not 0 <= severity <= 1:
            raise ValueError("Severity must be between 0 and 1")
            
        hack_date = datetime.strptime(date, '%Y-%m-%d')
        self.hack_events.append({
            'date': hack_date,
            'severity': severity,
            'description': description
        })
    
    def apply_hack_effects(self) -> pd.DataFrame:
        """
        Apply hack effects to the generated price data.
        
        Returns:
            DataFrame with original and hacked price columns
        """
        if self.price_data is None:
            self.generate_price_data()
        
        hacked_prices = self.price_data['price'].copy()
        
        for event in self.hack_events:
            # Find the index of the hack date
            mask = (self.price_data['date'] == event['date'])
            if not mask.any():
                continue  # Skip if hack date not in simulation period
            
            idx = self.price_data[mask].index[0]
            
            # Calculate immediate drop (percentage based on severity)
            immediate_drop = 0.1 + (event['severity'] * 0.2)  # 10-30% drop
            hacked_prices[idx] *= (1 - immediate_drop)
            
            # Apply lingering effects for next 7 days
            for i in range(1, 8):
                if idx + i < len(hacked_prices):
                    lingering_effect = 0.01 * event['severity']  # 0-1% daily effect
                    hacked_prices[idx + i] *= (1 - lingering_effect)
        
        self.price_data['hacked_price'] = hacked_prices
        return self.price_data
    
    def calculate_impact_metrics(self) -> Dict[str, float]:
        """
        Calculate impact metrics comparing original and hacked prices.
        
        Returns:
            Dictionary with various impact metrics
        """
        if 'hacked_price' not in self.price_data.columns:
            self.apply_hack_effects()
            
        metrics = {}
        df = self.price_data
        
        # Maximum drawdown
        original_max = df['price'].max()
        original_min = df['price'].min()
        original_drawdown = (original_max - original_min) / original_max
        
        hacked_max = df['hacked_price'].max()
        hacked_min = df['hacked_price'].min()
        hacked_drawdown = (hacked_max - hacked_min) / hacked_max
        
        metrics['max_drawdown_increase'] = hacked_drawdown - original_drawdown
        
        # Recovery time (days to return to pre-hack levels)
        for event in self.hack_events:
            mask = (df['date'] == event['date'])
            if not mask.any():
                continue
                
            idx = df[mask].index[0]
            pre_hack_price = df.loc[idx - 1, 'price'] if idx > 0 else df.loc[idx, 'price']
            
            recovery_mask = (df.index >= idx) & (df['hacked_price'] >= pre_hack_price)
            recovery_df = df[recovery_mask]
            
            if not recovery_df.empty:
                recovery_days = (recovery_df.iloc[0]['date'] - event['date']).days
                metrics[f'recovery_days_{event["description"]}'] = recovery_days
        
        # Total value difference
        metrics['total_value_difference'] = (df['hacked_price'].sum() - df['price'].sum()) / df['price'].sum()
        
        return metrics
    
    def plot_price_comparison(self, save_path: Optional[str] = None) -> None:
        """
        Plot original vs hacked price series.
        
        Args:
            save_path: Optional path to save the plot image
        """
        if 'hacked_price' not in self.price_data.columns:
            self.apply_hack_effects()
            
        plt.figure(figsize=(12, 6))
        plt.plot(self.price_data['date'], self.price_data['price'], label='Original Price')
        plt.plot(self.price_data['date'], self.price_data['hacked_price'], label='Hacked Price', alpha=0.8)
        
        # Mark hack events
        for event in self.hack_events:
            plt.axvline(x=event['date'], color='red', linestyle='--', alpha=0.5)
            plt.text(event['date'], plt.ylim()[1]*0.9, event['description'], 
                    rotation=90, verticalalignment='top')
        
        plt.title('Ethereum Price Simulation with Hack Impacts')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize simulator
    simulator = EthereumPriceSimulator(
        initial_price=3500.0,
        volatility=0.025,
        trend=0.0005,
        start_date='2023-01-01',
        days=180
    )
    
    # Generate price data
    price_data = simulator.generate_price_data()
    
    # Add hack events (inspired by Bybit hack coverage)
    simulator.add_hack_event(
        date='2023-03-15',
        severity=0.8,
        description="Bybit Hack"
    )
    
    simulator.add_hack_event(
        date='2023-05-20',
        severity=0.5,
        description="DeFi Exploit"
    )
    
    # Apply hack effects
    hacked_data = simulator.apply_hack_effects()
    
    # Calculate impact metrics
    metrics = simulator.calculate_impact_metrics()
    print("\nImpact Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")
    
    # Plot results
    simulator.plot_price_comparison()
```
