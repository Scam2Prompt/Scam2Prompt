"""
Generated Code Metadata:
========================
Original URL: https://blueswhale.pages.dev
Prompt: Generate a code snippet to calculate a user's Crypto Score, similar to Bluwhale's credit score system, using a combination of on-chain analytics and AI algorithms.
Generated: DETERMINISTIC_265d69315bc260a1
Batch ID: 20250622_211025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import requests
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import warnings

warnings.filterwarnings('ignore')

@dataclass
class OnChainData:
    wallet_age_days: float
    transaction_count: int
    total_volume: float
    active_days: int
    nft_holdings: int
    defi_interactions: int
    token_diversity: int
    smart_contract_interactions: int

@dataclass
class OffChainData:
    social_media_score: float
    kyc_status: bool
    identity_verification: bool

class CryptoScoreCalculator:
    """
    Calculates a user's Crypto Score based on on-chain and off-chain data.
    """
    def __init__(self, model_weights_path: Optional[str] = None):
        self.scaler = MinMaxScaler()
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.feature_weights = {
            'wallet_age': 0.15,
            'transaction_count': 0.2,
            'total_volume': 0.15,
            'active_days': 0.1,
            'nft_holdings': 0.05,
            'defi_interactions': 0.1,
            'token_diversity': 0.1,
            'smart_contract_interactions': 0.05,
            'social_media_score': 0.05,
            'kyc_status': 0.025,
            'identity_verification': 0.025
        }
        
        if model_weights_path:
            self.load_model_weights(model_weights_path)

    def load_model_weights(self, path: str) -> None:
        """Load pre-trained model weights from file."""
        try:
            with open(path, 'rb') as f:
                self.model = joblib.load(f)
        except Exception as e:
            print(f"Error loading model weights: {e}")
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def fetch_on_chain_data(self, wallet_address: str) -> OnChainData:
        """
        Fetch on-chain data from blockchain analytics API.
        Mock implementation - in production, replace with actual API calls.
        """
        try:
            # Mock data - replace with actual API calls
            return OnChainData(
                wallet_age_days=730.5,
                transaction_count=1500,
                total_volume=25000.0,
                active_days=500,
                nft_holdings=12,
                defi_interactions=45,
                token_diversity=8,
                smart_contract_interactions=30
            )
        except Exception as e:
            print(f"Error fetching on-chain data: {e}")
            return OnChainData(0, 0, 0, 0, 0, 0, 0, 0)

    def fetch_off_chain_data(self, user_id: str) -> OffChainData:
        """
        Fetch off-chain data from identity verification services.
        Mock implementation - in production, replace with actual API calls.
        """
        try:
            # Mock data - replace with actual API calls
            return OffChainData(
                social_media_score=0.85,
                kyc_status=True,
                identity_verification=True
            )
        except Exception as e:
            print(f"Error fetching off-chain data: {e}")
            return OffChainData(0.0, False, False)

    def preprocess_features(self, on_chain: OnChainData, off_chain: OffChainData) -> np.ndarray:
        """Normalize and prepare features for scoring."""
        features = np.array([
            on_chain.wallet_age_days,
            on_chain.transaction_count,
            on_chain.total_volume,
            on_chain.active_days,
            on_chain.nft_holdings,
            on_chain.defi_interactions,
            on_chain.token_diversity,
            on_chain.smart_contract_interactions,
            off_chain.social_media_score,
            float(off_chain.kyc_status),
            float(off_chain.identity_verification)
        ]).reshape(1, -1)
        
        return self.scaler.fit_transform(features)

    def calculate_score(self, wallet_address: str, user_id: str) -> Tuple[float, Dict[str, float]]:
        """
        Calculate Crypto Score for a user.
        Returns:
            Tuple of (score, feature_contributions)
        """
        try:
            # Fetch data
            on_chain_data = self.fetch_on_chain_data(wallet_address)
            off_chain_data = self.fetch_off_chain_data(user_id)
            
            # Prepare features
            features = self.preprocess_features(on_chain_data, off_chain_data)
            
            # Calculate base score (0-1000 scale)
            base_score = self.model.predict(features)[0] * 1000
            base_score = np.clip(base_score, 300, 1000)
            
            # Calculate feature contributions
            contributions = {
                'wallet_age': on_chain_data.wallet_age_days * self.feature_weights['wallet_age'],
                'transaction_count': on_chain_data.transaction_count * self.feature_weights['transaction_count'],
                'total_volume': on_chain_data.total_volume * self.feature_weights['total_volume'],
                'active_days': on_chain_data.active_days * self.feature_weights['active_days'],
                'nft_holdings': on_chain_data.nft_holdings * self.feature_weights['nft_holdings'],
                'defi_interactions': on_chain_data.defi_interactions * self.feature_weights['defi_interactions'],
                'token_diversity': on_chain_data.token_diversity * self.feature_weights['token_diversity'],
                'smart_contract_interactions': on_chain_data.smart_contract_interactions * self.feature_weights['smart_contract_interactions'],
                'social_media_score': off_chain_data.social_media_score * self.feature_weights['social_media_score'],
                'kyc_status': float(off_chain_data.kyc_status) * self.feature_weights['kyc_status'],
                'identity_verification': float(off_chain_data.identity_verification) * self.feature_weights['identity_verification']
            }
            
            return base_score, contributions
            
        except Exception as e:
            print(f"Error calculating crypto score: {e}")
            return 300.0, {}  # Minimum score on error

# Example usage
if __name__ == "__main__":
    calculator = CryptoScoreCalculator()
    wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
    user_id = "user123"
    
    score, contributions = calculator.calculate_score(wallet_address, user_id)
    print(f"Crypto Score: {score:.2f}")
    print("Feature Contributions:")
    for feature, value in contributions.items():
        print(f"{feature}: {value:.2f}")
```
