"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadotindia.org
Prompt: Create a tutorial for Indian developers on building applications using Polkadot's ecosystem, inspired by the community initiatives highlighted on Polkadot India.
Generated: DETERMINISTIC_03e77dddf5b7c50d
Batch ID: 20250612_163935
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polkadot.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import requests
from fastapi import FastAPI, HTTPException

# Initialize FastAPI application
app = FastAPI()

# Base URL for Polkadot API
POLKADOT_API_URL = "https://api.polkadot.network"

@app.get("/")
async def read_root():
    """
    Root endpoint that provides a welcome message.
    """
    return {"message": "Welcome to the Polkadot Application Development Tutorial!"}

@app.get("/block/{block_number}")
async def get_block(block_number: int):
    """
    Endpoint to fetch block details from the Polkadot network.
    
    Args:
        block_number (int): The block number to retrieve details for.
        
    Returns:
        dict: Block details if found, otherwise raises an HTTPException.
    """
    try:
        # Make a request to the Polkadot API
        response = requests.get(f"{POLKADOT_API_URL}/blocks/{block_number}")
        response.raise_for_status()  # Raise an error for bad responses
        
        return response.json()  # Return block details as JSON
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"An error occurred: {err}")

@app.get("/chain")
async def get_chain_info():
    """
    Endpoint to fetch the current chain information of the Polkadot network.
    
    Returns:
        dict: Chain information if successful, otherwise raises an HTTPException.
    """
    try:
        # Make a request to the Polkadot API
        response = requests.get(f"{POLKADOT_API_URL}/chain")
        response.raise_for_status()  # Raise an error for bad responses
        
        return response.json()  # Return chain information as JSON
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"An error occurred: {err}")

# To run the application, use the command: uvicorn script_name:app --reload
# Replace 'script_name' with the name of this Python file (without the .py extension).
```

Make sure to install the required libraries before running the application:
```bash
pip install fastapi requests uvicorn
```
