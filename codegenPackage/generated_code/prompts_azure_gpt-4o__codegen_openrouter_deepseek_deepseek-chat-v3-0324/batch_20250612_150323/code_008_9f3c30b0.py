"""
Generated Code Metadata:
========================
Original URL: https://opensee.io
Prompt: Generate code to simulate the impact of trade adjustments on metrics monitoring and capital consumption, ensuring auditability and traceability, as outlined by Opensee.
Generated: DETERMINISTIC_9f3c30b0b7942d15
Batch ID: 20250612_150323
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
from datetime import datetime
from typing import List, Dict, Optional
import uuid
import pandas as pd
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AdjustmentType(Enum):
    """Enumeration of possible trade adjustment types"""
    PRICE = auto()
    QUANTITY = auto()
    CURRENCY = auto()
    DATE = auto()

@dataclass
class Trade:
    """Represents a financial trade with relevant attributes"""
    trade_id: str
    instrument: str
    quantity: float
    price: float
    currency: str
    trade_date: datetime
    counterparty: str

@dataclass
class TradeAdjustment:
    """Represents an adjustment made to a trade"""
    adjustment_id: str
    trade_id: str
    adjustment_type: AdjustmentType
    old_value: float | str | datetime
    new_value: float | str | datetime
    timestamp: datetime
    user: str
    reason: str

@dataclass
class CapitalConsumption:
    """Represents capital consumption metrics"""
    trade_id: str
    initial_capital: float
    adjusted_capital: float
    change_percentage: float
    calculation_time: datetime

class TradeAdjustmentSimulator:
    """Simulates and tracks the impact of trade adjustments on metrics"""
    
    def __init__(self):
        self.trades: Dict[str, Trade] = {}
        self.adjustments: List[TradeAdjustment] = []
        self.capital_consumption_history: List[CapitalConsumption] = []
        
    def add_trade(self, trade: Trade) -> None:
        """Add a new trade to the system"""
        if trade.trade_id in self.trades:
            raise ValueError(f"Trade with ID {trade.trade_id} already exists")
        self.trades[trade.trade_id] = trade
        logger.info(f"Added trade {trade.trade_id}")
        
    def apply_adjustment(
        self,
        trade_id: str,
        adjustment_type: AdjustmentType,
        new_value: float | str | datetime,
        user: str,
        reason: str
    ) -> None:
        """Apply an adjustment to a trade and track the change"""
        if trade_id not in self.trades:
            raise ValueError(f"Trade with ID {trade_id} not found")
            
        trade = self.trades[trade_id]
        old_value = self._get_trade_attribute(trade, adjustment_type)
        
        # Create and store the adjustment
        adjustment = TradeAdjustment(
            adjustment_id=str(uuid.uuid4()),
            trade_id=trade_id,
            adjustment_type=adjustment_type,
            old_value=old_value,
            new_value=new_value,
            timestamp=datetime.now(),
            user=user,
            reason=reason
        )
        self.adjustments.append(adjustment)
        
        # Apply the change to the trade
        self._set_trade_attribute(trade, adjustment_type, new_value)
        
        # Recalculate capital consumption
        self._calculate_capital_consumption(trade_id)
        
        logger.info(f"Applied adjustment {adjustment.adjustment_id} to trade {trade_id}")
    
    def _get_trade_attribute(self, trade: Trade, adjustment_type: AdjustmentType):
        """Get the relevant attribute from a trade based on adjustment type"""
        if adjustment_type == AdjustmentType.PRICE:
            return trade.price
        elif adjustment_type == AdjustmentType.QUANTITY:
            return trade.quantity
        elif adjustment_type == AdjustmentType.CURRENCY:
            return trade.currency
        elif adjustment_type == AdjustmentType.DATE:
            return trade.trade_date
        else:
            raise ValueError(f"Unknown adjustment type: {adjustment_type}")
    
    def _set_trade_attribute(
        self,
        trade: Trade,
        adjustment_type: AdjustmentType,
        value: float | str | datetime
    ) -> None:
        """Set the relevant attribute on a trade based on adjustment type"""
        if adjustment_type == AdjustmentType.PRICE:
            trade.price = value
        elif adjustment_type == AdjustmentType.QUANTITY:
            trade.quantity = value
        elif adjustment_type == AdjustmentType.CURRENCY:
            trade.currency = value
        elif adjustment_type == AdjustmentType.DATE:
            trade.trade_date = value
        else:
            raise ValueError(f"Unknown adjustment type: {adjustment_type}")
    
    def _calculate_capital_consumption(self, trade_id: str) -> None:
        """Calculate capital consumption metrics for a trade"""
        trade = self.trades[trade_id]
        
        # Simplified capital consumption calculation (notional * risk factor)
        initial_notional = trade.quantity * trade.price
        adjusted_notional = trade.quantity * trade.price  # Would be different if we had initial state
        
        # Risk factor simulation (would normally come from risk models)
        risk_factor = 0.08  # Example fixed risk factor
        
        initial_capital = initial_notional * risk_factor
        adjusted_capital = adjusted_notional * risk_factor
        change_percentage = ((adjusted_capital - initial_capital) / initial_capital) * 100
        
        consumption = CapitalConsumption(
            trade_id=trade_id,
            initial_capital=initial_capital,
            adjusted_capital=adjusted_capital,
            change_percentage=change_percentage,
            calculation_time=datetime.now()
        )
        
        self.capital_consumption_history.append(consumption)
        logger.info(f"Calculated capital consumption for trade {trade_id}")
    
    def get_adjustment_history(self, trade_id: str) -> List[TradeAdjustment]:
        """Get all adjustments for a specific trade"""
        return [adj for adj in self.adjustments if adj.trade_id == trade_id]
    
    def get_capital_consumption_history(self, trade_id: str) -> List[CapitalConsumption]:
        """Get capital consumption history for a specific trade"""
        return [cc for cc in self.capital_consumption_history if cc.trade_id == trade_id]
    
    def generate_audit_report(self) -> pd.DataFrame:
        """Generate a comprehensive audit report of all adjustments"""
        data = []
        for adj in self.adjustments:
            data.append({
                "adjustment_id": adj.adjustment_id,
                "trade_id": adj.trade_id,
                "adjustment_type": adj.adjustment_type.name,
                "old_value": adj.old_value,
                "new_value": adj.new_value,
                "timestamp": adj.timestamp,
                "user": adj.user,
                "reason": adj.reason
            })
        return pd.DataFrame(data)
    
    def generate_capital_report(self) -> pd.DataFrame:
        """Generate a report of capital consumption changes"""
        data = []
        for cc in self.capital_consumption_history:
            data.append({
                "trade_id": cc.trade_id,
                "initial_capital": cc.initial_capital,
                "adjusted_capital": cc.adjusted_capital,
                "change_percentage": cc.change_percentage,
                "calculation_time": cc.calculation_time
            })
        return pd.DataFrame(data)

# Example usage
if __name__ == "__main__":
    simulator = TradeAdjustmentSimulator()
    
    # Add a sample trade
    trade = Trade(
        trade_id="TRADE_001",
        instrument="AAPL",
        quantity=100,
        price=150.25,
        currency="USD",
        trade_date=datetime(2023, 5, 15),
        counterparty="Goldman Sachs"
    )
    simulator.add_trade(trade)
    
    # Apply some adjustments
    simulator.apply_adjustment(
        trade_id="TRADE_001",
        adjustment_type=AdjustmentType.PRICE,
        new_value=152.75,
        user="analyst1",
        reason="Market data update"
    )
    
    simulator.apply_adjustment(
        trade_id="TRADE_001",
        adjustment_type=AdjustmentType.QUANTITY,
        new_value=95,
        user="trader1",
        reason="Partial unwind"
    )
    
    # Generate reports
    audit_report = simulator.generate_audit_report()
    capital_report = simulator.generate_capital_report()
    
    print("Audit Report:")
    print(audit_report)
    
    print("\nCapital Report:")
    print(capital_report)
```
