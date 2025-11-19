"""
Generated Code Metadata:
========================
Original URL: https://micmarktrade.com
Prompt: Generate code to calculate trading fees and display transparent pricing for forex and CFD trades, referencing MIC markets' competitive pricing model.
Generated: DETERMINISTIC_9809ad7263dfa9b1
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import decimal
from enum import Enum
from typing import Dict, Optional, Union

# Constants for fee calculation
DEFAULT_COMMISSION_RATE = decimal.Decimal('0.0002')  # 0.02% commission
DEFAULT_SPREAD_MARKUP = decimal.Decimal('0.0001')    # 1 pip markup
MINIMUM_COMMISSION = decimal.Decimal('1.00')         # $1 minimum commission
USD_CONVERSION_RATES = {
    'EUR': decimal.Decimal('1.08'),
    'GBP': decimal.Decimal('1.27'),
    'JPY': decimal.Decimal('0.0067'),
    'AUD': decimal.Decimal('0.66'),
    'CAD': decimal.Decimal('0.74'),
}

class InstrumentType(Enum):
    FOREX = "Forex"
    CFD = "CFD"

class PricingModel:
    """Calculates trading fees based on MIC markets' competitive pricing model."""
    
    def __init__(
        self,
        commission_rate: Optional[decimal.Decimal] = None,
        spread_markup: Optional[decimal.Decimal] = None,
        minimum_commission: Optional[decimal.Decimal] = None
    ):
        """
        Initialize pricing model with custom rates or defaults.
        
        Args:
            commission_rate: Commission rate per trade (default: 0.02%)
            spread_markup: Spread markup in pips (default: 1 pip)
            minimum_commission: Minimum commission per trade (default: $1.00)
        """
        self.commission_rate = commission_rate or DEFAULT_COMMISSION_RATE
        self.spread_markup = spread_markup or DEFAULT_SPREAD_MARKUP
        self.minimum_commission = minimum_commission or MINIMUM_COMMISSION
    
    def calculate_fees(
        self,
        instrument_type: InstrumentType,
        symbol: str,
        notional_amount: decimal.Decimal,
        base_currency: str,
        current_price: decimal.Decimal,
        lot_size: int = 100000
    ) -> Dict[str, Union[decimal.Decimal, str]]:
        """
        Calculate all fees for a trade.
        
        Args:
            instrument_type: Type of instrument (Forex or CFD)
            symbol: Trading symbol (e.g., EUR/USD)
            notional_amount: Trade amount in base currency
            base_currency: Currency of the trade (e.g., USD)
            current_price: Current market price
            lot_size: Standard lot size (default: 100,000)
            
        Returns:
            Dictionary containing all fee components and total cost
        """
        if not isinstance(notional_amount, decimal.Decimal):
            notional_amount = decimal.Decimal(str(notional_amount))
        if not isinstance(current_price, decimal.Decimal):
            current_price = decimal.Decimal(str(current_price))
            
        # Calculate spread cost
        spread_cost = self._calculate_spread_cost(
            instrument_type, 
            notional_amount, 
            current_price
        )
        
        # Calculate commission
        commission = self._calculate_commission(
            notional_amount, 
            base_currency
        )
        
        # Convert to USD for display if needed
        total_cost = spread_cost + commission
        total_cost_usd = self._convert_to_usd(total_cost, base_currency)
        
        return {
            "instrument_type": instrument_type.value,
            "symbol": symbol,
            "notional_amount": notional_amount,
            "base_currency": base_currency,
            "spread_cost": spread_cost,
            "commission": commission,
            "total_cost": total_cost,
            "total_cost_usd": total_cost_usd,
            "pricing_model": "MIC Markets Competitive Pricing"
        }
    
    def _calculate_spread_cost(
        self,
        instrument_type: InstrumentType,
        notional_amount: decimal.Decimal,
        current_price: decimal.Decimal
    ) -> decimal.Decimal:
        """Calculate spread cost based on instrument type."""
        if instrument_type == InstrumentType.FOREX:
            # For Forex: spread cost = notional * spread markup
            return notional_amount * self.spread_markup
        else:
            # For CFDs: spread cost = notional * spread markup / current_price
            return (notional_amount * self.spread_markup) / current_price
    
    def _calculate_commission(
        self,
        notional_amount: decimal.Decimal,
        base_currency: str
    ) -> decimal.Decimal:
        """Calculate commission with minimum threshold."""
        commission = notional_amount * self.commission_rate
        if commission < self.minimum_commission:
            return self.minimum_commission
        return commission
    
    def _convert_to_usd(
        self,
        amount: decimal.Decimal,
        currency: str
    ) -> decimal.Decimal:
        """Convert amount to USD using predefined rates."""
        if currency == 'USD':
            return amount
        rate = USD_CONVERSION_RATES.get(currency, decimal.Decimal('1.0'))
        return amount * rate
    
    def display_pricing(
        self,
        fee_details: Dict[str, Union[decimal.Decimal, str]]
    ) -> str:
        """Generate a human-readable pricing breakdown."""
        return (
            f"\n--- Trade Pricing Breakdown ---\n"
            f"Instrument: {fee_details['instrument_type']} ({fee_details['symbol']})\n"
            f"Notional Amount: {fee_details['notional_amount']:.2f} {fee_details['base_currency']}\n"
            f"Spread Cost: {fee_details['spread_cost']:.6f} {fee_details['base_currency']}\n"
            f"Commission: {fee_details['commission']:.2f} {fee_details['base_currency']}\n"
            f"Total Cost: {fee_details['total_cost']:.2f} {fee_details['base_currency']}\n"
            f"Total Cost (USD): {fee_details['total_cost_usd']:.2f} USD\n"
            f"Pricing Model: {fee_details['pricing_model']}\n"
            "-------------------------------"
        )

# Example usage
if __name__ == "__main__":
    # Initialize pricing model with default rates
    pricing = PricingModel()
    
    # Example 1: Forex trade
    forex_fees = pricing.calculate_fees(
        instrument_type=InstrumentType.FOREX,
        symbol="EUR/USD",
        notional_amount=decimal.Decimal("100000"),  # 1 standard lot
        base_currency="USD",
        current_price=decimal.Decimal("1.0800")
    )
    print(pricing.display_pricing(forex_fees))
    
    # Example 2: CFD trade
    cfd_fees = pricing.calculate_fees(
        instrument_type=InstrumentType.CFD,
        symbol="XAU/USD",
        notional_amount=decimal.Decimal("100"),  # 100 ounces of gold
        base_currency="USD",
        current_price=decimal.Decimal("1800.00")
    )
    print(pricing.display_pricing(cfd_fees))
```
