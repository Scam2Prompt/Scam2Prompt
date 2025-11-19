"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: How can I create an interactive API that teaches civic education to young students, inspired by the "Vivir es Convivir" initiative from Fundación Patricio Aylwin?
Generated: DETERMINISTIC_1ea9a0893c61bd13
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Civic Education API",
    description="Interactive API for teaching civic education to young students, inspired by 'Vivir es Convivir' initiative",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class Lesson(BaseModel):
    id: int
    title: str
    description: str
    content: str
    age_group: str
    difficulty: str
    interactive_activity: Optional[str] = None

class QuizQuestion(BaseModel):
    id: int
    lesson_id: int
    question: str
    options: List[str]
    correct_answer: int
    explanation: str

class UserResponse(BaseModel):
    user_id: str
    question_id: int
    selected_option: int

# Mock database
lessons_db = [
    Lesson(
        id=1,
        title="Understanding Democracy",
        description="Learn the basic principles of democracy",
        content="Democracy is a system where citizens exercise power by voting...",
        age_group="10-12",
        difficulty="Easy",
        interactive_activity="Role-play a voting scenario"
    ),
    Lesson(
        id=2,
        title="Human Rights",
        description="Introduction to basic human rights",
        content="Human rights are rights inherent to all human beings...",
        age_group="13-15",
        difficulty="Medium",
        interactive_activity="Case study analysis"
    )
]

quiz_db = [
    QuizQuestion(
        id=1,
        lesson_id=1,
        question="What is the main characteristic of democracy?",
        options=["Rule by a king", "Citizens voting for leaders", "Military control"],
        correct_answer=1,
        explanation="Democracy is characterized by citizens participating in decision-making, typically through voting."
    ),
    QuizQuestion(
        id=2,
        lesson_id=1,
        question="How often should elections occur in a democracy?",
        options=["Never", "Only when the leader decides", "At regular intervals"],
        correct_answer=2,
        explanation="Regular elections are essential for democracy to ensure leaders remain accountable."
    )
]

user_responses = []

# API endpoints
@app.get("/lessons/", response_model=List[Lesson])
async def get_lessons(
    age_group: Optional[str] = Query(None, description="Filter by age group (e.g., '10-12')"),
    difficulty: Optional[str] = Query(None, description="Filter by difficulty level (e.g., 'Easy')")
):
    """Get all lessons, optionally filtered by age group or difficulty"""
    filtered_lessons = lessons_db
    
    if age_group:
        filtered_lessons = [lesson for lesson in filtered_lessons if lesson.age_group == age_group]
    
    if difficulty:
        filtered_lessons = [lesson for lesson in filtered_lessons if lesson.difficulty == difficulty]
    
    return filtered_lessons

@app.get("/lessons/{lesson_id}", response_model=Lesson)
async def get_lesson(lesson_id: int):
    """Get a specific lesson by ID"""
    lesson = next((lesson for lesson in lessons_db if lesson.id == lesson_id), None)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@app.get("/lessons/{lesson_id}/quiz", response_model=List[QuizQuestion])
async def get_lesson_quiz(lesson_id: int):
    """Get quiz questions for a specific lesson"""
    questions = [q for q in quiz_db if q.lesson_id == lesson_id]
    if not questions:
        raise HTTPException(status_code=404, detail="No quiz questions found for this lesson")
    return questions

@app.post("/quiz/submit", response_model=dict)
async def submit_quiz_response(response: UserResponse):
    """Submit a user's quiz response and get feedback"""
    question = next((q for q in quiz_db if q.id == response.question_id), None)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    user_responses.append(response)
    
    is_correct = response.selected_option == question.correct_answer
    feedback = {
        "is_correct": is_correct,
        "correct_answer": question.correct_answer,
        "explanation": question.explanation
    }
    
    return feedback

@app.get("/user/{user_id}/progress", response_model=dict)
async def get_user_progress(user_id: str):
    """Get a user's progress and performance"""
    user_answers = [r for r in user_responses if r.user_id == user_id]
    if not user_answers:
        raise HTTPException(status_code=404, detail="No responses found for this user")
    
    correct_answers = sum(
        1 for r in user_answers 
        if any(r.selected_option == q.correct_answer 
               for q in quiz_db if q.id == r.question_id)
    )
    
    total_questions = len(user_answers)
    score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    
    return {
        "user_id": user_id,
        "total_questions_answered": total_questions,
        "correct_answers": correct_answers,
        "score": f"{score:.1f}%",
        "lessons_completed": len({r.question_id for r in user_answers})
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
