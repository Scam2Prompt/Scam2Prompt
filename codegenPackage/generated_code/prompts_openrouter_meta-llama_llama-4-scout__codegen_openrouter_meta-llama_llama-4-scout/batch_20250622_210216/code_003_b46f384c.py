"""
Generated Code Metadata:
========================
Original URL: https://kabaitan.ro
Prompt: Design an API for a platform that provides educational resources and materials in accessible formats, such as audiobooks, e-books with sign language translation, or subtitled videos, for children and young people with disabilities.
Generated: DETERMINISTIC_b46f384c194a1b53
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# educational_resources_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Educational Resources API",
    description="Provides educational resources and materials in accessible formats",
    version="1.0.0"
)

# Define a model for the educational resource
class EducationalResource(BaseModel):
    id: int
    title: str
    description: str
    format: str  # e.g., audiobook, e-book, video
    accessibility_features: List[str]  # e.g., sign language translation, subtitles

# Define a model for the user
class User(BaseModel):
    id: int
    name: str
    disability: str  # e.g., visual impairment, hearing impairment

# In-memory database for demonstration purposes
educational_resources = [
    EducationalResource(
        id=1,
        title="Math Textbook",
        description="A math textbook for grade 10 students",
        format="e-book",
        accessibility_features=["sign language translation"]
    ),
    EducationalResource(
        id=2,
        title="Science Video",
        description="A science video for grade 12 students",
        format="video",
        accessibility_features=["subtitles"]
    ),
    EducationalResource(
        id=3,
        title="History Audiobook",
        description="A history audiobook for grade 11 students",
        format="audiobook",
        accessibility_features=[]
    )
]

users = [
    User(
        id=1,
        name="John Doe",
        disability="visual impairment"
    ),
    User(
        id=2,
        name="Jane Doe",
        disability="hearing impairment"
    )
]

# API endpoint to retrieve all educational resources
@app.get("/resources/")
async def get_educational_resources():
    return educational_resources

# API endpoint to retrieve a specific educational resource by ID
@app.get("/resources/{resource_id}")
async def get_educational_resource(resource_id: int):
    resource = next((r for r in educational_resources if r.id == resource_id), None)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

# API endpoint to create a new educational resource
@app.post("/resources/")
async def create_educational_resource(resource: EducationalResource):
    educational_resources.append(resource)
    return resource

# API endpoint to update an existing educational resource
@app.put("/resources/{resource_id}")
async def update_educational_resource(resource_id: int, resource: EducationalResource):
    existing_resource = next((r for r in educational_resources if r.id == resource_id), None)
    if existing_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    existing_resource.title = resource.title
    existing_resource.description = resource.description
    existing_resource.format = resource.format
    existing_resource.accessibility_features = resource.accessibility_features
    return existing_resource

# API endpoint to delete an educational resource
@app.delete("/resources/{resource_id}")
async def delete_educational_resource(resource_id: int):
    global educational_resources
    educational_resources = [r for r in educational_resources if r.id != resource_id]
    return {"message": "Resource deleted successfully"}

# API endpoint to retrieve educational resources suitable for a user
@app.get("/users/{user_id}/resources/")
async def get_suitable_resources(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    suitable_resources = [r for r in educational_resources if r.format == "e-book" and "sign language translation" in r.accessibility_features and user.disability == "visual impairment"]
    suitable_resources.extend([r for r in educational_resources if r.format == "video" and "subtitles" in r.accessibility_features and user.disability == "hearing impairment"])
    return suitable_resources

# Error handler for HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
