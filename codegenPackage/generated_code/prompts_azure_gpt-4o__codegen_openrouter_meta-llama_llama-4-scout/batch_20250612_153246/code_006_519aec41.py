"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Develop a REST API for managing customer testimonials and reviews about hot tubs, inspired by the testimonial section on the Oasis Hot Tubs website.
Generated: DETERMINISTIC_519aec41ac2bcbd6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**hot_tub_testimonials_api.py**
```python
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from uuid import UUID
from sqlalchemy import create_engine, Column, String, Text, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from typing import Optional

# Database Connection
SQLALCHEMY_DATABASE_URL = "sqlite:///hot_tub_testimonials.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Model for Testimonial
class TestimonialBase(BaseModel):
    id: Optional[UUID]
    customer_name: str
    testimonial: str
    rating: int
    created_at: Optional[datetime]

class Testimonial(TestimonialBase):
    pass

# SQLAlchemy Model for Testimonial
class TestimonialModel(Base):
    __tablename__ = "testimonials"

    id = Column(String, primary_key=True)
    customer_name = Column(String, nullable=False)
    testimonial = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

Base.metadata.create_all(engine)

# FastAPI App
app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Create a new testimonial
@app.post("/testimonials", response_model=Testimonial, status_code=status.HTTP_201_CREATED)
async def create_testimonial(testimonial: TestimonialBase, db: SessionLocal = get_db()):
    try:
        new_testimonial = TestimonialModel(
            id=str(testimonial.id),
            customer_name=testimonial.customer_name,
            testimonial=testimonial.testimonial,
            rating=testimonial.rating,
        )
        db.add(new_testimonial)
        db.commit()
        db.refresh(new_testimonial)
        return JSONResponse(content={"id": new_testimonial.id, "customer_name": new_testimonial.customer_name, "testimonial": new_testimonial.testimonial, "rating": new_testimonial.rating, "created_at": new_testimonial.created_at}, status_code=status.HTTP_201_CREATED)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Get all testimonials
@app.get("/testimonials", response_model=List[Testimonial])
async def read_testimonials(db: SessionLocal = get_db()):
    try:
        testimonials = db.query(TestimonialModel).all()
        return [{"id": testimonial.id, "customer_name": testimonial.customer_name, "testimonial": testimonial.testimonial, "rating": testimonial.rating, "created_at": testimonial.created_at} for testimonial in testimonials]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Get a testimonial by ID
@app.get("/testimonials/{testimonial_id}", response_model=Testimonial)
async def read_testimonial(testimonial_id: UUID, db: SessionLocal = get_db()):
    try:
        testimonial = db.query(TestimonialModel).filter_by(id=str(testimonial_id)).first()
        if testimonial is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Testimonial not found")
        return {"id": testimonial.id, "customer_name": testimonial.customer_name, "testimonial": testimonial.testimonial, "rating": testimonial.rating, "created_at": testimonial.created_at}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Update a testimonial
@app.put("/testimonials/{testimonial_id}", response_model=Testimonial)
async def update_testimonial(testimonial_id: UUID, testimonial: TestimonialBase, db: SessionLocal = get_db()):
    try:
        existing_testimonial = db.query(TestimonialModel).filter_by(id=str(testimonial_id)).first()
        if existing_testimonial is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Testimonial not found")
        existing_testimonial.customer_name = testimonial.customer_name
        existing_testimonial.testimonial = testimonial.testimonial
        existing_testimonial.rating = testimonial.rating
        db.commit()
        db.refresh(existing_testimonial)
        return {"id": existing_testimonial.id, "customer_name": existing_testimonial.customer_name, "testimonial": existing_testimonial.testimonial, "rating": existing_testimonial.rating, "created_at": existing_testimonial.created_at}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Delete a testimonial
@app.delete("/testimonials/{testimonial_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_testimonial(testimonial_id: UUID, db: SessionLocal = get_db()):
    try:
        testimonial = db.query(TestimonialModel).filter_by(id=str(testimonial_id)).first()
        if testimonial is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Testimonial not found")
        db.delete(testimonial)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```

**main function to run the FastAPI app**
```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
