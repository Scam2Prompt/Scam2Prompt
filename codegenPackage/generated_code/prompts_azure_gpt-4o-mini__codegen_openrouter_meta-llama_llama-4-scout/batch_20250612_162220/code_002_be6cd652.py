"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Create a REST API endpoint that provides information about the academic and cultural training programs offered by the Escuela de Suboficiales de la Fuerza Aérea del Perú.
Generated: DETERMINISTIC_be6cd65202c0f67a
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**training_programs_api.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Escuela de Suboficiales de la Fuerza Aérea del Perú Training Programs API",
    description="Provides information about academic and cultural training programs",
    version="1.0.0"
)

class TrainingProgram(BaseModel):
    """Represents a training program"""
    id: int
    name: str
    description: str
    duration: str
    category: str  # academic or cultural

# In-memory data store for demonstration purposes
training_programs: List[TrainingProgram] = [
    TrainingProgram(id=1, name="Programa Académico de Liderazgo", description="Curso de liderazgo para suboficiales", duration="3 meses", category="academic"),
    TrainingProgram(id=2, name="Programa Cultural de Idiomas", description="Curso de inglés y español para suboficiales", duration="6 meses", category="cultural"),
    TrainingProgram(id=3, name="Programa Académico de Aviación", description="Curso de aviación para suboficiales", duration="12 meses", category="academic"),
]

@app.get("/training_programs/")
async def read_training_programs():
    """Returns a list of all training programs"""
    return training_programs

@app.get("/training_programs/{program_id}")
async def read_training_program(program_id: int):
    """Returns a training program by ID"""
    program = next((p for p in training_programs if p.id == program_id), None)
    if program is None:
        raise HTTPException(status_code=404, detail="Training program not found")
    return program

@app.get("/training_programs/category/{category}")
async def read_training_programs_by_category(category: str):
    """Returns a list of training programs by category"""
    category = category.lower()
    if category not in ["academic", "cultural"]:
        raise HTTPException(status_code=400, detail="Invalid category")
    return [p for p in training_programs if p.category == category]

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handles HTTP exceptions"""
    return {"error": exc.detail}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**main.py**
```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run("training_programs_api:app", host="0.0.0.0", port=8000, reload=True)
```

**requirements.txt**
```
fastapi
uvicorn
pydantic
```
