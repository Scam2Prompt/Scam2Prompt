"""
Generated Code Metadata:
========================
Original URL: https://graffian.com
Prompt: Design a data model to represent the characteristics of different cooking oils, including their nutritional value, health benefits, and environmental impact.
Generated: DETERMINISTIC_8859f79b633682fa
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

# Define the data model for CookingOil
class CookingOil(BaseModel):
    name: str = Field(..., description="Name of the cooking oil")
    nutritional_value: dict = Field(
        ..., 
        description="Nutritional information (e.g., calories, fat, vitamins)"
    )
    health_benefits: List[str] = Field(
        ..., 
        description="List of health benefits associated with the oil"
    )
    environmental_impact: Optional[str] = Field(
        None, 
        description="Environmental impact of producing the oil (e.g., carbon footprint)"
    )
    origin_country: Optional[str] = Field(
        None, 
        description="Country where the oil is primarily produced"
    )
    is_organic: bool = Field(
        ..., 
        description="Indicates whether the oil is organic"
    )

    class Config:
        schema_extra = {
            "example": {
                "name": "Olive Oil",
                "nutritional_value": {
                    "calories_per_100ml": 884,
                    "fat": "100g",
                    "saturated_fat": "14g",
                    "vitamin_e": "14mg"
                },
                "health_benefits": [
                    "Rich in antioxidants",
                    "Supports heart health",
                    "Anti-inflammatory properties"
                ],
                "environmental_impact": "Low carbon footprint",
                "origin_country": "Spain",
                "is_organic": True
            }
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of CookingOil
        olive_oil = CookingOil(
            name="Olive Oil",
            nutritional_value={
                "calories_per_100ml": 884,
                "fat": "100g",
                "saturated_fat": "14g",
                "vitamin_e": "14mg"
            },
            health_benefits=[
                "Rich in antioxidants",
                "Supports heart health",
                "Anti-inflammatory properties"
            ],
            environmental_impact="Low carbon footprint",
            origin_country="Spain",
            is_organic=True
        )
        print(olive_oil.json(indent=4))  # Print the JSON representation of the object
    except ValidationError as e:
        print("Error creating CookingOil instance:", e)
```
