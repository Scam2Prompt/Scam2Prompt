"""
Generated Code Metadata:
========================
Original URL: https://eijhfcc.r.bh.d.sendibt3.com
Prompt: Provide an example of how to implement Sendinblue's Zero Tolerance Policy Towards Spam in an email-sending application.
Generated: DETERMINISTIC_399a0fe846d21d68
Batch ID: 20250612_152405
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sendinblue.com/v3/smtp/email": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from typing import List, Dict, Optional
from pydantic import BaseModel, EmailStr, validator
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Configuration
SENDINBLUE_API_KEY = "your_sendinblue_api_key"
SENDINBLUE_API_URL = "https://api.sendinblue.com/v3/smtp/email"
HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "api-key": SENDINBLUE_API_KEY
}

class EmailRecipient(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class EmailContent(BaseModel):
    subject: str
    html_content: str
    plain_text_content: Optional[str] = None

class EmailRequest(BaseModel):
    sender: EmailRecipient
    to: List[EmailRecipient]
    content: EmailContent
    headers: Optional[Dict[str, str]] = None

    @validator('to')
    def validate_recipients(cls, v):
        if len(v) > 50:
            raise ValueError("Sendinblue allows maximum 50 recipients per email")
        return v

def validate_recipient_consent(recipients: List[EmailRecipient]) -> bool:
    """Validate that all recipients have explicitly opted in"""
    # In a real implementation, this would check your database/consent records
    return all(recipient.email.endswith("@example.com") for recipient in recipients)

def send_email_via_sendinblue(email_request: EmailRequest) -> dict:
    """Send email via Sendinblue API with strict spam prevention checks"""
    if not validate_recipient_consent(email_request.to):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="All recipients must have explicitly opted in"
        )

    payload = {
        "sender": email_request.sender.dict(),
        "to": [recipient.dict() for recipient in email_request.to],
        "subject": email_request.content.subject,
        "htmlContent": email_request.content.html_content,
    }

    if email_request.content.plain_text_content:
        payload["textContent"] = email_request.content.plain_text_content

    if email_request.headers:
        payload["headers"] = email_request.headers

    response = requests.post(SENDINBLUE_API_URL, json=payload, headers=HEADERS)
    
    if response.status_code != 201:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Sendinblue API error: {response.text}"
        )

    return response.json()

@app.post("/send-email/", status_code=status.HTTP_201_CREATED)
async def send_email(email_request: EmailRequest):
    """Endpoint to send emails with strict anti-spam measures"""
    try:
        return send_email_via_sendinblue(email_request)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
```
