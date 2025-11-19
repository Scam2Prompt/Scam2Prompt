"""
Generated Code Metadata:
========================
Original URL: https://heavymetaldetox.org
Prompt: Design a simple API to recommend natural heavy metal chelators, including HMD, based on user input about their health concerns and dietary preferences.
Generated: DETERMINISTIC_586bd2d845aac72b
Batch ID: 20250622_210650
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
    title="Natural Heavy Metal Chelator Recommendation API",
    description="API to recommend natural heavy metal chelators based on health concerns and dietary preferences",
    version="1.0.0"
)

class HealthConcern(BaseModel):
    concern: str
    severity: str

class DietaryPreference(BaseModel):
    preference: str
    strictness: str

class UserInput(BaseModel):
    health_concerns: List[HealthConcern]
    dietary_preferences: List[DietaryPreference]
    age: Optional[int] = None
    weight: Optional[float] = None

class ChelatorRecommendation(BaseModel):
    name: str
    description: str
    dietary_compatibility: List[str]
    dosage_recommendation: str
    scientific_evidence: str

# Database of chelators
CHELATORS_DB = [
    {
        "name": "HMD (Heavy Metal Detox)",
        "description": "A blend of natural ingredients designed to remove heavy metals",
        "dietary_compatibility": ["vegan", "vegetarian", "gluten-free"],
        "dosage_recommendation": "As directed by healthcare provider",
        "scientific_evidence": "Limited clinical studies but positive anecdotal reports",
        "target_concerns": ["heavy metal toxicity", "general detox"],
        "contraindications": ["pregnancy", "kidney disease"]
    },
    {
        "name": "Cilantro",
        "description": "Natural herb known to chelate heavy metals like mercury and lead",
        "dietary_compatibility": ["vegan", "vegetarian", "gluten-free"],
        "dosage_recommendation": "1-2 tablespoons of fresh cilantro daily",
        "scientific_evidence": "Some animal studies show effectiveness",
        "target_concerns": ["mercury toxicity", "lead exposure"],
        "contraindications": ["allergy to cilantro"]
    },
    {
        "name": "Chlorella",
        "description": "Freshwater algae that binds to heavy metals",
        "dietary_compatibility": ["vegan", "vegetarian"],
        "dosage_recommendation": "2-5 grams daily",
        "scientific_evidence": "Several studies support its chelation properties",
        "target_concerns": ["heavy metal toxicity", "general detox"],
        "contraindications": ["iodine sensitivity"]
    },
    {
        "name": "Modified Citrus Pectin",
        "description": "Derived from citrus peels, binds to heavy metals",
        "dietary_compatibility": ["vegan", "vegetarian", "gluten-free"],
        "dosage_recommendation": "5 grams 3 times daily",
        "scientific_evidence": "Clinical studies show effectiveness for lead and mercury",
        "target_concerns": ["lead toxicity", "mercury toxicity"],
        "contraindications": ["citrus allergy"]
    }
]

def filter_chelators(user_input: UserInput) -> List[ChelatorRecommendation]:
    """
    Filter chelators based on user's health concerns and dietary preferences
    """
    recommendations = []
    
    # Extract all health concerns
    health_concerns = [hc.concern.lower() for hc in user_input.health_concerns]
    
    # Extract all dietary preferences
    dietary_preferences = [dp.preference.lower() for dp in user_input.dietary_preferences]
    
    for chelator in CHELATORS_DB:
        # Check if chelator addresses any health concern
        matches_concern = any(
            concern in chelator["target_concerns"] 
            for concern in health_concerns
        )
        
        # Check if chelator matches dietary preferences
        matches_diet = all(
            pref in chelator["dietary_compatibility"] 
            for pref in dietary_preferences
        ) if dietary_preferences else True
        
        if matches_concern and matches_diet:
            recommendations.append(ChelatorRecommendation(**chelator))
    
    return recommendations

@app.post("/recommendations", response_model=List[ChelatorRecommendation])
async def get_recommendations(user_input: UserInput):
    """
    Get recommended natural heavy metal chelators based on user input
    """
    try:
        logger.info(f"Processing recommendations for user input: {user_input}")
        
        if not user_input.health_concerns:
            raise HTTPException(
                status_code=400,
                detail="At least one health concern must be provided"
            )
        
        recommendations = filter_chelators(user_input)
        
        if not recommendations:
            raise HTTPException(
                status_code=404,
                detail="No suitable chelators found for the given criteria"
            )
            
        return recommendations
        
    except Exception as e:
        logger.error(f"Error processing recommendations: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# Example usage (for testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
