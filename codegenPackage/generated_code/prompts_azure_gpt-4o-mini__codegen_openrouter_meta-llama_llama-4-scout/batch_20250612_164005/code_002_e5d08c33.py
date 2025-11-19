"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Create a REST API endpoint that allows for the management of independent contractor transitions to full-time employees, inspired by Connext's offerings.
Generated: DETERMINISTIC_e5d08c33cdcd9685
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum
from datetime import datetime

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///employee.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define an enumeration for employee status
class EmployeeStatus(PyEnum):
    CONTRACTOR = "contractor"
    FULL_TIME = "full_time"

# Define the Employee model
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(Enum(EmployeeStatus), default=EmployeeStatus.CONTRACTOR)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic model for employee
class EmployeeModel(BaseModel):
    id: int
    name: str
    status: EmployeeStatus

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a FastAPI application
app = FastAPI()

# Endpoint to get all employees
@app.get("/employees/", response_model=List[EmployeeModel])
def read_employees(db: SessionLocal = Depends(get_db)):
    return db.query(Employee).all()

# Endpoint to get an employee by ID
@app.get("/employees/{employee_id}", response_model=EmployeeModel)
def read_employee(employee_id: int, db: SessionLocal = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Endpoint to create a new employee
@app.post("/employees/", response_model=EmployeeModel)
def create_employee(employee: EmployeeModel, db: SessionLocal = Depends(get_db)):
    db_employee = Employee(name=employee.name, status=employee.status)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Endpoint to update an existing employee
@app.put("/employees/{employee_id}", response_model=EmployeeModel)
def update_employee(employee_id: int, employee: EmployeeModel, db: SessionLocal = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db_employee.name = employee.name
    db_employee.status = employee.status
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Endpoint to transition a contractor to full-time employee
@app.patch("/employees/{employee_id}/transition", response_model=EmployeeModel)
def transition_employee(employee_id: int, db: SessionLocal = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    if db_employee.status != EmployeeStatus.CONTRACTOR:
        raise HTTPException(status_code=400, detail="Employee is not a contractor")
    db_employee.status = EmployeeStatus.FULL_TIME
    db_employee.transition_date = datetime.now()
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Error handler for HTTP exceptions
@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    return {"error": exc.detail}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
sqlalchemy
pydantic
```

```bash
# Run the following commands in your terminal
# pip install -r requirements.txt
# python app.py
```
