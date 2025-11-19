"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Provide a Python example of an intermediary financial service that connects SMEs with lenders for short, medium, and long-term credit, as described on Adelanto.cl.
Generated: DETERMINISTIC_c21c925d3f0f5064
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

app = FastAPI(
    title="Adelanto Financial Intermediary API",
    description="API for connecting SMEs with lenders for short, medium, and long-term credit",
    version="1.0.0"
)

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock database
class Database:
    users: Dict[str, dict] = {}
    smes: Dict[str, dict] = {}
    lenders: Dict[str, dict] = {}
    loan_requests: Dict[str, dict] = {}
    loan_offers: Dict[str, dict] = {}

db = Database()

# Enums
class LoanTerm(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

class LoanStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    FUNDED = "funded"
    REPAID = "repaid"

class UserRole(str, Enum):
    SME = "sme"
    LENDER = "lender"
    ADMIN = "admin"

# Models
class UserBase(BaseModel):
    email: str
    full_name: str
    role: UserRole

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    is_active: bool = True

    class Config:
        orm_mode = True

class SME(BaseModel):
    id: str
    user_id: str
    business_name: str
    industry: str
    annual_revenue: float
    years_in_business: int
    credit_score: Optional[int] = None

    class Config:
        orm_mode = True

class Lender(BaseModel):
    id: str
    user_id: str
    institution_name: str
    max_loan_amount: float
    preferred_industries: List[str]
    min_credit_score: int

    class Config:
        orm_mode = True

class LoanRequest(BaseModel):
    id: str
    sme_id: str
    amount: float
    term: LoanTerm
    purpose: str
    status: LoanStatus = LoanStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True

class LoanOffer(BaseModel):
    id: str
    loan_request_id: str
    lender_id: str
    amount: float
    interest_rate: float
    term: LoanTerm
    status: LoanStatus = LoanStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True

# Auth functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(email: str):
    if email in db.users:
        return db.users[email]
    return None

def authenticate_user(email: str, password: str):
    user = get_user(email)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

# Dependency
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real app, validate the token here
    user = get_user(token)  # Simplified for example
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# Routes
@app.post("/register/sme", response_model=SME)
async def register_sme(user_data: UserCreate, sme_data: dict):
    if user_data.email in db.users:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user_data.password)
    user_id = str(uuid.uuid4())
    db.users[user_data.email] = {
        "id": user_id,
        "email": user_data.email,
        "full_name": user_data.full_name,
        "hashed_password": hashed_password,
        "role": UserRole.SME,
        "is_active": True
    }
    
    sme_id = str(uuid.uuid4())
    sme = {
        "id": sme_id,
        "user_id": user_id,
        "business_name": sme_data["business_name"],
        "industry": sme_data["industry"],
        "annual_revenue": sme_data["annual_revenue"],
        "years_in_business": sme_data["years_in_business"],
        "credit_score": sme_data.get("credit_score")
    }
    db.smes[sme_id] = sme
    return sme

@app.post("/register/lender", response_model=Lender)
async def register_lender(user_data: UserCreate, lender_data: dict):
    if user_data.email in db.users:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user_data.password)
    user_id = str(uuid.uuid4())
    db.users[user_data.email] = {
        "id": user_id,
        "email": user_data.email,
        "full_name": user_data.full_name,
        "hashed_password": hashed_password,
        "role": UserRole.LENDER,
        "is_active": True
    }
    
    lender_id = str(uuid.uuid4())
    lender = {
        "id": lender_id,
        "user_id": user_id,
        "institution_name": lender_data["institution_name"],
        "max_loan_amount": lender_data["max_loan_amount"],
        "preferred_industries": lender_data["preferred_industries"],
        "min_credit_score": lender_data["min_credit_score"]
    }
    db.lenders[lender_id] = lender
    return lender

@app.post("/loan-requests", response_model=LoanRequest)
async def create_loan_request(
    request_data: dict,
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != UserRole.SME:
        raise HTTPException(status_code=403, detail="Only SMEs can create loan requests")
    
    sme = next((s for s in db.smes.values() if s["user_id"] == current_user["id"]), None)
    if not sme:
        raise HTTPException(status_code=404, detail="SME profile not found")
    
    request_id = str(uuid.uuid4())
    loan_request = {
        "id": request_id,
        "sme_id": sme["id"],
        "amount": request_data["amount"],
        "term": request_data["term"],
        "purpose": request_data["purpose"],
        "status": LoanStatus.PENDING,
        "created_at": datetime.utcnow()
    }
    db.loan_requests[request_id] = loan_request
    return loan_request

@app.get("/loan-requests", response_model=List[LoanRequest])
async def get_loan_requests(
    term: Optional[LoanTerm] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != UserRole.LENDER:
        raise HTTPException(status_code=403, detail="Only lenders can view loan requests")
    
    lender = next((l for l in db.lenders.values() if l["user_id"] == current_user["id"]), None)
    if not lender:
        raise HTTPException(status_code=404, detail="Lender profile not found")
    
    requests = list(db.loan_requests.values())
    
    # Filter by term if provided
    if term:
        requests = [r for r in requests if r["term"] == term]
    
    # Filter by amount range if provided
    if min_amount is not None:
        requests = [r for r in requests if r["amount"] >= min_amount]
    if max_amount is not None:
        requests = [r for r in requests if r["amount"] <= max_amount]
    
    # Filter by lender preferences
    requests = [r for r in requests if r["status"] == LoanStatus.PENDING]
    
    # Get SME details for each request
    filtered_requests = []
    for req in requests:
        sme = db.smes.get(req["sme_id"])
        if sme and sme["credit_score"] >= lender["min_credit_score"]:
            if lender["preferred_industries"] and sme["industry"] in lender["preferred_industries"]:
                filtered_requests.append(req)
