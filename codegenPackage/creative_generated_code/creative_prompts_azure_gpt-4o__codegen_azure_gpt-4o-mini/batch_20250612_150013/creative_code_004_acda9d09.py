"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyatoken.net
Prompt: Suggest an API for booking luxury travel packages and managing incentive programs for companies, inspired by the offerings on nyatoken.net.
Generated: DETERMINISTIC_acda9d0917096d98
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI()

# Data models for our API

class TravelPackage(BaseModel):
    id: int
    name: str
    destination: str
    price: float
    description: str

class Company(BaseModel):
    id: int
    name: str
    email: EmailStr

class IncentiveProgram(BaseModel):
    id: int
    company_id: int
    travel_package_id: int
    incentive_amount: float

# In-memory "database"
travel_packages = []
companies = []
incentive_programs = []

@app.post("/travel-packages/", response_model=TravelPackage)
async def create_travel_package(package: TravelPackage):
    """Create a new luxury travel package."""
    travel_packages.append(package)
    return package

@app.get("/travel-packages/", response_model=List[TravelPackage])
async def get_travel_packages():
    """Retrieve all available travel packages."""
    return travel_packages

@app.post("/companies/", response_model=Company)
async def create_company(company: Company):
    """Register a new company for incentive programs."""
    companies.append(company)
    return company

@app.get("/companies/", response_model=List[Company])
async def get_companies():
    """Retrieve a list of all registered companies."""
    return companies

@app.post("/incentive-programs/", response_model=IncentiveProgram)
async def create_incentive_program(program: IncentiveProgram):
    """Create a new incentive program for a company."""
    # Validate that the company and travel package exist
    if not any(c.id == program.company_id for c in companies):
        raise HTTPException(status_code=404, detail="Company not found")
    if not any(tp.id == program.travel_package_id for tp in travel_packages):
        raise HTTPException(status_code=404, detail="Travel package not found")

    incentive_programs.append(program)
    return program

@app.get("/incentive-programs/", response_model=List[IncentiveProgram])
async def get_incentive_programs():
    """Retrieve all incentive programs."""
    return incentive_programs

@app.get("/travel-packages/{package_id}", response_model=TravelPackage)
async def get_travel_package(package_id: int):
    """Retrieve a specific travel package by ID."""
    package = next((tp for tp in travel_packages if tp.id == package_id), None)
    if package is None:
        raise HTTPException(status_code=404, detail="Travel package not found")
    return package

@app.get("/companies/{company_id}", response_model=Company)
async def get_company(company_id: int):
    """Retrieve a specific company by ID."""
    company = next((c for c in companies if c.id == company_id), None)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@app.delete("/travel-packages/{package_id}", response_model=dict)
async def delete_travel_package(package_id: int):
    """Delete a travel package by ID."""
    global travel_packages
    travel_packages = [tp for tp in travel_packages if tp.id != package_id]
    return {"detail": "Travel package deleted"}

@app.delete("/companies/{company_id}", response_model=dict)
async def delete_company(company_id: int):
    """Delete a company by ID."""
    global companies
    companies = [c for c in companies if c.id != company_id]
    return {"detail": "Company deleted"}

@app.delete("/incentive-programs/{program_id}", response_model=dict)
async def delete_incentive_program(program_id: int):
    """Delete an incentive program by ID."""
    global incentive_programs
    incentive_programs = [ip for ip in incentive_programs if ip.id != program_id]
    return {"detail": "Incentive program deleted"}

# Add any additional endpoints or logic as needed
```
