"""
Generated Code Metadata:
========================
Original URL: https://sweepstake-seven.vercel.app
Prompt: "Write a Python script to create a simple prediction market for a sweepstakes using Vercel as the deployment platform."
Generated: DETERMINISTIC_fc5e5f5cd45385d0
Batch ID: 20250622_205124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sweepstakes_market.py

"""
A simple prediction market for a sweepstakes using Python.
This script is designed to be deployed on Vercel as a serverless function.
Users can place bets on outcomes, and the market calculates payouts based on probabilities.

Requirements:
- Python 3.9+
- Install dependencies: `pip install fastapi uvicorn`

Deployment:
- Place this script in a Vercel project under the `api/` directory.
- Vercel will automatically detect it as a serverless function.
"""

from fastapi import FastAPI, HTTPException, Query
from typing import Dict, List
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# In-memory database for simplicity (not suitable for production)
# In production, use a proper database like PostgreSQL or MongoDB.
market_data = {
    "entries": {},  # Format: {"user_id": {"outcome": str, "amount": float}}
    "outcomes": {},  # Format: {"outcome": {"total_bets": float, "probability": float}}
}

# Models for request validation
class BetRequest(BaseModel):
    user_id: str
    outcome: str
    amount: float

class OutcomeRequest(BaseModel):
    outcome: str
    probability: float

@app.post("/place_bet/")
async def place_bet(bet: BetRequest):
    """
    Endpoint to place a bet on a specific outcome.
    """
    if bet.amount <= 0:
        raise HTTPException(status_code=400, detail="Bet amount must be greater than zero.")
    
    if bet.outcome not in market_data["outcomes"]:
        raise HTTPException(status_code=404, detail="Outcome not found in the market.")
    
    # Record the bet
    market_data["entries"][bet.user_id] = {"outcome": bet.outcome, "amount": bet.amount}
    market_data["outcomes"][bet.outcome]["total_bets"] += bet.amount
    
    return {"message": "Bet placed successfully.", "data": bet}

@app.post("/add_outcome/")
async def add_outcome(outcome: OutcomeRequest):
    """
    Endpoint to add a new outcome to the market.
    """
    if outcome.outcome in market_data["outcomes"]:
        raise HTTPException(status_code=400, detail="Outcome already exists.")
    
    if not (0 <= outcome.probability <= 1):
        raise HTTPException(status_code=400, detail="Probability must be between 0 and 1.")
    
    # Add the outcome
    market_data["outcomes"][outcome.outcome] = {"total_bets": 0.0, "probability": outcome.probability}
    
    return {"message": "Outcome added successfully.", "data": outcome}

@app.get("/market_status/")
async def market_status():
    """
    Endpoint to retrieve the current status of the market.
    """
    return {"market_data": market_data}

@app.get("/calculate_payouts/")
async def calculate_payouts():
    """
    Endpoint to calculate payouts for all users based on the market probabilities.
    """
    if not market_data["entries"]:
        raise HTTPException(status_code=404, detail="No bets placed yet.")
    
    payouts = {}
    for user_id, bet in market_data["entries"].items():
        outcome = bet["outcome"]
        amount = bet["amount"]
        probability = market_data["outcomes"][outcome]["probability"]
        
        # Calculate payout (simple formula: amount * (1 / probability))
        if probability > 0:
            payout = amount * (1 / probability)
        else:
            payout = 0.0
        
        payouts[user_id] = {"outcome": outcome, "bet_amount": amount, "payout": payout}
    
    return {"payouts": payouts}

# Error handling for unhandled routes
@app.get("/")
async def root():
    """
    Root endpoint to indicate the API is running.
    """
    return {"message": "Prediction Market API is running. Use the endpoints to interact with the market."}
```
