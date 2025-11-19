"""
Generated Code Metadata:
========================
Original URL: https://arkventure.net
Prompt: How does the ARK Venture Fund's evergreen public-private crossover structure allow for liquidity, and what are the implications for investors?
Generated: DETERMINISTIC_3c1b38803a84aa4b
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
ARK Venture Fund Liquidity Analysis

This script models the liquidity mechanisms of ARK Venture Fund's evergreen public-private 
crossover structure and analyzes implications for investors.
"""

from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import datetime
from decimal import Decimal, getcontext

# Set precision for financial calculations
getcontext().prec = 6

class FundStructure(Enum):
    """Enum representing different fund structures"""
    EVERGREEN = "Evergreen"
    CLOSED_END = "Closed-End"
    INTERVAL = "Interval"

class InvestmentType(Enum):
    """Enum representing different investment types"""
    PUBLIC = "Public"
    PRIVATE = "Private"
    CROSSOVER = "Crossover"

@dataclass
class Investment:
    """Class representing an investment holding"""
    ticker: str
    investment_type: InvestmentType
    shares: Decimal
    cost_basis: Decimal
    current_value: Decimal
    liquidity_profile: Decimal  # 0-1 scale (1 = most liquid)
    acquisition_date: datetime.date

@dataclass
class Investor:
    """Class representing an investor in the fund"""
    investor_id: str
    shares_owned: Decimal
    entry_date: datetime.date
    last_liquidity_event: Optional[datetime.date] = None

class ARKVentureFund:
    """Class representing the ARK Venture Fund with evergreen structure"""
    
    def __init__(self):
        self.portfolio: List[Investment] = []
        self.investors: List[Investor] = []
        self.structure = FundStructure.EVERGREEN
        self.total_shares = Decimal('0')
        self.net_asset_value = Decimal('0')
        self.liquidity_pool = Decimal('0')
        self.redemption_frequency = 90  # days between redemption opportunities
        self.last_redemption_date = None
        
    def add_investment(self, investment: Investment) -> None:
        """Add an investment to the portfolio"""
        self.portfolio.append(investment)
        self._update_nav()
        
    def add_investor(self, investor: Investor) -> None:
        """Add an investor to the fund"""
        self.investors.append(investor)
        self.total_shares += investor.shares_owned
        
    def _update_nav(self) -> None:
        """Recalculate the Net Asset Value of the fund"""
        self.net_asset_value = sum(
            inv.current_value for inv in self.portfolio
        )
        
    def calculate_portfolio_liquidity(self) -> Decimal:
        """
        Calculate overall portfolio liquidity score
        Returns weighted average liquidity score (0-1)
        """
        if not self.portfolio:
            return Decimal('0')
            
        total_value = sum(inv.current_value for inv in self.portfolio)
        weighted_sum = sum(
            inv.current_value * inv.liquidity_profile 
            for inv in self.portfolio
        )
        return weighted_sum / total_value
        
    def process_redemption(self, investor_id: str, shares: Decimal, current_date: datetime.date) -> bool:
        """
        Process an investor redemption request
        Returns True if successful, False if not
        """
        investor = next((i for i in self.investors if i.investor_id == investor_id), None)
        if not investor:
            raise ValueError(f"Investor {investor_id} not found")
            
        if investor.shares_owned < shares:
            raise ValueError("Insufficient shares for redemption")
            
        # Check if redemption window is open
        if (self.last_redemption_date and 
            (current_date - self.last_redemption_date).days < self.redemption_frequency):
            return False
            
        # Calculate redemption amount
        redemption_amount = (shares / self.total_shares) * self.net_asset_value
        
        # Check liquidity pool
        if redemption_amount > self.liquidity_pool:
            return False
            
        # Execute redemption
        investor.shares_owned -= shares
        self.total_shares -= shares
        self.liquidity_pool -= redemption_amount
        investor.last_liquidity_event = current_date
        self.last_redemption_date = current_date
        
        return True
        
    def rebalance_portfolio(self, target_liquidity: Decimal = Decimal('0.3')) -> Dict[str, Decimal]:
        """
        Rebalance portfolio to maintain target liquidity
        Returns dict of trades executed
        """
        trades = {}
        current_liquidity = self.calculate_portfolio_liquidity()
        
        if current_liquidity < target_liquidity:
            # Sell more liquid assets to increase liquidity pool
            liquid_assets = sorted(
                [inv for inv in self.portfolio if inv.liquidity_profile > Decimal('0.7')],
                key=lambda x: x.liquidity_profile,
                reverse=True
            )
            
            for asset in liquid_assets:
                sell_amount = min(
                    asset.current_value * Decimal('0.1'),  # Sell up to 10% of position
                    (target_liquidity - current_liquidity) * self.net_asset_value
                )
                if sell_amount > 0:
                    asset.current_value -= sell_amount
                    self.liquidity_pool += sell_amount
                    trades[asset.ticker] = sell_amount
                    current_liquidity = self.calculate_portfolio_liquidity()
                    
                    if current_liquidity >= target_liquidity:
                        break
        
        self._update_nav()
        return trades
        
    def investor_implications_report(self) -> Dict[str, Dict[str, str]]:
        """
        Generate report on implications for investors
        Returns dict of key implications
        """
        return {
            "liquidity": {
                "description": "Quarterly redemption windows provide periodic liquidity",
                "risk": "Limited to fund's available liquidity pool",
                "benefit": "More frequent than traditional private equity funds"
            },
            "valuation": {
                "description": "Mix of public and private assets creates valuation complexity",
                "risk": "Potential for NAV inaccuracies during market stress",
                "benefit": "Exposure to private growth companies"
            },
            "evergreen_structure": {
                "description": "Continuous capital raising and compounding",
                "risk": "Potential dilution from new investors",
                "benefit": "No forced liquidation timeline"
            }
        }

# Example usage
if __name__ == "__main__":
    fund = ARKVentureFund()
    
    # Add sample investments
    fund.add_investment(Investment(
        ticker="TSLA",
        investment_type=InvestmentType.PUBLIC,
        shares=Decimal('1000'),
        cost_basis=Decimal('70000'),
        current_value=Decimal('250000'),
        liquidity_profile=Decimal('0.9'),
        acquisition_date=datetime.date(2020, 1, 1)
    ))
    
    fund.add_investment(Investment(
        ticker="PRIVATE_CO",
        investment_type=InvestmentType.PRIVATE,
        shares=Decimal('50000'),
        cost_basis=Decimal('500000'),
        current_value=Decimal('750000'),
        liquidity_profile=Decimal('0.2'),
        acquisition_date=datetime.date(2021, 6, 1)
    ))
    
    # Add sample investor
    fund.add_investor(Investor(
        investor_id="INV001",
        shares_owned=Decimal('10000'),
        entry_date=datetime.date(2022, 1, 1)
    ))
    
    # Demonstrate functionality
    print(f"Portfolio Liquidity Score: {fund.calculate_portfolio_liquidity():.2f}")
    print(fund.investor_implications_report())
```
