"""
Generated Code Metadata:
========================
Original URL: https://immediateflow.co
Prompt: Generate code to calculate the expected returns of a bond portfolio, incorporating fixed-income principles discussed on Petrolio Italiano.
Generated: DETERMINISTIC_d256816ceb530777
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
from typing import List, Dict, Union, Optional

class BondPortfolio:
    """
    A class to calculate expected returns of a bond portfolio based on fixed-income principles.
    Handles various bond types, yield calculations, and portfolio aggregation.
    """
    
    def __init__(self, bonds: List[Dict[str, Union[str, float, int]]]):
        """
        Initialize the bond portfolio with a list of bond dictionaries.
        
        Parameters:
        -----------
        bonds : List[Dict]
            List of bond dictionaries with keys:
            - 'name': str (bond identifier)
            - 'face_value': float (par value)
            - 'coupon_rate': float (annual coupon rate as decimal)
            - 'years_to_maturity': int
            - 'payment_frequency': int (payments per year)
            - 'current_price': float (current market price)
            - 'bond_type': str ('government' or 'corporate')
            - 'credit_rating': Optional[str] (for corporate bonds)
        """
        self.bonds = bonds
        self.validate_bonds()
        
    def validate_bonds(self) -> None:
        """Validate bond data for required fields and proper values."""
        required_fields = ['name', 'face_value', 'coupon_rate', 'years_to_maturity',
                          'payment_frequency', 'current_price', 'bond_type']
        
        for bond in self.bonds:
            for field in required_fields:
                if field not in bond:
                    raise ValueError(f"Missing required field: {field}")
            
            if bond['coupon_rate'] < 0 or bond['coupon_rate'] > 1:
                raise ValueError("Coupon rate must be between 0 and 1")
                
            if bond['bond_type'] == 'corporate' and 'credit_rating' not in bond:
                raise ValueError("Corporate bonds must have a credit rating")
    
    def calculate_yield_to_maturity(self, bond: Dict) -> float:
        """
        Calculate yield to maturity (YTM) for a bond using Newton-Raphson method.
        
        Parameters:
        -----------
        bond : Dict
            Bond dictionary with required fields
            
        Returns:
        --------
        float
            Yield to maturity (annualized)
        """
        face_value = bond['face_value']
        coupon_rate = bond['coupon_rate']
        years = bond['years_to_maturity']
        freq = bond['payment_frequency']
        price = bond['current_price']
        
        coupon_payment = (coupon_rate * face_value) / freq
        periods = years * freq
        
        # Initial guess for YTM
        ytm = coupon_rate  # Initial guess as coupon rate
        
        # Newton-Raphson iteration
        tolerance = 1e-6
        max_iter = 100
        for _ in range(max_iter):
            price_estimate = 0
            derivative = 0
            
            for t in range(1, periods + 1):
                discount = (1 + ytm/freq) ** t
                price_estimate += coupon_payment / discount
                derivative -= t * coupon_payment / (freq * discount * (1 + ytm/freq))
            
            price_estimate += face_value / ((1 + ytm/freq) ** periods)
            derivative -= periods * face_value / (freq * (1 + ytm/freq) ** (periods + 1))
            
            error = price_estimate - price
            if abs(error) < tolerance:
                break
                
            ytm -= error / derivative
        
        return ytm
    
    def calculate_expected_return(self, bond: Dict) -> float:
        """
        Calculate expected return for a bond considering reinvestment risk and credit risk.
        
        Parameters:
        -----------
        bond : Dict
            Bond dictionary with required fields
            
        Returns:
        --------
        float
            Expected annual return
        """
        ytm = self.calculate_yield_to_maturity(bond)
        
        # Adjust for credit risk if corporate bond
        if bond['bond_type'] == 'corporate':
            credit_spread = self._get_credit_spread(bond['credit_rating'])
            ytm += credit_spread
        
        # Adjust for reinvestment risk (simplified approach)
        reinvestment_adjustment = 0.005  # 50 basis points adjustment
        expected_return = ytm - reinvestment_adjustment
        
        return expected_return
    
    def _get_credit_spread(self, rating: str) -> float:
        """
        Get credit spread based on bond rating (simplified).
        In practice, this would use market data or a credit spread model.
        """
        spreads = {
            'AAA': 0.005,
            'AA': 0.010,
            'A': 0.015,
            'BBB': 0.025,
            'BB': 0.040,
            'B': 0.060,
            'CCC': 0.100
        }
        return spreads.get(rating.upper(), 0.050)  # Default to 5% if rating not found
    
    def portfolio_expected_return(self, weights: Optional[List[float]] = None) -> float:
        """
        Calculate weighted average expected return for the portfolio.
        
        Parameters:
        -----------
        weights : Optional[List[float]]
            List of weights for each bond. If None, equal weighting is used.
            
        Returns:
        --------
        float
            Portfolio expected return (annualized)
        """
        if weights is None:
            weights = [1/len(self.bonds)] * len(self.bonds)
        elif len(weights) != len(self.bonds):
            raise ValueError("Weights length must match number of bonds")
        elif not np.isclose(sum(weights), 1.0):
            raise ValueError("Weights must sum to 1")
        
        returns = [self.calculate_expected_return(bond) for bond in self.bonds]
        portfolio_return = np.dot(weights, returns)
        
        return portfolio_return
    
    def get_portfolio_summary(self) -> pd.DataFrame:
        """
        Generate a summary DataFrame of all bonds in the portfolio with key metrics.
        
        Returns:
        --------
        pd.DataFrame
            Summary of bonds with calculated metrics
        """
        summary_data = []
        
        for bond in self.bonds:
            ytm = self.calculate_yield_to_maturity(bond)
            expected_return = self.calculate_expected_return(bond)
            
            summary_data.append({
                'Name': bond['name'],
                'Type': bond['bond_type'],
                'Coupon Rate': bond['coupon_rate'],
                'YTM': ytm,
                'Expected Return': expected_return,
                'Price': bond['current_price'],
                'Maturity (years)': bond['years_to_maturity'],
                'Credit Rating': bond.get('credit_rating', 'N/A')
            })
        
        return pd.DataFrame(summary_data)

# Example usage
if __name__ == "__main__":
    # Sample bond portfolio
    bonds = [
        {
            'name': 'US Treasury 5Y',
            'face_value': 1000,
            'coupon_rate': 0.025,
            'years_to_maturity': 5,
            'payment_frequency': 2,
            'current_price': 980,
            'bond_type': 'government'
        },
        {
            'name': 'Corp Bond A',
            'face_value': 1000,
            'coupon_rate': 0.045,
            'years_to_maturity': 10,
            'payment_frequency': 2,
            'current_price': 950,
            'bond_type': 'corporate',
            'credit_rating': 'BBB'
        }
    ]
    
    portfolio = BondPortfolio(bonds)
    
    # Calculate portfolio metrics
    print("Portfolio Expected Return:", portfolio.portfolio_expected_return())
    print("\nBond Summary:")
    print(portfolio.get_portfolio_summary())
```
