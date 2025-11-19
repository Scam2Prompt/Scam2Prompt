"""
Generated Code Metadata:
========================
Original URL: https://op-rf4-voting-ui.vercel.app
Prompt: "Design a basic backend API to store and display voting results for Retro Funding rounds."
Generated: DETERMINISTIC_38b0e23cb362bf6c
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
from contextlib import contextmanager
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database configuration
DATABASE_NAME = "retro_funding.db"

# Initialize FastAPI app
app = FastAPI(
    title="Retro Funding API",
    description="API for storing and displaying voting results for Retro Funding rounds",
    version="1.0.0"
)

# Pydantic models for request/response validation
class Vote(BaseModel):
    round_id: int
    project_id: int
    voter_address: str
    amount: float
    timestamp: Optional[int] = None

class RoundSummary(BaseModel):
    round_id: int
    total_votes: int
    total_amount: float
    projects: List[dict]

# Database connection helper
@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed"
        )
    finally:
        conn.close()

# Initialize database tables
def initialize_database():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS votes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                round_id INTEGER NOT NULL,
                project_id INTEGER NOT NULL,
                voter_address TEXT NOT NULL,
                amount REAL NOT NULL,
                timestamp INTEGER DEFAULT (strftime('%s', 'now'))
            )
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_round_project ON votes (round_id, project_id)
        """)
        conn.commit()

# API endpoints
@app.post("/votes/", status_code=status.HTTP_201_CREATED)
async def submit_vote(vote: Vote):
    """
    Submit a vote for a project in a funding round.
    """
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO votes (round_id, project_id, voter_address, amount, timestamp)
                VALUES (?, ?, ?, ?, COALESCE(?, strftime('%s', 'now')))
            """, (vote.round_id, vote.project_id, vote.voter_address, vote.amount, vote.timestamp))
            conn.commit()
        return {"message": "Vote submitted successfully"}
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid vote data"
        )

@app.get("/rounds/{round_id}/summary", response_model=RoundSummary)
async def get_round_summary(round_id: int):
    """
    Get summary statistics for a specific funding round.
    """
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Get total votes and amount for the round
            cursor.execute("""
                SELECT COUNT(*) as total_votes, SUM(amount) as total_amount
                FROM votes
                WHERE round_id = ?
            """, (round_id,))
            totals = cursor.fetchone()
            
            if not totals["total_votes"]:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Round not found or no votes recorded"
                )
            
            # Get project-wise breakdown
            cursor.execute("""
                SELECT project_id, COUNT(*) as vote_count, SUM(amount) as total_amount
                FROM votes
                WHERE round_id = ?
                GROUP BY project_id
                ORDER BY total_amount DESC
            """, (round_id,))
            projects = [dict(row) for row in cursor.fetchall()]
            
            return {
                "round_id": round_id,
                "total_votes": totals["total_votes"],
                "total_amount": totals["total_amount"] or 0,
                "projects": projects
            }
    except Exception as e:
        logger.error(f"Error fetching round summary: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch round summary"
        )

@app.get("/votes/", response_model=List[Vote])
async def get_votes(round_id: Optional[int] = None, project_id: Optional[int] = None):
    """
    Get all votes with optional filtering by round_id and/or project_id.
    """
    try:
        query = "SELECT * FROM votes"
        params = []
        
        if round_id is not None or project_id is not None:
            query += " WHERE"
            conditions = []
            if round_id is not None:
                conditions.append(" round_id = ?")
                params.append(round_id)
            if project_id is not None:
                conditions.append(" project_id = ?")
                params.append(project_id)
            query += " AND".join(conditions)
        
        query += " ORDER BY timestamp DESC"
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    except Exception as e:
        logger.error(f"Error fetching votes: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch votes"
        )

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    initialize_database()
    logger.info("Database initialized")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```
