"""
Generated Code Metadata:
========================
Original URL: https://motor-muse.com
Prompt: Create a RESTful API to manage and retrieve news articles related to electric vehicle price wars, specifically those involving Tesla in Australia.
Generated: DETERMINISTIC_5a0a2ca08c9d85ed
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Connection
SQLALCHEMY_DATABASE_URL = "sqlite:///news.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Model
class NewsArticle(BaseModel):
    id: int
    title: str
    content: str
    date: datetime
    source: str

    class Config:
        orm_mode = True

# SQLAlchemy Model
class NewsArticleDB(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    date = Column(DateTime)
    source = Column(String)

Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI(
    title="Electric Vehicle News API",
    description="Manage and retrieve news articles related to electric vehicle price wars, specifically those involving Tesla in Australia.",
    version="1.0.0",
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# API Endpoints
@app.get("/news/", response_model=List[NewsArticle])
async def read_news(db=SessionLocal()):
    return db.query(NewsArticleDB).all()

@app.get("/news/{news_id}", response_model=NewsArticle)
async def read_news_by_id(news_id: int, db=SessionLocal()):
    news = db.query(NewsArticleDB).filter(NewsArticleDB.id == news_id).first()
    if news is None:
        raise HTTPException(status_code=404, detail="News article not found")
    return news

@app.post("/news/", response_model=NewsArticle)
async def create_news(news: NewsArticle, db=SessionLocal()):
    db_news = NewsArticleDB(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

@app.put("/news/{news_id}", response_model=NewsArticle)
async def update_news(news_id: int, news: NewsArticle, db=SessionLocal()):
    db_news = db.query(NewsArticleDB).filter(NewsArticleDB.id == news_id).first()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News article not found")
    db_news.title = news.title
    db_news.content = news.content
    db_news.date = news.date
    db_news.source = news.source
    db.commit()
    db.refresh(db_news)
    return db_news

@app.delete("/news/{news_id}")
async def delete_news(news_id: int, db=SessionLocal()):
    db_news = db.query(NewsArticleDB).filter(NewsArticleDB.id == news_id).first()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News article not found")
    db.delete(db_news)
    db.commit()
    return {"message": "News article deleted"}

if __name__ == "__main__":
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
# Run with: 
# uvicorn app:app --host 0.0.0.0 --port 8000 --reload
# or 
python app.py
```
