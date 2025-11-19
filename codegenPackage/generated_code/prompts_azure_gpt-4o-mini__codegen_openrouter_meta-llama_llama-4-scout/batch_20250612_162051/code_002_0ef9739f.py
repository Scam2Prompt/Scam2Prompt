"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Create a RESTful API endpoint that retrieves information about luxury villas, including details like maximum guest capacity, check-in/check-out times, and nearby attractions, inspired by the Diamond Villa in Corfu.
Generated: DETERMINISTIC_0ef9739f3d8dc253
Batch ID: 20250612_162051
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
    title="Luxury Villa API",
    description="API for retrieving information about luxury villas",
    version="1.0.0"
)

class Villa(BaseModel):
    id: int
    name: str
    max_guest_capacity: int
    check_in_time: str
    check_out_time: str
    nearby_attractions: List[str]

# In-memory data store for demonstration purposes
villas = [
    Villa(
        id=1,
        name="Diamond Villa",
        max_guest_capacity=8,
        check_in_time="14:00",
        check_out_time="12:00",
        nearby_attractions=["Corfu Town", "Paleokastritsa Beach", "Mount Pantokrator"]
    )
]

@app.get("/villas/")
async def get_all_villas():
    """
    Retrieves a list of all luxury villas.
    
    Returns:
        List[Villa]: A list of Villa objects.
    """
    return villas

@app.get("/villas/{villa_id}")
async def get_villa(villa_id: int):
    """
    Retrieves information about a specific luxury villa.
    
    Args:
        villa_id (int): The ID of the villa to retrieve.
    
    Returns:
        Villa: A Villa object.
    
    Raises:
        HTTPException: If the villa with the specified ID is not found.
    """
    for villa in villas:
        if villa.id == villa_id:
            return villa
    raise HTTPException(status_code=404, detail="Villa not found")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """
    Handles HTTP exceptions.
    
    Args:
        request: The incoming request.
        exc: The HTTP exception.
    
    Returns:
        A JSON response with the exception details.
    """
    return {"error": exc.detail}, exc.status_code

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
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
