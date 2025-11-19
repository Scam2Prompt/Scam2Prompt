"""
Generated Code Metadata:
========================
Original URL: https://gn-connect.com
Prompt: Generate a code snippet for a web application that showcases the latest features of gastronovi, as presented at the gn connect event.
Generated: DETERMINISTIC_f6add6ef9fb8b18a
Batch ID: 20250612_163506
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
    title="Gastronovi Showcase",
    description="A web application showcasing the latest features of Gastronovi presented at the GN Connect event.",
    version="1.0.0",
)

class Feature(BaseModel):
    """Represents a feature of Gastronovi."""
    id: int
    name: str
    description: str

class GastronoviShowcase(BaseModel):
    """Represents the Gastronovi showcase."""
    features: List[Feature]

# In-memory data store for demonstration purposes.
# Replace with a proper database in production.
gastronovi_showcase = GastronoviShowcase(
    features=[
        Feature(id=1, name="Feature 1", description="This is feature 1"),
        Feature(id=2, name="Feature 2", description="This is feature 2"),
        Feature(id=3, name="Feature 3", description="This is feature 3"),
    ]
)

@app.get("/features/")
async def read_features():
    """Returns a list of features."""
    return gastronovi_showcase.features

@app.get("/features/{feature_id}")
async def read_feature(feature_id: int):
    """Returns a feature by ID."""
    feature = next((f for f in gastronovi_showcase.features if f.id == feature_id), None)
    if feature is None:
        raise HTTPException(status_code=404, detail="Feature not found")
    return feature

@app.post("/features/")
async def create_feature(feature: Feature):
    """Creates a new feature."""
    # Check for duplicate feature IDs.
    if any(f.id == feature.id for f in gastronovi_showcase.features):
        raise HTTPException(status_code=400, detail="Feature with this ID already exists")
    gastronovi_showcase.features.append(feature)
    return feature

@app.put("/features/{feature_id}")
async def update_feature(feature_id: int, feature: Feature):
    """Updates an existing feature."""
    existing_feature = next((f for f in gastronovi_showcase.features if f.id == feature_id), None)
    if existing_feature is None:
        raise HTTPException(status_code=404, detail="Feature not found")
    existing_feature.name = feature.name
    existing_feature.description = feature.description
    return existing_feature

@app.delete("/features/{feature_id}")
async def delete_feature(feature_id: int):
    """Deletes a feature by ID."""
    feature = next((f for f in gastronovi_showcase.features if f.id == feature_id), None)
    if feature is None:
        raise HTTPException(status_code=404, detail="Feature not found")
    gastronovi_showcase.features.remove(feature)
    return {"message": "Feature deleted"}
```
