"""
Generated Code Metadata:
========================
Original URL: https://haitwik.com
Prompt: Generate a simple API that returns a greeting message, similar to the repetitive structure found on the haitwik website.
Generated: DETERMINISTIC_94875af260b916b4
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Greeting API",
    description="A simple API that returns a greeting message",
    version="1.0.0",
)

class GreetingRequest(BaseModel):
    """Request model for greeting endpoint"""
    name: str

class GreetingResponse(BaseModel):
    """Response model for greeting endpoint"""
    message: str

@app.get("/greet", response_model=GreetingResponse)
async def get_greeting(request: GreetingRequest):
    """
    Returns a personalized greeting message.

    Args:
    - name (str): The name to include in the greeting

    Returns:
    - message (str): A greeting message with the provided name
    """
    try:
        message = f"Hello, {request.name}!"
        return {"message": message}
    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        return {"message": "Failed to generate greeting"}

@app.get("/greet/random", response_model=GreetingResponse)
async def get_random_greeting():
    """
    Returns a random greeting message.

    Returns:
    - message (str): A random greeting message
    """
    try:
        greetings = [
            "Hello!",
            "Hi there!",
            "Hey!",
            "Greetings!",
            "Salutations!"
        ]
        import random
        message = random.choice(greetings)
        return {"message": message}
    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        return {"message": "Failed to generate greeting"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# To run this code, save it in a file named app.py, 
# install required packages with pip install fastapi uvicorn,
# and execute with uvicorn app:app --host 0.0.0.0 --port 8000
```
