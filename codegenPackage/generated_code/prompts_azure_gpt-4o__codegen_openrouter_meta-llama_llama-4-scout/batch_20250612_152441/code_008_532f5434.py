"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Create an API endpoint to fetch and display the latest additions to an IPTV service, such as new movies, series, or TV shows, as highlighted on MaxEvent's site.
Generated: DETERMINISTIC_532f54340f5ef42e
Batch ID: 20250612_152441
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
import logging
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="IPTV API",
    description="API to fetch and display the latest additions to an IPTV service",
    version="1.0.0"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a model for IPTV content
class IPTVContent(BaseModel):
    id: int
    title: str
    type: str  # movie, series, tv_show
    added_at: datetime

# In-memory data store for demonstration purposes
# Replace with a database connection in production
iptv_content = [
    IPTVContent(id=1, title="Movie 1", type="movie", added_at=datetime(2024, 9, 1)),
    IPTVContent(id=2, title="Series 1", type="series", added_at=datetime(2024, 9, 5)),
    IPTVContent(id=3, title="TV Show 1", type="tv_show", added_at=datetime(2024, 9, 10)),
]

# API endpoint to fetch latest IPTV content
@app.get("/latest-content", response_model=List[IPTVContent])
async def get_latest_content():
    try:
        # Sort IPTV content by added_at in descending order
        latest_content = sorted(iptv_content, key=lambda x: x.added_at, reverse=True)
        
        return latest_content
    except Exception as e:
        logger.error(f"Error fetching latest content: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# API endpoint to fetch IPTV content by type
@app.get("/content/by-type", response_model=List[IPTVContent])
async def get_content_by_type(type: str):
    try:
        # Filter IPTV content by type
        content_by_type = [content for content in iptv_content if content.type == type]
        
        if not content_by_type:
            raise HTTPException(status_code=404, detail="No content found for the given type")
        
        return content_by_type
    except Exception as e:
        logger.error(f"Error fetching content by type: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

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
# uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
