"""
Generated Code Metadata:
========================
Original URL: https://searchhr.com.ar
Prompt: "Design an API for a vocational orientation platform, incorporating features from Search HR's Orientación Vocacional-Ocupacional services."
Generated: DETERMINISTIC_2843e11e24caadfe
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vocational_orientation_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Vocational Orientation API",
    description="API for vocational orientation platform",
    version="1.0.0"
)

# Define a model for the vocational profiles
class VocationalProfile(BaseModel):
    id: int
    name: str
    description: str
    skills: List[str]
    interests: List[str]

# Define a model for the search query
class SearchQuery(BaseModel):
    query: str

# In-memory database for demonstration purposes
vocational_profiles = [
    VocationalProfile(
        id=1,
        name="Software Developer",
        description="Develop software applications",
        skills=["Programming", "Software Development"],
        interests=["Technology", "Problem-solving"]
    ),
    VocationalProfile(
        id=2,
        name="Data Scientist",
        description="Analyze and interpret complex data",
        skills=["Data Analysis", "Machine Learning"],
        interests=["Data", "Statistics"]
    )
]

# API endpoint to retrieve all vocational profiles
@app.get("/profiles/", response_model=List[VocationalProfile])
def get_vocational_profiles():
    """Retrieve a list of all vocational profiles"""
    return vocational_profiles

# API endpoint to retrieve a vocational profile by ID
@app.get("/profiles/{profile_id}", response_model=VocationalProfile)
def get_vocational_profile(profile_id: int):
    """Retrieve a vocational profile by ID"""
    for profile in vocational_profiles:
        if profile.id == profile_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# API endpoint to search for vocational profiles
@app.post("/search/", response_model=List[VocationalProfile])
def search_vocational_profiles(query: SearchQuery):
    """Search for vocational profiles based on a query"""
    results = []
    for profile in vocational_profiles:
        if query.query.lower() in profile.name.lower() or query.query.lower() in profile.description.lower():
            results.append(profile)
    return results

# API endpoint to create a new vocational profile
@app.post("/profiles/", response_model=VocationalProfile)
def create_vocational_profile(profile: VocationalProfile):
    """Create a new vocational profile"""
    vocational_profiles.append(profile)
    return profile

# API endpoint to update an existing vocational profile
@app.put("/profiles/{profile_id}", response_model=VocationalProfile)
def update_vocational_profile(profile_id: int, profile: VocationalProfile):
    """Update an existing vocational profile"""
    for i, existing_profile in enumerate(vocational_profiles):
        if existing_profile.id == profile_id:
            vocational_profiles[i] = profile
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# API endpoint to delete a vocational profile
@app.delete("/profiles/{profile_id}")
def delete_vocational_profile(profile_id: int):
    """Delete a vocational profile"""
    for i, profile in enumerate(vocational_profiles):
        if profile.id == profile_id:
            del vocational_profiles[i]
            return {"message": "Profile deleted"}
    raise HTTPException(status_code=404, detail="Profile not found")

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
# Run the API
uvicorn vocational_orientation_api:app --host 0.0.0.0 --port 8000 --reload
```
