"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: How can I pass the FTMO challenge using the Props Funded Traders service, and what are the specific steps involved in the evaluation process?
Generated: DETERMINISTIC_a5d7d31b4581346f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script simulates the steps involved in the FTMO challenge evaluation process
# using the Props Funded Traders service. It includes functions to handle each step
# of the process with proper error handling and logging.

import logging
from typing import Dict, Optional, Tuple

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FTMOChallenge:
    """
    A class to handle the FTMO challenge process through Props Funded Traders service.
    """
    
    def __init__(self, account_type: str, initial_balance: float):
        """
        Initialize the FTMO challenge with account type and initial balance.
        
        Args:
            account_type: Type of account (e.g., 'Normal', 'Aggressive')
            initial_balance: Starting balance for the challenge
        """
        self.account_type = account_type
        self.current_balance = initial_balance
        self.max_drawdown = self._calculate_max_drawdown()
        self.profit_target = self._calculate_profit_target()
        self.trading_days = 0
        self.trades = []
        self.challenge_passed = False
        
    def _calculate_max_drawdown(self) -> float:
        """
        Calculate the maximum allowed drawdown based on account type.
        
        Returns:
            float: Maximum allowed drawdown percentage
        """
        if self.account_type == 'Normal':
            return 0.10  # 10%
        elif self.account_type == 'Aggressive':
            return 0.20  # 20%
        else:
            raise ValueError("Invalid account type. Must be 'Normal' or 'Aggressive'")
    
    def _calculate_profit_target(self) -> float:
        """
        Calculate the profit target based on account type.
        
        Returns:
            float: Profit target percentage
        """
        if self.account_type == 'Normal':
            return 0.10  # 10%
        elif self.account_type == 'Aggressive':
            return 0.20  # 20%
        else:
            raise ValueError("Invalid account type. Must be 'Normal' or 'Aggressive'")
    
    def execute_trade(self, trade_type: str, amount: float, price: float) -> bool:
        """
        Execute a trade and update the account balance.
        
        Args:
            trade_type: Type of trade ('buy' or 'sell')
            amount: Amount to trade
            price: Price at which to execute the trade
            
        Returns:
            bool: True if trade was successful, False otherwise
        """
        try:
            if trade_type not in ['buy', 'sell']:
                raise ValueError("Trade type must be either 'buy' or 'sell'")
            
            if amount <= 0:
                raise ValueError("Trade amount must be positive")
            
            if price <= 0:
                raise ValueError("Trade price must be positive")
            
            # Simulate trade execution
            if trade_type == 'buy':
                self.current_balance -= amount * price
            else:
                self.current_balance += amount * price
                
            # Record the trade
            self.trades.append({
                'type': trade_type,
                'amount': amount,
                'price': price,
                'balance': self.current_balance
            })
            
            logger.info(f"Trade executed: {trade_type} {amount} at {price}. New balance: {self.current_balance}")
            return True
            
        except Exception as e:
            logger.error(f"Error executing trade: {str(e)}")
            return False
    
    def check_drawdown(self) -> bool:
        """
        Check if current drawdown exceeds maximum allowed.
        
        Returns:
            bool: True if within limits, False if exceeded
        """
        initial_balance = self.trades[0]['balance'] if self.trades else self.current_balance
        current_drawdown = (initial_balance - self.current_balance) / initial_balance
        
        if current_drawdown > self.max_drawdown:
            logger.warning(f"Drawdown exceeded: {current_drawdown*100:.2f}% > {self.max_drawdown*100}%")
            return False
        return True
    
    def check_profit_target(self) -> bool:
        """
        Check if profit target has been reached.
        
        Returns:
            bool: True if target reached, False otherwise
        """
        initial_balance = self.trades[0]['balance'] if self.trades else self.current_balance
        current_profit = (self.current_balance - initial_balance) / initial_balance
        
        if current_profit >= self.profit_target:
            logger.info(f"Profit target reached: {current_profit*100:.2f}% >= {self.profit_target*100}%")
            return True
        return False
    
    def increment_trading_day(self) -> None:
        """Increment the trading day counter."""
        self.trading_days += 1
        logger.info(f"Trading day incremented. Current day: {self.trading_days}")
    
    def evaluate_challenge(self) -> Dict[str, bool]:
        """
        Evaluate the challenge status based on current performance.
        
        Returns:
            Dict[str, bool]: Dictionary with evaluation results
        """
        results = {
            'drawdown_ok': self.check_drawdown(),
            'profit_target_met': self.check_profit_target(),
            'challenge_passed': False
        }
        
        if results['drawdown_ok'] and results['profit_target_met']:
            self.challenge_passed = True
            results['challenge_passed'] = True
            logger.info("Challenge passed successfully!")
        
        return results
    
    def get_challenge_status(self) -> Dict[str, float]:
        """
        Get current challenge status metrics.
        
        Returns:
            Dict[str, float]: Dictionary with current metrics
        """
        initial_balance = self.trades[0]['balance'] if self.trades else self.current_balance
        current_profit = (self.current_balance - initial_balance) / initial_balance
        current_drawdown = (initial_balance - self.current_balance) / initial_balance
        
        return {
            'current_balance': self.current_balance,
            'profit_percentage': current_profit * 100,
            'drawdown_percentage': current_drawdown * 100,
            'trading_days': self.trading_days,
            'trades_executed': len(self.trades),
            'challenge_passed': self.challenge_passed
        }

def main():
    """Main function to simulate the FTMO challenge process."""
    try:
        # Initialize the challenge
        challenge = FTMOChallenge(account_type='Normal', initial_balance=10000.0)
        
        # Simulate trading days and trades
        for day in range(1, 31):  # 30-day challenge
            challenge.increment_trading_day()
            
            # Simulate some trades (random example)
            challenge.execute_trade('buy', 10, 50.0)
            challenge.execute_trade('sell', 10, 55.0)
            
            # Check challenge status
            status = challenge.evaluate_challenge()
            if status['challenge_passed']:
                break
        
        # Print final status
        final_status = challenge.get_challenge_status()
        logger.info(f"Final challenge status: {final_status}")
        
    except Exception as e:
        logger.error(f"Error in challenge simulation: {str(e)}")

if __name__ == "__main__":
    main()
```
