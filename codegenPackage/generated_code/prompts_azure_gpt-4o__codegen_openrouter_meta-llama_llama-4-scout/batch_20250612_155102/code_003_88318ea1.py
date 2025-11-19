"""
Generated Code Metadata:
========================
Original URL: https://monadawards.xyz
Prompt: Generate a satirical API specification for a fictional awards system that includes endpoints for submitting nominations, retrieving nominees, and filtering by categories like "Gymonad Bullies."
Generated: DETERMINISTIC_88318ea1bc1fe9a7
Batch ID: 20250612_155102
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
from typing import List

app = FastAPI(
    title="Absurd Awards API",
    description="A satirical API for submitting and managing absurd award nominations",
    version="1.0.0"
)

# Define a model for nominations
class Nomination(BaseModel):
    """A single nomination"""
    name: str
    category: str
    reason: str

# Define a model for nominee responses
class Nominee(BaseModel):
    """A single nominee"""
    id: int
    name: str
    category: str
    reason: str

# In-memory storage for nominations (replace with a database in production)
nominations: List[Nomination] = []
nominee_id: int = 1

# Endpoint to submit a nomination
@app.post("/nominations/")
async def create_nomination(nomination: Nomination):
    """Submit a new nomination"""
    global nominee_id
    try:
        # Add the nomination to the in-memory storage
        nominations.append(nomination)
        # Return the nominee with a generated ID
        nominee = Nominee(id=nominee_id, name=nomination.name, category=nomination.category, reason=nomination.reason)
        nominee_id += 1
        return nominee
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail="Failed to create nomination") from e

# Endpoint to retrieve all nominees
@app.get("/nominees/")
async def read_nominees():
    """Retrieve all nominees"""
    try:
        # Return all nominations as a list of nominees
        return [{"id": i+1, "name": n.name, "category": n.category, "reason": n.reason} for i, n in enumerate(nominations)]
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail="Failed to retrieve nominees") from e

# Endpoint to filter nominees by category
@app.get("/nominees/categories/{category}")
async def read_nominees_by_category(category: str):
    """Retrieve nominees filtered by category"""
    try:
        # Filter nominations by category and return as a list of nominees
        filtered_nominations = [n for n in nominations if n.category.lower() == category.lower()]
        return [{"id": i+1, "name": n.name, "category": n.category, "reason": n.reason} for i, n in enumerate(filtered_nominations)]
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail="Failed to retrieve nominees by category") from e

# Error handler for 404 Not Found
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    if exc.status_code == 404:
        return {"error": "Not Found", "detail": "The requested resource was not found"}
    return {"error": "Internal Server Error", "detail": "An unexpected error occurred"}

# Run the application
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
