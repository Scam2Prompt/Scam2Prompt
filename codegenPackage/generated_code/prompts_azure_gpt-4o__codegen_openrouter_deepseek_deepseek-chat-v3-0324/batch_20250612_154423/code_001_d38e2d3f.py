"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Generate code for integrating AI-enabled recruiting tools to streamline sourcing, screening, and first-round interviews, as described in Connext's Custom Recruiting service.
Generated: DETERMINISTIC_d38e2d3f7ecba065
Batch ID: 20250612_154423
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ai-recruiting-service.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from typing import List, Dict, Optional
import requests
from pydantic import BaseModel, ValidationError
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Recruiting Tool API",
    description="API for AI-enabled recruiting tools to streamline sourcing, screening, and first-round interviews",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration from environment variables
class Config:
    AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "https://api.ai-recruiting-service.com/v1")
    API_KEY = os.getenv("API_KEY", "default-api-key")
    MAX_CANDIDATES = int(os.getenv("MAX_CANDIDATES", 100))

# Data models using Pydantic
class Candidate(BaseModel):
    id: str
    name: str
    email: str
    resume_url: str
    skills: List[str]
    experience_years: int
    current_position: Optional[str] = None

class JobDescription(BaseModel):
    id: str
    title: str
    description: str
    required_skills: List[str]
    preferred_skills: List[str]
    min_experience: int

class ScreeningResult(BaseModel):
    candidate_id: str
    job_id: str
    match_score: float
    strengths: List[str]
    weaknesses: List[str]
    recommended: bool

class InterviewQuestion(BaseModel):
    question_id: str
    question_text: str
    skill_category: str
    difficulty: str

class InterviewResponse(BaseModel):
    question_id: str
    candidate_id: str
    response_text: str
    audio_url: Optional[str] = None

class InterviewEvaluation(BaseModel):
    question_id: str
    candidate_id: str
    relevance_score: float
    clarity_score: float
    technical_score: float
    overall_score: float
    feedback: str

# API Client for AI Service
class AIServiceClient:
    def __init__(self):
        self.base_url = Config.AI_SERVICE_URL
        self.headers = {
            "Authorization": f"Bearer {Config.API_KEY}",
            "Content-Type": "application/json"
        }

    def source_candidates(self, job_description: JobDescription) -> List[Candidate]:
        """Source candidates based on job description"""
        url = f"{self.base_url}/source"
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=job_description.dict(),
                timeout=30
            )
            response.raise_for_status()
            return [Candidate(**candidate) for candidate in response.json()["candidates"]]
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sourcing candidates: {e}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="AI service unavailable"
            )
        except ValidationError as e:
            logger.error(f"Validation error for candidate data: {e}")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Invalid candidate data received"
            )

    def screen_candidates(self, candidates: List[Candidate], job_description: JobDescription) -> List[ScreeningResult]:
        """Screen candidates against job requirements"""
        url = f"{self.base_url}/screen"
        payload = {
            "candidates": [candidate.dict() for candidate in candidates],
            "job_description": job_description.dict()
        }
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return [ScreeningResult(**result) for result in response.json()["results"]]
        except requests.exceptions.RequestException as e:
            logger.error(f"Error screening candidates: {e}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="AI screening service unavailable"
            )
        except ValidationError as e:
            logger.error(f"Validation error for screening results: {e}")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Invalid screening data received"
            )

    def generate_interview_questions(self, candidate: Candidate, job_description: JobDescription) -> List[InterviewQuestion]:
        """Generate interview questions for a candidate"""
        url = f"{self.base_url}/generate-questions"
        payload = {
            "candidate": candidate.dict(),
            "job_description": job_description.dict()
        }
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return [InterviewQuestion(**question) for question in response.json()["questions"]]
        except requests.exceptions.RequestException as e:
            logger.error(f"Error generating questions: {e}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="AI question generation service unavailable"
            )
        except ValidationError as e:
            logger.error(f"Validation error for questions: {e}")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Invalid question data received"
            )

    def evaluate_interview_response(self, response: InterviewResponse) -> InterviewEvaluation:
        """Evaluate a candidate's interview response"""
        url = f"{self.base_url}/evaluate-response"
        try:
            api_response = requests.post(
                url,
                headers=self.headers,
                json=response.dict(),
                timeout=30
            )
            api_response.raise_for_status()
            return InterviewEvaluation(**api_response.json())
        except requests.exceptions.RequestException as e:
            logger.error(f"Error evaluating response: {e}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="AI evaluation service unavailable"
            )
        except ValidationError as e:
            logger.error(f"Validation error for evaluation: {e}")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Invalid evaluation data received"
            )

# API Endpoints
ai_client = AIServiceClient()

@app.post("/source-candidates", response_model=List[Candidate], tags=["Sourcing"])
async def source_candidates(job_description: JobDescription):
    """Source potential candidates for a job"""
    try:
        candidates = ai_client.source_candidates(job_description)
        return candidates[:Config.MAX_CANDIDATES]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in sourcing: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during candidate sourcing"
        )

@app.post("/screen-candidates", response_model=List[ScreeningResult], tags=["Screening"])
async def screen_candidates(candidates: List[Candidate], job_description: JobDescription):
    """Screen candidates against job requirements"""
    try:
        if len(candidates) > Config.MAX_CANDIDATES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Maximum number of candidates exceeded ({Config.MAX_CANDIDATES})"
            )
        return ai_client.screen_candidates(candidates, job_description)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in screening: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during candidate screening"
        )

@app.post("/generate-questions", response_model=List[InterviewQuestion], tags=["Interview"])
async def generate_questions(candidate: Candidate, job_description: JobDescription):
    """Generate interview questions for a candidate"""
    try:
        return ai_client.generate_interview_questions(candidate, job_description)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in question generation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during question generation"
        )

@app.post("/evaluate-response", response_model=InterviewEvaluation, tags=["Interview"])
async def evaluate_response(response: InterviewResponse):
    """Evaluate a candidate's interview response"""
    try:
        return ai_client.evaluate_interview_response(response)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in response evaluation: {e}")
        raise HTTPException(
            status_code=status.H
