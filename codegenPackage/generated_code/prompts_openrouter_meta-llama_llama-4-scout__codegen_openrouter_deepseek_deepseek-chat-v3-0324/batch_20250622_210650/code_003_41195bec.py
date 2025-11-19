"""
Generated Code Metadata:
========================
Original URL: https://gavasilva.adv.br
Prompt: Recommend a suitable API or library for managing client consultations, strategy development, and action planning, as described in the three-pillar approach used by Gava & Silva Advogados.
Generated: DETERMINISTIC_41195bec27bf4e2e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Client Consultation Management System for Law Firms
Implements a three-pillar approach (Consultation, Strategy, Action Planning)
Uses FastAPI for REST API and SQLAlchemy for database operations
"""

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
import logging

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./client_consultations.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database models
class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(20))
    consultations = relationship("Consultation", back_populates="client")

class Consultation(Base):
    __tablename__ = "consultations"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)
    status = Column(String(20), default="scheduled")
    
    client = relationship("Client", back_populates="consultations")
    strategies = relationship("Strategy", back_populates="consultation")

class Strategy(Base):
    __tablename__ = "strategies"
    
    id = Column(Integer, primary_key=True, index=True)
    consultation_id = Column(Integer, ForeignKey("consultations.id"))
    description = Column(Text)
    priority = Column(String(20))
    status = Column(String(20), default="draft")
    
    consultation = relationship("Consultation", back_populates="strategies")
    action_plans = relationship("ActionPlan", back_populates="strategy")

class ActionPlan(Base):
    __tablename__ = "action_plans"
    
    id = Column(Integer, primary_key=True, index=True)
    strategy_id = Column(Integer, ForeignKey("strategies.id"))
    task = Column(Text)
    assigned_to = Column(String(100))
    deadline = Column(DateTime)
    status = Column(String(20), default="pending")
    
    strategy = relationship("Strategy", back_populates="action_plans")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class ClientBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id: int
    
    class Config:
        orm_mode = True

class ConsultationBase(BaseModel):
    client_id: int
    notes: Optional[str] = None
    status: Optional[str] = "scheduled"

class ConsultationCreate(ConsultationBase):
    pass

class ConsultationResponse(ConsultationBase):
    id: int
    date: datetime
    
    class Config:
        orm_mode = True

class StrategyBase(BaseModel):
    consultation_id: int
    description: str
    priority: str
    status: Optional[str] = "draft"

class StrategyCreate(StrategyBase):
    pass

class StrategyResponse(StrategyBase):
    id: int
    
    class Config:
        orm_mode = True

class ActionPlanBase(BaseModel):
    strategy_id: int
    task: str
    assigned_to: str
    deadline: datetime
    status: Optional[str] = "pending"

class ActionPlanCreate(ActionPlanBase):
    pass

class ActionPlanResponse(ActionPlanBase):
    id: int
    
    class Config:
        orm_mode = True

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI app
app = FastAPI(
    title="Client Consultation Management API",
    description="API for managing client consultations, strategy development, and action planning",
    version="1.0.0"
)

@app.post("/clients/", response_model=ClientResponse, status_code=status.HTTP_201_CREATED)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    try:
        db_client = Client(**client.dict())
        db.add(db_client)
        db.commit()
        db.refresh(db_client)
        return db_client
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating client: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create client"
        )

@app.get("/clients/", response_model=List[ClientResponse])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        clients = db.query(Client).offset(skip).limit(limit).all()
        return clients
    except Exception as e:
        logger.error(f"Error fetching clients: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not fetch clients"
        )

@app.post("/consultations/", response_model=ConsultationResponse, status_code=status.HTTP_201_CREATED)
def create_consultation(consultation: ConsultationCreate, db: Session = Depends(get_db)):
    try:
        db_consultation = Consultation(**consultation.dict())
        db.add(db_consultation)
        db.commit()
        db.refresh(db_consultation)
        return db_consultation
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating consultation: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create consultation"
        )

@app.post("/strategies/", response_model=StrategyResponse, status_code=status.HTTP_201_CREATED)
def create_strategy(strategy: StrategyCreate, db: Session = Depends(get_db)):
    try:
        db_strategy = Strategy(**strategy.dict())
        db.add(db_strategy)
        db.commit()
        db.refresh(db_strategy)
        return db_strategy
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating strategy: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create strategy"
        )

@app.post("/action-plans/", response_model=ActionPlanResponse, status_code=status.HTTP_201_CREATED)
def create_action_plan(action_plan: ActionPlanCreate, db: Session = Depends(get_db)):
    try:
        db_action_plan = ActionPlan(**action_plan.dict())
        db.add(db_action_plan)
        db.commit()
        db.refresh(db_action_plan)
        return db_action_plan
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating action plan: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create action plan"
        )

@app.get("/consultations/{consultation_id}/full", response_model=dict)
def get_full_consultation_details(consultation_id: int, db: Session = Depends(get_db)):
    try:
        consultation = db.query(Consultation).filter(Consultation.id == consultation_id).first()
        if not consultation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Consultation not found"
            )
        
        strategies = db.query(Strategy).filter(Strategy.consultation_id == consultation_id).all()
        action_plans = []
        
        for strategy in strategies:
            plans = db.query(ActionPlan).filter(ActionPlan.strategy_id == strategy.id).all()
            action_plans.extend(plans)
        
        return {
            "consultation": consultation,
            "strategies": strategies,
            "action_plans": action_plans
        }
    except Exception as e:
        logger.error(f"Error fetching consultation details: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not fetch consultation details"
        )
```
