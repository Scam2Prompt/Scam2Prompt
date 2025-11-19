"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: How can I create a training program API that aligns with the objectives of the Pakistan Readymade Garments Technical Training Institute (PRGTTI)?
Generated: DETERMINISTIC_a56ca3108c04180a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_program_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Pakistan Readymade Garments Technical Training Institute (PRGTTI) Training Program API",
    description="API for managing training programs at PRGTTI",
    version="1.0.0"
)

# Define a model for the training program
class TrainingProgram(BaseModel):
    id: int
    name: str
    description: str
    duration: str
    objectives: List[str]

# In-memory database for demonstration purposes
training_programs = [
    TrainingProgram(id=1, name="Garment Construction", description="Learn garment construction techniques", duration="3 months", objectives=["Improve garment construction skills", "Enhance productivity"]),
    TrainingProgram(id=2, name="Pattern Making", description="Learn pattern making techniques", duration="2 months", objectives=["Improve pattern making skills", "Enhance creativity"]),
]

# API endpoint to retrieve all training programs
@app.get("/training-programs/")
async def get_all_training_programs():
    """Retrieve a list of all training programs"""
    return training_programs

# API endpoint to retrieve a training program by ID
@app.get("/training-programs/{program_id}")
async def get_training_program(program_id: int):
    """Retrieve a training program by ID"""
    for program in training_programs:
        if program.id == program_id:
            return program
    raise HTTPException(status_code=404, detail="Training program not found")

# API endpoint to create a new training program
@app.post("/training-programs/")
async def create_training_program(program: TrainingProgram):
    """Create a new training program"""
    training_programs.append(program)
    return program

# API endpoint to update an existing training program
@app.put("/training-programs/{program_id}")
async def update_training_program(program_id: int, program: TrainingProgram):
    """Update an existing training program"""
    for i, existing_program in enumerate(training_programs):
        if existing_program.id == program_id:
            training_programs[i] = program
            return program
    raise HTTPException(status_code=404, detail="Training program not found")

# API endpoint to delete a training program
@app.delete("/training-programs/{program_id}")
async def delete_training_program(program_id: int):
    """Delete a training program"""
    for i, program in enumerate(training_programs):
        if program.id == program_id:
            del training_programs[i]
            return {"message": "Training program deleted successfully"}
    raise HTTPException(status_code=404, detail="Training program not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
