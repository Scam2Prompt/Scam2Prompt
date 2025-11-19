"""
Generated Code Metadata:
========================
Original URL: https://fundfa.com
Prompt: Create a function to simulate trading challenges for Traders Combat, incorporating customizable rules and account types mentioned on Fundfa.
Generated: DETERMINISTIC_ad3310a53e130079
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import Dict, List, Optional, Tuple

class AccountType(Enum):
    """Enum representing different account types available in Traders Combat."""
    STANDARD = "standard"
    PRO = "pro"
    ELITE = "elite"

class TradingRule:
    """Class representing a trading rule with its parameters."""
    
    def __init__(
        self,
        name: str,
        min_trades: int = 0,
        max_trades: int = 0,
        min_win_rate: float = 0.0,
        max_drawdown: float = 0.0,
        time_limit_days: int = 0
    ):
        """
        Initialize a trading rule with customizable parameters.
        
        Args:
            name: Name of the trading rule
            min_trades: Minimum number of trades required
            max_trades: Maximum number of trades allowed
            min_win_rate: Minimum win rate required (0.0 to 1.0)
            max_drawdown: Maximum allowed drawdown (0.0 to 1.0)
            time_limit_days: Time limit in days to complete the challenge
        """
        self.name = name
        self.min_trades = min_trades
        self.max_trades = max_trades
        self.min_win_rate = min_win_rate
        self.max_drawdown = max_drawdown
        self.time_limit_days = time_limit_days

class TradingChallengeSimulator:
    """Simulator for Traders Combat trading challenges."""
    
    def __init__(self):
        """Initialize the simulator with default rules for each account type."""
        self.rules: Dict[AccountType, List[TradingRule]] = {
            AccountType.STANDARD: [
                TradingRule(
                    name="Beginner Challenge",
                    min_trades=10,
                    max_trades=50,
                    min_win_rate=0.5,
                    max_drawdown=0.1,
                    time_limit_days=30
                )
            ],
            AccountType.PRO: [
                TradingRule(
                    name="Pro Challenge",
                    min_trades=20,
                    max_trades=100,
                    min_win_rate=0.6,
                    max_drawdown=0.08,
                    time_limit_days=14
                )
            ],
            AccountType.ELITE: [
                TradingRule(
                    name="Elite Challenge",
                    min_trades=30,
                    max_trades=150,
                    min_win_rate=0.7,
                    max_drawdown=0.05,
                    time_limit_days=7
                )
            ]
        }
    
    def add_rule(
        self,
        account_type: AccountType,
        rule: TradingRule
    ) -> None:
        """
        Add a custom trading rule for a specific account type.
        
        Args:
            account_type: Account type to add the rule to
            rule: TradingRule object to add
        """
        if account_type not in self.rules:
            self.rules[account_type] = []
        self.rules[account_type].append(rule)
    
    def simulate_trading_session(
        self,
        account_type: AccountType,
        rule_name: Optional[str] = None
    ) -> Tuple[bool, Dict[str, float]]:
        """
        Simulate a trading session and check if challenge rules are met.
        
        Args:
            account_type: Account type to simulate
            rule_name: Specific rule name to use (optional)
            
        Returns:
            Tuple of (success: bool, stats: dict) where stats contains performance metrics
        """
        if account_type not in self.rules:
            raise ValueError(f"Invalid account type: {account_type}")
            
        rules = self.rules[account_type]
        rule = None
        
        if rule_name:
            rule = next((r for r in rules if r.name == rule_name), None)
            if not rule:
                raise ValueError(f"Rule '{rule_name}' not found for account type {account_type}")
        else:
            rule = random.choice(rules)
        
        # Simulate trading performance
        num_trades = random.randint(rule.min_trades, rule.max_trades)
        win_rate = random.uniform(0.0, 1.0)
        drawdown = random.uniform(0.0, 0.2)  # Up to 20% drawdown
        
        # Check if challenge passed
        success = (
            num_trades >= rule.min_trades and
            num_trades <= rule.max_trades and
            win_rate >= rule.min_win_rate and
            drawdown <= rule.max_drawdown
        )
        
        stats = {
            "num_trades": num_trades,
            "win_rate": win_rate,
            "drawdown": drawdown,
            "rule_name": rule.name,
            "account_type": account_type.value
        }
        
        return success, stats
    
    def get_available_rules(self, account_type: AccountType) -> List[Dict[str, object]]:
        """
        Get all available rules for an account type.
        
        Args:
            account_type: Account type to get rules for
            
        Returns:
            List of dictionaries containing rule information
        """
        if account_type not in self.rules:
            raise ValueError(f"Invalid account type: {account_type}")
            
        return [
            {
                "name": rule.name,
                "min_trades": rule.min_trades,
                "max_trades": rule.max_trades,
                "min_win_rate": rule.min_win_rate,
                "max_drawdown": rule.max_drawdown,
                "time_limit_days": rule.time_limit_days
            }
            for rule in self.rules[account_type]
        ]

# Example usage
if __name__ == "__main__":
    simulator = TradingChallengeSimulator()
    
    # Add a custom rule
    custom_rule = TradingRule(
        name="Custom Challenge",
        min_trades=15,
        max_trades=75,
        min_win_rate=0.55,
        max_drawdown=0.09,
        time_limit_days=21
    )
    simulator.add_rule(AccountType.STANDARD, custom_rule)
    
    # Simulate a session
    account = AccountType.STANDARD
    success, stats = simulator.simulate_trading_session(account)
    
    print(f"Challenge {'passed' if success else 'failed'}!")
    print("Stats:", stats)
    
    # Get available rules
    print("\nAvailable rules for STANDARD account:")
    for rule in simulator.get_available_rules(account):
        print(rule)
```
