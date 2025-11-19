"""
Generated Code Metadata:
========================
Original URL: https://capitalwealthinvestmentltd.com
Prompt: Design a risk management system for investors on capitalwealthinvestmentltd, taking into account the risks associated with trading on margin and the potential for losses.
Generated: DETERMINISTIC_8a8a6567fe641bef
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 6

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RiskLevel(Enum):
    """Enum representing different risk levels."""
    LOW = auto()
    MODERATE = auto()
    HIGH = auto()
    EXTREME = auto()

class AssetClass(Enum):
    """Enum representing different asset classes."""
    STOCK = auto()
    BOND = auto()
    COMMODITY = auto()
    CRYPTO = auto()
    FOREX = auto()

@dataclass
class Position:
    """Class representing an investment position."""
    asset_id: str
    asset_class: AssetClass
    quantity: Decimal
    entry_price: Decimal
    current_price: Decimal
    margin_used: Decimal = Decimal('0')

    @property
    def market_value(self) -> Decimal:
        """Calculate current market value of the position."""
        return self.quantity * self.current_price

    @property
    def unrealized_pnl(self) -> Decimal:
        """Calculate unrealized profit and loss."""
        return (self.current_price - self.entry_price) * self.quantity

@dataclass
class Account:
    """Class representing an investor's account."""
    account_id: str
    balance: Decimal
    margin_enabled: bool = False
    margin_multiplier: Decimal = Decimal('1')
    positions: Dict[str, Position] = None

    def __post_init__(self):
        if self.positions is None:
            self.positions = {}

    @property
    def total_market_value(self) -> Decimal:
        """Calculate total market value of all positions."""
        return sum(pos.market_value for pos in self.positions.values())

    @property
    def total_margin_used(self) -> Decimal:
        """Calculate total margin used across all positions."""
        return sum(pos.margin_used for pos in self.positions.values())

    @property
    def available_balance(self) -> Decimal:
        """Calculate available balance considering margin."""
        if self.margin_enabled:
            return self.balance + (self.total_market_value - self.total_margin_used)
        return self.balance

    @property
    def margin_utilization(self) -> Decimal:
        """Calculate margin utilization ratio."""
        if not self.margin_enabled or self.total_market_value == 0:
            return Decimal('0')
        return self.total_margin_used / self.total_market_value

class RiskManagementSystem:
    """Main risk management system class."""
    
    MARGIN_WARNING_THRESHOLD = Decimal('0.7')
    MARGIN_LIQUIDATION_THRESHOLD = Decimal('0.9')
    
    def __init__(self, account: Account):
        self.account = account

    def assess_position_risk(self, position: Position) -> RiskLevel:
        """Assess risk level for a single position."""
        volatility_score = self._calculate_volatility_score(position.asset_class)
        margin_impact = position.margin_used / self.account.balance if self.account.balance > 0 else Decimal('0')
        
        risk_score = volatility_score * margin_impact
        
        if risk_score < Decimal('0.1'):
            return RiskLevel.LOW
        elif risk_score < Decimal('0.3'):
            return RiskLevel.MODERATE
        elif risk_score < Decimal('0.6'):
            return RiskLevel.HIGH
        else:
            return RiskLevel.EXTREME

    def assess_portfolio_risk(self) -> RiskLevel:
        """Assess overall portfolio risk."""
        if not self.account.positions:
            return RiskLevel.LOW
            
        weighted_risk = Decimal('0')
        total_weight = Decimal('0')
        
        for position in self.account.positions.values():
            position_risk = self.assess_position_risk(position)
            weight = position.market_value / self.account.total_market_value
            weighted_risk += Decimal(position_risk.value) * weight
            total_weight += weight
        
        if total_weight == 0:
            return RiskLevel.LOW
            
        avg_risk = weighted_risk / total_weight
        
        if avg_risk < 1.5:
            return RiskLevel.LOW
        elif avg_risk < 2.5:
            return RiskLevel.MODERATE
        elif avg_risk < 3.5:
            return RiskLevel.HIGH
        else:
            return RiskLevel.EXTREME

    def check_margin_requirements(self) -> bool:
        """Check if margin requirements are being met."""
        if not self.account.margin_enabled:
            return True
            
        utilization = self.account.margin_utilization
        
        if utilization > self.MARGIN_LIQUIDATION_THRESHOLD:
            logger.warning(f"Margin liquidation threshold exceeded: {utilization:.2%}")
            return False
        elif utilization > self.MARGIN_WARNING_THRESHOLD:
            logger.warning(f"Margin warning threshold exceeded: {utilization:.2%}")
            
        return True

    def calculate_max_position_size(self, asset_class: AssetClass, price: Decimal) -> Decimal:
        """Calculate maximum position size considering risk parameters."""
        if not self.account.margin_enabled:
            return self.account.balance / price
            
        volatility_score = self._calculate_volatility_score(asset_class)
        max_risk_exposure = self.account.balance * Decimal('0.25')  # Max 25% of balance per position
        position_size = max_risk_exposure / (price * volatility_score)
        
        return position_size

    def _calculate_volatility_score(self, asset_class: AssetClass) -> Decimal:
        """Calculate volatility score based on asset class."""
        # These values would typically come from historical data analysis
        volatility_scores = {
            AssetClass.STOCK: Decimal('0.2'),
            AssetClass.BOND: Decimal('0.05'),
            AssetClass.COMMODITY: Decimal('0.4'),
            AssetClass.CRYPTO: Decimal('0.8'),
            AssetClass.FOREX: Decimal('0.3')
        }
        
        return volatility_scores.get(asset_class, Decimal('0.5'))

    def liquidate_positions(self) -> List[str]:
        """Liquidate positions to meet margin requirements."""
        if not self.account.margin_enabled:
            return []
            
        liquidated = []
        positions_by_risk = sorted(
            self.account.positions.values(),
            key=lambda p: self.assess_position_risk(p).value,
            reverse=True
        )
        
        for position in positions_by_risk:
            if self.account.margin_utilization <= self.MARGIN_WARNING_THRESHOLD:
                break
                
            # Simulate liquidation
            self.account.balance += position.unrealized_pnl
            self.account.positions.pop(position.asset_id)
            liquidated.append(position.asset_id)
            logger.info(f"Liquidated position: {position.asset_id}")
            
        return liquidated

# Example usage
if __name__ == "__main__":
    # Create an account
    account = Account(
        account_id="12345",
        balance=Decimal('10000'),
        margin_enabled=True,
        margin_multiplier=Decimal('2')
    )
    
    # Add some positions
    account.positions["AAPL"] = Position(
        asset_id="AAPL",
        asset_class=AssetClass.STOCK,
        quantity=Decimal('10'),
        entry_price=Decimal('150'),
        current_price=Decimal('160'),
        margin_used=Decimal('750')  # 50% of position value (10 * 150 / 2)
    )
    
    account.positions["BTC"] = Position(
        asset_id="BTC",
        asset_class=AssetClass.CRYPTO,
        quantity=Decimal('0.5'),
        entry_price=Decimal('40000'),
        current_price=Decimal('38000'),
        margin_used=Decimal('10000')  # 50% of position value (0.5 * 40000 / 2)
    )
    
    # Initialize risk management system
    rms = RiskManagementSystem(account)
    
    # Check portfolio risk
    portfolio_risk = rms.assess_portfolio_risk()
    print(f"Portfolio Risk Level: {portfolio_risk.name}")
    
    # Check margin requirements
    if not rms.check_margin_requirements():
        print("Margin requirements not met. Liquidating positions...")
        liquidated = rms.liquidate_positions()
        print(f"Liquidated positions: {liquidated}")
```
