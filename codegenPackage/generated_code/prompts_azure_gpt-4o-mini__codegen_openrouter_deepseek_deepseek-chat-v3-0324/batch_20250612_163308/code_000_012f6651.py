"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Generate a code snippet for a tool management API that includes functionalities for tracking inventory of tools like "alicate," "furadeira," and "parafusadeira."
Generated: DETERMINISTIC_012f6651a8204dcb
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI(
    title="Tool Management API",
    description="API for tracking inventory of tools like Alicate, Furadeira, and Parafusadeira.",
    version="1.0.0"
)

# In-memory database for demonstration purposes
tool_inventory = {
    "alicate": {"quantity": 10, "location": "Shelf A"},
    "furadeira": {"quantity": 5, "location": "Shelf B"},
    "parafusadeira": {"quantity": 8, "location": "Shelf C"}
}

class Tool(BaseModel):
    name: str
    quantity: int
    location: str

class UpdateTool(BaseModel):
    quantity: int = None
    location: str = None

@app.get("/tools", response_model=Dict[str, Dict[str, str]])
def get_all_tools():
    """Retrieve all tools in the inventory."""
    return tool_inventory

@app.get("/tools/{tool_name}", response_model=Tool)
def get_tool(tool_name: str):
    """Retrieve a specific tool by name."""
    tool = tool_inventory.get(tool_name.lower())
    if not tool:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tool '{tool_name}' not found."
        )
    return {"name": tool_name, **tool}

@app.post("/tools", response_model=Tool, status_code=status.HTTP_201_CREATED)
def add_tool(tool: Tool):
    """Add a new tool to the inventory."""
    tool_name = tool.name.lower()
    if tool_name in tool_inventory:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Tool '{tool_name}' already exists."
        )
    tool_inventory[tool_name] = {
        "quantity": tool.quantity,
        "location": tool.location
    }
    return tool

@app.put("/tools/{tool_name}", response_model=Tool)
def update_tool(tool_name: str, tool_update: UpdateTool):
    """Update a tool's quantity and/or location."""
    tool_name = tool_name.lower()
    if tool_name not in tool_inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tool '{tool_name}' not found."
        )
    
    if tool_update.quantity is not None:
        tool_inventory[tool_name]["quantity"] = tool_update.quantity
    if tool_update.location is not None:
        tool_inventory[tool_name]["location"] = tool_update.location
    
    return {"name": tool_name, **tool_inventory[tool_name]}

@app.delete("/tools/{tool_name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tool(tool_name: str):
    """Remove a tool from the inventory."""
    tool_name = tool_name.lower()
    if tool_name not in tool_inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tool '{tool_name}' not found."
        )
    del tool_inventory[tool_name]
    return None
```
