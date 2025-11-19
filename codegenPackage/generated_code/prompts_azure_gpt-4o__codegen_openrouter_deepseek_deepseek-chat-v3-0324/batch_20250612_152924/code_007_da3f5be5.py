"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: Generate code to create a multilingual job posting system for recruiting Latin American talent in European markets, as discussed in Management en Red's blog.
Generated: DETERMINISTIC_da3f5be57263ee2b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Multilingual Job Posting System for Latin American Talent in European Markets
"""

import json
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Initialize FastAPI app
app = FastAPI(
    title="Multilingual Job Posting System",
    description="System for recruiting Latin American talent in European markets",
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

# Supported languages
class Language(str, Enum):
    SPANISH = "es"
    PORTUGUESE = "pt"
    ENGLISH = "en"
    GERMAN = "de"
    FRENCH = "fr"
    ITALIAN = "it"
    DUTCH = "nl"

# Job types
class JobType(str, Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    INTERNSHIP = "internship"

# Experience levels
class ExperienceLevel(str, Enum):
    ENTRY = "entry"
    MID = "mid"
    SENIOR = "senior"
    EXECUTIVE = "executive"

# Job posting model
class JobPosting(BaseModel):
    id: str = Field(..., description="Unique identifier for the job posting")
    title: Dict[Language, str] = Field(..., description="Job title in multiple languages")
    description: Dict[Language, str] = Field(..., description="Job description in multiple languages")
    requirements: Dict[Language, List[str]] = Field(..., description="Job requirements in multiple languages")
    location: str = Field(..., description="Job location (city, country)")
    job_type: JobType = Field(..., description="Type of employment")
    experience_level: ExperienceLevel = Field(..., description="Required experience level")
    salary_range: Optional[str] = Field(None, description="Salary range information")
    benefits: Dict[Language, List[str]] = Field(default_factory=dict, description="Job benefits in multiple languages")
    company: str = Field(..., description="Company name")
    contact_email: str = Field(..., description="Contact email for applications")
    posted_date: datetime = Field(default_factory=datetime.now, description="Date when job was posted")
    expiration_date: Optional[datetime] = Field(None, description="Date when job posting expires")
    is_active: bool = Field(default=True, description="Whether the job posting is active")

    @validator('contact_email')
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email format")
        return v

# In-memory database simulation
job_postings_db = {}

# Helper functions
def generate_job_id():
    return f"job_{len(job_postings_db) + 1}"

def validate_language_content(content: Dict[Language, str], field_name: str):
    if not content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} must contain at least one language"
        )
    for lang, text in content.items():
        if not text.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"{field_name} text for language {lang} cannot be empty"
            )

# API Endpoints
@app.post("/jobs/", response_model=JobPosting, status_code=status.HTTP_201_CREATED)
async def create_job_posting(job: JobPosting):
    """Create a new job posting"""
    job_id = generate_job_id()
    job.id = job_id
    
    # Validate required multilingual fields
    validate_language_content(job.title, "title")
    validate_language_content(job.description, "description")
    
    job_postings_db[job_id] = job.dict()
    return job

@app.get("/jobs/", response_model=List[JobPosting])
async def get_job_postings(
    language: Language = Query(Language.SPANISH, description="Preferred language for job details"),
    job_type: Optional[JobType] = None,
    experience_level: Optional[ExperienceLevel] = None,
    location: Optional[str] = None,
    active_only: bool = True
):
    """Get all job postings with optional filters"""
    filtered_jobs = []
    
    for job_id, job_data in job_postings_db.items():
        job = JobPosting(**job_data)
        
        if active_only and not job.is_active:
            continue
        if job_type and job.job_type != job_type:
            continue
        if experience_level and job.experience_level != experience_level:
            continue
        if location and job.location.lower() != location.lower():
            continue
            
        filtered_jobs.append(job)
    
    return filtered_jobs

@app.get("/jobs/{job_id}", response_model=JobPosting)
async def get_job_posting(job_id: str, language: Language = Query(Language.SPANISH)):
    """Get a specific job posting by ID"""
    if job_id not in job_postings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job posting not found"
        )
    return JobPosting(**job_postings_db[job_id])

@app.put("/jobs/{job_id}", response_model=JobPosting)
async def update_job_posting(job_id: str, job_update: JobPosting):
    """Update an existing job posting"""
    if job_id not in job_postings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job posting not found"
        )
    
    # Validate required multilingual fields
    validate_language_content(job_update.title, "title")
    validate_language_content(job_update.description, "description")
    
    job_postings_db[job_id] = job_update.dict()
    return job_update

@app.patch("/jobs/{job_id}/status", response_model=JobPosting)
async def update_job_status(job_id: str, is_active: bool):
    """Update the active status of a job posting"""
    if job_id not in job_postings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job posting not found"
        )
    
    job_data = job_postings_db[job_id]
    job_data["is_active"] = is_active
    job_postings_db[job_id] = job_data
    return JobPosting(**job_data)

@app.delete("/jobs/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_job_posting(job_id: str):
    """Delete a job posting"""
    if job_id not in job_postings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job posting not found"
        )
    del job_postings_db[job_id]
    return JSONResponse(content=None, status_code=status.HTTP_204_NO_CONTENT)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Service health check"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# Sample data initialization
def initialize_sample_data():
    sample_job = JobPosting(
        id="job_1",
        title={
            Language.SPANISH: "Desarrollador de Software",
            Language.PORTUGUESE: "Desenvolvedor de Software",
            Language.ENGLISH: "Software Developer",
            Language.GERMAN: "Softwareentwickler"
        },
        description={
            Language.SPANISH: "Buscamos un desarrollador de software con experiencia en Python.",
            Language.PORTUGUESE: "Procuramos um desenvolvedor de software com experiência em Python.",
            Language.ENGLISH: "We're looking for a software developer with Python experience.",
            Language.GERMAN: "Wir suchen einen Softwareentwickler mit Python-Erfahrung."
        },
        requirements={
            Language.SPANISH: ["Experiencia con Python", "Conocimientos de bases de datos"],
            Language.PORTUGUESE: ["Experiência com Python", "Conhecimento de bancos de dados"],
            Language.ENGLISH: ["Python experience", "Database knowledge"],
            Language.GERMAN: ["Python-Erfahrung", "Datenbankkenntnisse"]
        },
        location="Berlin, Germany",
        job_type=JobType.FULL_TIME,
        experience_level=ExperienceLevel.MID,
        salary_range="€50,000 - €70,000",
        benefits={
            Language.SPANISH: ["Seguro médico", "Horario flexible"],
            Language.PORTUGUESE: ["Seguro de saúde", "Horário flexível"],
            Language.ENGLISH:
