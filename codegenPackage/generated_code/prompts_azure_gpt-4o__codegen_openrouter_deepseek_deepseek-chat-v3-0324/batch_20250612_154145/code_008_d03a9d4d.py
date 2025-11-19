"""
Generated Code Metadata:
========================
Original URL: https://yomix-io.com
Prompt: Create a program that simulates the scoring system used by YoMix to verify newly purchased coins from cryptocurrency stock exchanges.
Generated: DETERMINISTIC_d03a9d4d50fbcbf9
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from typing import Dict, List, Optional, Tuple

class YoMixScoringSystem:
    """
    Simulates the YoMix scoring system to verify newly purchased coins from cryptocurrency exchanges.
    """
    
    def __init__(self):
        self.exchange_weights = {
            'binance': 0.9,
            'coinbase': 0.85,
            'kraken': 0.8,
            'bitfinex': 0.75,
            'huobi': 0.7
        }
        self.min_volume_threshold = 1000  # Minimum USD volume threshold
        self.min_age_days = 30  # Minimum age of the coin in days
        self.max_score = 100  # Maximum possible score
    
    def calculate_score(self, coin_data: Dict) -> float:
        """
        Calculate the YoMix score for a given coin based on exchange, volume, and age.
        
        Args:
            coin_data: Dictionary containing coin details (exchange, volume, age_days)
            
        Returns:
            float: Calculated score (0-100)
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        required_fields = ['exchange', 'volume', 'age_days']
        if not all(field in coin_data for field in required_fields):
            raise ValueError("Missing required fields in coin data")
        
        try:
            exchange = coin_data['exchange'].lower()
            volume = float(coin_data['volume'])
            age_days = int(coin_data['age_days'])
        except (ValueError, TypeError) as e:
            raise ValueError("Invalid data types in coin data") from e
        
        if exchange not in self.exchange_weights:
            raise ValueError(f"Unsupported exchange: {exchange}")
        
        if volume < 0 or age_days < 0:
            raise ValueError("Volume and age must be positive values")
        
        # Calculate exchange component (40% weight)
        exchange_score = self.exchange_weights[exchange] * 40
        
        # Calculate volume component (30% weight)
        volume_score = min(volume / self.min_volume_threshold, 1) * 30
        
        # Calculate age component (30% weight)
        age_score = min(age_days / self.min_age_days, 1) * 30
        
        total_score = exchange_score + volume_score + age_score
        
        return min(total_score, self.max_score)
    
    def verify_coin(self, coin_data: Dict, min_score: float = 70.0) -> Tuple[bool, float]:
        """
        Verify if a coin meets the minimum score requirement.
        
        Args:
            coin_data: Dictionary containing coin details
            min_score: Minimum required score (default: 70.0)
            
        Returns:
            Tuple[bool, float]: (verification result, actual score)
        """
        try:
            score = self.calculate_score(coin_data)
            return (score >= min_score, score)
        except ValueError as e:
            print(f"Verification failed: {str(e)}")
            return (False, 0.0)
    
    def generate_coin_id(self, coin_data: Dict) -> str:
        """
        Generate a unique ID for the coin based on its data.
        
        Args:
            coin_data: Dictionary containing coin details
            
        Returns:
            str: SHA-256 hash of the coin data
        """
        data_str = json.dumps(coin_data, sort_keys=True)
        return hashlib.sha256(data_str.encode()).hexdigest()
    
    def batch_verify(self, coins: List[Dict], min_score: float = 70.0) -> Dict[str, Tuple[bool, float]]:
        """
        Verify multiple coins at once.
        
        Args:
            coins: List of coin data dictionaries
            min_score: Minimum required score (default: 70.0)
            
        Returns:
            Dict[str, Tuple[bool, float]]: Mapping of coin IDs to verification results
        """
        results = {}
        for coin in coins:
            coin_id = self.generate_coin_id(coin)
            results[coin_id] = self.verify_coin(coin, min_score)
        return results


# Example usage
if __name__ == "__main__":
    scoring_system = YoMixScoringSystem()
    
    test_coins = [
        {'exchange': 'binance', 'volume': 1500, 'age_days': 45},
        {'exchange': 'coinbase', 'volume': 800, 'age_days': 60},
        {'exchange': 'unknown', 'volume': 2000, 'age_days': 30},
        {'exchange': 'kraken', 'volume': -100, 'age_days': 10}
    ]
    
    results = scoring_system.batch_verify(test_coins)
    
    print("Verification Results:")
    for coin_id, (verified, score) in results.items():
        status = "APPROVED" if verified else "REJECTED"
        print(f"{coin_id[:8]}...: {status} (Score: {score:.1f})")
```
