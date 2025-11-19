"""
Generated Code Metadata:
========================
Original URL: https://tkshop6.shop
Prompt: "Generate code for a custom 404 error page using a routing framework, returning a JSON object with a specific error code and message."
Generated: DETERMINISTIC_0b0561a8c307c4fc
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# custom_404_handler.py

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

app = FastAPI()

# Define a custom exception for 404 errors
class Custom404Exception(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)

# Define a route to handle 404 errors
@app.exception_handler(Custom404Exception)
async def custom_404_exception_handler(request: Request, exc: Custom404Exception):
    """
    Handle custom 404 exceptions and return a JSON response.

    Args:
    request (Request): The incoming request.
    exc (Custom404Exception): The custom 404 exception.

    Returns:
    Response: A JSON response with the error details.
    """
    error_code = exc.status_code
    error_message = exc.detail

    # Create a JSON response with the error details
    json_response = JSONResponse(
        content={"error_code": error_code, "error_message": error_message},
        media_type="application/json",
        status_code=error_code,
    )

    return json_response

# Define a route to test the custom 404 handler
@app.get("/test-404")
async def test_custom_404():
    """
    Test the custom 404 handler.

    Raises:
    Custom404Exception: A custom 404 exception.
    """
    raise Custom404Exception("Resource not found")

# Define a catch-all route to handle unknown routes
@app.get("/{catch_all:path}", include_in_schema=False)
async def catch_all(request: Request):
    """
    Catch-all route to handle unknown routes.

    Args:
    request (Request): The incoming request.

    Raises:
    Custom404Exception: A custom 404 exception.
    """
    raise Custom404Exception("Resource not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
