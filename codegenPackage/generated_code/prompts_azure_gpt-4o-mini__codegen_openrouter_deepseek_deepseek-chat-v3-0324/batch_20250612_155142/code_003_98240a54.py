"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Develop a RESTful API endpoint that retrieves information about COVID-19 safety measures and infection control protocols for a home care service, based on Shareth Homecare's guidelines.
Generated: DETERMINISTIC_98240a542f4f0a4c
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title="Shareth Homecare COVID-19 API",
    description="API for retrieving COVID-19 safety measures and infection control protocols",
    version="1.0.0"
)

class SafetyMeasure(BaseModel):
    id: int
    title: str
    description: str
    category: str
    is_mandatory: bool
    last_updated: str

# In-memory database (replace with actual database in production)
safety_measures_db = [
    {
        "id": 1,
        "title": "Hand Hygiene",
        "description": "Wash hands with soap and water for at least 20 seconds or use alcohol-based hand sanitizer before and after client contact.",
        "category": "Personal Hygiene",
        "is_mandatory": True,
        "last_updated": "2023-10-15"
    },
    {
        "id": 2,
        "title": "Personal Protective Equipment",
        "description": "Wear appropriate PPE (mask, gloves, gown, eye protection) based on client's condition and procedure being performed.",
        "category": "PPE",
        "is_mandatory": True,
        "last_updated": "2023-10-15"
    },
    {
        "id": 3,
        "title": "Social Distancing",
        "description": "Maintain at least 6 feet distance from others when possible, especially in common areas.",
        "category": "General Safety",
        "is_mandatory": True,
        "last_updated": "2023-09-28"
    },
    {
        "id": 4,
        "title": "Surface Disinfection",
        "description": "Regularly disinfect high-touch surfaces in the client's home using EPA-approved disinfectants.",
        "category": "Environmental",
        "is_mandatory": True,
        "last_updated": "2023-10-01"
    },
    {
        "id": 5,
        "title": "Symptom Monitoring",
        "description": "Self-monitor for COVID-19 symptoms daily and report any symptoms immediately.",
        "category": "Health Monitoring",
        "is_mandatory": True,
        "last_updated": "2023-10-10"
    }
]

@app.get("/measures", response_model=list[SafetyMeasure], tags=["Safety Measures"])
async def get_all_safety_measures():
    """
    Retrieve all COVID-19 safety measures and infection control protocols.
    """
    return safety_measures_db

@app.get("/measures/{measure_id}", response_model=SafetyMeasure, tags=["Safety Measures"])
async def get_safety_measure(measure_id: int):
    """
    Retrieve a specific safety measure by ID.
    """
    measure = next((m for m in safety_measures_db if m["id"] == measure_id), None)
    if not measure:
        raise HTTPException(status_code=404, detail="Safety measure not found")
    return measure

@app.get("/measures/category/{category}", response_model=list[SafetyMeasure], tags=["Safety Measures"])
async def get_measures_by_category(category: str):
    """
    Retrieve safety measures by category.
    """
    category_measures = [m for m in safety_measures_db if m["category"].lower() == category.lower()]
    if not category_measures:
        raise HTTPException(
            status_code=404,
            detail=f"No measures found for category '{category}'"
        )
    return category_measures

@app.get("/measures/search/", response_model=list[SafetyMeasure], tags=["Safety Measures"])
async def search_measures(query: Optional[str] = None):
    """
    Search safety measures by title or description.
    """
    if not query:
        return safety_measures_db
    
    query = query.lower()
    results = [
        m for m in safety_measures_db
        if query in m["title"].lower() or query in m["description"].lower()
    ]
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
