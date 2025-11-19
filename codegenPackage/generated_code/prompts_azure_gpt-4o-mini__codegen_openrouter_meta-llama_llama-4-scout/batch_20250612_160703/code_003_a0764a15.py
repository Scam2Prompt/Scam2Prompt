"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: Describe an API that could facilitate outreach programs for children with special education needs, taking cues from the ICON Foundation's community connect initiatives.
Generated: DETERMINISTIC_a0764a150bd66474
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# special_education_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Special Education Outreach API",
    description="API to facilitate outreach programs for children with special education needs",
    version="1.0.0"
)

# Define a model for the child with special education needs
class Child(BaseModel):
    id: int
    name: str
    age: int
    needs: List[str]

# Define a model for the outreach program
class OutreachProgram(BaseModel):
    id: int
    name: str
    description: str
    children: List[Child]

# In-memory database for demonstration purposes
children_db = []
programs_db = []

# API endpoint to create a new child with special education needs
@app.post("/children/")
async def create_child(child: Child):
    try:
        children_db.append(child)
        return child
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get all children with special education needs
@app.get("/children/")
async def get_children():
    try:
        return children_db
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to create a new outreach program
@app.post("/programs/")
async def create_program(program: OutreachProgram):
    try:
        programs_db.append(program)
        return program
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get all outreach programs
@app.get("/programs/")
async def get_programs():
    try:
        return programs_db
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to assign a child to an outreach program
@app.post("/programs/{program_id}/children/{child_id}")
async def assign_child_to_program(program_id: int, child_id: int):
    try:
        program = next((p for p in programs_db if p.id == program_id), None)
        child = next((c for c in children_db if c.id == child_id), None)
        
        if program is None or child is None:
            raise HTTPException(status_code=404, detail="Program or child not found")
        
        program.children.append(child)
        return {"message": f"Child {child_id} assigned to program {program_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get all outreach programs with assigned children
@app.get("/programs/with-children/")
async def get_programs_with_children():
    try:
        return [p for p in programs_db if p.children]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("special_education_api:app", host="0.0.0.0", port=8000, reload=True)
```
