"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Develop an API endpoint that returns random questions categorized by topics such as weird/funny and personality, similar to the features on dex.chat.
Generated: DETERMINISTIC_c7b704b22efdbfb4
Batch ID: 20250612_164121
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
from typing import List, Dict
import random

app = FastAPI()

# Database mock (in a real app, this would be a proper database)
questions_db = {
    "weird_funny": [
        "If you could have any superpower, but it had to be completely useless, what would it be?",
        "What would be the worst 'buy one get one free' sale of all time?",
        "If animals could talk, which would be the rudest?",
    ],
    "personality": [
        "What's a personality trait you admire in others but don't possess yourself?",
        "What's something you believed as a child that you now realize was ridiculous?",
        "How would your best friend describe you in three words?",
    ]
}

class QuestionResponse(BaseModel):
    topic: str
    question: str

@app.get("/questions/random", response_model=QuestionResponse)
async def get_random_question(topic: str = None):
    """
    Get a random question from the database.
    
    Args:
        topic (str, optional): Specific topic to get question from. 
                              If not provided, a random topic is chosen.
    
    Returns:
        QuestionResponse: A response containing the topic and random question.
    
    Raises:
        HTTPException: If the requested topic doesn't exist or no questions are available.
    """
    try:
        # If no topic specified, choose a random one
        if topic is None:
            topic = random.choice(list(questions_db.keys()))
        
        # Validate topic exists
        if topic not in questions_db:
            raise HTTPException(status_code=404, detail="Topic not found")
        
        # Get questions for the topic
        questions = questions_db.get(topic, [])
        if not questions:
            raise HTTPException(status_code=404, detail="No questions available for this topic")
        
        # Select random question
        random_question = random.choice(questions)
        
        return {
            "topic": topic,
            "question": random_question
        }
        
    except Exception as e:
        # Log the error in production (would use proper logging)
        # logger.error(f"Error fetching random question: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/questions/topics", response_model=List[str])
async def get_available_topics():
    """
    Get list of available question topics.
    
    Returns:
        List[str]: List of available topic names.
    """
    return list(questions_db.keys())

# For production, you would also want to add:
# - Proper database connection
# - Authentication/authorization
# - Rate limiting
# - Comprehensive logging
# - Monitoring
# - Proper test coverage
```
