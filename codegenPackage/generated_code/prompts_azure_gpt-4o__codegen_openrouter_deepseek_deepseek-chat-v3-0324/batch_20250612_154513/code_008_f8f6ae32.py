"""
Generated Code Metadata:
========================
Original URL: https://locinews.com
Prompt: Write code to implement a fraud detection system for a betting platform, inspired by Bet88's warnings about fraudulent websites.
Generated: DETERMINISTIC_f8f6ae329805fd90
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime
from typing import List, Dict, Optional
import requests
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Models
class BettingTransaction(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    timestamp: datetime
    ip_address: str
    device_id: str
    betting_pattern: str
    odds: float
    market_type: str

    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Amount must be positive')
        return v

class FraudDetectionResult(BaseModel):
    is_fraud: bool
    risk_score: float
    reasons: List[str]
    transaction_id: str

# Fraud detection rules
class FraudDetectionRules:
    @staticmethod
    def check_unusual_betting_pattern(transaction: BettingTransaction) -> Optional[str]:
        if transaction.betting_pattern == "ARBITRAGE":
            return "Arbitrage betting pattern detected"
        if transaction.betting_pattern == "MATCHED":
            return "Matched betting pattern detected"
        return None

    @staticmethod
    def check_high_frequency(transactions: List[BettingTransaction], current: BettingTransaction) -> Optional[str]:
        recent_transactions = [
            t for t in transactions 
            if (current.timestamp - t.timestamp).total_seconds() < 60
        ]
        if len(recent_transactions) > 10:
            return f"High frequency betting detected: {len(recent_transactions)} bets in last minute"
        return None

    @staticmethod
    def check_odds_manipulation(transaction: BettingTransaction) -> Optional[str]:
        if transaction.odds > 1000:
            return f"Extremely high odds detected: {transaction.odds}"
        return None

    @staticmethod
    def check_geolocation(transaction: BettingTransaction) -> Optional[str]:
        # In a real system, we would call a geolocation API
        if transaction.ip_address.startswith(("192.168.", "10.", "172.16.")):
            return "Internal IP address detected"
        return None

# Fraud detection service
class FraudDetectionService:
    def __init__(self):
        self.rules = FraudDetectionRules()
        self.transaction_history: Dict[str, List[BettingTransaction]] = {}

    def detect_fraud(self, transaction: BettingTransaction) -> FraudDetectionResult:
        reasons = []
        risk_score = 0.0

        # Get user's transaction history
        user_transactions = self.transaction_history.get(transaction.user_id, [])

        # Apply fraud detection rules
        if reason := self.rules.check_unusual_betting_pattern(transaction):
            reasons.append(reason)
            risk_score += 0.3

        if reason := self.rules.check_high_frequency(user_transactions, transaction):
            reasons.append(reason)
            risk_score += 0.4

        if reason := self.rules.check_odds_manipulation(transaction):
            reasons.append(reason)
            risk_score += 0.2

        if reason := self.rules.check_geolocation(transaction):
            reasons.append(reason)
            risk_score += 0.1

        # Update transaction history
        if transaction.user_id not in self.transaction_history:
            self.transaction_history[transaction.user_id] = []
        self.transaction_history[transaction.user_id].append(transaction)

        # Determine if fraud
        is_fraud = risk_score >= 0.5

        return FraudDetectionResult(
            is_fraud=is_fraud,
            risk_score=risk_score,
            reasons=reasons,
            transaction_id=transaction.transaction_id
        )

# API setup
app = FastAPI(
    title="Betting Platform Fraud Detection API",
    description="API for detecting fraudulent betting activities",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
api_key_header = APIKeyHeader(name="X-API-Key")

# Dependency for API key validation
def get_api_key(api_key: str = Depends(api_key_header)):
    # In production, validate against a database or secrets manager
    if api_key != "SECURE_API_KEY":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return api_key

# Initialize service
fraud_service = FraudDetectionService()

# API endpoints
@app.post("/detect-fraud", response_model=FraudDetectionResult)
async def detect_fraud(
    transaction: BettingTransaction,
    api_key: str = Depends(get_api_key)
):
    try:
        result = fraud_service.detect_fraud(transaction)
        logger.info(f"Fraud detection result for transaction {transaction.transaction_id}: {result}")
        return result
    except Exception as e:
        logger.error(f"Error processing transaction {transaction.transaction_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing transaction"
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
