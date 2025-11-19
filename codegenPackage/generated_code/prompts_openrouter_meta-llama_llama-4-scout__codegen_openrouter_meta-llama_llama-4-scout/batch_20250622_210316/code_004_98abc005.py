"""
Generated Code Metadata:
========================
Original URL: https://florencefinance.pages.dev
Prompt: "Design a simple API for a DeFi lending platform like Florence Finance, including endpoints for lending, borrowing, and leaderboard management."
Generated: DETERMINISTIC_98abc005d6684498
Batch ID: 20250622_210316
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///florence_finance.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class User(BaseModel):
    id: int
    name: str
    balance: float

class Loan(BaseModel):
    id: int
    user_id: int
    amount: float
    interest_rate: float

class BorrowRequest(BaseModel):
    user_id: int
    loan_id: int
    amount: float

# SQLAlchemy Models
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Float)

class LoanDB(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    interest_rate = Column(Float)

class BorrowRequestDB(Base):
    __tablename__ = "borrow_requests"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    loan_id = Column(Integer)
    amount = Column(Float)

# API Initialization
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

# Leaderboard
leaderboard = []

# Endpoints
@app.post("/users/")
def create_user(user: User):
    db = SessionLocal()
    user_db = UserDB(id=user.id, name=user.name, balance=user.balance)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

@app.get("/users/")
def read_users(db: SessionLocal = Depends(get_db)):
    return db.query(UserDB).all()

@app.post("/loans/")
def create_loan(loan: Loan):
    db = SessionLocal()
    loan_db = LoanDB(id=loan.id, user_id=loan.user_id, amount=loan.amount, interest_rate=loan.interest_rate)
    db.add(loan_db)
    db.commit()
    db.refresh(loan_db)
    return loan_db

@app.get("/loans/")
def read_loans(db: SessionLocal = Depends(get_db)):
    return db.query(LoanDB).all()

@app.post("/borrow_requests/")
def create_borrow_request(borrow_request: BorrowRequest):
    db = SessionLocal()
    borrow_request_db = BorrowRequestDB(user_id=borrow_request.user_id, loan_id=borrow_request.loan_id, amount=borrow_request.amount)
    db.add(borrow_request_db)
    db.commit()
    db.refresh(borrow_request_db)
    return borrow_request_db

@app.get("/borrow_requests/")
def read_borrow_requests(db: SessionLocal = Depends(get_db)):
    return db.query(BorrowRequestDB).all()

@app.post("/lend/")
def lend(user_id: int, amount: float, db: SessionLocal = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.balance += amount
    db.commit()
    db.refresh(user)
    return {"message": "Lend successful"}

@app.post("/borrow/")
def borrow(user_id: int, loan_id: int, amount: float, db: SessionLocal = Depends(get_db)):
    loan = db.query(LoanDB).filter(LoanDB.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    user.balance -= amount
    db.commit()
    db.refresh(user)
    return {"message": "Borrow successful"}

@app.get("/leaderboard/")
def get_leaderboard():
    leaderboard.clear()
    db = SessionLocal()
    users = db.query(UserDB).all()
    for user in users:
        leaderboard.append({"id": user.id, "name": user.name, "balance": user.balance})
    leaderboard.sort(key=lambda x: x["balance"], reverse=True)
    return leaderboard

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return {"access_token": "token", "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py

from app import app

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

To run:
```bash
# Create a new terminal
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
