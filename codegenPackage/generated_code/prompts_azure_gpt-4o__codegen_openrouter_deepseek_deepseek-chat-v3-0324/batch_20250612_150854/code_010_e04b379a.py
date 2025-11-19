"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.net
Prompt: Create an AI model to detect early signs of trading flow shifts and order intensity changes in cryptocurrency markets, inspired by Stable Capital's early shift detection features.
Generated: DETERMINISTIC_e04b379a5515a5f5
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score
import joblib
import logging
from datetime import datetime
from typing import Tuple, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TradingFlowAnalyzer:
    """
    AI model to detect early signs of trading flow shifts and order intensity changes
    in cryptocurrency markets.
    """
    
    def __init__(self, model_path: Optional[str] = None):
        """
        Initialize the analyzer.
        
        Args:
            model_path: Path to load a pre-trained model. If None, creates new model.
        """
        self.model = None
        self.scaler = StandardScaler()
        self.features = [
            'order_book_imbalance',
            'trade_volume_ratio',
            'price_velocity',
            'order_flow_imbalance',
            'liquidity_consumption_rate',
            'spread_volatility'
        ]
        
        if model_path:
            self.load_model(model_path)
        else:
            self._initialize_model()
    
    def _initialize_model(self) -> None:
        """Initialize the isolation forest model with pipeline."""
        self.model = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', IsolationForest(
                n_estimators=100,
                contamination=0.05,
                random_state=42,
                n_jobs=-1
            ))
        ])
    
    def preprocess_data(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess raw market data into features for the model.
        
        Args:
            raw_data: DataFrame containing raw market data
            
        Returns:
            Processed DataFrame with engineered features
        """
        try:
            # Calculate features
            processed_data = pd.DataFrame(index=raw_data.index)
            
            # Order book imbalance
            processed_data['order_book_imbalance'] = (
                raw_data['bid_volume'] - raw_data['ask_volume']
            ) / (raw_data['bid_volume'] + raw_data['ask_volume'])
            
            # Trade volume ratio
            processed_data['trade_volume_ratio'] = (
                raw_data['buy_volume'] / raw_data['sell_volume']
            ).replace([np.inf, -np.inf], np.nan).fillna(1.0)
            
            # Price velocity (price change over time)
            processed_data['price_velocity'] = raw_data['mid_price'].pct_change().rolling(5).mean()
            
            # Order flow imbalance
            processed_data['order_flow_imbalance'] = (
                raw_data['buy_order_count'] - raw_data['sell_order_count']
            ) / (raw_data['buy_order_count'] + raw_data['sell_order_count'])
            
            # Liquidity consumption rate
            processed_data['liquidity_consumption_rate'] = (
                raw_data['taker_buy_volume'] - raw_data['taker_sell_volume']
            ).rolling(10).std()
            
            # Spread volatility
            processed_data['spread_volatility'] = (
                raw_data['ask_price'] - raw_data['bid_price']
            ).rolling(10).std()
            
            # Forward fill any remaining NA values
            processed_data = processed_data.ffill().bfill()
            
            return processed_data[self.features]
        
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise
    
    def train(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> None:
        """
        Train the model on historical data.
        
        Args:
            X: Features DataFrame
            y: Optional labels (not used for unsupervised learning)
        """
        try:
            logger.info("Starting model training...")
            self.model.fit(X)
            logger.info("Model training completed successfully.")
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
    
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Predict anomalies in trading flow.
        
        Args:
            X: Features DataFrame
            
        Returns:
            Array of predictions (-1 for anomaly, 1 for normal)
        """
        try:
            return self.model.predict(X)
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            raise
    
    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> Dict[str, float]:
        """
        Evaluate model performance on labeled data.
        
        Args:
            X: Features DataFrame
            y: True labels (1 for normal, -1 for anomaly)
            
        Returns:
            Dictionary of evaluation metrics
        """
        try:
            y_pred = self.predict(X)
            report = classification_report(y, y_pred, output_dict=True)
            f1 = f1_score(y, y_pred, average='weighted')
            
            return {
                'precision': report['weighted avg']['precision'],
                'recall': report['weighted avg']['recall'],
                'f1_score': f1,
                'accuracy': report['accuracy']
            }
        except Exception as e:
            logger.error(f"Error during evaluation: {str(e)}")
            raise
    
    def save_model(self, filepath: str) -> None:
        """
        Save the trained model to disk.
        
        Args:
            filepath: Path to save the model
        """
        try:
            joblib.dump(self.model, filepath)
            logger.info(f"Model saved successfully to {filepath}")
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise
    
    def load_model(self, filepath: str) -> None:
        """
        Load a trained model from disk.
        
        Args:
            filepath: Path to the saved model
        """
        try:
            self.model = joblib.load(filepath)
            logger.info(f"Model loaded successfully from {filepath}")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
    
    def detect_shift(self, market_data: pd.DataFrame) -> Tuple[bool, float]:
        """
        Detect trading flow shifts in real-time market data.
        
        Args:
            market_data: DataFrame containing current market data
            
        Returns:
            Tuple of (is_shift_detected, anomaly_score)
        """
        try:
            # Preprocess the data
            features = self.preprocess_data(market_data)
            
            # Get the latest data point
            latest_features = features.iloc[-1:].values.reshape(1, -1)
            
            # Predict anomaly
            prediction = self.predict(latest_features)[0]
            
            # Calculate anomaly score
            anomaly_score = self.model.decision_function(latest_features)[0]
            
            return (prediction == -1, anomaly_score)
        
        except Exception as e:
            logger.error(f"Error during shift detection: {str(e)}")
            raise

def prepare_training_data(data_path: str) -> Tuple[pd.DataFrame, Optional[pd.Series]]:
    """
    Prepare training data from historical market data.
    
    Args:
        data_path: Path to historical data CSV file
        
    Returns:
        Tuple of (features, labels) where labels may be None for unsupervised learning
    """
    try:
        data = pd.read_csv(data_path, parse_dates=['timestamp'])
        data.set_index('timestamp', inplace=True)
        
        analyzer = TradingFlowAnalyzer()
        features = analyzer.preprocess_data(data)
        
        # In a real implementation, you would have labeled data
        # For this example, we'll return None for labels
        return features, None
    
    except Exception as e:
        logger.error(f"Error preparing training data: {str(e)}")
        raise

def main():
    """Main execution function for training and testing the model."""
    try:
        # Example usage
        data_path = 'historical_market_data.csv'
        
        # Prepare data
        features, _ = prepare_training_data(data_path)
        
        # Split data (even though we don't have labels)
        X_train, X_test = train_test_split(features, test_size=0.2, random_state=42)
        
        # Initialize and train model
        analyzer = TradingFlowAnalyzer()
        analyzer.train(X_train)
        
        # Save model
        analyzer.save_model('trading_flow_model.joblib')
        
        # Load model (demonstration)
        loaded_analyzer = TradingFlowAnalyzer('trading_flow_model.joblib')
        
        # Simulate real-time detection
        sample_data = X_test.sample(1)
        is_shift, score = loaded_analyzer.detect_shift(sample_data)
        
        logger.info(f"Shift detected: {is_shift} with score: {score:.4f}")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise

if __name__ == '__main__':
    main()
```
