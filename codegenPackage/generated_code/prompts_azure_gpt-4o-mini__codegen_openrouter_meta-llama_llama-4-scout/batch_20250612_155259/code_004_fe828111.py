"""
Generated Code Metadata:
========================
Original URL: https://cancellationflights.com
Prompt: How can I create an API endpoint to handle account suspension requests in a RESTful service?
Generated: DETERMINISTIC_fe8281118e2876cc
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# account_suspension_api.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Account Suspension API",
    description="API endpoint to handle account suspension requests",
    version="1.0.0"
)

class SuspensionRequest(BaseModel):
    """Request body for account suspension"""
    user_id: int
    reason: str
    suspended_by: int

class SuspensionResponse(BaseModel):
    """Response body for account suspension"""
    user_id: int
    suspended: bool
    reason: str

# In-memory storage for demonstration purposes only
# Replace with a proper database in production
suspended_accounts = {}

@app.post("/accounts/suspend", response_model=SuspensionResponse, status_code=status.HTTP_201_CREATED)
async def suspend_account(suspension_request: SuspensionRequest):
    """
    Suspend a user account.

    :param suspension_request: Suspension request body
    :return: Suspension response body
    """
    try:
        user_id = suspension_request.user_id
        if user_id in suspended_accounts:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Account already suspended")

        suspended_accounts[user_id] = {
            "reason": suspension_request.reason,
            "suspended_by": suspension_request.suspended_by
        }

        return SuspensionResponse(
            user_id=user_id,
            suspended=True,
            reason=suspension_request.reason
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/accounts/{user_id}/suspension-status", response_model=Optional[SuspensionResponse])
async def get_suspension_status(user_id: int):
    """
    Get the suspension status of a user account.

    :param user_id: ID of the user account
    :return: Suspension response body or None if not suspended
    """
    try:
        account_info = suspended_accounts.get(user_id)
        if account_info is None:
            return None

        return SuspensionResponse(
            user_id=user_id,
            suspended=True,
            reason=account_info["reason"]
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.delete("/accounts/{user_id}/suspend", status_code=status.HTTP_204_NO_CONTENT)
async def unsuspend_account(user_id: int):
    """
    Unsuspend a user account.

    :param user_id: ID of the user account
    """
    try:
        if user_id not in suspended_accounts:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found or not suspended")

        del suspended_accounts[user_id]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
