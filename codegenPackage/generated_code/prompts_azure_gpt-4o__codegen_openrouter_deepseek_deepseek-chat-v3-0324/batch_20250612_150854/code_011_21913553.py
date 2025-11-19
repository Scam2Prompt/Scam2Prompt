"""
Generated Code Metadata:
========================
Original URL: https://immediate-crest.com
Prompt: Develop code to simulate income investing strategies using dividend-paying stocks and REITs, inspired by Immediate Crest V2's educational content.
Generated: DETERMINISTIC_21913553a56f4c58
Batch ID: 20250612_150854
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
from typing import List, Dict, Tuple, Optional
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt
from enum import Enum

class AssetType(Enum):
    STOCK = "Stock"
    REIT = "REIT"

class Asset:
    def __init__(self, 
                 name: str, 
                 asset_type: AssetType, 
                 current_price: float, 
                 dividend_yield: float, 
                 dividend_frequency: int = 4,
                 dividend_growth_rate: float = 0.0,
                 price_growth_rate: float = 0.0):
        """
        Initialize an investment asset.
        
        Args:
            name: Name of the asset
            asset_type: Type of asset (Stock or REIT)
            current_price: Current price per share
            dividend_yield: Annual dividend yield (percentage)
            dividend_frequency: Number of dividend payments per year
            dividend_growth_rate: Annual dividend growth rate (percentage)
            price_growth_rate: Annual price growth rate (percentage)
        """
        self.name = name
        self.asset_type = asset_type
        self.current_price = current_price
        self.dividend_yield = dividend_yield / 100
        self.dividend_frequency = dividend_frequency
        self.dividend_growth_rate = dividend_growth_rate / 100
        self.price_growth_rate = price_growth_rate / 100
        self.purchase_date = None
        self.purchase_price = None
        
    def calculate_dividend(self, shares: float, current_date: datetime) -> float:
        """
        Calculate dividend payment for given shares at current date.
        
        Args:
            shares: Number of shares owned
            current_date: Current date for calculation
            
        Returns:
            Dividend amount
        """
        if self.purchase_date is None:
            return 0.0
            
        years_held = (current_date - self.purchase_date).days / 365.25
        current_yield = self.dividend_yield * (1 + self.dividend_growth_rate) ** years_held
        dividend_per_share = (current_yield * self.current_price) / self.dividend_frequency
        return dividend_per_share * shares
        
    def update_price(self, current_date: datetime) -> None:
        """
        Update asset price based on growth rate and time elapsed.
        
        Args:
            current_date: Current date for price update
        """
        if self.purchase_date is None:
            return
            
        years_held = (current_date - self.purchase_date).days / 365.25
        self.current_price = self.purchase_price * (1 + self.price_growth_rate) ** years_held

class Portfolio:
    def __init__(self, initial_capital: float = 10000.0):
        """
        Initialize an investment portfolio.
        
        Args:
            initial_capital: Starting investment capital
        """
        self.initial_capital = initial_capital
        self.available_cash = initial_capital
        self.assets: Dict[str, Tuple[Asset, float]] = {}  # {asset_name: (asset, shares)}
        self.transaction_history = []
        self.dividend_history = []
        self.value_history = []
        
    def add_asset(self, asset: Asset, shares: float, purchase_date: datetime) -> None:
        """
        Purchase an asset and add it to the portfolio.
        
        Args:
            asset: Asset to purchase
            shares: Number of shares to purchase
            purchase_date: Date of purchase
        """
        if asset.name in self.assets:
            raise ValueError(f"Asset {asset.name} already exists in portfolio")
            
        cost = shares * asset.current_price
        if cost > self.available_cash:
            raise ValueError("Insufficient funds for purchase")
            
        asset.purchase_date = purchase_date
        asset.purchase_price = asset.current_price
        self.assets[asset.name] = (asset, shares)
        self.available_cash -= cost
        
        self.transaction_history.append({
            'date': purchase_date,
            'type': 'BUY',
            'asset': asset.name,
            'shares': shares,
            'price': asset.current_price,
            'total': cost
        })
        
    def reinvest_dividends(self, current_date: datetime) -> None:
        """
        Reinvest all dividends received into purchasing more shares.
        
        Args:
            current_date: Current date for dividend calculation
        """
        total_dividends = 0.0
        
        for asset_name, (asset, shares) in self.assets.items():
            dividend = asset.calculate_dividend(shares, current_date)
            total_dividends += dividend
            
            if dividend > 0:
                self.dividend_history.append({
                    'date': current_date,
                    'asset': asset_name,
                    'amount': dividend,
                    'shares': shares
                })
        
        if total_dividends > 0:
            self.available_cash += total_dividends
            self._distribute_reinvestment(total_dividends, current_date)
            
    def _distribute_reinvestment(self, amount: float, current_date: datetime) -> None:
        """
        Distribute reinvestment amount proportionally across assets.
        
        Args:
            amount: Total amount to reinvest
            current_date: Current date for reinvestment
        """
        total_value = self.calculate_portfolio_value(current_date)
        
        for asset_name, (asset, shares) in self.assets.items():
            asset_value = asset.current_price * shares
            allocation = asset_value / total_value
            reinvest_amount = amount * allocation
            
            if reinvest_amount > 0:
                new_shares = reinvest_amount / asset.current_price
                self.assets[asset.name] = (asset, shares + new_shares)
                
                self.transaction_history.append({
                    'date': current_date,
                    'type': 'REINVEST',
                    'asset': asset.name,
                    'shares': new_shares,
                    'price': asset.current_price,
                    'total': reinvest_amount
                })
    
    def calculate_portfolio_value(self, current_date: datetime) -> float:
        """
        Calculate total portfolio value at given date.
        
        Args:
            current_date: Date for valuation
            
        Returns:
            Total portfolio value
        """
        total_value = self.available_cash
        
        for asset, shares in self.assets.values():
            asset.update_price(current_date)
            total_value += asset.current_price * shares
            
        return total_value
    
    def record_portfolio_value(self, current_date: datetime) -> None:
        """
        Record portfolio value at current date.
        
        Args:
            current_date: Date for recording
        """
        value = self.calculate_portfolio_value(current_date)
        self.value_history.append({
            'date': current_date,
            'value': value,
            'cash': self.available_cash
        })
        
    def generate_report(self) -> Dict:
        """
        Generate a summary report of the portfolio.
        
        Returns:
            Dictionary containing portfolio metrics
        """
        if not self.value_history:
            return {}
            
        latest = self.value_history[-1]
        start_date = self.value_history[0]['date']
        end_date = latest['date']
        
        total_dividends = sum(d['amount'] for d in self.dividend_history)
        total_return = latest['value'] - self.initial_capital
        annualized_return = (latest['value'] / self.initial_capital) ** (1 / ((end_date - start_date).days / 365.25)) - 1
        
        return {
            'start_date': start_date,
            'end_date': end_date,
            'initial_capital': self.initial_capital,
            'final_value': latest['value'],
            'total_return': total_return,
            'annualized_return': annualized_return * 100,
            'total_dividends': total_dividends,
            'cash_position': latest['cash']
        }

class Simulation:
    def __init__(self, 
                 portfolio: Portfolio,
                 start_date: datetime,
                 end_date: datetime,
                 rebalance_frequency: int = 12):
        """
        Initialize a portfolio simulation.
        
        Args:
            portfolio: Portfolio to simulate
            start_date: Simulation start date
            end_date: Simulation end date
            rebalance_frequency: Months between rebalancing (0 for no rebalancing)
        """
        self.portfolio = portfolio
        self.start_date = start_date
        self.end_date = end_date
        self.rebalance_frequency = rebalance_frequency
        
    def run(self) -> None:
        """
        Run the portfolio simulation.
        """
        current_date = self.start_date
        last_rebalance = None
        
        while current_date <= self.end_date:
            # Update asset prices
            for asset, _ in self.portfolio.assets.values():
                asset.update_price(current_date)
            
            # Record portfolio value
            self.portfolio.record_portfolio_value(current_date)
            
            # Reinvest dividends (quarterly)
            if current_date.month in [3, 6, 9, 12] and current_date.day == 1:
                self.portfolio.reinvest_dividends(current_date)
            
            # Rebalance portfolio (if enabled
