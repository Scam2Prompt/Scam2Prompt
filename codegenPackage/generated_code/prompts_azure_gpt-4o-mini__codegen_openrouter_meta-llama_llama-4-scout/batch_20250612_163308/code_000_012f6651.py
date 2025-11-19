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
# tool_management_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Tool Management API",
    description="API for managing tool inventory",
    version="1.0.0"
)

class Tool(BaseModel):
    """Tool model"""
    name: str
    quantity: int

class ToolManagementSystem:
    """Tool management system class"""
    def __init__(self):
        self.tools = {}

    def add_tool(self, tool: Tool):
        """Add tool to inventory"""
        if tool.name in self.tools:
            self.tools[tool.name].quantity += tool.quantity
        else:
            self.tools[tool.name] = tool

    def remove_tool(self, tool_name: str, quantity: int):
        """Remove tool from inventory"""
        if tool_name not in self.tools:
            raise HTTPException(status_code=404, detail="Tool not found")
        if self.tools[tool_name].quantity < quantity:
            raise HTTPException(status_code=400, detail="Insufficient quantity")
        self.tools[tool_name].quantity -= quantity
        if self.tools[tool_name].quantity == 0:
            del self.tools[tool_name]

    def get_tool(self, tool_name: str):
        """Get tool from inventory"""
        return self.tools.get(tool_name)

    def list_tools(self):
        """List all tools in inventory"""
        return list(self.tools.values())

tool_system = ToolManagementSystem()

# Initialize with some tools
tool_system.add_tool(Tool(name="alicate", quantity=10))
tool_system.add_tool(Tool(name="furadeira", quantity=5))
tool_system.add_tool(Tool(name="parafusadeira", quantity=8))

@app.post("/tools/")
async def create_tool(tool: Tool):
    """Create a new tool"""
    try:
        tool_system.add_tool(tool)
        return {"message": "Tool created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tools/")
async def read_tools():
    """Read all tools"""
    return tool_system.list_tools()

@app.get("/tools/{tool_name}")
async def read_tool(tool_name: str):
    """Read a tool by name"""
    tool = tool_system.get_tool(tool_name)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool

@app.put("/tools/{tool_name}")
async def update_tool(tool_name: str, tool: Tool):
    """Update a tool"""
    try:
        tool_system.remove_tool(tool_name, tool_system.get_tool(tool_name).quantity)
        tool_system.add_tool(tool)
        return {"message": "Tool updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/tools/{tool_name}")
async def delete_tool(tool_name: str, quantity: int):
    """Delete a tool"""
    try:
        tool_system.remove_tool(tool_name, quantity)
        return {"message": "Tool deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
