"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Create an API endpoint that allows users to query for different types of tables, including "правоъгълна," "кръгла," and "елипсовидна" options, along with their prices.
Generated: DETERMINISTIC_0a0b82597e3820d5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(
    title="Table Query API",
    description="API for querying different types of tables and their prices",
    version="1.0.0"
)

# Define a model for the table types
class TableType(BaseModel):
    name: str
    price: float

# In-memory data store for demonstration purposes
# Replace with a database connection in a real application
table_data: Dict[str, List[TableType]] = {
    "правоъгълна": [
        TableType(name="правоъгълна - small", price=100.0),
        TableType(name="правоъгълна - medium", price=200.0),
        TableType(name="правоъгълна - large", price=300.0),
    ],
    "кръгла": [
        TableType(name="кръгла - small", price=150.0),
        TableType(name="кръгла - medium", price=250.0),
        TableType(name="кръгла - large", price=350.0),
    ],
    "елипсовидна": [
        TableType(name="елипсовидна - small", price=120.0),
        TableType(name="елипсовидна - medium", price=220.0),
        TableType(name="елипсовидна - large", price=320.0),
    ],
}

# API endpoint to query for different types of tables
@app.get("/tables/{table_type}")
async def get_tables(table_type: str):
    """
    Query for different types of tables and their prices.

    Args:
    table_type (str): The type of table to query (e.g., "правоъгълна", "кръгла", "елипсовидна")

    Returns:
    List[TableType]: A list of tables of the specified type along with their prices

    Raises:
    HTTPException: If the table type is not found
    """
    try:
        tables = table_data[table_type]
        return tables
    except KeyError:
        raise HTTPException(status_code=404, detail="Table type not found")

# API endpoint to query for all table types
@app.get("/tables")
async def get_all_tables():
    """
    Query for all available table types.

    Returns:
    Dict[str, List[TableType]]: A dictionary of all table types and their corresponding tables
    """
    return table_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run the application using
# uvicorn app:app --host 0.0.0.0 --port 8000
```
