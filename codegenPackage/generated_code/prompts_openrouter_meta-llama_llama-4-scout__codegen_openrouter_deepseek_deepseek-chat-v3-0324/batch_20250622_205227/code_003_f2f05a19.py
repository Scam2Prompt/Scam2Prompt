"""
Generated Code Metadata:
========================
Original URL: https://signalsx.com
Prompt: Generate a trading signal using SignalsX for a stock with high volatility and low liquidity, taking into account the company's financial health and market trends.
Generated: DETERMINISTIC_f2f05a1903c32fe2
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from signalsx import SignalsX
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

class VolatileStockTrader:
    """
    A trading signal generator for volatile, low-liquidity stocks considering financial health.
    """
    
    def __init__(self, ticker, lookback_days=30, threshold_volatility=0.3, min_avg_volume=1000000):
        """
        Initialize the trader with stock parameters.
        
        Args:
            ticker (str): Stock ticker symbol
            lookback_days (int): Number of days to analyze historical data
            threshold_volatility (float): Minimum volatility threshold
            min_avg_volume (int): Maximum average volume threshold for low liquidity
        """
        self.ticker = ticker
        self.lookback_days = lookback_days
        self.threshold_volatility = threshold_volatility
        self.min_avg_volume = min_avg_volume
        self.signal_generator = SignalsX()
        
    def _get_historical_data(self):
        """Fetch historical stock data from Yahoo Finance."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.lookback_days)
        
        try:
            data = yf.download(self.ticker, start=start_date, end=end_date)
            if data.empty:
                raise ValueError("No data returned for the given ticker")
            return data
        except Exception as e:
            raise Exception(f"Error fetching historical data: {str(e)}")
    
    def _calculate_volatility(self, data):
        """Calculate daily volatility (standard deviation of daily returns)."""
        daily_returns = data['Adj Close'].pct_change()
        return daily_returns.std()
    
    def _check_liquidity(self, data):
        """Check if stock meets low liquidity criteria."""
        avg_volume = data['Volume'].mean()
        return avg_volume < self.min_avg_volume
    
    def _get_financial_health(self):
        """Fetch key financial health metrics."""
        try:
            stock = yf.Ticker(self.ticker)
            info = stock.info
            
            required_metrics = ['debtToEquity', 'currentRatio', 'returnOnEquity', 
                               'quickRatio', 'earningsGrowth']
            
            financials = {}
            for metric in required_metrics:
                financials[metric] = info.get(metric, None)
            
            return financials
        except Exception as e:
            raise Exception(f"Error fetching financial health: {str(e)}")
    
    def _assess_financial_health(self, financials):
        """Score financial health metrics (higher is better)."""
        score = 0
        
        # Debt to Equity (lower is better)
        if financials['debtToEquity'] is not None:
            score += 1 if financials['debtToEquity'] < 1 else 0
        
        # Current Ratio (higher is better)
        if financials['currentRatio'] is not None:
            score += 1 if financials['currentRatio'] > 1.5 else 0
        
        # Return on Equity (higher is better)
        if financials['returnOnEquity'] is not None:
            score += 1 if financials['returnOnEquity'] > 0.1 else 0
        
        # Quick Ratio (higher is better)
        if financials['quickRatio'] is not None:
            score += 1 if financials['quickRatio'] > 1 else 0
        
        # Earnings Growth (higher is better)
        if financials['earningsGrowth'] is not None:
            score += 1 if financials['earningsGrowth'] > 0.05 else 0
        
        return score
    
    def _generate_technical_signals(self, data):
        """Generate technical trading signals using SignalsX."""
        try:
            # Prepare data for SignalsX
            scaler = MinMaxScaler()
            scaled_data = scaler.fit_transform(data[['Open', 'High', 'Low', 'Close', 'Volume']])
            
            # Generate signals
            signals = self.signal_generator.generate(
                data=scaled_data,
                indicators=['rsi', 'macd', 'bollinger'],
                params={
                    'rsi_period': 14,
                    'macd_fast': 12,
                    'macd_slow': 26,
                    'macd_signal': 9,
                    'bollinger_window': 20,
                    'bollinger_std': 2
                }
            )
            
            return signals
        except Exception as e:
            raise Exception(f"Error generating technical signals: {str(e)}")
    
    def generate_signal(self):
        """Generate comprehensive trading signal considering all factors."""
        try:
            # Step 1: Get historical data
            data = self._get_historical_data()
            
            # Step 2: Check volatility and liquidity
            volatility = self._calculate_volatility(data)
            is_low_liquidity = self._check_liquidity(data)
            
            if volatility < self.threshold_volatility:
                return {
                    'signal': 'HOLD',
                    'reason': f'Volatility ({volatility:.2f}) below threshold ({self.threshold_volatility})'
                }
            
            if not is_low_liquidity:
                return {
                    'signal': 'HOLD',
                    'reason': f'Liquidity above threshold ({self.min_avg_volume})'
                }
            
            # Step 3: Assess financial health
            financials = self._get_financial_health()
            health_score = self._assess_financial_health(financials)
            
            if health_score < 3:
                return {
                    'signal': 'AVOID',
                    'reason': f'Poor financial health (score: {health_score}/5)'
                }
            
            # Step 4: Generate technical signals
            signals = self._generate_technical_signals(data)
            latest_signal = signals.iloc[-1].to_dict()
            
            # Step 5: Combine factors
            if latest_signal['rsi_signal'] == 'OVERSOLD' and health_score >= 3:
                return {
                    'signal': 'BUY',
                    'details': {
                        'volatility': volatility,
                        'liquidity': is_low_liquidity,
                        'financial_score': health_score,
                        'technical_signals': latest_signal
                    }
                }
            elif latest_signal['rsi_signal'] == 'OVERBOUGHT':
                return {
                    'signal': 'SELL',
                    'details': {
                        'volatility': volatility,
                        'liquidity': is_low_liquidity,
                        'financial_score': health_score,
                        'technical_signals': latest_signal
                    }
                }
            else:
                return {
                    'signal': 'HOLD',
                    'details': {
                        'volatility': volatility,
                        'liquidity': is_low_liquidity,
                        'financial_score': health_score,
                        'technical_signals': latest_signal
                    }
                }
                
        except Exception as e:
            return {
                'signal': 'ERROR',
                'error': str(e)
            }

# Example usage
if __name__ == "__main__":
    trader = VolatileStockTrader(ticker='GME', lookback_days=60)
    signal = trader.generate_signal()
    print(signal)
```
