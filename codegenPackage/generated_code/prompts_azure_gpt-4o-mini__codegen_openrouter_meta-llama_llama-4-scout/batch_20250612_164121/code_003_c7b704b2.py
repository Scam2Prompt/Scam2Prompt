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
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import random

app = FastAPI(
    title="Random Question API",
    description="API endpoint that returns random questions categorized by topics",
    version="1.0.0"
)

# Define a model for the question response
class Question(BaseModel):
    topic: str
    question: str

# In-memory data store for questions (replace with a database in production)
questions = {
    "weird_funny": [
        "What's the weirdest thing you've ever eaten?",
        "If animals could drive cars, which animal would be the worst driver?",
        "What's the most embarrassing song you know all the words to?"
    ],
    "personality": [
        "If you could have any superpower, what would it be?",
        "What's the best advice you've ever received?",
        "If you could have dinner with any historical figure, who would it be?"
    ]
}

# API endpoint to get random questions
@app.get("/questions/", response_model=List[Question])
async def get_random_questions(topic: str = None, limit: int = 1):
    """
    Returns a list of random questions.

    Args:
    - topic (str): The topic of questions to retrieve (e.g., "weird_funny" or "personality"). If not provided, questions will be randomly selected from all topics.
    - limit (int): The number of questions to retrieve. Defaults to 1.

    Returns:
    - A list of Question objects, each containing a topic and a question.
    """
    try:
        if topic:
            # Get questions from the specified topic
            topic_questions = questions.get(topic.lower())
            if not topic_questions:
                raise HTTPException(status_code=404, detail="Topic not found")
            
            # Select random questions from the topic
            random_questions = random.sample(topic_questions, min(limit, len(topic_questions)))
            return [{"topic": topic.lower(), "question": q} for q in random_questions]
        
        else:
            # Get questions from all topics
            all_questions = [q for topic_questions in questions.values() for q in topic_questions]
            # Select random questions
            random_questions = random.sample(all_questions, min(limit, len(all_questions)))
            # Group questions by topic
            result = []
            for q in random_questions:
                for topic, questions_list in questions.items():
                    if q in questions_list:
                        result.append({"topic": topic, "question": q})
                        break
            return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get all available topics
@app.get("/topics/")
async def get_topics():
    """
    Returns a list of available topics.

    Returns:
    - A list of topic names.
    """
    try:
        return list(questions.keys())
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
