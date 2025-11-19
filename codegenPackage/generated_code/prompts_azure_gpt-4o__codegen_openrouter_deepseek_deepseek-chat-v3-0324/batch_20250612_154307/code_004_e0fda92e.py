"""
Generated Code Metadata:
========================
Original URL: https://conhyper.pages.dev
Prompt: Create a roadmap feature for a blockchain-based platform that displays upcoming features and a changelog, inspired by the "Product Roadmap" and "Changelog" sections of the website.
Generated: DETERMINISTIC_e0fda92e3761d5f3
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roadmap.py

from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Blockchain Platform Roadmap API",
    description="API for managing and displaying product roadmap and changelog",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Status(str, Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    DELAYED = "delayed"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class RoadmapItem(BaseModel):
    id: str
    title: str
    description: str
    status: Status
    priority: Priority
    target_release: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @validator('target_release')
    def validate_target_release(cls, v):
        if v and not v.startswith(('Q1', 'Q2', 'Q3', 'Q4')):
            raise ValueError('Target release should be in format QX YYYY')
        return v

class ChangelogItem(BaseModel):
    id: str
    version: str
    release_date: datetime
    changes: List[str]
    created_at: datetime = Field(default_factory=datetime.now)

# In-memory database (replace with actual database in production)
roadmap_db: Dict[str, RoadmapItem] = {}
changelog_db: Dict[str, ChangelogItem] = {}

@app.get("/roadmap", response_model=List[RoadmapItem])
async def get_roadmap(status: Optional[Status] = None):
    """Get all roadmap items, optionally filtered by status"""
    if status:
        return [item for item in roadmap_db.values() if item.status == status]
    return list(roadmap_db.values())

@app.post("/roadmap", response_model=RoadmapItem)
async def create_roadmap_item(item: RoadmapItem):
    """Create a new roadmap item"""
    if item.id in roadmap_db:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    roadmap_db[item.id] = item
    return item

@app.get("/roadmap/{item_id}", response_model=RoadmapItem)
async def get_roadmap_item(item_id: str):
    """Get a specific roadmap item by ID"""
    if item_id not in roadmap_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return roadmap_db[item_id]

@app.put("/roadmap/{item_id}", response_model=RoadmapItem)
async def update_roadmap_item(item_id: str, item: RoadmapItem):
    """Update a roadmap item"""
    if item_id not in roadmap_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item.updated_at = datetime.now()
    roadmap_db[item_id] = item
    return item

@app.delete("/roadmap/{item_id}")
async def delete_roadmap_item(item_id: str):
    """Delete a roadmap item"""
    if item_id not in roadmap_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del roadmap_db[item_id]
    return {"message": "Item deleted successfully"}

@app.get("/changelog", response_model=List[ChangelogItem])
async def get_changelog(limit: Optional[int] = None):
    """Get all changelog items, optionally limited by count"""
    items = sorted(changelog_db.values(), key=lambda x: x.release_date, reverse=True)
    if limit:
        items = items[:limit]
    return items

@app.post("/changelog", response_model=ChangelogItem)
async def create_changelog_item(item: ChangelogItem):
    """Create a new changelog item"""
    if item.id in changelog_db:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    changelog_db[item.id] = item
    return item

@app.get("/changelog/{item_id}", response_model=ChangelogItem)
async def get_changelog_item(item_id: str):
    """Get a specific changelog item by ID"""
    if item_id not in changelog_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return changelog_db[item_id]

def load_initial_data():
    """Load initial sample data"""
    try:
        with open("initial_data.json") as f:
            data = json.load(f)
            
            for item in data.get("roadmap", []):
                roadmap_item = RoadmapItem(**item)
                roadmap_db[roadmap_item.id] = roadmap_item
                
            for item in data.get("changelog", []):
                changelog_item = ChangelogItem(**item)
                changelog_db[changelog_item.id] = changelog_item
                
    except FileNotFoundError:
        print("No initial data file found, starting with empty databases")
    except json.JSONDecodeError:
        print("Error parsing initial data file")

# Load initial data when starting
load_initial_data()
```

```json
// initial_data.json
{
    "roadmap": [
        {
            "id": "1",
            "title": "Smart Contract Upgrade",
            "description": "Implement new smart contract features for improved functionality",
            "status": "in_progress",
            "priority": "high",
            "target_release": "Q3 2023"
        },
        {
            "id": "2",
            "title": "Mobile Wallet Integration",
            "description": "Add support for mobile wallet connections",
            "status": "planned",
            "priority": "medium",
            "target_release": "Q4 2023"
        },
        {
            "id": "3",
            "title": "Cross-Chain Support",
            "description": "Enable transactions across different blockchain networks",
            "status": "planned",
            "priority": "critical",
            "target_release": "Q1 2024"
        }
    ],
    "changelog": [
        {
            "id": "1",
            "version": "1.2.0",
            "release_date": "2023-05-15T00:00:00",
            "changes": [
                "Added support for ERC-721 tokens",
                "Improved transaction speed by 20%",
                "Fixed wallet connection issues"
            ]
        },
        {
            "id": "2",
            "version": "1.1.0",
            "release_date": "2023-03-10T00:00:00",
            "changes": [
                "Implemented new dashboard UI",
                "Added transaction history export",
                "Fixed minor security vulnerabilities"
            ]
        }
    ]
}
```

```python
# requirements.txt
fastapi>=0.95.0
uvicorn>=0.21.0
pydantic>=1.10.0
python-multipart>=0.0.5
```

```bash
# run.sh
uvicorn roadmap:app --reload --host 0.0.0.0 --port 8000
```
