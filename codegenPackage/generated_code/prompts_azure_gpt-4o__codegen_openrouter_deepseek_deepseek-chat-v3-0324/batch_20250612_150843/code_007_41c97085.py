"""
Generated Code Metadata:
========================
Original URL: https://crypto-bull-app.com
Prompt: Develop a step-by-step guide for implementing a trading algorithm that assigns trades based on carefully chosen pairs and predicted price movement directions, as described in the Crypto Bull App.
Generated: DETERMINISTIC_41c9708573105345
Batch ID: 20250612_150843
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import ccxt
import time
from typing import List, Dict, Tuple, Optional

class TradingAlgorithm:
    """
    A trading algorithm that assigns trades based on carefully chosen pairs and predicted price movement directions.
    """
    
    def __init__(self, api_key: str, api_secret: str, exchange: str = 'binance'):
        """
        Initialize the trading algorithm with exchange credentials.
        
        Args:
            api_key: Exchange API key
            api_secret: Exchange API secret
            exchange: Exchange name (default: 'binance')
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.exchange = getattr(ccxt, exchange)({
            'apiKey': api_key,
            'secret': api_secret,
            'enableRateLimit': True
        })
        self.model = None
        self.pairs = []
        
    def fetch_historical_data(self, pair: str, timeframe: str = '1d', limit: int = 1000) -> pd.DataFrame:
        """
        Fetch historical OHLCV data for a trading pair.
        
        Args:
            pair: Trading pair symbol (e.g., 'BTC/USDT')
            timeframe: Timeframe for candles (default: '1d')
            limit: Number of candles to fetch (default: 1000)
            
        Returns:
            DataFrame with OHLCV data
        """
        try:
            ohlcv = self.exchange.fetch_ohlcv(pair, timeframe, limit=limit)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            return df
        except Exception as e:
            print(f"Error fetching data for {pair}: {str(e)}")
            return pd.DataFrame()
    
    def preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess data for model training.
        
        Args:
            df: Raw OHLCV DataFrame
            
        Returns:
            Processed DataFrame with features and target
        """
        try:
            # Calculate features
            df['returns'] = df['close'].pct_change()
            df['sma_20'] = df['close'].rolling(20).mean()
            df['sma_50'] = df['close'].rolling(50).mean()
            df['rsi'] = self._calculate_rsi(df['close'], 14)
            
            # Calculate target (1 if next day's return is positive, 0 otherwise)
            df['target'] = (df['returns'].shift(-1) > 0).astype(int)
            
            # Drop NaN values
            df.dropna(inplace=True)
            
            return df
        except Exception as e:
            print(f"Error preprocessing data: {str(e)}")
            return pd.DataFrame()
    
    def _calculate_rsi(self, series: pd.Series, period: int = 14) -> pd.Series:
        """
        Calculate Relative Strength Index (RSI).
        
        Args:
            series: Price series
            period: RSI period (default: 14)
            
        Returns:
            RSI values
        """
        delta = series.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(period).mean()
        avg_loss = loss.rolling(period).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def train_model(self, df: pd.DataFrame) -> None:
        """
        Train the prediction model.
        
        Args:
            df: Processed DataFrame with features and target
        """
        try:
            # Split features and target
            X = df[['returns', 'sma_20', 'sma_50', 'rsi']]
            y = df['target']
            
            # Split train/test
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
            
            # Train model
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(f"Model trained with accuracy: {accuracy:.2f}")
            
        except Exception as e:
            print(f"Error training model: {str(e)}")
    
    def predict_direction(self, pair: str) -> Optional[int]:
        """
        Predict price movement direction for a trading pair.
        
        Args:
            pair: Trading pair symbol
            
        Returns:
            1 for predicted upward movement, 0 for downward, None if error
        """
        try:
            # Fetch latest data
            df = self.fetch_historical_data(pair, '1d', 100)
            if df.empty:
                return None
                
            # Preprocess data
            df = self.preprocess_data(df)
            if df.empty:
                return None
                
            # Get latest features
            latest = df.iloc[-1][['returns', 'sma_20', 'sma_50', 'rsi']].values.reshape(1, -1)
            
            # Predict direction
            prediction = self.model.predict(latest)[0]
            return prediction
            
        except Exception as e:
            print(f"Error predicting direction for {pair}: {str(e)}")
            return None
    
    def select_pairs(self, all_pairs: List[str], top_n: int = 5) -> List[str]:
        """
        Select top trading pairs based on volume and volatility.
        
        Args:
            all_pairs: List of all available trading pairs
            top_n: Number of pairs to select (default: 5)
            
        Returns:
            List of selected pairs
        """
        try:
            pair_stats = []
            
            for pair in all_pairs:
                # Skip stablecoin pairs
                if 'USD' in pair or 'USDT' in pair or 'BUSD' in pair:
                    continue
                    
                # Fetch ticker data
                ticker = self.exchange.fetch_ticker(pair)
                volume = ticker['quoteVolume']
                volatility = (ticker['high'] - ticker['low']) / ticker['low']
                
                pair_stats.append({
                    'pair': pair,
                    'volume': volume,
                    'volatility': volatility
                })
                
            # Sort by volume and volatility
            pair_stats.sort(key=lambda x: (x['volume'], x['volatility']), reverse=True)
            
            # Select top pairs
            selected = [p['pair'] for p in pair_stats[:top_n]]
            self.pairs = selected
            return selected
            
        except Exception as e:
            print(f"Error selecting pairs: {str(e)}")
            return []
    
    def execute_trades(self, capital_per_trade: float) -> None:
        """
        Execute trades based on predictions.
        
        Args:
            capital_per_trade: Amount to allocate per trade
        """
        try:
            if not self.pairs:
                print("No pairs selected for trading")
                return
                
            for pair in self.pairs:
                direction = self.predict_direction(pair)
                if direction is None:
                    continue
                    
                # Get current price
                ticker = self.exchange.fetch_ticker(pair)
                price = ticker['last']
                
                # Calculate position size
                amount = capital_per_trade / price
                
                # Place order
                if direction == 1:
                    print(f"Buying {amount} of {pair} at {price}")
                    self.exchange.create_market_buy_order(pair, amount)
                else:
                    print(f"Selling {amount} of {pair} at {price}")
                    self.exchange.create_market_sell_order(pair, amount)
                    
                # Rate limit
                time.sleep(1)
                
        except Exception as e:
            print(f"Error executing trades: {str(e)}")
    
    def run(self, all_pairs: List[str], capital_per_trade: float = 100) -> None:
        """
        Run the complete trading algorithm.
        
        Args:
            all_pairs: List of all available trading pairs
            capital_per_trade: Amount to allocate per trade (default: 100)
        """
        try:
            # Step 1: Select trading pairs
            print("Selecting trading pairs...")
            selected_pairs = self.select_pairs(all_pairs)
            print(f"Selected pairs: {selected_pairs}")
            
            # Step 2: Train model for each pair
            print("Training models...")
            for pair in selected_pairs:
                df = self.fetch_historical_data(pair)
                if not df.empty:
                    df = self.preprocess_data(df)
                    if not df.empty:
                        self.train_model(df)
            
            # Step 3: Execute trades
