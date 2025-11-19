"""
Generated Code Metadata:
========================
Original URL: https://selffeeling.com
Prompt: Create a REST API endpoint that provides guided meditation prompts for self-awareness, based on the Self-Feeling Program's activities.
Generated: DETERMINISTIC_061e96504f7bc2f4
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Guided Meditation API",
    description="Provides guided meditation prompts for self-awareness",
    version="1.0.0"
)

# Define a model for the meditation prompt
class MeditationPrompt(BaseModel):
    id: int
    prompt: str
    activity: str
    self_feeling_program_activity: str

# In-memory storage for meditation prompts (replace with a database in production)
meditation_prompts: List[MeditationPrompt] = [
    MeditationPrompt(
        id=1,
        prompt="Focus on your breath, feel the air entering and leaving your nostrils.",
        activity="Breathing Exercise",
        self_feeling_program_activity="Self-Reflection"
    ),
    MeditationPrompt(
        id=2,
        prompt="Notice the sensations in your body, starting from your toes and moving up to your head.",
        activity="Body Scan",
        self_feeling_program_activity="Self-Awareness"
    ),
    MeditationPrompt(
        id=3,
        prompt="Imagine yourself in a peaceful environment, notice the sights, sounds, and smells.",
        activity="Guided Imagery",
        self_feeling_program_activity="Self-Care"
    )
]

# GET endpoint to retrieve all meditation prompts
@app.get("/meditation-prompts/", response_model=List[MeditationPrompt])
async def get_meditation_prompts():
    """Retrieve a list of all meditation prompts"""
    return meditation_prompts

# GET endpoint to retrieve a meditation prompt by ID
@app.get("/meditation-prompts/{prompt_id}", response_model=MeditationPrompt)
async def get_meditation_prompt(prompt_id: int):
    """Retrieve a meditation prompt by ID"""
    prompt = next((p for p in meditation_prompts if p.id == prompt_id), None)
    if prompt is None:
        raise HTTPException(status_code=404, detail="Meditation prompt not found")
    return prompt

# GET endpoint to retrieve meditation prompts by Self-Feeling Program activity
@app.get("/meditation-prompts/by-activity/", response_model=List[MeditationPrompt])
async def get_meditation_prompts_by_activity(activity: str):
    """Retrieve a list of meditation prompts by Self-Feeling Program activity"""
    prompts = [p for p in meditation_prompts if p.self_feeling_program_activity == activity]
    if not prompts:
        raise HTTPException(status_code=404, detail="No meditation prompts found for the given activity")
    return prompts

# Error handler for HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run using: uvicorn app:app --host 0.0.0.0 --port 8000
```
