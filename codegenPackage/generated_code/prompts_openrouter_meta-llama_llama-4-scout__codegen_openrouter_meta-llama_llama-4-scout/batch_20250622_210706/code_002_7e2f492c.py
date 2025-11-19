"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Generate a RESTful API for searching and streaming anime content, inspired by HiAnime's features and functionality.
Generated: DETERMINISTIC_7e2f492cbd73e877
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**anime_api.py**
```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import json
from anime_database import AnimeDatabase

# Initialize FastAPI app
app = FastAPI(
    title="Anime API",
    description="A RESTful API for searching and streaming anime content",
    version="1.0.0"
)

# Initialize anime database
anime_db = AnimeDatabase()

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define Pydantic models
class Anime(BaseModel):
    id: int
    title: str
    description: str
    episodes: int
    genres: List[str]

class SearchAnimeRequest(BaseModel):
    query: str
    page: Optional[int] = 1
    limit: Optional[int] = 10

class AnimeStreamRequest(BaseModel):
    anime_id: int
    episode: int

# Define routes
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    # For demonstration purposes, return a dummy token
    return {"access_token": "dummy_token", "token_type": "bearer"}

@app.get("/anime")
async def get_animes(token: str = Depends(oauth2_scheme)):
    animes = anime_db.get_animes()
    return JSONResponse(content=[anime.dict() for anime in animes], media_type="application/json")

@app.get("/anime/{anime_id}")
async def get_anime(anime_id: int, token: str = Depends(oauth2_scheme)):
    anime = anime_db.get_anime(anime_id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return JSONResponse(content=anime.dict(), media_type="application/json")

@app.post("/anime/search")
async def search_animes(search_request: SearchAnimeRequest, token: str = Depends(oauth2_scheme)):
    results = anime_db.search_animes(search_request.query, search_request.page, search_request.limit)
    return JSONResponse(content=[anime.dict() for anime in results], media_type="application/json")

@app.get("/anime/{anime_id}/stream")
async def stream_anime(anime_stream_request: AnimeStreamRequest, token: str = Depends(oauth2_scheme)):
    anime_id = anime_stream_request.anime_id
    episode = anime_stream_request.episode
    stream_url = anime_db.get_stream_url(anime_id, episode)
    if not stream_url:
        raise HTTPException(status_code=404, detail="Stream not found")
    return StreamingResponse(stream_url, media_type="application/octet-stream")

# Error handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code, media_type="application/json")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**anime_database.py**
```python
import sqlite3
from typing import List

class AnimeDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("anime.db")
        self.cursor = self.conn.cursor()

    def get_animes(self):
        self.cursor.execute("SELECT * FROM animes")
        rows = self.cursor.fetchall()
        return [self.row_to_anime(row) for row in rows]

    def get_anime(self, anime_id: int):
        self.cursor.execute("SELECT * FROM animes WHERE id = ?", (anime_id,))
        row = self.cursor.fetchone()
        return self.row_to_anime(row) if row else None

    def search_animes(self, query: str, page: int, limit: int):
        offset = (page - 1) * limit
        self.cursor.execute("SELECT * FROM animes WHERE title LIKE ? LIMIT ? OFFSET ?", (f"%{query}%", limit, offset))
        rows = self.cursor.fetchall()
        return [self.row_to_anime(row) for row in rows]

    def get_stream_url(self, anime_id: int, episode: int):
        self.cursor.execute("SELECT stream_url FROM streams WHERE anime_id = ? AND episode = ?", (anime_id, episode))
        row = self.cursor.fetchone()
        return row[0] if row else None

    @staticmethod
    def row_to_anime(row):
        return Anime(
            id=row[0],
            title=row[1],
            description=row[2],
            episodes=row[3],
            genres=row[4].split(",")
        )
```

**schema.sql**
```sql
CREATE TABLE animes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    episodes INTEGER,
    genres TEXT
);

CREATE TABLE streams (
    id INTEGER PRIMARY KEY,
    anime_id INTEGER,
    episode INTEGER,
    stream_url TEXT,
    FOREIGN KEY (anime_id) REFERENCES animes (id)
);
```

**Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "anime_api:app", "--host", "0.0.0.0", "--port", "8000"]
```

**requirements.txt**
```
fastapi
uvicorn
pydantic
sqlite3
```
