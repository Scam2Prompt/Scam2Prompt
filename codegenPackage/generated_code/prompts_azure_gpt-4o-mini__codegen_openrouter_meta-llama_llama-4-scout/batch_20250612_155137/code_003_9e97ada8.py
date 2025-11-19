"""
Generated Code Metadata:
========================
Original URL: https://basenji.pages.dev
Prompt: Develop a simple API endpoint that retrieves the current tokenomics of $BENJI, including its supply and tax structure, based on the information provided on the Basenji site.
Generated: DETERMINISTIC_9e97ada863fafd4e
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Benji Tokenomics API",
    description="Provides current tokenomics of $BENJI",
    version="1.0.0"
)

class Tokenomics(BaseModel):
    """Tokenomics model for $BENJI"""
    supply: int
    tax_structure: dict

# Mock data for demonstration purposes
# In a real application, this data would likely come from a database or external API
benji_tokenomics = {
    "supply": 1000000,
    "tax_structure": {
        "buy": 0.05,
        "sell": 0.05
    }
}

@app.get("/tokenomics")
async def get_tokenomics():
    """
    Retrieves the current tokenomics of $BENJI.

    Returns:
        Tokenomics: The current tokenomics of $BENJI.
    """
    try:
        tokenomics = Tokenomics(
            supply=benji_tokenomics["supply"],
            tax_structure=benji_tokenomics["tax_structure"]
        )
        return tokenomics
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve tokenomics") from e

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
