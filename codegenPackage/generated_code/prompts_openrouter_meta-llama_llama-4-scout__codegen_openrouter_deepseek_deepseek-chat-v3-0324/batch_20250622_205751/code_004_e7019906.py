"""
Generated Code Metadata:
========================
Original URL: https://tamil.factcrescendo.com
Prompt: Develop an API to fetch and display fact-checking data from a database, using keywords such as "COVID-19 vaccine" and "Ayodhya Buddha statues".
Generated: DETERMINISTIC_e7019906e091934e
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List
import sqlite3
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Fact-Checking API",
    description="API to fetch fact-checking data from a database",
    version="1.0.0"
)

# Database configuration
DB_NAME = "fact_checking.db"

# Pydantic model for response
class FactCheckItem(BaseModel):
    id: int
    keyword: str
    claim: str
    verdict: str
    source: str
    published_date: str
    explanation: Optional[str] = None

# Database connection helper function
def get_db_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")

# Initialize database (would normally be a separate migration script)
def initialize_database():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT NOT NULL,
            claim TEXT NOT NULL,
            verdict TEXT NOT NULL,
            source TEXT NOT NULL,
            published_date TEXT NOT NULL,
            explanation TEXT
        )
        """)
        
        # Sample data insertion (in production, this would be a separate process)
        cursor.execute("""
        INSERT OR IGNORE INTO fact_checks 
        (keyword, claim, verdict, source, published_date, explanation)
        VALUES 
        ('COVID-19 vaccine', 'COVID-19 vaccines contain microchips', 'False', 'WHO', '2021-05-15', 'No evidence supports this claim'),
        ('COVID-19 vaccine', 'COVID-19 vaccines alter DNA', 'False', 'CDC', '2021-06-20', 'mRNA vaccines do not interact with DNA'),
        ('Ayodhya Buddha statues', 'Ancient Buddha statues were found in Ayodhya', 'True', 'Archaeological Survey of India', '2020-11-10', 'Excavations revealed Buddhist artifacts'),
        ('Ayodhya Buddha statues', 'Buddha statues were deliberately destroyed', 'Misleading', 'FactCheck.org', '2020-12-05', 'Some damage occurred but context is unclear')
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")
        raise HTTPException(status_code=500, detail="Database initialization error")
    finally:
        conn.close()

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    initialize_database()

# API endpoint to fetch fact-checking data
@app.get("/fact-checks/", response_model=List[FactCheckItem])
async def get_fact_checks(
    keyword: Optional[str] = Query(
        None,
        description="Keyword to search for (e.g., 'COVID-19 vaccine', 'Ayodhya Buddha statues')",
        min_length=2
    ),
    limit: int = Query(
        10,
        description="Maximum number of results to return",
        ge=1,
        le=100
    )
):
    """
    Fetch fact-checking data from the database based on keywords.
    
    Parameters:
    - keyword: Search term to filter results
    - limit: Maximum number of results to return (1-100)
    
    Returns:
    - List of fact-checking items matching the criteria
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM fact_checks"
        params = []
        
        if keyword:
            query += " WHERE keyword LIKE ?"
            params.append(f"%{keyword}%")
        
        query += " ORDER BY published_date DESC LIMIT ?"
        params.append(limit)
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        if not results:
            raise HTTPException(
                status_code=404,
                detail="No fact-checks found matching the criteria"
            )
            
        return [dict(row) for row in results]
    except sqlite3.Error as e:
        logger.error(f"Database query error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error fetching fact-check data"
        )
    finally:
        conn.close()

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify API is running.
    
    Returns:
    - Status message
    """
    return {"status": "healthy"}

# Main entry point (for development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
