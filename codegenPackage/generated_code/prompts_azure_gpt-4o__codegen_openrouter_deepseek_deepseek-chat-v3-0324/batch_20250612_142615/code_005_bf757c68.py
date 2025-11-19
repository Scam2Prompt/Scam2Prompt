"""
Generated Code Metadata:
========================
Original URL: https://tjsftc.com
Prompt: Develop a program that tracks the ROI (return on investment) of copy trading on Binance, using data from the platform's copy trading feature.
Generated: DETERMINISTIC_bf757c681d454f6e
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

import pandas as pd
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('BinanceCopyTradingROI')

class BinanceCopyTradingTracker:
    """
    A class to track ROI from Binance copy trading feature.
    """
    
    def __init__(self, api_key: str, api_secret: str):
        """
        Initialize the Binance client and validate credentials.
        
        Args:
            api_key: Binance API key
            api_secret: Binance API secret
        """
        self.client = Client(api_key, api_secret)
        self.validate_credentials()
        
        # Initialize data storage
        self.portfolio_history = []
        self.trade_history = []
        
    def validate_credentials(self) -> None:
        """Validate Binance API credentials."""
        try:
            self.client.get_account()
            logger.info("Successfully authenticated with Binance API")
        except BinanceAPIException as e:
            logger.error(f"Authentication failed: {e.message}")
            raise

    def get_copy_trading_portfolio(self) -> Dict:
        """
        Fetch current copy trading portfolio from Binance.
        
        Returns:
            Dictionary containing portfolio information
        """
        try:
            # Note: Binance doesn't have a direct copy trading API endpoint as of now
            # This is a placeholder for when they implement it
            # For now, we'll simulate with spot account info
            account = self.client.get_account()
            
            portfolio = {
                'timestamp': datetime.utcnow(),
                'total_balance': float(account['totalWalletBalance']),
                'positions': [
                    {
                        'asset': balance['asset'],
                        'free': float(balance['free']),
                        'locked': float(balance['locked'])
                    }
                    for balance in account['balances'] 
                    if float(balance['free']) > 0 or float(balance['locked']) > 0
                ]
            }
            
            logger.info("Fetched copy trading portfolio")
            return portfolio
            
        except BinanceAPIException as e:
            logger.error(f"Failed to fetch portfolio: {e.message}")
            raise

    def get_copy_trading_history(self, days: int = 30) -> List[Dict]:
        """
        Fetch copy trading history from Binance.
        
        Args:
            days: Number of days of history to fetch
            
        Returns:
            List of historical trades
        """
        try:
            # Placeholder for actual copy trading history endpoint
            # Using spot trade history as a substitute
            end_time = datetime.utcnow()
            start_time = end_time - timedelta(days=days)
            
            trades = []
            for symbol in self._get_traded_symbols():
                symbol_trades = self.client.get_my_trades(
                    symbol=symbol,
                    startTime=int(start_time.timestamp() * 1000),
                    endTime=int(end_time.timestamp() * 1000)
                )
                trades.extend(symbol_trades)
            
            formatted_trades = [
                {
                    'timestamp': datetime.fromtimestamp(trade['time'] / 1000),
                    'symbol': trade['symbol'],
                    'side': trade['isBuyer'] and 'BUY' or 'SELL',
                    'price': float(trade['price']),
                    'quantity': float(trade['qty']),
                    'commission': float(trade['commission']),
                    'commission_asset': trade['commissionAsset']
                }
                for trade in trades
            ]
            
            logger.info(f"Fetched {len(formatted_trades)} copy trading records")
            return formatted_trades
            
        except BinanceAPIException as e:
            logger.error(f"Failed to fetch trade history: {e.message}")
            raise

    def _get_traded_symbols(self) -> List[str]:
        """Get list of symbols with trading activity."""
        try:
            exchange_info = self.client.get_exchange_info()
            return [symbol['symbol'] for symbol in exchange_info['symbols']]
        except BinanceAPIException as e:
            logger.error(f"Failed to fetch traded symbols: {e.message}")
            raise

    def track_performance(self, initial_investment: float) -> Dict:
        """
        Calculate ROI and other performance metrics.
        
        Args:
            initial_investment: The initial amount invested
            
        Returns:
            Dictionary with performance metrics
        """
        try:
            current_portfolio = self.get_copy_trading_portfolio()
            current_value = current_portfolio['total_balance']
            
            roi = ((current_value - initial_investment) / initial_investment) * 100
            absolute_return = current_value - initial_investment
            
            trades = self.get_copy_trading_history()
            winning_trades = len([t for t in trades if t['side'] == 'SELL' and 
                                (t['price'] * t['quantity']) > (trades[trades.index(t)-1]['price'] * trades[trades.index(t)-1]['quantity'])])
            
            performance = {
                'initial_investment': initial_investment,
                'current_value': current_value,
                'absolute_return': absolute_return,
                'roi_percentage': roi,
                'total_trades': len(trades),
                'winning_trades': winning_trades,
                'win_rate': (winning_trades / len(trades)) * 100 if trades else 0,
                'last_updated': datetime.utcnow()
            }
            
            logger.info(f"Calculated performance metrics: ROI {roi:.2f}%")
            return performance
            
        except Exception as e:
            logger.error(f"Failed to calculate performance: {str(e)}")
            raise

    def generate_report(self, initial_investment: float, output_format: str = 'csv') -> None:
        """
        Generate a performance report.
        
        Args:
            initial_investment: Initial investment amount
            output_format: Output format ('csv' or 'console')
        """
        try:
            performance = self.track_performance(initial_investment)
            trades = self.get_copy_trading_history()
            
            if output_format.lower() == 'csv':
                # Create directory if it doesn't exist
                os.makedirs('reports', exist_ok=True)
                
                # Save performance metrics
                perf_df = pd.DataFrame([performance])
                perf_file = f"reports/performance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                perf_df.to_csv(perf_file, index=False)
                
                # Save trade history
                trades_df = pd.DataFrame(trades)
                trades_file = f"reports/trades_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                trades_df.to_csv(trades_file, index=False)
                
                logger.info(f"Reports saved to {perf_file} and {trades_file}")
                
            elif output_format.lower() == 'console':
                print("\n=== Performance Summary ===")
                print(f"Initial Investment: ${initial_investment:,.2f}")
                print(f"Current Value: ${performance['current_value']:,.2f}")
                print(f"Absolute Return: ${performance['absolute_return']:,.2f}")
                print(f"ROI: {performance['roi_percentage']:.2f}%")
                print(f"Total Trades: {performance['total_trades']}")
                print(f"Win Rate: {performance['win_rate']:.2f}%")
                print(f"Last Updated: {performance['last_updated']}")
                
                print("\n=== Recent Trades ===")
                for trade in trades[-5:]:
                    print(f"{trade['timestamp']} - {trade['symbol']} {trade['side']} {trade['quantity']} @ {trade['price']}")
                    
            else:
                raise ValueError("Invalid output format. Choose 'csv' or 'console'")
                
        except Exception as e:
            logger.error(f"Failed to generate report: {str(e)}")
            raise

    def run_continuous_tracking(self, initial_investment: float, interval_hours: int = 24) -> None:
        """
        Continuously track performance at regular intervals.
        
        Args:
            initial_investment: Initial investment amount
            interval_hours: Tracking interval in hours
        """
        logger.info(f"Starting continuous tracking with {interval_hours} hour intervals")
        
        try:
            while True:
                self.generate_report(initial_investment, output_format='csv')
                logger.info(f"Sleeping for {interval_hours} hours...")
                time.sleep(interval_hours * 3600)
                
        except KeyboardInterrupt:
            logger.info("Stopping continuous tracking")
        except Exception as e:
            logger.error(f"Continuous tracking failed: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    # Load API keys from environment variables for security
    API_KEY =
