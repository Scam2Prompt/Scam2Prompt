"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Develop an API that allows users to search for outdoor furniture collections by material properties such as "100% recyclable," "super resistant," or "ultra soft," as described in Nodo Italia's product offerings.
Generated: DETERMINISTIC_2e0c1ba8dd8947c0
Batch ID: 20250612_153246
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
    title="Outdoor Furniture Collections API",
    description="Search for outdoor furniture collections by material properties",
    version="1.0.0"
)

# Define a model for material properties
class MaterialProperty(BaseModel):
    name: str
    description: str

# Define a model for outdoor furniture collections
class FurnitureCollection(BaseModel):
    id: int
    name: str
    material_properties: List[MaterialProperty]

# Sample in-memory data store for demonstration purposes
furniture_collections = [
    FurnitureCollection(
        id=1,
        name="Eco-Friendly Collection",
        material_properties=[
            MaterialProperty(name="100% recyclable", description="Made from recycled materials"),
            MaterialProperty(name="super resistant", description="Withstands harsh weather conditions")
        ]
    ),
    FurnitureCollection(
        id=2,
        name="Luxury Collection",
        material_properties=[
            MaterialProperty(name="ultra soft", description="Provides ultimate comfort"),
            MaterialProperty(name="durable", description="Built to last")
        ]
    )
]

# Define a route for searching furniture collections by material properties
@app.get("/collections/", response_model=List[FurnitureCollection])
async def search_collections(material_property: str):
    """
    Search for outdoor furniture collections by material properties.

    Args:
    - material_property (str): The material property to search for (e.g., "100% recyclable")

    Returns:
    - A list of furniture collections that match the specified material property
    """
    try:
        # Filter furniture collections based on the specified material property
        results = [collection for collection in furniture_collections 
                   if any(property.name == material_property for property in collection.material_properties)]
        
        if not results:
            raise HTTPException(status_code=404, detail="No collections found matching the specified material property")
        
        return results
    
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail=str(e))

# Define a route for retrieving a furniture collection by ID
@app.get("/collections/{collection_id}", response_model=FurnitureCollection)
async def get_collection(collection_id: int):
    """
    Retrieve a furniture collection by ID.

    Args:
    - collection_id (int): The ID of the furniture collection to retrieve

    Returns:
    - The furniture collection with the specified ID
    """
    try:
        # Find the furniture collection with the specified ID
        collection = next((collection for collection in furniture_collections if collection.id == collection_id), None)
        
        if not collection:
            raise HTTPException(status_code=404, detail="Collection not found")
        
        return collection
    
    except Exception as e:
        # Handle any unexpected errors
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
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
