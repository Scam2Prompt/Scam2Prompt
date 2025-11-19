"""
Generated Code Metadata:
========================
Original URL: https://corgiaixyz.pages.dev
Prompt: Design an API for a referral mechanism in an NFT marketplace, inspired by CorgiAI's ecosystem.
Generated: DETERMINISTIC_f312fcd50406d478
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()

# Define the Referral model
class Referral(BaseModel):
    referrer: str  # The address of the referrer
    referee: str   # The address of the referee

# Define the ReferralProgram model
class ReferralProgram(BaseModel):
    id: str
    referrer: str
    referee: str
    reward: float
    created_at: str

# In-memory storage for demonstration purposes
referral_programs = {}

# Generate a unique referral code
def generate_referral_code():
    return str(uuid.uuid4())

# Get the current referral program
def get_referral_program(referrer: str):
    return referral_programs.get(referrer)

# Create a new referral program
def create_referral_program(referrer: str, referee: str, reward: float):
    referral_code = generate_referral_code()
    referral_programs[referrer] = ReferralProgram(
        id=referral_code,
        referrer=referrer,
        referee=referee,
        reward=reward,
        created_at="2023-01-01T00:00:00"
    )
    return referral_programs[referrer]

# Referral API Endpoints
@app.post("/referrals/")
async def create_referral(referral: Referral):
    try:
        existing_program = get_referral_program(referral.referrer)
        if existing_program:
            raise HTTPException(status_code=400, detail="Referrer already has an active referral program")
        
        new_program = create_referral_program(referral.referrer, referral.referee, 10.0)
        return JSONResponse(content=new_program.dict(), status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/referrals/{referrer}")
async def get_referral_program_by_referrer(referrer: str):
    try:
        program = get_referral_program(referrer)
        if not program:
            raise HTTPException(status_code=404, detail="Referral program not found")
        return JSONResponse(content=program.dict(), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/referrals/")
async def get_all_referral_programs():
    try:
        return JSONResponse(content=[program.dict() for program in referral_programs.values()], status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Error Handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
```

```python
# main.py
from referral_api import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
