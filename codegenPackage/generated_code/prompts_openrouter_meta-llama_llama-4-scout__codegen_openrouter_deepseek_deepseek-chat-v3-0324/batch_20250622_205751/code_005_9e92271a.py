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
"""
Trait Analysis REST API Service
This service provides endpoints for analyzing NFT traits and calculating rarity scores.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI(
    title="Trait Analysis API",
    description="API for analyzing NFT traits and calculating rarity scores",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@traitsniper.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database mock (in production, use a real database)
traits_db = {}
collections_db = {}
analyses_db = {}

class Trait(BaseModel):
    trait_type: str
    value: str
    count: int
    rarity_score: Optional[float] = None

class NFT(BaseModel):
    token_id: str
    traits: List[Trait]
    overall_rarity: Optional[float] = None

class Collection(BaseModel):
    collection_id: UUID
    name: str
    description: Optional[str] = None
    nfts: List[NFT]
    total_supply: int

class AnalysisRequest(BaseModel):
    collection_id: UUID
    recalculate: Optional[bool] = False

class AnalysisResult(BaseModel):
    analysis_id: UUID
    collection_id: UUID
    status: str
    top_rarities: List[NFT]
    timestamp: str

@app.post("/collections/", status_code=status.HTTP_201_CREATED)
async def create_collection(collection: Collection):
    """
    Create a new NFT collection for trait analysis.
    """
    if collection.collection_id in collections_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Collection ID already exists"
        )
    
    collections_db[collection.collection_id] = collection
    return {"message": "Collection created successfully", "collection_id": collection.collection_id}

@app.get("/collections/{collection_id}", response_model=Collection)
async def get_collection(collection_id: UUID):
    """
    Retrieve collection details by ID.
    """
    if collection_id not in collections_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collection not found"
        )
    return collections_db[collection_id]

@app.post("/analyses/", status_code=status.HTTP_202_ACCEPTED)
async def create_analysis(request: AnalysisRequest):
    """
    Initiate a new trait analysis for a collection.
    """
    if request.collection_id not in collections_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collection not found"
        )
    
    analysis_id = uuid4()
    analyses_db[analysis_id] = {
        "status": "processing",
        "collection_id": request.collection_id
    }
    
    # In a real implementation, this would trigger an async analysis process
    return {
        "message": "Analysis started",
        "analysis_id": analysis_id,
        "status_check_url": f"/analyses/{analysis_id}/status"
    }

@app.get("/analyses/{analysis_id}", response_model=AnalysisResult)
async def get_analysis(analysis_id: UUID):
    """
    Retrieve analysis results by ID.
    """
    if analysis_id not in analyses_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Analysis not found"
        )
    
    # Mock result - in production this would come from completed analysis
    mock_result = AnalysisResult(
        analysis_id=analysis_id,
        collection_id=analyses_db[analysis_id]["collection_id"],
        status="completed",
        top_rarities=[],
        timestamp="2023-01-01T00:00:00Z"
    )
    
    return mock_result

@app.get("/collections/{collection_id}/nfts/{token_id}", response_model=NFT)
async def get_nft_details(collection_id: UUID, token_id: str):
    """
    Get detailed trait information for a specific NFT.
    """
    if collection_id not in collections_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collection not found"
        )
    
    collection = collections_db[collection_id]
    for nft in collection.nfts:
        if nft.token_id == token_id:
            return nft
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="NFT not found in collection"
    )

@app.get("/collections/{collection_id}/traits", response_model=List[Trait])
async def get_collection_traits(collection_id: UUID):
    """
    Get all unique traits for a collection with their counts and rarity scores.
    """
    if collection_id not in collections_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collection not found"
        )
    
    # In production, this would aggregate traits from the collection's NFTs
    return []

@app.get("/health")
async def health_check():
    """
    Health check endpoint for service monitoring.
    """
    return {"status": "healthy"}

# Error handlers
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(exc)
    )

@app.exception_handler(Exception)
async def generic_error_handler(request, exc):
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="An unexpected error occurred"
    )
```
