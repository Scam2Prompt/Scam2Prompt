"""
Generated Code Metadata:
========================
Original URL: https://anotherbrilliantidea.com
Prompt: Write code to integrate a CRM system tailored for funeral homes, focusing on automating client follow-ups and answering FAQs using AI, as described in the Brilliant Marketing System™.
Generated: DETERMINISTIC_852632f1d040b3c0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from typing import List, Dict, Optional
import openai
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./funeral_crm.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# OpenAI configuration
openai.api_key = "your-openai-api-key"  # Replace with actual key

# Database Models
class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=False)
    address = Column(String(200), nullable=True)
    service_date = Column(DateTime, nullable=True)
    deceased_name = Column(String(100), nullable=False)
    relationship = Column(String(50), nullable=True)
    follow_up_date = Column(DateTime, nullable=True)
    follow_up_completed = Column(Boolean, default=False)
    notes = Column(Text, nullable=True)

class FAQ(Base):
    __tablename__ = "faqs"
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(255), nullable=False)
    answer = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)

class FollowUpTemplate(Base):
    __tablename__ = "follow_up_templates"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    days_after_service = Column(Integer, nullable=False)
    message_template = Column(Text, nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Models
class ClientCreate(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: str
    address: Optional[str] = None
    service_date: Optional[datetime.datetime] = None
    deceased_name: str
    relationship: Optional[str] = None
    notes: Optional[str] = None

class ClientResponse(ClientCreate):
    id: int
    follow_up_date: Optional[datetime.datetime] = None
    follow_up_completed: bool

    class Config:
        orm_mode = True

class FAQCreate(BaseModel):
    question: str
    answer: str
    category: str

class FAQResponse(FAQCreate):
    id: int

    class Config:
        orm_mode = True

class FollowUpTemplateCreate(BaseModel):
    name: str
    days_after_service: int
    message_template: str

class FollowUpTemplateResponse(FollowUpTemplateCreate):
    id: int

    class Config:
        orm_mode = True

class AIResponseRequest(BaseModel):
    client_id: int
    question: str

class AIResponse(BaseModel):
    response: str
    is_ai_generated: bool

# FastAPI App
app = FastAPI(title="Funeral Home CRM", description="CRM system for funeral homes with AI integration")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# AI Integration
def generate_ai_response(question: str, context: str = "") -> str:
    try:
        prompt = f"""
        You are a compassionate funeral home assistant. Answer the following question professionally and empathetically.
        Context: {context}
        Question: {question}
        Answer:
        """
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        
        return response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"Error generating AI response: {e}")
        return "I'm sorry, I'm having trouble answering that right now. Please contact our staff directly for assistance."

# Follow-up Automation
def schedule_follow_ups():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        process_due_follow_ups,
        trigger=IntervalTrigger(hours=1),
        id='follow_up_processing',
        replace_existing=True
    )
    scheduler.start()

def process_due_follow_ups():
    db = SessionLocal()
    try:
        now = datetime.datetime.now()
        due_follow_ups = db.query(Client).filter(
            Client.follow_up_date <= now,
            Client.follow_up_completed == False
        ).all()
        
        for client in due_follow_ups:
            template = db.query(FollowUpTemplate).filter(
                FollowUpTemplate.days_after_service == (now.date() - client.service_date.date()).days
            ).first()
            
            if template:
                send_follow_up(client, template.message_template)
                client.follow_up_completed = True
                db.commit()
                logger.info(f"Sent follow-up to client {client.id}")
    except Exception as e:
        logger.error(f"Error processing follow-ups: {e}")
    finally:
        db.close()

def send_follow_up(client: Client, message_template: str):
    # In a real implementation, this would send an email or SMS
    message = message_template.format(
        first_name=client.first_name,
        last_name=client.last_name,
        deceased_name=client.deceased_name
    )
    logger.info(f"Follow-up message for {client.email or client.phone}:\n{message}")

# API Endpoints
@app.post("/clients/", response_model=ClientResponse)
def create_client(client: ClientCreate, db=Depends(get_db)):
    try:
        db_client = Client(**client.dict())
        if db_client.service_date:
            db_client.follow_up_date = db_client.service_date + datetime.timedelta(days=7)
        db.add(db_client)
        db.commit()
        db.refresh(db_client)
        return db_client
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating client: {e}")
        raise HTTPException(status_code=400, detail="Error creating client")

@app.get("/clients/", response_model=List[ClientResponse])
def read_clients(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    return db.query(Client).offset(skip).limit(limit).all()

@app.post("/faqs/", response_model=FAQResponse)
def create_faq(faq: FAQCreate, db=Depends(get_db)):
    try:
        db_faq = FAQ(**faq.dict())
        db.add(db_faq)
        db.commit()
        db.refresh(db_faq)
        return db_faq
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating FAQ: {e}")
        raise HTTPException(status_code=400, detail="Error creating FAQ")

@app.get("/faqs/", response_model=List[FAQResponse])
def read_faqs(category: Optional[str] = None, db=Depends(get_db)):
    query = db.query(FAQ)
    if category:
        query = query.filter(FAQ.category == category)
    return query.all()

@app.post("/ai/answer", response_model=AIResponse)
def get_ai_response(request: AIResponseRequest, db=Depends(get_db)):
    try:
        client = db.query(Client).filter(Client.id == request.client_id).first()
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        
        # First try to find a matching FAQ
        faq = db.query(FAQ).filter(FAQ.question.ilike(f"%{request.question}%")).first()
        if faq:
            return AIResponse(response=faq.answer, is_ai_generated=False)
        
        # If no FAQ found, generate AI response
        context = f"""
        Client: {client.first_name} {client.last_name}
        Deceased: {client.deceased_name}
        Relationship: {client.relationship}
        Service Date: {client.service_date}
        """
        
        ai_response = generate_ai_response(request.question, context)
        return AIResponse(response=ai_response, is_ai_generated=True)
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail="Error generating response")

@app.post("/follow-up-templates/",
