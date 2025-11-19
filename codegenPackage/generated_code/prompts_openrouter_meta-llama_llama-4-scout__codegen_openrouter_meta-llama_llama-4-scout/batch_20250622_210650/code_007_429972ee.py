"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: "Design a RESTful API for managing generator rentals, including endpoints for booking, payment, and maintenance scheduling."
Generated: DETERMINISTIC_429972eed83cd15e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# generator_rental_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///generator_rental.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class Generator(BaseModel):
    id: int
    type: str
    rental_price: float

class Rental(BaseModel):
    id: int
    generator_id: int
    rental_date: datetime
    return_date: datetime
    total_cost: float

class Payment(BaseModel):
    id: int
    rental_id: int
    payment_date: datetime
    amount: float

class Maintenance(BaseModel):
    id: int
    generator_id: int
    maintenance_date: datetime
    description: str

# SQLAlchemy Models
class GeneratorModel(Base):
    __tablename__ = "generators"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    rental_price = Column(Float)

class RentalModel(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True)
    generator_id = Column(Integer)
    rental_date = Column(DateTime)
    return_date = Column(DateTime)
    total_cost = Column(Float)

class PaymentModel(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    rental_id = Column(Integer)
    payment_date = Column(DateTime)
    amount = Column(Float)

class MaintenanceModel(Base):
    __tablename__ = "maintenances"

    id = Column(Integer, primary_key=True)
    generator_id = Column(Integer)
    maintenance_date = Column(DateTime)
    description = Column(String)

# FastAPI App
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# OAuth2 Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Endpoints
@app.post("/generators/")
def create_generator(generator: Generator, db: SessionLocal = Depends(get_db)):
    db_generator = GeneratorModel(**generator.dict())
    db.add(db_generator)
    db.commit()
    db.refresh(db_generator)
    return JSONResponse(content={"id": db_generator.id}, status_code=201)

@app.get("/generators/")
def read_generators(db: SessionLocal = Depends(get_db)):
    generators = db.query(GeneratorModel).all()
    return JSONResponse(content=[g.to_dict() for g in generators], status_code=200)

@app.post("/rentals/")
def create_rental(rental: Rental, db: SessionLocal = Depends(get_db)):
    db_rental = RentalModel(**rental.dict())
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return JSONResponse(content={"id": db_rental.id}, status_code=201)

@app.get("/rentals/")
def read_rentals(db: SessionLocal = Depends(get_db)):
    rentals = db.query(RentalModel).all()
    return JSONResponse(content=[r.to_dict() for r in rentals], status_code=200)

@app.post("/payments/")
def create_payment(payment: Payment, db: SessionLocal = Depends(get_db)):
    db_payment = PaymentModel(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return JSONResponse(content={"id": db_payment.id}, status_code=201)

@app.get("/payments/")
def read_payments(db: SessionLocal = Depends(get_db)):
    payments = db.query(PaymentModel).all()
    return JSONResponse(content=[p.to_dict() for p in payments], status_code=200)

@app.post("/maintenances/")
def create_maintenance(maintenance: Maintenance, db: SessionLocal = Depends(get_db)):
    db_maintenance = MaintenanceModel(**maintenance.dict())
    db.add(db_maintenance)
    db.commit()
    db.refresh(db_maintenance)
    return JSONResponse(content={"id": db_maintenance.id}, status_code=201)

@app.get("/maintenances/")
def read_maintenances(db: SessionLocal = Depends(get_db)):
    maintenances = db.query(MaintenanceModel).all()
    return JSONResponse(content=[m.to_dict() for m in maintenances], status_code=200)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return JSONResponse(content={"access_token": "token", "token_type": "bearer"}, status_code=200)

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    return JSONResponse(content={"username": "user"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# models.py

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GeneratorModel(Base):
    __tablename__ = "generators"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    rental_price = Column(Float)

    def to_dict(self):
        return {"id": self.id, "type": self.type, "rental_price": self.rental_price}

class RentalModel(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True)
    generator_id = Column(Integer)
    rental_date = Column(DateTime)
    return_date = Column(DateTime)
    total_cost = Column(Float)

    def to_dict(self):
        return {"id": self.id, "generator_id": self.generator_id, "rental_date": self.rental_date, "return_date": self.return_date, "total_cost": self.total_cost}

class PaymentModel(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    rental_id = Column(Integer)
    payment_date = Column(DateTime)
    amount = Column(Float)

    def to_dict(self):
        return {"id": self.id, "rental_id": self.rental_id, "payment_date": self.payment_date, "amount": self.amount}

class MaintenanceModel(Base):
    __tablename__ = "maintenances"

    id = Column(Integer, primary_key=True)
    generator_id = Column(Integer)
    maintenance_date = Column(DateTime)
    description = Column(String)

    def to_dict(self):
        return {"id": self.id, "generator_id": self.generator_id, "maintenance_date": self.maintenance_date, "description": self.description}
```

```python
# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///generator_rental.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
```
