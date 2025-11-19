"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Develop an API endpoint that allows users to search for Endeavor Schools by state and program type, such as STEM or Active Athletes.
Generated: DETERMINISTIC_bce884021e596448
Batch ID: 20250612_162325
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
from typing import List, Optional

app = FastAPI(
    title="Endeavor Schools API",
    description="API for searching Endeavor Schools by state and program type",
    version="1.0.0"
)

# Define the ProgramType enum
from enum import Enum
class ProgramType(str, Enum):
    stem = "STEM"
    active_athletes = "Active Athletes"
    art = "Art"
    music = "Music"

# Define the EndeavorSchool model
class EndeavorSchool(BaseModel):
    id: int
    name: str
    state: str
    program_type: ProgramType

# In-memory data store for demonstration purposes
# Replace with a database connection in production
endeavor_schools: List[EndeavorSchool] = [
    EndeavorSchool(id=1, name="School 1", state="CA", program_type=ProgramType.stem),
    EndeavorSchool(id=2, name="School 2", state="NY", program_type=ProgramType.active_athletes),
    EndeavorSchool(id=3, name="School 3", state="CA", program_type=ProgramType.art),
    EndeavorSchool(id=4, name="School 4", state="FL", program_type=ProgramType.stem),
    EndeavorSchool(id=5, name="School 5", state="NY", program_type=ProgramType.music),
]

# Define the SearchSchoolsRequest model
class SearchSchoolsRequest(BaseModel):
    state: Optional[str]
    program_type: Optional[ProgramType]

# Define the API endpoint for searching Endeavor Schools
@app.get("/schools/", response_model=List[EndeavorSchool])
async def search_schools(request: SearchSchoolsRequest):
    try:
        # Filter schools by state and program type
        filtered_schools = [
            school for school in endeavor_schools
            if (request.state is None or school.state == request.state)
            and (request.program_type is None or school.program_type == request.program_type)
        ]
        return filtered_schools
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Define the API endpoint for getting a specific Endeavor School by ID
@app.get("/schools/{school_id}", response_model=EndeavorSchool)
async def get_school(school_id: int):
    try:
        # Find the school by ID
        school = next((school for school in endeavor_schools if school.id == school_id), None)
        if school is None:
            raise HTTPException(status_code=404, detail="School not found")
        return school
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
