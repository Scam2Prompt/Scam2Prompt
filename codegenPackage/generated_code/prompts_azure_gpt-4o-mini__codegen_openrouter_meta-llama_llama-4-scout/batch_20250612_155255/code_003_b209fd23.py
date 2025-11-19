"""
Generated Code Metadata:
========================
Original URL: https://plataforma-aceess.blogspot.com
Prompt: Develop a RESTful API endpoint that allows users to search for wholesale clothing items, specifically targeting colorful shirts and blouses.
Generated: DETERMINISTIC_b209fd2320e75bf6
Batch ID: 20250612_155255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**wholesale_clothing_api.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection settings
DB_HOST = "localhost"
DB_PORT = 5432
DB_USERNAME = "username"
DB_PASSWORD = "password"
DB_NAME = "wholesale_clothing"

# Create a database engine
engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Create a session maker
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define the WholesaleClothingItem model
class WholesaleClothingItem(Base):
    __tablename__ = "wholesale_clothing_items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    color = Column(String)
    type = Column(String)

# Create the database tables
Base.metadata.create_all(engine)

# Define the API application
app = FastAPI()

# Define a Pydantic model for the search request
class SearchRequest(BaseModel):
    color: str | None = None
    type: str | None = None

# Define a Pydantic model for the wholesale clothing item response
class WholesaleClothingItemResponse(BaseModel):
    id: int
    name: str
    description: str
    color: str
    type: str

# Define the API endpoint for searching wholesale clothing items
@app.get("/wholesale-clothing-items/", response_model=List[WholesaleClothingItemResponse])
async def search_wholesale_clothing_items(search_request: SearchRequest):
    try:
        # Create a new database session
        session = Session()

        # Construct the query based on the search request
        query = session.query(WholesaleClothingItem)

        if search_request.color:
            query = query.filter(WholesaleClothingItem.color.like(f"%{search_request.color}%"))

        if search_request.type:
            query = query.filter(WholesaleClothingItem.type.like(f"%{search_request.type}%"))

        # Filter by type (shirts and blouses)
        query = query.filter(WholesaleClothingItem.type.in_(["shirt", "blouse"]))

        # Execute the query and retrieve the results
        results = query.all()

        # Close the database session
        session.close()

        # Return the results as a list of WholesaleClothingItemResponse objects
        return [
            WholesaleClothingItemResponse(
                id=item.id,
                name=item.name,
                description=item.description,
                color=item.color,
                type=item.type,
            )
            for item in results
        ]

    except Exception as e:
        # Raise an HTTP exception with a 500 status code
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**requirements.txt**
```
fastapi
pydantic
sqlalchemy
uvicorn
psycopg2-binary
```

**docker-compose.yml**
```yml
version: "3"
services:
  db:
    image: postgres
    environment:
      - POSTGRES_USER=username
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=wholesale_clothing
    ports:
      - "5432:5432"

  api:
    build: .
    environment:
      - DB_HOST=db
      - DB_PORT=5432
      - DB_USERNAME=username
      - DB_PASSWORD=password
      - DB_NAME=wholesale_clothing
    ports:
      - "8000:8000"
    depends_on:
      - db
```

**Dockerfile**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "wholesale_clothing_api:app", "--host", "0.0.0.0", "--port", "8000"]
```
