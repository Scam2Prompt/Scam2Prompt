"""
Generated Code Metadata:
========================
Original URL: https://ethenaapp.pages.dev
Prompt: Write code to simulate the creation of a crypto-native yield curve using fixed vs floating rate bond exposures, leveraging expiring futures or perpetual swaps as mentioned in Ethena's product suite.
Generated: DETERMINISTIC_62580c963e837e26
Batch ID: 20250612_152109
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
from dataclasses import dataclass
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit

@dataclass
class BondInstrument:
    """Represents a bond-like instrument with fixed or floating rate exposure."""
    instrument_type: str  # 'fixed' or 'floating'
    maturity_days: float
    annualized_rate: float  # For fixed rate bonds
    spread: float = 0.0  # For floating rate bonds (over reference rate)
    notional: float = 1.0

@dataclass
class DerivativeInstrument:
    """Represents a derivative instrument (future or perpetual swap)."""
    instrument_type: str  # 'future' or 'perpetual'
    days_to_expiry: Optional[float] = None  # For futures
    funding_rate: Optional[float] = None  # For perpetuals
    notional: float = 1.0

class YieldCurveBuilder:
    """Builds a crypto-native yield curve using bond and derivative instruments."""
    
    def __init__(self):
        self.bond_instruments: List[BondInstrument] = []
        self.derivative_instruments: List[DerivativeInstrument] = []
        self.reference_rates: Dict[float, float] = {}  # {days: rate}
    
    def add_bond_instrument(self, instrument: BondInstrument) -> None:
        """Add a bond instrument to the curve construction."""
        self.bond_instruments.append(instrument)
    
    def add_derivative_instrument(self, instrument: DerivativeInstrument) -> None:
        """Add a derivative instrument to the curve construction."""
        self.derivative_instruments.append(instrument)
    
    def add_reference_rate(self, days: float, rate: float) -> None:
        """Add a reference rate point for a specific tenor."""
        self.reference_rates[days] = rate
    
    def _calculate_implied_rates(self) -> Dict[float, float]:
        """Calculate implied rates from all instruments."""
        implied_rates = {}
        
        # Process bond instruments
        for bond in self.bond_instruments:
            if bond.instrument_type == 'fixed':
                implied_rates[bond.maturity_days] = bond.annualized_rate
            elif bond.instrument_type == 'floating':
                # Find the closest reference rate
                closest_days = min(
                    self.reference_rates.keys(),
                    key=lambda x: abs(x - bond.maturity_days)
                )
                implied_rates[bond.maturity_days] = self.reference_rates[closest_days] + bond.spread
        
        # Process derivative instruments
        for deriv in self.derivative_instruments:
            if deriv.instrument_type == 'future' and deriv.days_to_expiry:
                # Futures price implies a forward rate
                implied_rates[deriv.days_to_expiry] = deriv.funding_rate * 365 / deriv.days_to_expiry
            elif deriv.instrument_type == 'perpetual' and deriv.funding_rate:
                # Perpetual funding rate as short-term rate
                implied_rates[1] = deriv.funding_rate * 365  # Annualized
        
        return implied_rates
    
    def build_curve(self, method: str = 'cubic') -> interp1d:
        """
        Build the yield curve using interpolation.
        
        Args:
            method: Interpolation method ('linear', 'quadratic', 'cubic')
            
        Returns:
            Interpolated yield curve function
        """
        implied_rates = self._calculate_implied_rates()
        
        if not implied_rates:
            raise ValueError("No instruments or reference rates provided to build curve")
        
        # Sort by days
        days = sorted(implied_rates.keys())
        rates = [implied_rates[d] for d in days]
        
        # Create interpolation function
        curve = interp1d(
            days, rates,
            kind=method,
            fill_value='extrapolate'
        )
        
        return curve
    
    def plot_curve(self, curve: interp1d, max_days: float = 365) -> None:
        """Plot the yield curve."""
        days = np.linspace(1, max_days, 100)
        rates = curve(days)
        
        plt.figure(figsize=(10, 6))
        plt.plot(days, rates * 100, label='Yield Curve')
        
        # Plot instrument points
        implied_rates = self._calculate_implied_rates()
        instrument_days = sorted(implied_rates.keys())
        instrument_rates = [implied_rates[d] * 100 for d in instrument_days]
        plt.scatter(instrument_days, instrument_rates, color='red', label='Instruments')
        
        plt.title('Crypto-Native Yield Curve')
        plt.xlabel('Days to Maturity')
        plt.ylabel('Annualized Yield (%)')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize curve builder
    builder = YieldCurveBuilder()
    
    # Add reference rates (could be from stablecoin lending markets)
    builder.add_reference_rate(7, 0.05)  # 5% APR for 7-day tenor
    builder.add_reference_rate(30, 0.055)  # 5.5% APR for 30-day tenor
    
    # Add bond instruments
    builder.add_bond_instrument(BondInstrument('fixed', 90, 0.06))  # 6% fixed for 90 days
    builder.add_bond_instrument(BondInstrument('floating', 60, 0.0, 0.01))  # SOFR + 1%
    
    # Add derivative instruments
    builder.add_derivative_instrument(DerivativeInstrument('future', days_to_expiry=180, funding_rate=0.07))
    builder.add_derivative_instrument(DerivativeInstrument('perpetual', funding_rate=0.0002))  # 0.02% daily
    
    # Build and plot curve
    try:
        curve = builder.build_curve(method='cubic')
        builder.plot_curve(curve)
    except ValueError as e:
        print(f"Error building yield curve: {e}")
```
