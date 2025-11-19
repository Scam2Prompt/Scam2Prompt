"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brix-group.com
Prompt: How does Brix Group recommend handling server errors, specifically error 454?
Generated: DETERMINISTIC_dde7e7a791861d60
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# server_error_handler.py

from http import HTTPStatus

class ServerError(Exception):
    """Custom exception to handle server errors."""
    pass

def handle_server_error(error_code):
    """
    Handles server errors based on the provided error code.
    
    Args:
        error_code (int): The error code returned by the server.
    
    Returns:
        str: A user-friendly message explaining the error and next steps.
    
    Raises:
        ServerError: If the error code is 454, raises a custom exception.
    """
    try:
        error_messages = {
            HTTPStatus.INTERNAL_SERVER_ERROR: "Internal server error occurred.",
            HTTPStatus.NOT_FOUND: "Resource not found.",
            HTTPStatus.UNAUTHORIZED: "Unauthorized access attempt detected.",
            454: "Session expired. Please log in again to continue.",
        }
        
        # Check if the error code is specifically 454 (Session expired).
        if error_code == 454:
            raise ServerError("Error 454: Session expired. User action required.")
        
        # Return a general error message if recognized
        return error_messages.get(error_code, "An unknown error occurred.")
    
    except ServerError as e:
        # Log the error (could be to a file or monitoring service in production)
        print(f"Logging error: {str(e)}")
        # Re-raise the exception so it can be handled upstream if needed
        raise
    
    except Exception as e:
        # Handle unexpected errors gracefully and log them
        print(f"Unexpected error occurred: {str(e)}")
        return "An unexpected error occurred. Please try again later."

# Example usage:
if __name__ == "__main__":
    try:
        # Simulate handling various error codes
        print(handle_server_error(454))  # Should raise a ServerError
        print(handle_server_error(404))  # Should return "Resource not found."
        print(handle_server_error(500))  # Should return "Internal server error occurred."
        print(handle_server_error(123))  # Should return "An unknown error occurred."
    except ServerError as e:
        print(f"Handled specific error: {str(e)}")
    except Exception as e:
        print(f"Unhandled exception: {str(e)}")
```
