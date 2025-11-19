"""
Generated Code Metadata:
========================
Original URL: https://digitalwealthtraders.com
Prompt: Generate code to calculate leverage and spreads for Forex and CFD trading, incorporating the trading conditions described on Digitalwealthtraders.
Generated: DETERMINISTIC_fb89b5331ec926bd
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Dict, List, Optional, Tuple

class InstrumentType(Enum):
    """Enum representing different types of trading instruments."""
    FOREX_MAJOR = "Forex Major"
    FOREX_MINOR = "Forex Minor"
    FOREX_EXOTIC = "Forex Exotic"
    CFD_INDICES = "CFD Indices"
    CFD_COMMODITIES = "CFD Commodities"
    CFD_CRYPTO = "CFD Crypto"
    CFD_STOCKS = "CFD Stocks"

class TradingConditions:
    """Class to store trading conditions for different instrument types."""
    
    def __init__(self):
        # Initialize default trading conditions
        self.conditions: Dict[InstrumentType, Dict[str, float]] = {
            InstrumentType.FOREX_MAJOR: {
                "leverage": 500,
                "spread": 0.8,
                "min_lot_size": 0.01,
                "max_lot_size": 100
            },
            InstrumentType.FOREX_MINOR: {
                "leverage": 500,
                "spread": 1.2,
                "min_lot_size": 0.01,
                "max_lot_size": 50
            },
            InstrumentType.FOREX_EXOTIC: {
                "leverage": 200,
                "spread": 2.5,
                "min_lot_size": 0.01,
                "max_lot_size": 20
            },
            InstrumentType.CFD_INDICES: {
                "leverage": 100,
                "spread": 1.0,
                "min_lot_size": 0.1,
                "max_lot_size": 50
            },
            InstrumentType.CFD_COMMODITIES: {
                "leverage": 100,
                "spread": 1.5,
                "min_lot_size": 0.1,
                "max_lot_size": 30
            },
            InstrumentType.CFD_CRYPTO: {
                "leverage": 25,
                "spread": 10.0,
                "min_lot_size": 0.01,
                "max_lot_size": 5
            },
            InstrumentType.CFD_STOCKS: {
                "leverage": 10,
                "spread": 5.0,
                "min_lot_size": 0.1,
                "max_lot_size": 10
            }
        }
    
    def get_conditions(self, instrument_type: InstrumentType) -> Dict[str, float]:
        """Get trading conditions for a specific instrument type.
        
        Args:
            instrument_type: The type of instrument to get conditions for.
            
        Returns:
            Dictionary containing trading conditions.
            
        Raises:
            ValueError: If instrument type is not found.
        """
        if instrument_type not in self.conditions:
            raise ValueError(f"Unknown instrument type: {instrument_type}")
        return self.conditions[instrument_type]

class TradingCalculator:
    """Class to perform trading calculations based on trading conditions."""
    
    def __init__(self, trading_conditions: TradingConditions):
        """Initialize with trading conditions."""
        self.trading_conditions = trading_conditions
    
    def calculate_margin_requirement(
        self,
        instrument_type: InstrumentType,
        lot_size: float,
        contract_size: float = 100000,
        current_price: Optional[float] = None
    ) -> float:
        """Calculate margin requirement for a trade.
        
        Args:
            instrument_type: Type of instrument being traded.
            lot_size: Size of the trade in lots.
            contract_size: Size of one lot (default 100,000 for Forex).
            current_price: Current price of the instrument (required for non-Forex).
            
        Returns:
            Margin requirement in account currency.
            
        Raises:
            ValueError: If invalid parameters are provided.
        """
        conditions = self.trading_conditions.get_conditions(instrument_type)
        
        if lot_size < conditions["min_lot_size"] or lot_size > conditions["max_lot_size"]:
            raise ValueError(f"Lot size must be between {conditions['min_lot_size']} and {conditions['max_lot_size']}")
        
        leverage = conditions["leverage"]
        
        if instrument_type.value.startswith("Forex"):
            margin = (lot_size * contract_size) / leverage
        else:
            if current_price is None:
                raise ValueError("Current price is required for non-Forex instruments")
            margin = (lot_size * contract_size * current_price) / leverage
        
        return round(margin, 2)
    
    def calculate_spread_cost(
        self,
        instrument_type: InstrumentType,
        lot_size: float,
        contract_size: float = 100000,
        pip_value: Optional[float] = None
    ) -> float:
        """Calculate the cost of the spread for a trade.
        
        Args:
            instrument_type: Type of instrument being traded.
            lot_size: Size of the trade in lots.
            contract_size: Size of one lot (default 100,000 for Forex).
            pip_value: Value of one pip in account currency (optional).
            
        Returns:
            Spread cost in account currency.
            
        Raises:
            ValueError: If invalid parameters are provided.
        """
        conditions = self.trading_conditions.get_conditions(instrument_type)
        
        if lot_size < conditions["min_lot_size"] or lot_size > conditions["max_lot_size"]:
            raise ValueError(f"Lot size must be between {conditions['min_lot_size']} and {conditions['max_lot_size']}")
        
        spread_in_pips = conditions["spread"]
        
        if pip_value is None:
            # Default pip value calculation for Forex (assuming quote currency is account currency)
            pip_value = 10 if instrument_type.value.startswith("Forex") else 1
        
        spread_cost = spread_in_pips * pip_value * lot_size
        return round(spread_cost, 2)
    
    def calculate_effective_leverage(
        self,
        instrument_type: InstrumentType,
        account_balance: float,
        lot_size: float,
        contract_size: float = 100000,
        current_price: Optional[float] = None
    ) -> float:
        """Calculate the effective leverage of a position.
        
        Args:
            instrument_type: Type of instrument being traded.
            account_balance: Current account balance.
            lot_size: Size of the trade in lots.
            contract_size: Size of one lot (default 100,000 for Forex).
            current_price: Current price of the instrument (required for non-Forex).
            
        Returns:
            Effective leverage ratio.
            
        Raises:
            ValueError: If invalid parameters are provided.
        """
        if account_balance <= 0:
            raise ValueError("Account balance must be positive")
        
        position_value = self.calculate_position_value(
            instrument_type, lot_size, contract_size, current_price
        )
        margin = self.calculate_margin_requirement(
            instrument_type, lot_size, contract_size, current_price
        )
        
        if margin == 0:
            return 0.0
        
        effective_leverage = position_value / margin
        return round(effective_leverage, 2)
    
    def calculate_position_value(
        self,
        instrument_type: InstrumentType,
        lot_size: float,
        contract_size: float = 100000,
        current_price: Optional[float] = None
    ) -> float:
        """Calculate the total value of a position.
        
        Args:
            instrument_type: Type of instrument being traded.
            lot_size: Size of the trade in lots.
            contract_size: Size of one lot (default 100,000 for Forex).
            current_price: Current price of the instrument (required for non-Forex).
            
        Returns:
            Position value in account currency.
            
        Raises:
            ValueError: If invalid parameters are provided.
        """
        if instrument_type.value.startswith("Forex"):
            return lot_size * contract_size
        else:
            if current_price is None:
                raise ValueError("Current price is required for non-Forex instruments")
            return lot_size * contract_size * current_price

# Example usage
if __name__ == "__main__":
    try:
        # Initialize trading conditions and calculator
        conditions = TradingConditions()
        calculator = TradingCalculator(conditions)
        
        # Example 1: Forex Major pair
        instrument = InstrumentType.FOREX_MAJOR
        lot_size = 1.0
        
        margin = calculator.calculate_margin_requirement(instrument, lot_size)
        spread_cost = calculator.calculate_spread_cost(instrument, lot_size)
        leverage = calculator.calculate_effective_leverage(instrument, 10000, lot_size)
        
        print(f"Forex Major (1 lot):")
        print(f"Margin required: ${margin}")
        print(f"Spread cost: ${spread_cost}")
        print(f"Effective leverage: {leverage}:1")
        
        # Example 2: CFD Stock
        instrument = InstrumentType.CFD_STOCKS
        lot_size = 5.0
        current_price = 150.50  # Example stock price
        
        margin = calculator.calculate_margin_requirement(instrument, lot_size, 100, current_price)
        spread
