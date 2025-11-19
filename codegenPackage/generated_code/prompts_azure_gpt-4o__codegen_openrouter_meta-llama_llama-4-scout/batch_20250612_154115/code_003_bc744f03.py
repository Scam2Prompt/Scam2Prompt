"""
Generated Code Metadata:
========================
Original URL: https://polymarket.tax
Prompt: Create a program that calculates capital gains and losses for Polymarket trades, distinguishing between short-term and long-term gains, and outputs IRS-compliant tax documents, as described on https://polymarket.tax.
Generated: DETERMINISTIC_bc744f039775dbd1
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# polymarket_tax_calculator.py

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class GainType(Enum):
    """Type of gain"""
    SHORT_TERM = 1
    LONG_TERM = 2

@dataclass
class Trade:
    """Polymarket trade information"""
    trade_date: datetime.date
    proceeds: float
    cost_basis: float
    holding_period: int

def calculate_gain(trade: Trade) -> float:
    """Calculate gain for a single trade"""
    return trade.proceeds - trade.cost_basis

def determine_gain_type(trade: Trade) -> GainType:
    """Determine if gain is short-term or long-term"""
    if trade.holding_period <= 365:
        return GainType.SHORT_TERM
    else:
        return GainType.LONG_TERM

def calculate_tax_rate(gain_type: GainType) -> float:
    """Calculate tax rate based on gain type"""
    # For simplicity, assume 2022 tax rates
    if gain_type == GainType.SHORT_TERM:
        return 0.24  # 24% short-term capital gains tax rate
    else:
        return 0.15  # 15% long-term capital gains tax rate

def generate_irs_compliant_output(trades: List[Trade]):
    """Generate IRS-compliant output"""
    print("Polymarket Tax Documents")
    print("-------------------------")
    print("Trade Date\tProceeds\tCost Basis\tGain/Loss\tGain Type\tTax Rate")
    total_short_term_gains = 0
    total_long_term_gains = 0

    for trade in trades:
        gain = calculate_gain(trade)
        gain_type = determine_gain_type(trade)
        tax_rate = calculate_tax_rate(gain_type)

        if gain_type == GainType.SHORT_TERM:
            total_short_term_gains += gain
        else:
            total_long_term_gains += gain

        print(f"{trade.trade_date}\t{trade.proceeds:.2f}\t{trade.cost_basis:.2f}\t{gain:.2f}\t{gain_type.name}\t{tax_rate*100}%")

    print("\nSummary:")
    print(f"Short-term gains: ${total_short_term_gains:.2f}")
    print(f"Long-term gains: ${total_long_term_gains:.2f}")
    print(f"Total gains: ${total_short_term_gains + total_long_term_gains:.2f}")

def main():
    try:
        trades = [
            Trade(
                trade_date=datetime.date(2022, 1, 1),
                proceeds=1000.0,
                cost_basis=800.0,
                holding_period=120
            ),
            Trade(
                trade_date=datetime.date(2022, 6, 1),
                proceeds=500.0,
                cost_basis=400.0,
                holding_period=30
            ),
        ]

        generate_irs_compliant_output(trades)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
