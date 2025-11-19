"""
Generated Code Metadata:
========================
Original URL: https://proximus-re.was-systems.com
Prompt: Generate a code snippet that validates user input for a recommendation system, ensuring that all fields are filled out correctly before submission.
Generated: DETERMINISTIC_0bf9b748e34c5491
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, Optional, List
from pydantic import BaseModel, validator, ValidationError

class RecommendationInput(BaseModel):
    """
    Model for validating recommendation system input.
    """
    user_id: str
    item_id: str
    rating: float
    categories: List[str]
    feedback: Optional[str] = None

    @validator('user_id')
    def user_id_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('User ID cannot be empty')
        return v

    @validator('item_id')
    def item_id_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Item ID cannot be empty')
        return v

    @validator('rating')
    def rating_must_be_valid(cls, v):
        if not (0 <= v <= 5):
            raise ValueError('Rating must be between 0 and 5')
        return v

    @validator('categories')
    def categories_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('At least one category must be provided')
        return v

def validate_recommendation_input(input_data: Dict) -> Dict:
    """
    Validates recommendation input data and returns cleaned data or errors.
    
    Args:
        input_data: Dictionary containing user input data
        
    Returns:
        Dict: Either the validated data or error messages
    """
    try:
        validated_data = RecommendationInput(**input_data)
        return {
            'status': 'success',
            'data': validated_data.dict()
        }
    except ValidationError as e:
        errors = []
        for error in e.errors():
            field = error['loc'][0]
            msg = error['msg']
            errors.append(f"{field}: {msg}")
        return {
            'status': 'error',
            'errors': errors
        }

# Example usage
if __name__ == "__main__":
    test_input = {
        "user_id": "user123",
        "item_id": "item456",
        "rating": 4.5,
        "categories": ["books", "fiction"],
        "feedback": "Great recommendation!"
    }
    
    result = validate_recommendation_input(test_input)
    print(result)
```
