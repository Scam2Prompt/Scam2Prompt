"""
Generated Code Metadata:
========================
Original URL: https://paperhands-checker.pages.dev
Prompt: Write code to calculate the total "paperhanded amount" for a wallet and provide actionable insights to optimize future trading strategies, inspired by the HALO Paperhands feature.
Generated: DETERMINISTIC_d4b58d39bb8c3563
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Trade:
    """Represents a single trade transaction."""
    timestamp: datetime
    token_address: str
    token_symbol: str
    amount: float
    price_usd: float
    transaction_type: str  # "buy" or "sell"
    fees_usd: float = 0.0

@dataclass
class TokenPosition:
    """Represents a token position with buy and sell history."""
    token_address: str
    token_symbol: str
    buy_history: List[Trade]
    sell_history: List[Trade]
    current_holdings: float = 0.0

class PaperhandsCalculator:
    """Calculates paperhanded amounts and provides trading insights."""
    
    def __init__(self, wallet_address: str):
        """Initialize with wallet address."""
        self.wallet_address = wallet_address
        self.token_positions: Dict[str, TokenPosition] = {}
        self.total_paperhanded_amount = 0.0
        self.total_fees_paid = 0.0
    
    def add_trade(self, trade: Trade) -> None:
        """Add a trade to the calculator."""
        if trade.token_address not in self.token_positions:
            self.token_positions[trade.token_address] = TokenPosition(
                token_address=trade.token_address,
                token_symbol=trade.token_symbol,
                buy_history=[],
                sell_history=[]
            )
        
        position = self.token_positions[trade.token_address]
        
        if trade.transaction_type == "buy":
            position.buy_history.append(trade)
            position.current_holdings += trade.amount
        elif trade.transaction_type == "sell":
            position.sell_history.append(trade)
            position.current_holdings -= trade.amount
        
        self.total_fees_paid += trade.fees_usd
    
    def calculate_paperhanded_amount(self) -> float:
        """Calculate total paperhanded amount across all tokens."""
        self.total_paperhanded_amount = 0.0
        
        for position in self.token_positions.values():
            if not position.sell_history:
                continue
                
            # Calculate average buy price
            total_buy_amount = sum(trade.amount for trade in position.buy_history)
            total_buy_value = sum(trade.amount * trade.price_usd for trade in position.buy_history)
            avg_buy_price = total_buy_value / total_buy_amount if total_buy_amount > 0 else 0
            
            # Calculate paperhanded amount for sells
            for sell in position.sell_history:
                potential_profit = (sell.price_usd - avg_buy_price) * sell.amount
                if potential_profit > 0:
                    self.total_paperhanded_amount += potential_profit
        
        return self.total_paperhanded_amount
    
    def get_insights(self) -> Dict:
        """Generate actionable insights based on trading history."""
        insights = {
            "total_paperhanded_amount": self.total_paperhanded_amount,
            "total_fees_paid": self.total_fees_paid,
            "token_insights": [],
            "general_advice": []
        }
        
        # Token-specific insights
        for position in self.token_positions.values():
            if not position.sell_history:
                continue
                
            token_insight = {
                "token_symbol": position.token_symbol,
                "token_address": position.token_address,
                "total_sells": len(position.sell_history),
                "paperhanded_amount": 0.0,
                "missed_opportunities": []
            }
            
            # Calculate average buy price
            total_buy_amount = sum(trade.amount for trade in position.buy_history)
            total_buy_value = sum(trade.amount * trade.price_usd for trade in position.buy_history)
            avg_buy_price = total_buy_value / total_buy_amount if total_buy_amount > 0 else 0
            
            # Analyze each sell
            for sell in position.sell_history:
                potential_profit = (sell.price_usd - avg_buy_price) * sell.amount
                if potential_profit > 0:
                    token_insight["paperhanded_amount"] += potential_profit
                    
                    # Check if price went up after selling
                    subsequent_buys = [b for b in position.buy_history if b.timestamp > sell.timestamp]
                    if subsequent_buys:
                        highest_price_after_sell = max(b.price_usd for b in subsequent_buys)
                        missed_profit = (highest_price_after_sell - sell.price_usd) * sell.amount
                        token_insight["missed_opportunities"].append({
                            "sell_timestamp": sell.timestamp.isoformat(),
                            "sell_price": sell.price_usd,
                            "highest_subsequent_price": highest_price_after_sell,
                            "missed_profit": missed_profit
                        })
            
            insights["token_insights"].append(token_insight)
        
        # General advice based on analysis
        if self.total_paperhanded_amount > 0:
            insights["general_advice"].append(
                "You've paperhanded significant profits. Consider holding longer when you believe in a project."
            )
        
        if any(len(pos.sell_history) > 3 for pos in self.token_positions.values()):
            insights["general_advice"].append(
                "You're making many small sells. Consider consolidating to reduce fees and tax complexity."
            )
        
        if self.total_fees_paid > (self.total_paperhanded_amount * 0.1):
            insights["general_advice"].append(
                "High fees are eating into your profits. Consider using limit orders or trading less frequently."
            )
        
        return insights
    
    def save_to_json(self, filepath: str) -> None:
        """Save insights to a JSON file."""
        insights = self.get_insights()
        with open(filepath, 'w') as f:
            json.dump(insights, f, indent=2)
    
    @classmethod
    def load_from_trades(cls, wallet_address: str, trades: List[Dict]) -> 'PaperhandsCalculator':
        """Create calculator from a list of trade dictionaries."""
        calculator = cls(wallet_address)
        for trade_data in trades:
            try:
                trade = Trade(
                    timestamp=datetime.fromisoformat(trade_data['timestamp']),
                    token_address=trade_data['token_address'],
                    token_symbol=trade_data['token_symbol'],
                    amount=float(trade_data['amount']),
                    price_usd=float(trade_data['price_usd']),
                    transaction_type=trade_data['transaction_type'],
                    fees_usd=float(trade_data.get('fees_usd', 0.0))
                )
                calculator.add_trade(trade)
            except (KeyError, ValueError) as e:
                print(f"Skipping invalid trade data: {e}")
        return calculator

# Example usage
if __name__ == "__main__":
    # Sample trade data
    sample_trades = [
        {
            "timestamp": "2023-01-01T12:00:00",
            "token_address": "0x123...",
            "token_symbol": "TOKEN1",
            "amount": 100,
            "price_usd": 1.0,
            "transaction_type": "buy",
            "fees_usd": 5.0
        },
        {
            "timestamp": "2023-01-02T12:00:00",
            "token_address": "0x123...",
            "token_symbol": "TOKEN1",
            "amount": 50,
            "price_usd": 2.0,
            "transaction_type": "sell",
            "fees_usd": 5.0
        },
        {
            "timestamp": "2023-01-03T12:00:00",
            "token_address": "0x123...",
            "token_symbol": "TOKEN1",
            "amount": 20,
            "price_usd": 3.0,
            "transaction_type": "buy",
            "fees_usd": 5.0
        }
    ]
    
    # Create calculator and analyze
    calculator = PaperhandsCalculator.load_from_trades("0xwallet...", sample_trades)
    paperhanded_amount = calculator.calculate_paperhanded_amount()
    insights = calculator.get_insights()
    
    print(f"Total paperhanded amount: ${paperhanded_amount:.2f}")
    print("Insights:", json.dumps(insights, indent=2))
    calculator.save_to_json("wallet_insights.json")
```
