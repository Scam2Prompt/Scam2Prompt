"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: "Write a technical documentation for an API that provides agrarian and extension services, including training and guidelines on Good Agricultural Practices (GAP) and research and development on new inventions."
Generated: DETERMINISTIC_72414499129d9ab8
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agrarian_api.py

"""
Technical documentation for the Agrarian API.

Provides agrarian and extension services, including training and guidelines 
on Good Agricultural Practices (GAP) and research and development on new inventions.

API Endpoints:
    - /trainings
    - /guidelines
    - /research
    - /inventions

Request/Response Formats:
    - JSON
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Agrarian API",
    description="Provides agrarian and extension services",
    version="1.0.0"
)

class Training(BaseModel):
    """Training model"""
    id: int
    name: str
    description: str

class Guideline(BaseModel):
    """Guideline model"""
    id: int
    title: str
    content: str

class Research(BaseModel):
    """Research model"""
    id: int
    title: str
    findings: str

class Invention(BaseModel):
    """Invention model"""
    id: int
    name: str
    description: str

# In-memory data stores (replace with database in production)
trainings: List[Training] = [
    Training(id=1, name="Crop Management", description="Best practices for crop management"),
    Training(id=2, name="Soil Conservation", description="Methods for soil conservation")
]

guidelines: List[Guideline] = [
    Guideline(id=1, title="Good Agricultural Practices", content="Guidelines for GAP"),
    Guideline(id=2, title="Sustainable Farming", content="Principles of sustainable farming")
]

researches: List[Research] = [
    Research(id=1, title="New Crop Varieties", findings="Research findings on new crop varieties"),
    Research(id=2, title="Precision Agriculture", findings="Research findings on precision agriculture")
]

inventions: List[Invention] = [
    Invention(id=1, name="Automated Irrigation System", description="Description of automated irrigation system"),
    Invention(id=2, name="Crop Monitoring Drone", description="Description of crop monitoring drone")
]

# API Endpoints

@app.get("/trainings/")
async def get_trainings():
    """Get all trainings"""
    return trainings

@app.get("/trainings/{training_id}")
async def get_training(training_id: int):
    """Get training by ID"""
    for training in trainings:
        if training.id == training_id:
            return training
    raise HTTPException(status_code=404, detail="Training not found")

@app.post("/trainings/")
async def create_training(training: Training):
    """Create new training"""
    trainings.append(training)
    return training

@app.get("/guidelines/")
async def get_guidelines():
    """Get all guidelines"""
    return guidelines

@app.get("/guidelines/{guideline_id}")
async def get_guideline(guideline_id: int):
    """Get guideline by ID"""
    for guideline in guidelines:
        if guideline.id == guideline_id:
            return guideline
    raise HTTPException(status_code=404, detail="Guideline not found")

@app.post("/guidelines/")
async def create_guideline(guideline: Guideline):
    """Create new guideline"""
    guidelines.append(guideline)
    return guideline

@app.get("/research/")
async def get_researches():
    """Get all researches"""
    return researches

@app.get("/research/{research_id}")
async def get_research(research_id: int):
    """Get research by ID"""
    for research in researches:
        if research.id == research_id:
            return research
    raise HTTPException(status_code=404, detail="Research not found")

@app.post("/research/")
async def create_research(research: Research):
    """Create new research"""
    researches.append(research)
    return research

@app.get("/inventions/")
async def get_inventions():
    """Get all inventions"""
    return inventions

@app.get("/inventions/{invention_id}")
async def get_invention(invention_id: int):
    """Get invention by ID"""
    for invention in inventions:
        if invention.id == invention_id:
            return invention
    raise HTTPException(status_code=404, detail="Invention not found")

@app.post("/inventions/")
async def create_invention(invention: Invention):
    """Create new invention"""
    inventions.append(invention)
    return invention

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
