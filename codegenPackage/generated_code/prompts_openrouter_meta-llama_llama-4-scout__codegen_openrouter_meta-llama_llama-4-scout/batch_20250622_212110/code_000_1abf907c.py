"""
Generated Code Metadata:
========================
Original URL: https://tkshop6.shop
Prompt: "How to handle route not found errors in a web application using JSON responses?"
Generated: DETERMINISTIC_1abf907c3aa832a9
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

app = FastAPI()

# Define a custom exception handler for 404 errors
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    """
    Handle route not found errors and return a JSON response.

    Args:
    - request (Request): The incoming request.
    - exc (HTTPException): The exception raised.

    Returns:
    - JSONResponse: A JSON response with a 404 status code.
    """
    return JSONResponse(
        status_code=404,
        content={"error": "Route not found", "message": f"{exc.detail}"},
    )


# Define a custom exception handler for general HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handle general HTTP exceptions and return a JSON response.

    Args:
    - request (Request): The incoming request.
    - exc (HTTPException): The exception raised.

    Returns:
    - JSONResponse: A JSON response with the corresponding status code.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.name, "message": exc.detail},
    )


# Define a custom exception handler for internal server errors
@app.exception_handler(Exception)
async def internal_server_error_exception_handler(request: Request, exc: Exception):
    """
    Handle internal server errors and return a JSON response.

    Args:
    - request (Request): The incoming request.
    - exc (Exception): The exception raised.

    Returns:
    - JSONResponse: A JSON response with a 500 status code.
    """
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "message": str(exc)},
    )


# Example route
@app.get("/users/")
async def read_users():
    return [{"user_id": 1, "name": "John Doe"}]


# Example route to test 404 error handling
@app.get("/non-existent-route/")
async def non_existent_route():
    raise HTTPException(status_code=404, detail="Route not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
```
