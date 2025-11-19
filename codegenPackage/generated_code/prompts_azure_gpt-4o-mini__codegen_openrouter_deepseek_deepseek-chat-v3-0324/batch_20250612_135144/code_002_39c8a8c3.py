"""
Generated Code Metadata:
========================
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Develop a study plan API that incorporates interleaving and generative learning techniques for UKMPPD exam preparation, as mentioned in the Atria content.
Generated: DETERMINISTIC_39c8a8c309537355
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Study Plan API for UKMPPD Exam Preparation
Incorporates interleaving and generative learning techniques
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, timedelta
import random
import uuid
from enum import Enum

app = FastAPI(
    title="UKMPPD Study Plan API",
    description="API for generating personalized study plans with interleaving and generative learning techniques",
    version="1.0.0"
)

# Data Models
class TopicDifficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class Topic(BaseModel):
    id: str
    name: str
    category: str
    difficulty: TopicDifficulty
    estimated_study_time: int  # in minutes

class StudySession(BaseModel):
    id: str
    date: date
    topics: List[Topic]
    duration: int  # in minutes
    session_type: str  # e.g., "interleaved", "focused", "generative"

class StudyPlan(BaseModel):
    id: str
    user_id: str
    start_date: date
    end_date: date
    total_study_hours: int
    sessions: List[StudySession]

class GeneratePlanRequest(BaseModel):
    user_id: str
    topics: List[Topic]
    start_date: date
    end_date: date
    daily_study_hours: int
    interleaving_ratio: float = 0.3  # 30% interleaved sessions by default
    generative_ratio: float = 0.2    # 20% generative sessions by default

# In-memory database (replace with persistent storage in production)
study_plans_db = {}

# Helper Functions
def calculate_total_study_days(start_date: date, end_date: date) -> int:
    return (end_date - start_date).days + 1

def generate_session_id() -> str:
    return str(uuid.uuid4())

def select_topics_for_interleaving(topics: List[Topic], count: int) -> List[Topic]:
    """Select topics from different categories for interleaving"""
    categories = list(set(topic.category for topic in topics))
    selected = []
    
    while len(selected) < count and categories:
        # Pick a random category
        category = random.choice(categories)
        # Get all topics from that category
        category_topics = [t for t in topics if t.category == category]
        if category_topics:
            selected.append(random.choice(category_topics))
            categories.remove(category)  # Ensure we get topics from different categories
    
    # If we still need more topics, fill randomly
    while len(selected) < count and topics:
        topic = random.choice(topics)
        if topic not in selected:
            selected.append(topic)
    
    return selected[:count]

def create_generative_session(topics: List[Topic], duration: int) -> StudySession:
    """Create a generative learning session"""
    # Select a topic that hasn't been covered recently
    selected_topic = random.choice(topics)
    
    return StudySession(
        id=generate_session_id(),
        date=date.today(),  # Will be updated when added to plan
        topics=[selected_topic],
        duration=duration,
        session_type="generative"
    )

def create_interleaved_session(topics: List[Topic], duration: int) -> StudySession:
    """Create an interleaved learning session"""
    # Number of topics to interleave (3-5 topics per session)
    num_topics = min(max(3, duration // 30), 5)  # 30 min per topic
    
    selected_topics = select_topics_for_interleaving(topics, num_topics)
    
    return StudySession(
        id=generate_session_id(),
        date=date.today(),  # Will be updated when added to plan
        topics=selected_topics,
        duration=duration,
        session_type="interleaved"
    )

def create_focused_session(topic: Topic, duration: int) -> StudySession:
    """Create a focused learning session on a single topic"""
    return StudySession(
        id=generate_session_id(),
        date=date.today(),  # Will be updated when added to plan
        topics=[topic],
        duration=duration,
        session_type="focused"
    )

# API Endpoints
@app.post("/study-plans/", response_model=StudyPlan, status_code=status.HTTP_201_CREATED)
async def generate_study_plan(request: GeneratePlanRequest):
    """Generate a personalized study plan with interleaving and generative learning"""
    try:
        # Validate input
        if request.start_date > request.end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="End date must be after start date"
            )
        
        if not request.topics:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least one topic is required"
            )
        
        total_days = calculate_total_study_days(request.start_date, request.end_date)
        total_study_minutes = total_days * request.daily_study_hours * 60
        total_available_minutes = sum(t.estimated_study_time for t in request.topics)
        
        if total_study_minutes < total_available_minutes * 0.8:  # At least 80% coverage
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Insufficient study time to cover topics adequately"
            )
        
        # Generate plan
        plan_id = str(uuid.uuid4())
        study_plan = StudyPlan(
            id=plan_id,
            user_id=request.user_id,
            start_date=request.start_date,
            end_date=request.end_date,
            total_study_hours=total_days * request.daily_study_hours,
            sessions=[]
        )
        
        # Calculate session counts
        total_sessions = total_days * 2  # Assuming 2 sessions per day
        interleaved_sessions = int(total_sessions * request.interleaving_ratio)
        generative_sessions = int(total_sessions * request.generative_ratio)
        focused_sessions = total_sessions - interleaved_sessions - generative_sessions
        
        # Create sessions
        all_sessions = []
        
        # Create interleaved sessions
        for _ in range(interleaved_sessions):
            session_duration = random.randint(90, 120)  # 1.5-2 hour sessions
            session = create_interleaved_session(request.topics, session_duration)
            all_sessions.append(session)
        
        # Create generative sessions
        for _ in range(generative_sessions):
            session_duration = random.randint(60, 90)  # 1-1.5 hour sessions
            session = create_generative_session(request.topics, session_duration)
            all_sessions.append(session)
        
        # Create focused sessions
        for _ in range(focused_sessions):
            topic = random.choice(request.topics)
            session_duration = min(topic.estimated_study_time, 120)  # Cap at 2 hours
            session = create_focused_session(topic, session_duration)
            all_sessions.append(session)
        
        # Shuffle sessions to mix types
        random.shuffle(all_sessions)
        
        # Assign dates to sessions (spread evenly across study period)
        current_date = request.start_date
        sessions_per_day = 2  # Morning and afternoon sessions
        sessions_assigned = 0
        
        while current_date <= request.end_date and sessions_assigned < len(all_sessions):
            for i in range(sessions_per_day):
                if sessions_assigned < len(all_sessions):
                    all_sessions[sessions_assigned].date = current_date
                    sessions_assigned += 1
            current_date += timedelta(days=1)
        
        # Add sessions to plan
        study_plan.sessions = all_sessions
        
        # Store plan
        study_plans_db[plan_id] = study_plan
        
        return study_plan
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/study-plans/{plan_id}", response_model=StudyPlan)
async def get_study_plan(plan_id: str):
    """Retrieve a study plan by ID"""
    if plan_id not in study_plans_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Study plan not found"
        )
    return study_plans_db[plan_id]

@app.get("/study-plans/user/{user_id}", response_model=List[StudyPlan])
async def get_user_study_plans(user_id: str):
    """Retrieve all study plans for a user"""
    user_plans = [plan for plan in study_plans_db.values() if plan.user_id == user_id]
    return user_plans

@app.delete("/study-pl
