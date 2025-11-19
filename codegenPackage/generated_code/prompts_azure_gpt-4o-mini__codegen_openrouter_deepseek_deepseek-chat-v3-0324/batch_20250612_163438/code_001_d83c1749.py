"""
Generated Code Metadata:
========================
Original URL: https://haciendodestinos.com
Prompt: Write a code snippet for an API that analyzes tourism data to identify potential growth areas in Argentina, inspired by the insights from Haciendo Destinos.
Generated: DETERMINISTIC_d83c1749f481e113
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Initialize FastAPI app
app = FastAPI(
    title="Tourism Data Analysis API",
    description="API to analyze tourism data and identify growth areas in Argentina",
    version="1.0.0"
)

# Pydantic model for request data validation
class TourismData(BaseModel):
    region: str
    visitors: int
    revenue: float
    infrastructure_score: float
    accessibility_score: float
    attractions_count: int

class AnalysisRequest(BaseModel):
    data: List[TourismData]
    n_clusters: Optional[int] = 3

# Helper function to preprocess data
def preprocess_data(data: List[TourismData]) -> pd.DataFrame:
    """Convert input data to DataFrame and preprocess for clustering."""
    df = pd.DataFrame([item.dict() for item in data])
    
    # Select features for clustering
    features = df[['visitors', 'revenue', 'infrastructure_score', 
                  'accessibility_score', 'attractions_count']]
    
    # Standardize features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    return df, scaled_features

@app.post("/analyze-growth-areas/", summary="Identify potential tourism growth areas")
async def analyze_growth_areas(request: AnalysisRequest):
    """
    Analyze tourism data to identify potential growth areas using K-means clustering.
    
    Args:
        request: AnalysisRequest containing tourism data and number of clusters.
        
    Returns:
        JSON response with regions grouped by growth potential.
    """
    try:
        # Preprocess data
        df, features = preprocess_data(request.data)
        
        # Perform K-means clustering
        kmeans = KMeans(n_clusters=request.n_clusters, random_state=42)
        clusters = kmeans.fit_predict(features)
        
        # Add cluster labels to dataframe
        df['cluster'] = clusters
        
        # Calculate cluster means to identify high-potential clusters
        cluster_means = df.groupby('cluster').mean(numeric_only=True)
        
        # Identify cluster with highest growth potential (highest mean scores)
        potential_cluster = cluster_means[
            ['visitors', 'revenue', 'infrastructure_score', 
             'accessibility_score', 'attractions_count']
        ].mean(axis=1).idxmax()
        
        # Get regions in the high-potential cluster
        growth_areas = df[df['cluster'] == potential_cluster]['region'].tolist()
        
        # Prepare response
        response = {
            "growth_areas": growth_areas,
            "cluster_analysis": cluster_means.to_dict(),
            "potential_cluster": int(potential_cluster)
        }
        
        return response
    
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid input data: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Sample test endpoint
@app.get("/test", include_in_schema=False)
async def test_endpoint():
    """Test endpoint with sample data."""
    sample_data = [
        {
            "region": "Buenos Aires",
            "visitors": 500000,
            "revenue": 45000000,
            "infrastructure_score": 8.5,
            "accessibility_score": 9.0,
            "attractions_count": 120
        },
        {
            "region": "Mendoza",
            "visitors": 350000,
            "revenue": 32000000,
            "infrastructure_score": 7.2,
            "accessibility_score": 7.5,
            "attractions_count": 85
        }
    ]
    return {"message": "API is working", "sample_data": sample_data}
```
