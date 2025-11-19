"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Develop a leaderboard system for tracking user points in the XSwap ecosystem, referencing the features mentioned on the webpage.
Generated: DETERMINISTIC_8bb68121877dbb7e
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional
import sqlite3
from sqlite3 import Error
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="XSwap Leaderboard API")

# Database setup
DATABASE = "xswap_leaderboard.db"

def create_connection():
    """Create a database connection to SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        raise

def initialize_database():
    """Initialize the database with required tables."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        
        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Points table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS points (
            point_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            points INTEGER NOT NULL DEFAULT 0,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        """)
        
        # Transactions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            points_change INTEGER NOT NULL,
            transaction_type TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        """)
        
        conn.commit()
    except Error as e:
        print(f"Error initializing database: {e}")
        raise
    finally:
        if conn:
            conn.close()

# Pydantic models
class User(BaseModel):
    user_id: str
    username: str
    email: Optional[str] = None

class PointsUpdate(BaseModel):
    user_id: str
    points_change: int
    transaction_type: str
    
    @validator('points_change')
    def validate_points_change(cls, v):
        if v == 0:
            raise ValueError("Points change cannot be zero")
        return v

class LeaderboardEntry(BaseModel):
    user_id: str
    username: str
    points: int
    rank: int

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    initialize_database()

# API Endpoints
@app.post("/users/register", response_model=User)
async def register_user(user: User):
    """Register a new user in the system."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        
        # Check if user already exists
        cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user.user_id,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="User already exists")
        
        # Insert new user
        cursor.execute(
            "INSERT INTO users (user_id, username, email) VALUES (?, ?, ?)",
            (user.user_id, user.username, user.email)
        )
        
        # Initialize points
        cursor.execute(
            "INSERT INTO points (user_id, points) VALUES (?, 0)",
            (user.user_id,)
        )
        
        conn.commit()
        return user
    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()

@app.post("/points/update", status_code=200)
async def update_points(update: PointsUpdate):
    """Update user points and record transaction."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (update.user_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="User not found")
        
        # Update points
        cursor.execute(
            """
            UPDATE points 
            SET points = points + ?, 
                last_updated = CURRENT_TIMESTAMP 
            WHERE user_id = ?
            """,
            (update.points_change, update.user_id)
        )
        
        # Record transaction
        cursor.execute(
            """
            INSERT INTO transactions (user_id, points_change, transaction_type)
            VALUES (?, ?, ?)
            """,
            (update.user_id, update.points_change, update.transaction_type)
        )
        
        conn.commit()
        return {"message": "Points updated successfully"}
    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()

@app.get("/leaderboard", response_model=List[LeaderboardEntry])
async def get_leaderboard(limit: int = 100):
    """Get the current leaderboard ranked by points."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        
        cursor.execute(
            """
            SELECT u.user_id, u.username, p.points
            FROM users u
            JOIN points p ON u.user_id = p.user_id
            ORDER BY p.points DESC
            LIMIT ?
            """,
            (limit,)
        )
        
        results = cursor.fetchall()
        leaderboard = []
        
        for rank, (user_id, username, points) in enumerate(results, start=1):
            leaderboard.append(
                LeaderboardEntry(
                    user_id=user_id,
                    username=username,
                    points=points,
                    rank=rank
                )
            )
        
        return leaderboard
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()

@app.get("/users/{user_id}/points", response_model=int)
async def get_user_points(user_id: str):
    """Get current points for a specific user."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT points FROM points WHERE user_id = ?",
            (user_id,)
        )
        
        result = cursor.fetchone()
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        
        return result[0]
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()

@app.get("/users/{user_id}/transactions")
async def get_user_transactions(user_id: str, limit: int = 50):
    """Get transaction history for a specific user."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="User not found")
        
        cursor.execute(
            """
            SELECT transaction_id, points_change, transaction_type, timestamp
            FROM transactions
            WHERE user_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
            """,
            (user_id, limit)
        )
        
        transactions = []
        for row in cursor.fetchall():
            transactions.append({
                "transaction_id": row[0],
                "points_change": row[1],
                "transaction_type": row[2],
                "timestamp": row[3]
            })
        
        return {"transactions": transactions}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
