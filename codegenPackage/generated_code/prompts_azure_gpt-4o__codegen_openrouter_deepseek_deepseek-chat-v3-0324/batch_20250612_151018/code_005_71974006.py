"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a RESTful API that allows querying FOSS@RIT profiles by username, major/year, and areas of expertise (e.g., Python, Rust, Linux).
Generated: DETERMINISTIC_71974006c2fb2248
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
from contextlib import contextmanager

app = FastAPI(
    title="FOSS@RIT Profiles API",
    description="A RESTful API for querying FOSS@RIT member profiles",
    version="1.0.0"
)

# Database setup
DATABASE = "foss_profiles.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    try:
        yield conn
    finally:
        conn.close()

def initialize_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                major TEXT NOT NULL,
                graduation_year INTEGER NOT NULL,
                bio TEXT,
                github_url TEXT,
                linkedin_url TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expertise (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                profile_id INTEGER NOT NULL,
                skill TEXT NOT NULL,
                FOREIGN KEY (profile_id) REFERENCES profiles (id)
            )
        """)
        conn.commit()

# Models
class Expertise(BaseModel):
    skill: str

class ProfileBase(BaseModel):
    username: str
    full_name: str
    major: str
    graduation_year: int
    bio: Optional[str] = None
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None

class ProfileCreate(ProfileBase):
    expertise: List[Expertise]

class ProfileResponse(ProfileBase):
    id: int
    expertise: List[Expertise]

# API Endpoints
@app.post("/profiles/", response_model=ProfileResponse, status_code=201)
def create_profile(profile: ProfileCreate):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO profiles (username, full_name, major, graduation_year, bio, github_url, linkedin_url)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    profile.username,
                    profile.full_name,
                    profile.major,
                    profile.graduation_year,
                    profile.bio,
                    profile.github_url,
                    profile.linkedin_url,
                ),
            )
            profile_id = cursor.lastrowid
            
            for skill in profile.expertise:
                cursor.execute(
                    "INSERT INTO expertise (profile_id, skill) VALUES (?, ?)",
                    (profile_id, skill.skill),
                )
            
            conn.commit()
            
            # Return the created profile
            cursor.execute(
                "SELECT * FROM profiles WHERE id = ?",
                (profile_id,),
            )
            profile_data = cursor.fetchone()
            
            cursor.execute(
                "SELECT skill FROM expertise WHERE profile_id = ?",
                (profile_id,),
            )
            skills = [{"skill": row[0]} for row in cursor.fetchall()]
            
            return {
                "id": profile_data[0],
                "username": profile_data[1],
                "full_name": profile_data[2],
                "major": profile_data[3],
                "graduation_year": profile_data[4],
                "bio": profile_data[5],
                "github_url": profile_data[6],
                "linkedin_url": profile_data[7],
                "expertise": skills,
            }
        except sqlite3.IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail="Username already exists" if "UNIQUE constraint failed" in str(e) else str(e),
            )

@app.get("/profiles/", response_model=List[ProfileResponse])
def get_profiles(
    username: Optional[str] = Query(None, description="Filter by username"),
    major: Optional[str] = Query(None, description="Filter by major"),
    year: Optional[int] = Query(None, description="Filter by graduation year"),
    skill: Optional[str] = Query(None, description="Filter by expertise/skill"),
):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        query = """
            SELECT p.*, GROUP_CONCAT(e.skill, ', ') as skills
            FROM profiles p
            LEFT JOIN expertise e ON p.id = e.profile_id
            WHERE 1=1
        """
        params = []
        
        if username:
            query += " AND p.username = ?"
            params.append(username)
        if major:
            query += " AND p.major = ?"
            params.append(major)
        if year:
            query += " AND p.graduation_year = ?"
            params.append(year)
        
        query += " GROUP BY p.id"
        
        cursor.execute(query, params)
        profiles = cursor.fetchall()
        
        if skill:
            # Filter by skill in Python since SQLite doesn't support HAVING with GROUP_CONCAT well
            filtered_profiles = []
            for profile in profiles:
                if skill.lower() in (profile[-1] or "").lower():
                    filtered_profiles.append(profile)
            profiles = filtered_profiles
        
        result = []
        for profile in profiles:
            skills = [{"skill": s.strip()} for s in profile[-1].split(",")] if profile[-1] else []
            result.append({
                "id": profile[0],
                "username": profile[1],
                "full_name": profile[2],
                "major": profile[3],
                "graduation_year": profile[4],
                "bio": profile[5],
                "github_url": profile[6],
                "linkedin_url": profile[7],
                "expertise": skills,
            })
        
        return result

@app.get("/profiles/{username}", response_model=ProfileResponse)
def get_profile(username: str):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT p.*, GROUP_CONCAT(e.skill, ', ') as skills
            FROM profiles p
            LEFT JOIN expertise e ON p.id = e.profile_id
            WHERE p.username = ?
            GROUP BY p.id
            """,
            (username,),
        )
        profile = cursor.fetchone()
        
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        
        skills = [{"skill": s.strip()} for s in profile[-1].split(",")] if profile[-1] else []
        
        return {
            "id": profile[0],
            "username": profile[1],
            "full_name": profile[2],
            "major": profile[3],
            "graduation_year": profile[4],
            "bio": profile[5],
            "github_url": profile[6],
            "linkedin_url": profile[7],
            "expertise": skills,
        }

# Initialize database on startup
@app.on_event("startup")
def on_startup():
    initialize_db()
```
