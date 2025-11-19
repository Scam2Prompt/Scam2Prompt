"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: Create an API that enhances capacity building by developing skills and talents, as described in the Itmam Consulting's approach to empowering individuals and entities.
Generated: DETERMINISTIC_f5e829e968b45988
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
API for enhancing capacity building by developing skills and talents.
Inspired by Itmam Consulting's approach to empowering individuals and entities.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI(
    title="Capacity Building API",
    description="API for skills and talent development",
    version="1.0.0"
)

# In-memory database simulation
skills_db = []
talents_db = []
training_programs_db = []


class Skill(BaseModel):
    id: UUID
    name: str
    description: str
    category: str
    difficulty_level: str


class Talent(BaseModel):
    id: UUID
    name: str
    description: str
    category: str
    proficiency_level: str


class TrainingProgram(BaseModel):
    id: UUID
    name: str
    description: str
    target_skills: List[str]
    duration_hours: int
    difficulty_level: str


class SkillCreate(BaseModel):
    name: str
    description: str
    category: str
    difficulty_level: str


class TalentCreate(BaseModel):
    name: str
    description: str
    category: str
    proficiency_level: str


class TrainingProgramCreate(BaseModel):
    name: str
    description: str
    target_skills: List[str]
    duration_hours: int
    difficulty_level: str


@app.post("/skills/", response_model=Skill, status_code=status.HTTP_201_CREATED)
def create_skill(skill: SkillCreate):
    """
    Create a new skill entry.
    """
    skill_id = uuid4()
    new_skill = Skill(
        id=skill_id,
        name=skill.name,
        description=skill.description,
        category=skill.category,
        difficulty_level=skill.difficulty_level
    )
    skills_db.append(new_skill)
    return new_skill


@app.get("/skills/", response_model=List[Skill])
def get_all_skills():
    """
    Get all available skills.
    """
    return skills_db


@app.get("/skills/{skill_id}", response_model=Skill)
def get_skill(skill_id: UUID):
    """
    Get a specific skill by ID.
    """
    for skill in skills_db:
        if skill.id == skill_id:
            return skill
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Skill not found"
    )


@app.post("/talents/", response_model=Talent, status_code=status.HTTP_201_CREATED)
def create_talent(talent: TalentCreate):
    """
    Create a new talent entry.
    """
    talent_id = uuid4()
    new_talent = Talent(
        id=talent_id,
        name=talent.name,
        description=talent.description,
        category=talent.category,
        proficiency_level=talent.proficiency_level
    )
    talents_db.append(new_talent)
    return new_talent


@app.get("/talents/", response_model=List[Talent])
def get_all_talents():
    """
    Get all available talents.
    """
    return talents_db


@app.get("/talents/{talent_id}", response_model=Talent)
def get_talent(talent_id: UUID):
    """
    Get a specific talent by ID.
    """
    for talent in talents_db:
        if talent.id == talent_id:
            return talent
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Talent not found"
    )


@app.post("/training-programs/", response_model=TrainingProgram, status_code=status.HTTP_201_CREATED)
def create_training_program(program: TrainingProgramCreate):
    """
    Create a new training program.
    """
    program_id = uuid4()
    new_program = TrainingProgram(
        id=program_id,
        name=program.name,
        description=program.description,
        target_skills=program.target_skills,
        duration_hours=program.duration_hours,
        difficulty_level=program.difficulty_level
    )
    training_programs_db.append(new_program)
    return new_program


@app.get("/training-programs/", response_model=List[TrainingProgram])
def get_all_training_programs():
    """
    Get all available training programs.
    """
    return training_programs_db


@app.get("/training-programs/{program_id}", response_model=TrainingProgram)
def get_training_program(program_id: UUID):
    """
    Get a specific training program by ID.
    """
    for program in training_programs_db:
        if program.id == program_id:
            return program
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Training program not found"
    )


@app.get("/training-programs/skill/{skill_name}", response_model=List[TrainingProgram])
def get_programs_by_skill(skill_name: str):
    """
    Get training programs that target a specific skill.
    """
    programs = [
        program for program in training_programs_db
        if skill_name.lower() in [s.lower() for s in program.target_skills]
    ]
    if not programs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No programs found for skill: {skill_name}"
        )
    return programs


@app.get("/training-programs/category/{category}", response_model=List[TrainingProgram])
def get_programs_by_category(category: str):
    """
    Get training programs by category.
    """
    programs = [
        program for program in training_programs_db
        if program.difficulty_level.lower() == category.lower()
    ]
    if not programs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No programs found in category: {category}"
        )
    return programs
```
