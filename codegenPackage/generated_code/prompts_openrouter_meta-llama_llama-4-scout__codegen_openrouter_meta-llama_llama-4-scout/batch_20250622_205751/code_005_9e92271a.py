"""
Generated Code Metadata:
========================
Original URL: https://trait-sniper.pro
Prompt: "How would you design a RESTful API for a trait analysis service like Trait Sniper, including endpoints and request/response formats?"
Generated: DETERMINISTIC_9e92271a47f593b1
Batch ID: 20250622_205751
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
from enum import Enum

app = FastAPI(
    title="Trait Sniper API",
    description="A RESTful API for trait analysis service",
    version="1.0.0"
)

class TraitType(str, Enum):
    """Enum for trait types"""
    personality = "personality"
    behavior = "behavior"

class Trait(BaseModel):
    """Model for trait"""
    id: int
    name: str
    description: str

class UserTraits(BaseModel):
    """Model for user traits"""
    user_id: int
    traits: List[Trait]

class AnalyzeRequest(BaseModel):
    """Model for analysis request"""
    user_id: int
    trait_type: TraitType

class AnalyzeResponse(BaseModel):
    """Model for analysis response"""
    user_id: int
    traits: List[Trait]

# In-memory storage for demonstration purposes
traits_db = {
    1: UserTraits(
        user_id=1,
        traits=[
            Trait(id=1, name="Extraversion", description="Outgoing and sociable"),
            Trait(id=2, name="Conscientiousness", description="Organized and responsible")
        ]
    )
}

@app.get("/traits/")
async def get_traits():
    """Get all traits"""
    traits = []
    for user_traits in traits_db.values():
        traits.extend(user_traits.traits)
    return traits

@app.get("/traits/{trait_id}")
async def get_trait(trait_id: int):
    """Get trait by ID"""
    for user_traits in traits_db.values():
        for trait in user_traits.traits:
            if trait.id == trait_id:
                return trait
    raise HTTPException(status_code=404, detail="Trait not found")

@app.post("/analyze/")
async def analyze(analyze_request: AnalyzeRequest):
    """Analyze user traits"""
    user_traits = traits_db.get(analyze_request.user_id)
    if not user_traits:
        raise HTTPException(status_code=404, detail="User not found")
    
    filtered_traits = [trait for trait in user_traits.traits if trait.name == analyze_request.trait_type.value]
    return AnalyzeResponse(
        user_id=analyze_request.user_id,
        traits=filtered_traits
    )

@app.post("/users/{user_id}/traits/")
async def create_user_trait(user_id: int, trait: Trait):
    """Create user trait"""
    if user_id not in traits_db:
        traits_db[user_id] = UserTraits(user_id=user_id, traits=[])
    
    traits_db[user_id].traits.append(trait)
    return trait

@app.put("/users/{user_id}/traits/{trait_id}")
async def update_user_trait(user_id: int, trait_id: int, trait: Trait):
    """Update user trait"""
    if user_id not in traits_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    for existing_trait in traits_db[user_id].traits:
        if existing_trait.id == trait_id:
            existing_trait.name = trait.name
            existing_trait.description = trait.description
            return existing_trait
    raise HTTPException(status_code=404, detail="Trait not found")

@app.delete("/users/{user_id}/traits/{trait_id}")
async def delete_user_trait(user_id: int, trait_id: int):
    """Delete user trait"""
    if user_id not in traits_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    traits_db[user_id].traits = [trait for trait in traits_db[user_id].traits if trait.id != trait_id]
    return {"message": "Trait deleted"}

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
