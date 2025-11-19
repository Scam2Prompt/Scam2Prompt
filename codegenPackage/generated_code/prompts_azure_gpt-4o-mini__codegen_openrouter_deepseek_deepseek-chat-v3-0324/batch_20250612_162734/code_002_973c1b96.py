"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Create an API endpoint that retrieves details about various "aparelhagem" tools and their specifications for a construction application.
Generated: DETERMINISTIC_973c1b96bb646860
Batch ID: 20250612_162734
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
from typing import List, Optional

app = FastAPI(
    title="Aparelhagem Tools API",
    description="API for retrieving details about various construction tools and their specifications",
    version="1.0.0"
)

# Database mock
tools_db = [
    {
        "id": 1,
        "name": "Hammer",
        "category": "Hand Tools",
        "weight_kg": 0.5,
        "length_cm": 30,
        "material": "Steel",
        "description": "A versatile tool for driving nails."
    },
    {
        "id": 2,
        "name": "Circular Saw",
        "category": "Power Tools",
        "weight_kg": 4.2,
        "length_cm": 35,
        "material": "Metal/Plastic",
        "description": "Electric saw for cutting wood and other materials.",
        "power_watts": 1500,
        "voltage_v": 220
    },
    {
        "id": 3,
        "name": "Measuring Tape",
        "category": "Measuring Tools",
        "weight_kg": 0.2,
        "length_cm": 500,
        "material": "Plastic/Metal",
        "description": "Retractable tape for taking measurements."
    }
]

# Models
class Tool(BaseModel):
    id: int
    name: str
    category: str
    weight_kg: float
    length_cm: float
    material: str
    description: str
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Hammer",
                "category": "Hand Tools",
                "weight_kg": 0.5,
                "length_cm": 30,
                "material": "Steel",
                "description": "A versatile tool for driving nails."
            }
        }

class PowerTool(Tool):
    power_watts: int
    voltage_v: int

    class Config:
        schema_extra = {
            "example": {
                "id": 2,
                "name": "Circular Saw",
                "category": "Power Tools",
                "weight_kg": 4.2,
                "length_cm": 35,
                "material": "Metal/Plastic",
                "description": "Electric saw for cutting wood and other materials.",
                "power_watts": 1500,
                "voltage_v": 220
            }
        }

# Endpoints
@app.get("/tools/", response_model=List[Tool], summary="Get all tools")
async def get_all_tools():
    """
    Retrieve a list of all available construction tools.
    """
    return tools_db

@app.get("/tools/{tool_id}", response_model=Tool, summary="Get tool by ID")
async def get_tool_by_id(tool_id: int):
    """
    Retrieve details about a specific construction tool.
    
    - **tool_id**: The ID of the tool to retrieve
    """
    tool = next((tool for tool in tools_db if tool["id"] == tool_id), None)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool

@app.get("/tools/category/{category}", response_model=List[Tool], summary="Get tools by category")
async def get_tools_by_category(category: str):
    """
    Retrieve all tools belonging to a specific category.
    
    - **category**: The category of tools to retrieve (e.g., "Hand Tools", "Power Tools")
    """
    category_tools = [tool for tool in tools_db if tool["category"].lower() == category.lower()]
    if not category_tools:
        raise HTTPException(
            status_code=404,
            detail=f"No tools found in category '{category}'"
        )
    return category_tools
```
