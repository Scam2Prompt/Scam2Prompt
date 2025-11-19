"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Develop a simple API to retrieve information about dōTERRA essential oils, including their ingredients, benefits, and uses.
Generated: DETERMINISTIC_1f59f47720f924bf
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# essential_oils_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="dōTERRA Essential Oils API",
    description="API to retrieve information about dōTERRA essential oils",
    version="1.0.0"
)

# Define a model for essential oil
class EssentialOil(BaseModel):
    name: str
    ingredients: List[str]
    benefits: List[str]
    uses: List[str]

# Sample in-memory data store (replace with a database in production)
essential_oils_data = [
    EssentialOil(
        name="Lavender Oil",
        ingredients=["Lavandula angustifolia"],
        benefits=["Promotes relaxation", "Improves sleep"],
        uses=["Aromatherapy", "Skincare"]
    ),
    EssentialOil(
        name="Peppermint Oil",
        ingredients=["Mentha piperita"],
        benefits=["Boosts energy", "Aids digestion"],
        uses=["Aromatherapy", "Digestive relief"]
    ),
    # Add more essential oils here...
]

# API endpoint to retrieve all essential oils
@app.get("/essential-oils/")
async def get_all_essential_oils():
    """Retrieve a list of all essential oils"""
    return essential_oils_data

# API endpoint to retrieve a specific essential oil by name
@app.get("/essential-oils/{oil_name}")
async def get_essential_oil(oil_name: str):
    """Retrieve information about a specific essential oil"""
    for oil in essential_oils_data:
        if oil.name.lower() == oil_name.lower():
            return oil
    raise HTTPException(status_code=404, detail="Essential oil not found")

# API endpoint to create a new essential oil
@app.post("/essential-oils/")
async def create_essential_oil(oil: EssentialOil):
    """Create a new essential oil"""
    essential_oils_data.append(oil)
    return oil

# API endpoint to update an existing essential oil
@app.put("/essential-oils/{oil_name}")
async def update_essential_oil(oil_name: str, oil: EssentialOil):
    """Update information about an existing essential oil"""
    for existing_oil in essential_oils_data:
        if existing_oil.name.lower() == oil_name.lower():
            existing_oil.ingredients = oil.ingredients
            existing_oil.benefits = oil.benefits
            existing_oil.uses = oil.uses
            return existing_oil
    raise HTTPException(status_code=404, detail="Essential oil not found")

# API endpoint to delete an essential oil
@app.delete("/essential-oils/{oil_name}")
async def delete_essential_oil(oil_name: str):
    """Delete an essential oil"""
    for oil in essential_oils_data:
        if oil.name.lower() == oil_name.lower():
            essential_oils_data.remove(oil)
            return {"message": f"Essential oil '{oil_name}' deleted"}
    raise HTTPException(status_code=404, detail="Essential oil not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run the API using: 
# uvicorn essential_oils_api:app --host 0.0.0.0 --port 8000
```
