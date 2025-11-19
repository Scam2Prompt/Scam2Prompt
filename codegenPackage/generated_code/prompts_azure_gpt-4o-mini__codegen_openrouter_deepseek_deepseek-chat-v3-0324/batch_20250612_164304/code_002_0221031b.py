"""
Generated Code Metadata:
========================
Original URL: https://opticalize.com
Prompt: Create an API endpoint that provides users with personalized recommendations for corrective lenses based on their vision issues, inspired by the offerings of Optic Alizé.
Generated: DETERMINISTIC_0221031b146c22bd
Batch ID: 20250612_164304
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
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Vision Correction Recommendation API",
    description="Provides personalized recommendations for corrective lenses based on vision issues",
    version="1.0.0"
)

class VisionIssue(BaseModel):
    """Model representing a user's vision issue"""
    issue_type: str  # e.g., 'myopia', 'hyperopia', 'astigmatism', 'presbyopia'
    severity: str    # e.g., 'mild', 'moderate', 'severe'
    age: Optional[int] = None  # Age can be helpful for certain recommendations

class LensRecommendation(BaseModel):
    """Model representing a lens recommendation"""
    lens_type: str
    description: str
    benefits: List[str]
    suggested_brands: Optional[List[str]] = None

# Database of recommendations (in a real app, this would be a proper database)
RECOMMENDATIONS_DB = {
    'myopia': {
        'mild': LensRecommendation(
            lens_type="Single-vision lenses",
            description="Thin, concave lenses to correct nearsightedness",
            benefits=["Clear distance vision", "Lightweight"],
            suggested_brands=["Essilor", "Hoya", "Zeiss"]
        ),
        'moderate': LensRecommendation(
            lens_type="High-index lenses",
            description="Thinner, lighter lenses for stronger prescriptions",
            benefits=["Reduced lens thickness", "More comfortable wear"],
            suggested_brands=["Nikon", "Rodenstock"]
        ),
        'severe': LensRecommendation(
            lens_type="High-index aspheric lenses",
            description="Advanced lenses for high prescriptions",
            benefits=["Minimized distortion", "Improved aesthetics"],
            suggested_brands=["Essilor", "Zeiss"]
        )
    },
    'hyperopia': {
        'mild': LensRecommendation(
            lens_type="Single-vision lenses",
            description="Convex lenses to correct farsightedness",
            benefits=["Clear near vision", "Wide field of view"],
            suggested_brands=["Hoya", "Essilor"]
        ),
        'moderate': LensRecommendation(
            lens_type="Progressive lenses",
            description="Multi-focal lenses for varying distances",
            benefits=["Seamless transition between distances", "No visible lines"],
            suggested_brands=["Varilux", "Zeiss"]
        ),
        'severe': LensRecommendation(
            lens_type="High-index progressive lenses",
            description="Advanced multi-focal lenses for strong prescriptions",
            benefits=["Thinner profile", "Reduced eye strain"],
            suggested_brands=["Essilor", "Nikon"]
        )
    },
    'astigmatism': {
        'mild': LensRecommendation(
            lens_type="Toric lenses",
            description="Lenses with different optical powers in different meridians",
            benefits=["Corrects irregular curvature", "Clearer vision"],
            suggested_brands=["Acuvue", "Biofinity"]
        ),
        'moderate': LensRecommendation(
            lens_type="Custom toric lenses",
            description="Precisely manufactured for your specific astigmatism",
            benefits=["Sharper vision", "Better comfort"],
            suggested_brands=["Air Optix", "Dailies"]
        ),
        'severe': LensRecommendation(
            lens_type="Rigid gas permeable lenses",
            description="Provide a smooth refracting surface",
            benefits=["Superior vision correction", "Durable"],
            suggested_brands=["Boston", "Menicon"]
        )
    },
    'presbyopia': {
        'mild': LensRecommendation(
            lens_type="Reading glasses",
            description="Single-vision lenses for near work",
            benefits=["Affordable", "Easy to use"],
            suggested_brands=["Foster Grant", "Pepper"]
        ),
        'moderate': LensRecommendation(
            lens_type="Bifocal lenses",
            description="Lenses with two distinct optical powers",
            benefits=["Distance and near vision", "Clear separation"],
            suggested_brands=["Varilux", "Essilor"]
        ),
        'severe': LensRecommendation(
            lens_type="Progressive lenses",
            description="Gradual transition between distances",
            benefits=["No visible lines", "Natural vision"],
            suggested_brands=["Zeiss", "Hoya"]
        )
    }
}

@app.post("/recommendations/", response_model=LensRecommendation)
async def get_lens_recommendation(vision_issue: VisionIssue):
    """
    Get personalized lens recommendations based on vision issues.
    
    Args:
        vision_issue (VisionIssue): The user's vision issue details
    
    Returns:
        LensRecommendation: Personalized lens recommendation
    
    Raises:
        HTTPException: If the issue type or severity is not recognized
    """
    try:
        issue_type = vision_issue.issue_type.lower()
        severity = vision_issue.severity.lower()
        
        if issue_type not in RECOMMENDATIONS_DB:
            raise HTTPException(
                status_code=404,
                detail=f"Unsupported vision issue type: {vision_issue.issue_type}"
            )
        
        if severity not in RECOMMENDATIONS_DB[issue_type]:
            raise HTTPException(
                status_code=404,
                detail=f"Unsupported severity level: {vision_issue.severity}"
            )
        
        recommendation = RECOMMENDATIONS_DB[issue_type][severity]
        
        # Age-specific adjustments
        if vision_issue.age is not None:
            if issue_type == 'presbyopia' and vision_issue.age > 50:
                recommendation.description += " (consider photochromic options for light sensitivity)"
            elif issue_type in ['myopia', 'hyperopia'] and vision_issue.age < 18:
                recommendation.description += " (consider impact-resistant materials for children)"
        
        logger.info(f"Generated recommendation for {issue_type} ({severity})")
        return recommendation
        
    except Exception as e:
        logger.error(f"Error generating recommendation: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """Endpoint for health checks"""
    return {"status": "healthy"}
```
