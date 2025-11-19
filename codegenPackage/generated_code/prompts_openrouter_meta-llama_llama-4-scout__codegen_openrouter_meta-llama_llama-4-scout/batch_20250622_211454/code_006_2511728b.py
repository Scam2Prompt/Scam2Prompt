"""
Generated Code Metadata:
========================
Original URL: https://sctoll.io
Prompt: "Create an API to retrieve information about Brixton Forged's wheel collection, including details about their FDE Series, Carbon+ Series, and Magnesium+ Series wheels."
Generated: DETERMINISTIC_2511728bfb483174
Batch ID: 20250622_211454
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
    title="Brixton Forged Wheel Collection API",
    description="API to retrieve information about Brixton Forged's wheel collection",
    version="1.0.0"
)

class Wheel(BaseModel):
    """Base model for wheels"""
    name: str
    description: str
    series: str
    sizes: List[str]
    finish: List[str]

class FDE_Series(Wheel):
    """Model for FDE Series wheels"""
    def __init__(self, **kwargs):
        super().__init__(series="FDE Series", **kwargs)

class Carbon_Plus_Series(Wheel):
    """Model for Carbon+ Series wheels"""
    def __init__(self, **kwargs):
        super().__init__(series="Carbon+ Series", **kwargs)

class Magnesium_Plus_Series(Wheel):
    """Model for Magnesium+ Series wheels"""
    def __init__(self, **kwargs):
        super().__init__(series="Magnesium+ Series", **kwargs)

# Sample in-memory data store (replace with a database in production)
wheels = [
    FDE_Series(name="FDE-01", description="The FDE Series is our most popular wheel line.", sizes=["17x7.5", "18x8.5"], finish=["Gloss Black", "Satellite Silver"]),
    Carbon_Plus_Series(name="CP-01", description="The Carbon+ Series is our high-performance wheel line.", sizes=["19x9.5", "20x10.5"], finish=["Gloss Black", "Carbon Fiber"]),
    Magnesium_Plus_Series(name="MP-01", description="The Magnesium+ Series is our lightweight wheel line.", sizes=["17x7.5", "18x8.5"], finish=["Gloss Black", "Matte Black"]),
]

@app.get("/wheels/")
async def get_all_wheels():
    """Retrieve a list of all wheels"""
    return wheels

@app.get("/wheels/series/")
async def get_wheel_series():
    """Retrieve a list of all wheel series"""
    series = list(set([wheel.series for wheel in wheels]))
    return [{"series": s} for s in series]

@app.get("/wheels/series/{series}")
async def get_wheels_by_series(series: str):
    """Retrieve a list of wheels for a specific series"""
    result = [wheel for wheel in wheels if wheel.series == series]
    if not result:
        raise HTTPException(status_code=404, detail=f"No wheels found for series '{series}'")
    return result

@app.get("/wheels/{wheel_name}")
async def get_wheel(wheel_name: str):
    """Retrieve details about a specific wheel"""
    result = next((wheel for wheel in wheels if wheel.name == wheel_name), None)
    if not result:
        raise HTTPException(status_code=404, detail=f"No wheel found with name '{wheel_name}'")
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
pydantic
uvicorn
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
# or 
python app.py 
```
