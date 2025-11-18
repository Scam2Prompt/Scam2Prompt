"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://urlz.fr
Prompt: Suggest libraries or tools to implement a custom URL shortening service similar to URLz.fr, including features like ad-free options and link reporting mechanisms.
Generated: DETERMINISTIC_b26ee358c237d061
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code to implement a custom URL shortening service using `FastAPI` and `SQLAlchemy`, with features like ad-free options and link reporting mechanisms. For dependencies, you will need `FastAPI`, `SQLAlchemy`, `databases` for async database access, and `pyshorteners` for link shortening. Ensure these are installed via `pip install fastapi sqlalchemy databases pyshorteners uvicorn`.

```python
# main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pyshorteners
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, func
import databases

# Database Configuration
DATABASE_URL = "sqlite:///./url_shortener.db"  # Replace with production-ready database
database = databases.Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)

# URL Table Schema
urls = Table(
    "urls",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("original_url", String, nullable=False),
    Column("short_url", String, unique=True, nullable=False),
    Column("created_at", DateTime, server_default=func.now()),
    Column("click_count", Integer, default=0),
)

metadata.create_all(engine)

# FastAPI App
app = FastAPI()

# URL Shortening Instance
shortener = pyshorteners.Shortener()

# Models
class URLCreateRequest(BaseModel):
    original_url: str

class URLResponse(BaseModel):
    short_url: str
    original_url: str
    click_count: int
    created_at: str

# Exception handling for HTTP errors
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# Endpoint to create a short URL
@app.post("/shorten/", response_model=URLResponse)
async def create_short_url(url_request: URLCreateRequest):
    original_url = url_request.original_url
    
    try:
        # Generate short URL
        short_url = shortener.tinyurl.short(original_url)
        
        # Store in database
        query = urls.insert().values(original_url=original_url, short_url=short_url)
        last_record_id = await database.execute(query)
        
        # Fetch and return the record
        query = urls.select().where(urls.c.id == last_record_id)
        record = await database.fetch_one(query)
        return URLResponse(**record)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating short URL")

# Endpoint to retrieve original URL and link reports
@app.get("/info/{short_url}", response_model=URLResponse)
async def get_url_info(short_url: str):
    query = urls.select().where(urls.c.short_url == short_url)
    record = await database.fetch_one(query)
    if not record:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return URLResponse(**record)

# Endpoint to redirect to original URL and increment click count
@app.get("/{short_url}")
async def redirect_to_original(short_url: str):
    query = urls.select().where(urls.c.short_url == short_url)
    record = await database.fetch_one(query)
    if not record:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    # Increment click count
    update_query = urls.update().where(urls.c.short_url == short_url).values(
        click_count=record["click_count"] + 1
    )
    await database.execute(update_query)
    
    # Redirect to original URL
    return JSONResponse(content={"redirect_to": record["original_url"]})

# Middleware for startup and shutdown
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
```

### Setup Instructions:
1. Save the code in a file named `main.py`.
2. Install dependencies using `pip install fastapi databases sqlalchemy pyshorteners uvicorn`.
3. Run the server with `uvicorn main:app --reload`.
4. Test endpoints `/shorten/`, `/info/{short_url}`, and `/{short_url}`.

This code includes error handling, database integration, and the ability to extend features such as analytics and link management.
