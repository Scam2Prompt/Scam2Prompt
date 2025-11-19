"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Develop a RESTful API endpoint that retrieves information about different safari experiences in Tanzania, including mid-range and luxury options, and formats the data for a mobile app.
Generated: DETERMINISTIC_ca102ea597463df8
Batch ID: 20250612_164122
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
    title="Tanzania Safari Experiences API",
    description="API for retrieving information about different safari experiences in Tanzania",
    version="1.0.0"
)

# Define a model for the safari experience data
class SafariExperience(BaseModel):
    id: int
    name: str
    description: str
    price: float
    rating: float
    category: str  # mid-range or luxury

# In-memory data store for demonstration purposes
safari_experiences = [
    SafariExperience(id=1, name="Mid-Range Serengeti Safari", description="Explore the Serengeti National Park", price=800.0, rating=4.5, category="mid-range"),
    SafariExperience(id=2, name="Luxury Ngorongoro Crater Safari", description="Experience the best of Ngorongoro Crater", price=2500.0, rating=4.9, category="luxury"),
    SafariExperience(id=3, name="Mid-Range Tarangire Safari", description="Discover the Tarangire National Park", price=600.0, rating=4.2, category="mid-range"),
    SafariExperience(id=4, name="Luxury Mount Kilimanjaro Climb", description="Conquer the highest peak in Africa", price=3500.0, rating=4.8, category="luxury"),
]

# API endpoint to retrieve all safari experiences
@app.get("/safari-experiences/", response_model=List[SafariExperience])
async def get_all_safari_experiences():
    """Retrieve a list of all safari experiences"""
    return safari_experiences

# API endpoint to retrieve safari experiences by category
@app.get("/safari-experiences/{category}", response_model=List[SafariExperience])
async def get_safari_experiences_by_category(category: str):
    """Retrieve a list of safari experiences by category (mid-range or luxury)"""
    try:
        category = category.lower()
        if category not in ["mid-range", "luxury"]:
            raise HTTPException(status_code=400, detail="Invalid category")
        return [experience for experience in safari_experiences if experience.category == category]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to retrieve a single safari experience by ID
@app.get("/safari-experiences/{experience_id}", response_model=SafariExperience)
async def get_safari_experience(experience_id: int):
    """Retrieve a single safari experience by ID"""
    try:
        experience = next((exp for exp in safari_experiences if exp.id == experience_id), None)
        if experience is None:
            raise HTTPException(status_code=404, detail="Experience not found")
        return experience
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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
