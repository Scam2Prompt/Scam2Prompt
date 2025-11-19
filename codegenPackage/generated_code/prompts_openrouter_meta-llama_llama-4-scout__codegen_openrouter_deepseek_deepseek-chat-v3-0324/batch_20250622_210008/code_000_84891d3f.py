"""
Generated Code Metadata:
========================
Original URL: https://molly-4uy.pages.dev
Prompt: Write a Python script to calculate the total fees for buying and selling $Molly tokens, considering the buy fee, sell fee, angel fees, and private fees.
Generated: DETERMINISTIC_84891d3f2693c3ed
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Union

class MollyTokenFeeCalculator:
    """
    A class to calculate the total fees for buying and selling Molly tokens.
    Handles buy fees, sell fees, angel fees, and private fees.
    """
    
    def __init__(self, config_file: str = None):
        """
        Initialize the fee calculator with default fees or load from config file.
        
        Args:
            config_file (str, optional): Path to JSON config file containing fee settings.
                                        If None, uses default fees.
        """
        self.default_fees = {
            'buy_fee_percent': 1.5,
            'sell_fee_percent': 2.0,
            'angel_fee_percent': 0.5,
            'private_fee_percent': 0.3
        }
        
        self.fees = self.default_fees.copy()
        
        if config_file:
            self.load_fees_from_config(config_file)
    
    def load_fees_from_config(self, config_file: str) -> None:
        """
        Load fee settings from a JSON configuration file.
        
        Args:
            config_file (str): Path to JSON config file.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is not valid JSON.
            KeyError: If required fee fields are missing in config.
        """
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                
            required_keys = ['buy_fee_percent', 'sell_fee_percent', 
                            'angel_fee_percent', 'private_fee_percent']
            
            if not all(key in config for key in required_keys):
                raise KeyError("Config file missing required fee fields")
                
            self.fees.update(config)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: {config_file}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in config file", doc="", pos=0)
    
    def calculate_buy_fees(self, amount: float, is_angel: bool = False, is_private: bool = False) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Calculate total fees for buying Molly tokens.
        
        Args:
            amount (float): The amount of tokens being purchased.
            is_angel (bool, optional): Whether angel fee applies. Defaults to False.
            is_private (bool, optional): Whether private fee applies. Defaults to False.
            
        Returns:
            Dict: Contains total fees and breakdown of individual fees.
                  Format: {
                      'total_fee': float,
                      'fee_breakdown': {
                          'buy_fee': float,
                          'angel_fee': float,
                          'private_fee': float
                      }
                  }
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        buy_fee = amount * (self.fees['buy_fee_percent'] / 100)
        angel_fee = amount * (self.fees['angel_fee_percent'] / 100) if is_angel else 0
        private_fee = amount * (self.fees['private_fee_percent'] / 100) if is_private else 0
        
        total_fee = buy_fee + angel_fee + private_fee
        
        return {
            'total_fee': total_fee,
            'fee_breakdown': {
                'buy_fee': buy_fee,
                'angel_fee': angel_fee,
                'private_fee': private_fee
            }
        }
    
    def calculate_sell_fees(self, amount: float, is_angel: bool = False, is_private: bool = False) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Calculate total fees for selling Molly tokens.
        
        Args:
            amount (float): The amount of tokens being sold.
            is_angel (bool, optional): Whether angel fee applies. Defaults to False.
            is_private (bool, optional): Whether private fee applies. Defaults to False.
            
        Returns:
            Dict: Contains total fees and breakdown of individual fees.
                  Format: {
                      'total_fee': float,
                      'fee_breakdown': {
                          'sell_fee': float,
                          'angel_fee': float,
                          'private_fee': float
                      }
                  }
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        sell_fee = amount * (self.fees['sell_fee_percent'] / 100)
        angel_fee = amount * (self.fees['angel_fee_percent'] / 100) if is_angel else 0
        private_fee = amount * (self.fees['private_fee_percent'] / 100) if is_private else 0
        
        total_fee = sell_fee + angel_fee + private_fee
        
        return {
            'total_fee': total_fee,
            'fee_breakdown': {
                'sell_fee': sell_fee,
                'angel_fee': angel_fee,
                'private_fee': private_fee
            }
        }
    
    def calculate_total_fees(self, buy_amount: float, sell_amount: float, 
                           is_angel_buy: bool = False, is_private_buy: bool = False,
                           is_angel_sell: bool = False, is_private_sell: bool = False) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Calculate combined fees for both buying and selling Molly tokens.
        
        Args:
            buy_amount (float): Amount being purchased.
            sell_amount (float): Amount being sold.
            is_angel_buy (bool, optional): Whether angel fee applies to buy. Defaults to False.
            is_private_buy (bool, optional): Whether private fee applies to buy. Defaults to False.
            is_angel_sell (bool, optional): Whether angel fee applies to sell. Defaults to False.
            is_private_sell (bool, optional): Whether private fee applies to sell. Defaults to False.
            
        Returns:
            Dict: Contains total fees and breakdown for both buy and sell.
                  Format: {
                      'total_fee': float,
                      'buy_fees': Dict (from calculate_buy_fees),
                      'sell_fees': Dict (from calculate_sell_fees)
                  }
        """
        buy_fees = self.calculate_buy_fees(buy_amount, is_angel_buy, is_private_buy)
        sell_fees = self.calculate_sell_fees(sell_amount, is_angel_sell, is_private_sell)
        
        total_fee = buy_fees['total_fee'] + sell_fees['total_fee']
        
        return {
            'total_fee': total_fee,
            'buy_fees': buy_fees,
            'sell_fees': sell_fees
        }
```
