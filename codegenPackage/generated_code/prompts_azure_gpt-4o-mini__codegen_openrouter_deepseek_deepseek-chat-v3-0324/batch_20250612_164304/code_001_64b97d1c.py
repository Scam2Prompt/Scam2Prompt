"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: Generate a code snippet that integrates a digital tool for optimizing professional contacts in coworking environments, as discussed on NetCoworking.
Generated: DETERMINISTIC_64b97d1c3f36ce68
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
import requests
from pydantic import BaseModel, ValidationError, HttpUrl, EmailStr
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="NetCoworking Contact Optimizer",
    description="API for optimizing professional contacts in coworking environments",
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

# Pydantic models for data validation
class Contact(BaseModel):
    name: str
    email: EmailStr
    profession: str
    skills: List[str]
    bio: Optional[str] = None
    social_links: Optional[Dict[str, HttpUrl]] = None

class ContactOptimizationRequest(BaseModel):
    contacts: List[Contact]
    optimization_criteria: Dict[str, str]  # e.g., {"skill": "Python", "profession": "Developer"}

class OptimizationResponse(BaseModel):
    optimized_contacts: List[Contact]
    match_score: Dict[str, float]  # Contact email to match score mapping

# Mock database or external service integration
class ContactOptimizer:
    @staticmethod
    def optimize_contacts(request: ContactOptimizationRequest) -> OptimizationResponse:
        """
        Optimizes contacts based on given criteria.
        Implements matching algorithm based on skills and profession.
        """
        optimized_contacts = []
        match_scores = {}
        
        for contact in request.contacts:
            score = 0.0
            
            # Profession matching
            if (profession_criteria := request.optimization_criteria.get("profession")):
                if profession_criteria.lower() in contact.profession.lower():
                    score += 0.5
            
            # Skill matching
            if (skill_criteria := request.optimization_criteria.get("skill")):
                normalized_skills = [skill.lower() for skill in contact.skills]
                if skill_criteria.lower() in normalized_skills:
                    score += 0.5
            
            if score > 0:
                optimized_contacts.append(contact)
                match_scores[contact.email] = score
        
        # Sort by match score (descending)
        optimized_contacts.sort(
            key=lambda x: match_scores[x.email],
            reverse=True
        )
        
        return OptimizationResponse(
            optimized_contacts=optimized_contacts,
            match_score=match_scores
        )

# API Endpoints
@app.post("/optimize-contacts", response_model=OptimizationResponse)
async def optimize_contacts(request: ContactOptimizationRequest):
    """
    Endpoint to optimize professional contacts based on given criteria.
    Accepts a list of contacts and optimization criteria, returns optimized list.
    """
    try:
        optimizer = ContactOptimizer()
        return optimizer.optimize_contacts(request)
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=json.loads(e.json())
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """Endpoint for health checks"""
    return {"status": "healthy"}

# Example usage (would be in separate test file in production)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
