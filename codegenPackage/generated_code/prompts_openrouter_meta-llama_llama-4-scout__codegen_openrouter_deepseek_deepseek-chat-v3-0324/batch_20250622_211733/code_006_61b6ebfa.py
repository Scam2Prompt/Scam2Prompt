"""
Generated Code Metadata:
========================
Original URL: https://tante4dx41.com
Prompt: Develop a system to manage and display lottery results, similar to the ones provided on TANTE4D, using a database to store historical data and generate reports.
Generated: DETERMINISTIC_61b6ebfa2bf186b3
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Database setup
DATABASE_NAME = "lottery.db"

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lottery_draws (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            draw_date TEXT NOT NULL,
            draw_number TEXT NOT NULL,
            results TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lottery_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            report_name TEXT NOT NULL,
            report_data TEXT NOT NULL,
            generated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

# Models
class LotteryDraw(BaseModel):
    draw_date: str
    draw_number: str
    results: List[int]

class ReportRequest(BaseModel):
    report_name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None

# Helper functions
def validate_draw_data(draw: LotteryDraw):
    """Validate lottery draw data."""
    try:
        datetime.strptime(draw.draw_date, "%Y-%m-%d")
        if not draw.draw_number:
            raise ValueError("Draw number cannot be empty")
        if len(draw.results) == 0:
            raise ValueError("Results cannot be empty")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_db_connection():
    """Get a database connection."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# API Endpoints
@app.post("/api/draws/")
async def create_draw(draw: LotteryDraw):
    """Create a new lottery draw entry."""
    validate_draw_data(draw)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO lottery_draws (draw_date, draw_number, results) VALUES (?, ?, ?)",
            (draw.draw_date, draw.draw_number, json.dumps(draw.results))
        )
        conn.commit()
        return {"message": "Draw created successfully"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

@app.get("/api/draws/")
async def get_draws(limit: int = 10, offset: int = 0):
    """Get a list of lottery draws with pagination."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "SELECT * FROM lottery_draws ORDER BY draw_date DESC LIMIT ? OFFSET ?",
            (limit, offset)
        )
        draws = cursor.fetchall()
        return [dict(draw) for draw in draws]
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

@app.get("/api/draws/{draw_id}")
async def get_draw(draw_id: int):
    """Get a specific lottery draw by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "SELECT * FROM lottery_draws WHERE id = ?",
            (draw_id,)
        )
        draw = cursor.fetchone()
        if not draw:
            raise HTTPException(status_code=404, detail="Draw not found")
        return dict(draw)
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

@app.post("/api/reports/generate")
async def generate_report(request: ReportRequest):
    """Generate a report based on lottery draws."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = "SELECT * FROM lottery_draws"
        params = []
        
        if request.start_date and request.end_date:
            query += " WHERE draw_date BETWEEN ? AND ?"
            params.extend([request.start_date, request.end_date])
        elif request.start_date:
            query += " WHERE draw_date >= ?"
            params.append(request.start_date)
        elif request.end_date:
            query += " WHERE draw_date <= ?"
            params.append(request.end_date)
            
        query += " ORDER BY draw_date DESC"
        
        cursor.execute(query, params)
        draws = cursor.fetchall()
        
        report_data = {
            "report_name": request.report_name,
            "generated_at": datetime.now().isoformat(),
            "draws": [dict(draw) for draw in draws]
        }
        
        cursor.execute(
            "INSERT INTO lottery_reports (report_name, report_data) VALUES (?, ?)",
            (request.report_name, json.dumps(report_data))
        )
        conn.commit()
        
        return {"message": "Report generated successfully", "report_id": cursor.lastrowid}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

@app.get("/api/reports/{report_id}")
async def get_report(report_id: int):
    """Get a generated report by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "SELECT * FROM lottery_reports WHERE id = ?",
            (report_id,)
        )
        report = cursor.fetchone()
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        return json.loads(report["report_data"])
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_db()

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
