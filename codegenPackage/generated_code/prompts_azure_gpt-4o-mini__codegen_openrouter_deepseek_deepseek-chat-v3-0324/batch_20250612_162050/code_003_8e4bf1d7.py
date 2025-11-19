"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Develop an API that allows users to receive customized workout routines based on their fitness goals, similar to the personalized training approach of Carol Crespo.
Generated: DETERMINISTIC_8e4bf1d7f4062cb5
Batch ID: 20250612_162050
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
import random

app = FastAPI(
    title="Personalized Workout API",
    description="API to generate customized workout routines based on fitness goals",
    version="1.0.0"
)

# Data models
class Exercise(BaseModel):
    name: str
    description: str
    sets: int
    reps: int
    duration: Optional[str] = None  # For timed exercises like planks

class WorkoutRoutine(BaseModel):
    goal: str
    difficulty: str
    exercises: List[Exercise]
    duration_minutes: int

class UserRequest(BaseModel):
    goal: str
    difficulty: str = "intermediate"
    available_equipment: List[str] = []
    workout_duration: int = 30

# Exercise database
EXERCISE_DB = {
    "strength": {
        "beginner": [
            {"name": "Bodyweight Squats", "description": "Basic squat with no weight", "sets": 3, "reps": 12},
            {"name": "Push-ups", "description": "Standard push-up form", "sets": 3, "reps": 10},
            {"name": "Plank", "description": "Hold plank position", "sets": 3, "duration": "30 seconds"}
        ],
        "intermediate": [
            {"name": "Dumbbell Squats", "description": "Squat holding dumbbells", "sets": 4, "reps": 10},
            {"name": "Dumbbell Bench Press", "description": "Press dumbbells while lying on bench", "sets": 4, "reps": 8},
            {"name": "Bent-over Rows", "description": "Row dumbbells with bent torso", "sets": 3, "reps": 10}
        ],
        "advanced": [
            {"name": "Barbell Deadlifts", "description": "Lift barbell from ground to hip level", "sets": 5, "reps": 5},
            {"name": "Weighted Pull-ups", "description": "Pull-ups with added weight", "sets": 4, "reps": 6},
            {"name": "Overhead Press", "description": "Press barbell overhead", "sets": 4, "reps": 6}
        ]
    },
    "weight_loss": {
        "beginner": [
            {"name": "Jumping Jacks", "description": "Basic jumping jack motion", "sets": 3, "duration": "1 minute"},
            {"name": "Bodyweight Lunges", "description": "Alternating lunges", "sets": 3, "reps": 10},
            {"name": "Mountain Climbers", "description": "Alternating knee drives", "sets": 3, "duration": "30 seconds"}
        ],
        "intermediate": [
            {"name": "Burpees", "description": "Full body explosive exercise", "sets": 4, "reps": 10},
            {"name": "Kettlebell Swings", "description": "Hip-hinge swing motion", "sets": 4, "reps": 15},
            {"name": "Jump Rope", "description": "Basic jump rope", "sets": 3, "duration": "1 minute"}
        ],
        "advanced": [
            {"name": "Box Jumps", "description": "Explosive jumps onto box", "sets": 4, "reps": 8},
            {"name": "Battle Ropes", "description": "Alternating waves with heavy ropes", "sets": 4, "duration": "45 seconds"},
            {"name": "Sprint Intervals", "description": "30 second sprints", "sets": 6, "duration": "30 seconds"}
        ]
    },
    "endurance": {
        "beginner": [
            {"name": "Brisk Walking", "description": "Sustained fast walking", "sets": 1, "duration": "20 minutes"},
            {"name": "Cycling", "description": "Moderate pace cycling", "sets": 1, "duration": "20 minutes"},
            {"name": "Swimming", "description": "Freestyle laps", "sets": 1, "duration": "15 minutes"}
        ],
        "intermediate": [
            {"name": "Jogging", "description": "Sustained running at moderate pace", "sets": 1, "duration": "30 minutes"},
            {"name": "Rowing", "description": "Machine rowing at steady pace", "sets": 1, "duration": "20 minutes"},
            {"name": "Circuit Training", "description": "Alternating exercises with minimal rest", "sets": 3, "duration": "10 minutes"}
        ],
        "advanced": [
            {"name": "Long Distance Running", "description": "Sustained running at challenging pace", "sets": 1, "duration": "45 minutes"},
            {"name": "HIIT", "description": "High intensity interval training", "sets": 1, "duration": "30 minutes"},
            {"name": "Hill Repeats", "description": "Repeated uphill sprints", "sets": 6, "duration": "1 minute"}
        ]
    }
}

# Valid goals and difficulties
VALID_GOALS = ["strength", "weight_loss", "endurance"]
VALID_DIFFICULTIES = ["beginner", "intermediate", "advanced"]

def filter_exercises_by_equipment(exercises: List[Exercise], available_equipment: List[str]) -> List[Exercise]:
    """Filter exercises based on available equipment."""
    filtered = []
    for exercise in exercises:
        # For simplicity, we'll assume bodyweight exercises are always available
        if "dumbbell" in exercise["name"].lower() and "dumbbell" not in available_equipment:
            continue
        if "barbell" in exercise["name"].lower() and "barbell" not in available_equipment:
            continue
        if "kettlebell" in exercise["name"].lower() and "kettlebell" not in available_equipment:
            continue
        filtered.append(exercise)
    return filtered

@app.post("/generate-workout", response_model=WorkoutRoutine)
async def generate_workout(user_request: UserRequest):
    """
    Generate a personalized workout routine based on user's goals, difficulty level,
    available equipment, and desired workout duration.
    """
    # Validate input
    if user_request.goal.lower() not in VALID_GOALS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid goal. Must be one of: {', '.join(VALID_GOALS)}"
        )
    
    if user_request.difficulty.lower() not in VALID_DIFFICULTIES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid difficulty. Must be one of: {', '.join(VALID_DIFFICULTIES)}"
        )
    
    if user_request.workout_duration < 10 or user_request.workout_duration > 120:
        raise HTTPException(
            status_code=400,
            detail="Workout duration must be between 10 and 120 minutes"
        )
    
    # Get exercises for the goal and difficulty
    goal = user_request.goal.lower()
    difficulty = user_request.difficulty.lower()
    
    try:
        exercises = EXERCISE_DB[goal][difficulty]
    except KeyError:
        raise HTTPException(
            status_code=500,
            detail="Exercise database configuration error"
        )
    
    # Filter exercises based on available equipment
    available_equipment = [e.lower() for e in user_request.available_equipment]
    filtered_exercises = filter_exercises_by_equipment(exercises, available_equipment)
    
    if not filtered_exercises:
        raise HTTPException(
            status_code=400,
            detail="No exercises available for your equipment. Try adding more equipment options."
        )
    
    # Select 3-5 exercises based on workout duration
    num_exercises = min(max(3, user_request.workout_duration // 10), 5)
    selected_exercises = random.sample(filtered_exercises, min(num_exercises, len(filtered_exercises)))
    
    # Convert to Exercise objects
    exercise_objects = [Exercise(**ex) for ex in selected_exercises]
    
    return WorkoutRoutine(
        goal=goal.capitalize(),
        difficulty=difficulty.capitalize(),
        exercises=exercise_objects,
        duration_minutes=user_request.workout_duration
    )

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy"}

# For running with uvicorn directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
