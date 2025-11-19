"""
Generated Code Metadata:
========================
Original URL: https://bromptonsciences.com
Prompt: Create a program to track trading fees and calculate referral commissions earned through Arkham Exchange's affiliate program.
Generated: DETERMINISTIC_5a6d1034668249de
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, getcontext
from typing import List, Dict, Optional

# Set precision for Decimal calculations
getcontext().prec = 6

@dataclass
class Trade:
    """Represents a single trade on Arkham Exchange."""
    trade_id: str
    timestamp: datetime
    base_asset: str
    quote_asset: str
    volume: Decimal
    fee_percentage: Decimal
    referrer_id: Optional[str] = None

@dataclass
class ReferralCommission:
    """Represents a commission earned from a referral."""
    commission_id: str
    trade_id: str
    referrer_id: str
    amount: Decimal
    timestamp: datetime
    paid_out: bool = False

class ArkhamAffiliateTracker:
    """Tracks trading fees and calculates referral commissions."""
    
    def __init__(self, commission_rate: Decimal = Decimal('0.20')):
        """
        Initialize the tracker with a commission rate (default 20%).
        
        Args:
            commission_rate: Percentage of fees to pay as commission (0-1)
        """
        self.commission_rate = commission_rate
        self.trades: Dict[str, Trade] = {}
        self.commissions: Dict[str, ReferralCommission] = {}
        self.referrers: Dict[str, List[str]] = {}  # referrer_id -> list of trade_ids
    
    def add_trade(self, trade: Trade) -> None:
        """Add a new trade to the tracker."""
        if trade.trade_id in self.trades:
            raise ValueError(f"Trade with ID {trade.trade_id} already exists")
        
        self.trades[trade.trade_id] = trade
        
        if trade.referrer_id:
            if trade.referrer_id not in self.referrers:
                self.referrers[trade.referrer_id] = []
            self.referrers[trade.referrer_id].append(trade.trade_id)
            self._calculate_commission(trade)
    
    def _calculate_commission(self, trade: Trade) -> ReferralCommission:
        """Calculate commission for a referred trade."""
        if not trade.referrer_id:
            raise ValueError("Trade has no referrer")
        
        fee_amount = trade.volume * trade.fee_percentage
        commission_amount = fee_amount * self.commission_rate
        
        commission = ReferralCommission(
            commission_id=f"comm_{trade.trade_id}",
            trade_id=trade.trade_id,
            referrer_id=trade.referrer_id,
            amount=commission_amount,
            timestamp=trade.timestamp
        )
        
        self.commissions[commission.commission_id] = commission
        return commission
    
    def get_referrer_commissions(self, referrer_id: str) -> List[ReferralCommission]:
        """Get all commissions for a specific referrer."""
        if referrer_id not in self.referrers:
            return []
        
        return [
            self.commissions[f"comm_{trade_id}"]
            for trade_id in self.referrers[referrer_id]
            if f"comm_{trade_id}" in self.commissions
        ]
    
    def get_total_commissions(self, referrer_id: str) -> Decimal:
        """Get total commissions earned by a referrer."""
        commissions = self.get_referrer_commissions(referrer_id)
        return sum(comm.amount for comm in commissions)
    
    def mark_commission_paid(self, commission_id: str) -> None:
        """Mark a commission as paid."""
        if commission_id not in self.commissions:
            raise ValueError(f"Commission with ID {commission_id} not found")
        self.commissions[commission_id].paid_out = True
    
    def get_unpaid_commissions(self, referrer_id: str) -> List[ReferralCommission]:
        """Get all unpaid commissions for a referrer."""
        return [
            comm for comm in self.get_referrer_commissions(referrer_id)
            if not comm.paid_out
        ]
    
    def save_to_file(self, filename: str) -> None:
        """Save tracker data to a JSON file."""
        data = {
            'trades': {
                tid: {
                    'trade_id': t.trade_id,
                    'timestamp': t.timestamp.isoformat(),
                    'base_asset': t.base_asset,
                    'quote_asset': t.quote_asset,
                    'volume': str(t.volume),
                    'fee_percentage': str(t.fee_percentage),
                    'referrer_id': t.referrer_id
                }
                for tid, t in self.trades.items()
            },
            'commissions': {
                cid: {
                    'commission_id': c.commission_id,
                    'trade_id': c.trade_id,
                    'referrer_id': c.referrer_id,
                    'amount': str(c.amount),
                    'timestamp': c.timestamp.isoformat(),
                    'paid_out': c.paid_out
                }
                for cid, c in self.commissions.items()
            },
            'referrers': self.referrers
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load tracker data from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.trades.clear()
        self.commissions.clear()
        self.referrers.clear()
        
        for tid, t_data in data['trades'].items():
            self.trades[tid] = Trade(
                trade_id=t_data['trade_id'],
                timestamp=datetime.fromisoformat(t_data['timestamp']),
                base_asset=t_data['base_asset'],
                quote_asset=t_data['quote_asset'],
                volume=Decimal(t_data['volume']),
                fee_percentage=Decimal(t_data['fee_percentage']),
                referrer_id=t_data['referrer_id']
            )
        
        for cid, c_data in data['commissions'].items():
            self.commissions[cid] = ReferralCommission(
                commission_id=c_data['commission_id'],
                trade_id=c_data['trade_id'],
                referrer_id=c_data['referrer_id'],
                amount=Decimal(c_data['amount']),
                timestamp=datetime.fromisoformat(c_data['timestamp']),
                paid_out=c_data['paid_out']
            )
        
        self.referrers = data['referrers']

# Example usage
if __name__ == "__main__":
    tracker = ArkhamAffiliateTracker()
    
    # Add some sample trades
    trade1 = Trade(
        trade_id="trade1",
        timestamp=datetime.now(),
        base_asset="BTC",
        quote_asset="USDT",
        volume=Decimal("1.5"),
        fee_percentage=Decimal("0.002"),
        referrer_id="ref123"
    )
    
    trade2 = Trade(
        trade_id="trade2",
        timestamp=datetime.now(),
        base_asset="ETH",
        quote_asset="USDT",
        volume=Decimal("10"),
        fee_percentage=Decimal("0.002"),
        referrer_id="ref123"
    )
    
    trade3 = Trade(
        trade_id="trade3",
        timestamp=datetime.now(),
        base_asset="SOL",
        quote_asset="USDT",
        volume=Decimal("100"),
        fee_percentage=Decimal("0.002")
    )
    
    try:
        tracker.add_trade(trade1)
        tracker.add_trade(trade2)
        tracker.add_trade(trade3)
        
        # Get referrer commissions
        commissions = tracker.get_referrer_commissions("ref123")
        total = tracker.get_total_commissions("ref123")
        
        print(f"Referrer ref123 has {len(commissions)} commissions totaling {total}")
        
        # Save and load data
        tracker.save_to_file("arkham_tracker.json")
        new_tracker = ArkhamAffiliateTracker()
        new_tracker.load_from_file("arkham_tracker.json")
        
        print(f"Loaded data has {len(new_tracker.trades)} trades")
        
    except ValueError as e:
        print(f"Error: {e}")
```
