"""
Generated Code Metadata:
========================
Original URL: https://ait.claims
Prompt: "Generate a Python API for handling insurance claims using AI."
Generated: DETERMINISTIC_e90056e8eedba62d
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# insurance_claims_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Define data model for insurance claim
class InsuranceClaim(BaseModel):
    claim_id: int
    claimant_name: str
    claim_amount: float
    claim_reason: str
    claim_date: str

# Define data model for AI prediction
class PredictionRequest(BaseModel):
    claim_amount: float
    claim_reason: str

# Sample in-memory data store (replace with a database in production)
claims_data = [
    InsuranceClaim(claim_id=1, claimant_name="John Doe", claim_amount=1000.0, claim_reason="Accident", claim_date="2022-01-01"),
    InsuranceClaim(claim_id=2, claimant_name="Jane Doe", claim_amount=500.0, claim_reason="Theft", claim_date="2022-01-15"),
]

# Load sample dataset for AI model training
try:
    df = pd.DataFrame({
        'claim_amount': [1000.0, 500.0, 2000.0, 1500.0, 2500.0],
        'claim_reason': ['Accident', 'Theft', 'Accident', 'Theft', 'Accident'],
        'approved': [1, 0, 1, 0, 1]
    })
except Exception as e:
    logger.error(f"Failed to load dataset: {e}")

# Train AI model
try:
    X = df[['claim_amount', pd.Categorical(df['claim_reason']).codes]]
    y = df['approved']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
except Exception as e:
    logger.error(f"Failed to train AI model: {e}")

# API endpoint to submit a new insurance claim
@app.post("/claims/")
async def create_claim(claim: InsuranceClaim):
    try:
        claims_data.append(claim)
        return {"message": f"Claim {claim.claim_id} created successfully"}
    except Exception as e:
        logger.error(f"Failed to create claim: {e}")
        raise HTTPException(status_code=500, detail="Failed to create claim")

# API endpoint to get all insurance claims
@app.get("/claims/")
async def get_claims():
    try:
        return claims_data
    except Exception as e:
        logger.error(f"Failed to retrieve claims: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve claims")

# API endpoint to make a prediction using the AI model
@app.post("/predict/")
async def make_prediction(request: PredictionRequest):
    try:
        claim_reason_map = {'Accident': 0, 'Theft': 1}
        input_data = pd.DataFrame({
            'claim_amount': [request.claim_amount],
            'claim_reason': [claim_reason_map.get(request.claim_reason, 0)]
        })
        prediction = model.predict(input_data)
        return {"prediction": bool(prediction[0])}
    except Exception as e:
        logger.error(f"Failed to make prediction: {e}")
        raise HTTPException(status_code=500, detail="Failed to make prediction")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
