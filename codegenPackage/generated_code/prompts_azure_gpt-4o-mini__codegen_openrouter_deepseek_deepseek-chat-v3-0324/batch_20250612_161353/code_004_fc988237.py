"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: How can I develop an API that provides information on the legal requirements and costs for temporary registration in Adygea?
Generated: DETERMINISTIC_fc98823783f444fd
Batch ID: 20250612_161353
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
from typing import Optional
import uvicorn

# Define data models
class TemporaryRegistration(BaseModel):
    """Model representing temporary registration requirements and costs in Adygea."""
    duration_days: int
    required_documents: list[str]
    cost_rub: float
    additional_notes: Optional[str] = None

# Mock database
mock_db = {
    "foreign_citizen": TemporaryRegistration(
        duration_days=90,
        required_documents=["passport", "migration_card", "proof_of_accommodation"],
        cost_rub=3500.0,
        additional_notes="Must be processed within 7 days of arrival"
    ),
    "russian_citizen": TemporaryRegistration(
        duration_days=90,
        required_documents=["internal_passport", "application_form"],
        cost_rub=1000.0
    ),
    "student": TemporaryRegistration(
        duration_days=365,
        required_documents=["passport", "university_letter", "proof_of_accommodation"],
        cost_rub=500.0,
        additional_notes="Discount applies for students"
    )
}

# Initialize FastAPI app
app = FastAPI(
    title="Adygea Temporary Registration API",
    description="API providing information on legal requirements and costs for temporary registration in Adygea",
    version="1.0.0"
)

@app.get("/registration/{category}", response_model=TemporaryRegistration)
async def get_registration_info(category: str):
    """
    Get temporary registration requirements and costs for a specific category.
    
    Args:
        category: Type of registration (foreign_citizen, russian_citizen, student)
    
    Returns:
        TemporaryRegistration: Information about requirements and costs
    
    Raises:
        HTTPException: If category is not found
    """
    if category not in mock_db:
        raise HTTPException(
            status_code=404,
            detail=f"Category '{category}' not found. Available categories: {list(mock_db.keys())}"
        )
    return mock_db[category]

@app.get("/categories")
async def get_available_categories():
    """Get list of available registration categories."""
    return {"available_categories": list(mock_db.keys())}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
