"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Create a Python script to simulate the compounding of earnings by deploying tenderized tokens into yield farming protocols.
Generated: DETERMINISTIC_728e585135111f34
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto
import random
from datetime import datetime, timedelta

class Protocol(Enum):
    AAVE = auto()
    COMPOUND = auto()
    YEARN = auto()
    CURVE = auto()

@dataclass
class Token:
    name: str
    symbol: str
    decimals: int
    price: float  # in USD

@dataclass
class Position:
    token: Token
    amount: float
    protocol: Protocol
    apy: float
    start_time: datetime
    end_time: Optional[datetime] = None

class YieldSimulator:
    def __init__(self):
        self.positions: List[Position] = []
        self.token_prices: Dict[str, Token] = {}
        self.protocol_apys: Dict[Protocol, float] = {
            Protocol.AAVE: 0.05,
            Protocol.COMPOUND: 0.06,
            Protocol.YEARN: 0.08,
            Protocol.CURVE: 0.12
        }
    
    def add_token(self, name: str, symbol: str, decimals: int, price: float) -> None:
        """Add a new token to the simulator."""
        if symbol in self.token_prices:
            raise ValueError(f"Token {symbol} already exists")
        self.token_prices[symbol] = Token(name, symbol, decimals, price)
    
    def get_token(self, symbol: str) -> Token:
        """Get token by symbol."""
        if symbol not in self.token_prices:
            raise ValueError(f"Token {symbol} not found")
        return self.token_prices[symbol]
    
    def get_protocol_apy(self, protocol: Protocol) -> float:
        """Get current APY for a protocol."""
        return self.protocol_apys.get(protocol, 0.0)
    
    def update_protocol_apy(self, protocol: Protocol, new_apy: float) -> None:
        """Update the APY for a protocol."""
        if protocol not in Protocol:
            raise ValueError("Invalid protocol")
        if new_apy < 0:
            raise ValueError("APY cannot be negative")
        self.protocol_apys[protocol] = new_apy
    
    def open_position(
        self,
        token_symbol: str,
        amount: float,
        protocol: Protocol,
        duration_days: int,
        custom_apy: Optional[float] = None
    ) -> Position:
        """Open a new yield farming position."""
        token = self.get_token(token_symbol)
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        apy = custom_apy if custom_apy is not None else self.get_protocol_apy(protocol)
        
        start_time = datetime.now()
        end_time = start_time + timedelta(days=duration_days)
        
        position = Position(
            token=token,
            amount=amount,
            protocol=protocol,
            apy=apy,
            start_time=start_time,
            end_time=end_time
        )
        
        self.positions.append(position)
        return position
    
    def calculate_compounded_earnings(self, position: Position, as_of_date: datetime) -> float:
        """Calculate compounded earnings for a position up to a specific date."""
        if position.end_time and as_of_date > position.end_time:
            as_of_date = position.end_time
        
        duration = (as_of_date - position.start_time).total_seconds() / (365 * 24 * 3600)
        
        if duration <= 0:
            return 0.0
        
        # Daily compounding
        periods_per_year = 365
        rate_per_period = position.apy / periods_per_year
        total_periods = duration * periods_per_year
        
        compounded_amount = position.amount * math.pow(1 + rate_per_period, total_periods)
        earnings = compounded_amount - position.amount
        
        return earnings
    
    def simulate_all_positions(self, days: int = 30) -> Dict[str, float]:
        """Simulate all positions for a given number of days."""
        results = {}
        as_of_date = datetime.now() + timedelta(days=days)
        
        for i, position in enumerate(self.positions):
            earnings = self.calculate_compounded_earnings(position, as_of_date)
            value = earnings * position.token.price
            results[f"position_{i}_{position.token.symbol}_{position.protocol.name}"] = value
        
        return results
    
    def close_position(self, position_index: int) -> float:
        """Close a position and return the total value."""
        if position_index < 0 or position_index >= len(self.positions):
            raise ValueError("Invalid position index")
        
        position = self.positions[position_index]
        position.end_time = datetime.now()
        
        earnings = self.calculate_compounded_earnings(position, position.end_time)
        total_value = (position.amount + earnings) * position.token.price
        
        del self.positions[position_index]
        return total_value

def main():
    # Initialize simulator
    simulator = YieldSimulator()
    
    # Add some tokens
    simulator.add_token("Ethereum", "ETH", 18, 3000.0)
    simulator.add_token("USD Coin", "USDC", 6, 1.0)
    simulator.add_token("Wrapped Bitcoin", "WBTC", 8, 40000.0)
    
    # Open some positions
    eth_position = simulator.open_position("ETH", 10.0, Protocol.AAVE, 90)
    usdc_position = simulator.open_position("USDC", 5000.0, Protocol.COMPOUND, 180)
    wbtc_position = simulator.open_position("WBTC", 0.5, Protocol.CURVE, 365)
    
    # Simulate earnings after 30 days
    print("Simulating earnings after 30 days...")
    earnings = simulator.simulate_all_positions(30)
    for position, value in earnings.items():
        print(f"{position}: ${value:,.2f}")
    
    # Close a position
    print("\nClosing ETH position...")
    eth_value = simulator.close_position(0)
    print(f"Received ${eth_value:,.2f} from closing position")

if __name__ == "__main__":
    main()
```
