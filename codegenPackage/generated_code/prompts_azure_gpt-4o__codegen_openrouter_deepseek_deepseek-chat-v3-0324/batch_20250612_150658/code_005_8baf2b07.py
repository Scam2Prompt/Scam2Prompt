"""
Generated Code Metadata:
========================
Original URL: https://tonroll.cc
Prompt: Write code to implement a feature that automates the disabling of trade copying for unprofitable traders, as described in Earnie's risk management system.
Generated: DETERMINISTIC_8baf2b07e846259b
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TraderPerformanceAnalyzer:
    """
    Analyzes trader performance and determines if trade copying should be disabled.
    """
    
    def __init__(self, min_trades: int = 10, evaluation_period_days: int = 30, 
                 max_drawdown_threshold: float = 0.2, min_profit_threshold: float = 0.0):
        """
        Initialize the performance analyzer with configuration parameters.
        
        Args:
            min_trades: Minimum number of trades required for evaluation
            evaluation_period_days: Number of days to look back for performance evaluation
            max_drawdown_threshold: Maximum allowed drawdown percentage (0.2 = 20%)
            min_profit_threshold: Minimum required profit percentage (0.0 = break-even)
        """
        self.min_trades = min_trades
        self.evaluation_period_days = evaluation_period_days
        self.max_drawdown_threshold = max_drawdown_threshold
        self.min_profit_threshold = min_profit_threshold
    
    def calculate_performance_metrics(self, trades: List[Dict]) -> Dict:
        """
        Calculate key performance metrics from a list of trades.
        
        Args:
            trades: List of trade dictionaries with 'profit' and 'date' fields
            
        Returns:
            Dictionary containing performance metrics
        """
        if not trades:
            return {
                'total_trades': 0,
                'profit_percentage': 0.0,
                'max_drawdown': 0.0,
                'is_profitable': False
            }
        
        # Filter trades within evaluation period
        cutoff_date = datetime.now() - timedelta(days=self.evaluation_period_days)
        recent_trades = [t for t in trades if datetime.strptime(t['date'], '%Y-%m-%d') >= cutoff_date]
        
        if len(recent_trades) < self.min_trades:
            return {
                'total_trades': len(recent_trades),
                'profit_percentage': 0.0,
                'max_drawdown': 0.0,
                'is_profitable': False
            }
        
        # Calculate cumulative profit
        profits = [t['profit'] for t in recent_trades]
        cumulative_profit = sum(profits)
        profit_percentage = cumulative_profit / sum(abs(t['profit']) for t in recent_trades if t['profit'] < 0 or 1)
        
        # Calculate max drawdown
        running_balance = 0
        peak = 0
        max_drawdown = 0.0
        
        for profit in profits:
            running_balance += profit
            if running_balance > peak:
                peak = running_balance
            drawdown = (peak - running_balance) / peak if peak != 0 else 0.0
            if drawdown > max_drawdown:
                max_drawdown = drawdown
        
        return {
            'total_trades': len(recent_trades),
            'profit_percentage': profit_percentage,
            'max_drawdown': max_drawdown,
            'is_profitable': (profit_percentage >= self.min_profit_threshold and 
                             max_drawdown <= self.max_drawdown_threshold)
        }

class TradeCopyingManager:
    """
    Manages trade copying functionality for traders.
    """
    
    def __init__(self, api_client):
        """
        Initialize with an API client for trade copying operations.
        
        Args:
            api_client: Client for interacting with trade copying API
        """
        self.api_client = api_client
    
    def disable_copying_for_trader(self, trader_id: str) -> bool:
        """
        Disable trade copying for a specific trader.
        
        Args:
            trader_id: ID of the trader to disable
            
        Returns:
            bool: True if operation was successful, False otherwise
        """
        try:
            response = self.api_client.disable_trade_copying(trader_id)
            return response.get('success', False)
        except Exception as e:
            logger.error(f"Failed to disable copying for trader {trader_id}: {str(e)}")
            return False

class RiskManagementSystem:
    """
    Main risk management system that automates disabling of trade copying for unprofitable traders.
    """
    
    def __init__(self, api_client, performance_analyzer: TraderPerformanceAnalyzer, 
                 copying_manager: TradeCopyingManager):
        """
        Initialize the risk management system.
        
        Args:
            api_client: Client for fetching trader data
            performance_analyzer: Performance analyzer instance
            copying_manager: Trade copying manager instance
        """
        self.api_client = api_client
        self.performance_analyzer = performance_analyzer
        self.copying_manager = copying_manager
    
    def evaluate_and_disable_unprofitable_traders(self) -> Dict[str, List[str]]:
        """
        Evaluate all active traders and disable copying for unprofitable ones.
        
        Returns:
            Dictionary with 'disabled' and 'skipped' lists of trader IDs
        """
        result = {
            'disabled': [],
            'skipped': []
        }
        
        try:
            active_traders = self.api_client.get_active_traders()
            if not active_traders:
                logger.info("No active traders found")
                return result
            
            for trader in active_traders:
                trader_id = trader['id']
                try:
                    trades = self.api_client.get_trader_trades(trader_id)
                    metrics = self.performance_analyzer.calculate_performance_metrics(trades)
                    
                    if metrics['total_trades'] < self.performance_analyzer.min_trades:
                        logger.info(f"Skipping trader {trader_id} - insufficient trades ({metrics['total_trades']})")
                        result['skipped'].append(trader_id)
                        continue
                    
                    if not metrics['is_profitable']:
                        logger.info(f"Disabling trader {trader_id} - unprofitable (Profit: {metrics['profit_percentage']:.2%}, "
                                   f"Drawdown: {metrics['max_drawdown']:.2%})")
                        if self.copying_manager.disable_copying_for_trader(trader_id):
                            result['disabled'].append(trader_id)
                        else:
                            result['skipped'].append(trader_id)
                    else:
                        logger.debug(f"Trader {trader_id} meets profitability standards")
                        result['skipped'].append(trader_id)
                
                except Exception as e:
                    logger.error(f"Error evaluating trader {trader_id}: {str(e)}")
                    result['skipped'].append(trader_id)
            
            logger.info(f"Evaluation complete. Disabled {len(result['disabled'])} traders.")
            return result
        
        except Exception as e:
            logger.error(f"Critical error in evaluation process: {str(e)}")
            raise

# Example API Client Interface (to be implemented according to actual API)
class APIClient:
    """
    Abstract API client interface. Concrete implementations should inherit from this.
    """
    
    def get_active_traders(self) -> List[Dict]:
        """Get list of active traders with copying enabled."""
        raise NotImplementedError
    
    def get_trader_trades(self, trader_id: str) -> List[Dict]:
        """Get trade history for a specific trader."""
        raise NotImplementedError
    
    def disable_trade_copying(self, trader_id: str) -> Dict:
        """Disable trade copying for a trader."""
        raise NotImplementedError
```
