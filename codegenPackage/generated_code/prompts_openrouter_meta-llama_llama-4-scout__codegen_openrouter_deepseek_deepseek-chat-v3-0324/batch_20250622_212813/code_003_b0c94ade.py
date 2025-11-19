"""
Generated Code Metadata:
========================
Original URL: https://staylodu.io
Prompt: Design an API endpoint to retrieve and display the current top contributors on Loud, including their mindshare, earnings, and rankings.
Generated: DETERMINISTIC_b0c94aded253ed04
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
import asyncpg
import os
from fastapi.middleware.cors import CORSMiddleware

# Database connection settings
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/loud")

app = FastAPI(
    title="Loud Contributors API",
    description="API to retrieve top contributors on Loud platform",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response validation
class Contributor(BaseModel):
    user_id: str
    username: str
    avatar_url: str
    mindshare: float
    earnings: float
    ranking: int
    last_updated: datetime

class TopContributorsResponse(BaseModel):
    contributors: List[Contributor]
    count: int
    last_updated: datetime

# Database connection pool
async def get_db_connection():
    return await asyncpg.connect(DATABASE_URL)

@app.on_event("startup")
async def startup():
    app.state.db_pool = await asyncpg.create_pool(DATABASE_URL)

@app.on_event("shutdown")
async def shutdown():
    await app.state.db_pool.close()

@app.get("/contributors/top", response_model=TopContributorsResponse)
async def get_top_contributors(limit: int = 10):
    """
    Retrieve the top contributors on Loud platform.
    
    Parameters:
    - limit: Number of top contributors to return (default: 10, max: 100)
    
    Returns:
    - List of contributors with their mindshare, earnings, and rankings
    """
    if limit <= 0 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 100"
        )

    try:
        async with app.state.db_pool.acquire() as connection:
            query = """
                SELECT 
                    user_id, 
                    username, 
                    avatar_url, 
                    mindshare, 
                    earnings, 
                    ranking,
                    last_updated
                FROM contributors
                ORDER BY ranking ASC
                LIMIT $1;
            """
            records = await connection.fetch(query, limit)
            
            contributors = [
                Contributor(
                    user_id=record["user_id"],
                    username=record["username"],
                    avatar_url=record["avatar_url"],
                    mindshare=record["mindshare"],
                    earnings=record["earnings"],
                    ranking=record["ranking"],
                    last_updated=record["last_updated"]
                ) for record in records
            ]
            
            # Get the latest update timestamp
            latest_update = await connection.fetchval(
                "SELECT MAX(last_updated) FROM contributors;"
            )
            
            return TopContributorsResponse(
                contributors=contributors,
                count=len(contributors),
                last_updated=latest_update
            )
            
    except asyncpg.PostgresError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify API is running.
    """
    try:
        async with app.state.db_pool.acquire() as connection:
            await connection.execute("SELECT 1")
        return {"status": "healthy"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Service unavailable: {str(e)}"
        )
```
