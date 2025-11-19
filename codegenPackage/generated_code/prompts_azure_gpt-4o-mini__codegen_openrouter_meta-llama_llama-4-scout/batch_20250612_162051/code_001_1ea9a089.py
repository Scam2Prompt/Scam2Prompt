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
# civic_education_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Civic Education API",
    description="Interactive API to teach civic education to young students",
    version="1.0.0"
)

# Define a model for the civic education content
class CivicContent(BaseModel):
    id: int
    question: str
    answers: List[str]
    correct_answer: int

# In-memory storage for civic education content
civic_content = [
    CivicContent(
        id=1,
        question="What is the main purpose of a constitution?",
        answers=["To establish a government", "To elect leaders", "To create laws", "To promote equality"],
        correct_answer=0
    ),
    CivicContent(
        id=2,
        question="What is the right to vote?",
        answers=["A privilege for adults", "A responsibility for citizens", "A duty for everyone", "A right for all citizens"],
        correct_answer=3
    )
]

# API endpoint to retrieve all civic education content
@app.get("/civic-content/")
async def get_civic_content():
    """Retrieve a list of all civic education content"""
    return civic_content

# API endpoint to retrieve a single civic education content by ID
@app.get("/civic-content/{content_id}")
async def get_civic_content_by_id(content_id: int):
    """Retrieve a single civic education content by ID"""
    for content in civic_content:
        if content.id == content_id:
            return content
    raise HTTPException(status_code=404, detail="Content not found")

# API endpoint to submit an answer and receive feedback
@app.post("/civic-content/{content_id}/submit")
async def submit_answer(content_id: int, answer: int):
    """Submit an answer and receive feedback"""
    for content in civic_content:
        if content.id == content_id:
            if answer == content.correct_answer:
                return {"feedback": "Correct!", "correct_answer": content.answers[content.correct_answer]}
            else:
                return {"feedback": "Incorrect", "correct_answer": content.answers[content.correct_answer]}
    raise HTTPException(status_code=404, detail="Content not found")

# Error handler for 404 exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return {"error": exc.detail}

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run using: uvicorn civic_education_api:app --host 0.0.0.0 --port 8000
```
