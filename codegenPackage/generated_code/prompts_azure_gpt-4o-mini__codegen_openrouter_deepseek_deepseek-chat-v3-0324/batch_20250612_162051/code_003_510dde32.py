"""
Generated Code Metadata:
========================
Original URL: https://chatnchill.com
Prompt: Develop an API endpoint that retrieves information about the famous Caribbean Pig Roast at Chat 'N' Chill®, including menu items and timings.
Generated: DETERMINISTIC_510dde3235e20589
Batch ID: 20250612_162051
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
from datetime import time

app = FastAPI(
    title="Chat 'N' Chill® Caribbean Pig Roast API",
    description="API to retrieve information about the famous Caribbean Pig Roast at Chat 'N' Chill®",
    version="1.0.0"
)

class MenuItem(BaseModel):
    """Model representing a menu item at the pig roast"""
    name: str
    description: str
    price: float
    is_vegetarian: bool = False

class PigRoastInfo(BaseModel):
    """Model containing all information about the pig roast"""
    event_name: str
    description: str
    location: str
    operating_days: List[str]
    start_time: time
    end_time: time
    menu_items: List[MenuItem]

# Mock data - in a real application this would come from a database
PIG_ROAST_DATA = PigRoastInfo(
    event_name="Caribbean Pig Roast",
    description="The famous weekly pig roast at Chat 'N' Chill® with delicious Caribbean flavors",
    location="Chat 'N' Chill®, George Town, Exuma, Bahamas",
    operating_days=["Sunday"],
    start_time=time(12, 0),  # 12:00 PM
    end_time=time(18, 0),    # 6:00 PM
    menu_items=[
        MenuItem(
            name="Roast Pork",
            description="Slow-roasted pork with Caribbean spices",
            price=15.99,
            is_vegetarian=False
        ),
        MenuItem(
            name="Jerk Chicken",
            description="Grilled chicken with traditional jerk seasoning",
            price=12.99,
            is_vegetarian=False
        ),
        MenuItem(
            name="Vegetable Rice",
            description="Flavorful rice with mixed vegetables",
            price=8.99,
            is_vegetarian=True
        ),
        MenuItem(
            name="Peas and Rice",
            description="Traditional Bahamian side dish",
            price=7.99,
            is_vegetarian=True
        ),
        MenuItem(
            name="Macaroni and Cheese",
            description="Creamy Caribbean-style mac and cheese",
            price=9.99,
            is_vegetarian=True
        )
    ]
)

@app.get(
    "/pig-roast",
    response_model=PigRoastInfo,
    summary="Get information about the Caribbean Pig Roast",
    response_description="Complete information about the pig roast including menu and timings"
)
async def get_pig_roast_info():
    """
    Retrieve all information about the famous Caribbean Pig Roast at Chat 'N' Chill®.
    
    Returns:
        PigRoastInfo: Complete details including menu items, timings, and location.
    """
    try:
        return PIG_ROAST_DATA
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving pig roast information: {str(e)}"
        )

@app.get(
    "/pig-roast/menu",
    response_model=List[MenuItem],
    summary="Get the pig roast menu items",
    response_description="List of all menu items available at the pig roast"
)
async def get_menu_items(vegetarian_only: Optional[bool] = False):
    """
    Retrieve the menu items for the pig roast.
    
    Args:
        vegetarian_only (bool, optional): If True, returns only vegetarian items. Defaults to False.
    
    Returns:
        List[MenuItem]: List of menu items matching the filter criteria.
    """
    try:
        if vegetarian_only:
            return [item for item in PIG_ROAST_DATA.menu_items if item.is_vegetarian]
        return PIG_ROAST_DATA.menu_items
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving menu items: {str(e)}"
        )

@app.get(
    "/pig-roast/timings",
    response_model=dict,
    summary="Get the pig roast operating hours",
    response_description="Operating days and times for the pig roast"
)
async def get_operating_hours():
    """
    Retrieve the operating days and times for the pig roast.
    
    Returns:
        dict: Contains operating days, start time, and end time.
    """
    try:
        return {
            "operating_days": PIG_ROAST_DATA.operating_days,
            "start_time": PIG_ROAST_DATA.start_time.strftime("%H:%M"),
            "end_time": PIG_ROAST_DATA.end_time.strftime("%H:%M")
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving operating hours: {str(e)}"
        )
```
