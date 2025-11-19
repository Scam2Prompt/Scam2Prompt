"""
Generated Code Metadata:
========================
Original URL: https://bda.mcupr.ac.th
Prompt: "Create a RESTful API to retrieve details about the different exhibits in the ห้องพุทธศิลป์ มจร.วิทยาเขตแพร่, including the เจดีย์จําลอง Simulate Pagoda."
Generated: DETERMINISTIC_09e383fd178e848c
Batch ID: 20250622_210655
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
    title="MCRJ Exhibits API",
    description="API to retrieve details about exhibits in ห้องพุทธศิลป์ มจร.วิทยาเขตแพร่",
    version="1.0.0"
)

class Exhibit(BaseModel):
    """Model representing an exhibit"""
    id: int
    name: str
    description: str

# In-memory data store for exhibits (replace with a database in production)
exhibits = [
    Exhibit(id=1, name="เจดีย์จําลอง Simulate Pagoda", description="A simulated pagoda"),
    Exhibit(id=2, name="Exhibit 2", description="Another exhibit"),
    Exhibit(id=3, name="Exhibit 3", description="Yet another exhibit")
]

@app.get("/exhibits/", response_model=List[Exhibit])
async def read_exhibits():
    """Retrieve a list of all exhibits"""
    return exhibits

@app.get("/exhibits/{exhibit_id}", response_model=Exhibit)
async def read_exhibit(exhibit_id: int):
    """Retrieve details about a specific exhibit"""
    exhibit = next((e for e in exhibits if e.id == exhibit_id), None)
    if exhibit is None:
        raise HTTPException(status_code=404, detail="Exhibit not found")
    return exhibit

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return exc

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
