"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Suggest APIs for managing and analyzing data from shelters and helplines, such as those supported by Sauti Kenya, to improve organizational capacity and sustainability.
Generated: DETERMINISTIC_42b6097dd440349a
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
DATABASE_NAME = "shelter_management.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    try:
        yield conn
    finally:
        conn.close()

# Models
class Shelter(BaseModel):
    id: Optional[int] = None
    name: str
    location: str
    capacity: int
    current_occupancy: int
    contact: str
    services: List[str]
    last_updated: Optional[datetime] = None

class Helpline(BaseModel):
    id: Optional[int] = None
    name: str
    contact: str
    operating_hours: str
    languages: List[str]
    services_offered: List[str]

class Report(BaseModel):
    id: Optional[int] = None
    shelter_id: int
    report_date: datetime
    occupancy: int
    resources_used: dict
    issues_reported: List[str]

# Initialize FastAPI
app = FastAPI(
    title="Shelter and Helpline Management API",
    description="API for managing and analyzing data from shelters and helplines",
    version="1.0.0"
)

# Helper functions
def initialize_database():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS shelters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                capacity INTEGER NOT NULL,
                current_occupancy INTEGER NOT NULL,
                contact TEXT NOT NULL,
                services TEXT NOT NULL,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS helplines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT NOT NULL,
                operating_hours TEXT NOT NULL,
                languages TEXT NOT NULL,
                services_offered TEXT NOT NULL
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                shelter_id INTEGER NOT NULL,
                report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                occupancy INTEGER NOT NULL,
                resources_used TEXT NOT NULL,
                issues_reported TEXT NOT NULL,
                FOREIGN KEY (shelter_id) REFERENCES shelters (id)
            )
        """)
        conn.commit()

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    initialize_database()
    logger.info("Database initialized")

# Shelter endpoints
@app.post("/shelters/", response_model=Shelter)
def create_shelter(shelter: Shelter, db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute(
            """
            INSERT INTO shelters (name, location, capacity, current_occupancy, contact, services)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                shelter.name,
                shelter.location,
                shelter.capacity,
                shelter.current_occupancy,
                shelter.contact,
                ",".join(shelter.services)
            )
        )
        db.commit()
        shelter.id = cursor.lastrowid
        return shelter
    except Exception as e:
        logger.error(f"Error creating shelter: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating shelter")

@app.get("/shelters/", response_model=List[Shelter])
def get_shelters(db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM shelters")
        rows = cursor.fetchall()
        shelters = []
        for row in rows:
            shelters.append(Shelter(
                id=row[0],
                name=row[1],
                location=row[2],
                capacity=row[3],
                current_occupancy=row[4],
                contact=row[5],
                services=row[6].split(","),
                last_updated=row[7]
            ))
        return shelters
    except Exception as e:
        logger.error(f"Error fetching shelters: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching shelters")

# Helpline endpoints
@app.post("/helplines/", response_model=Helpline)
def create_helpline(helpline: Helpline, db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute(
            """
            INSERT INTO helplines (name, contact, operating_hours, languages, services_offered)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                helpline.name,
                helpline.contact,
                helpline.operating_hours,
                ",".join(helpline.languages),
                ",".join(helpline.services_offered)
            )
        )
        db.commit()
        helpline.id = cursor.lastrowid
        return helpline
    except Exception as e:
        logger.error(f"Error creating helpline: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating helpline")

@app.get("/helplines/", response_model=List[Helpline])
def get_helplines(db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM helplines")
        rows = cursor.fetchall()
        helplines = []
        for row in rows:
            helplines.append(Helpline(
                id=row[0],
                name=row[1],
                contact=row[2],
                operating_hours=row[3],
                languages=row[4].split(","),
                services_offered=row[5].split(",")
            ))
        return helplines
    except Exception as e:
        logger.error(f"Error fetching helplines: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching helplines")

# Reporting endpoints
@app.post("/reports/", response_model=Report)
def create_report(report: Report, db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute(
            """
            INSERT INTO reports (shelter_id, occupancy, resources_used, issues_reported)
            VALUES (?, ?, ?, ?)
            """,
            (
                report.shelter_id,
                report.occupancy,
                str(report.resources_used),
                ",".join(report.issues_reported)
            )
        )
        db.commit()
        report.id = cursor.lastrowid
        return report
    except Exception as e:
        logger.error(f"Error creating report: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating report")

@app.get("/analytics/occupancy/")
def get_occupancy_analytics(db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute("""
            SELECT s.name, s.capacity, AVG(r.occupancy) as avg_occupancy, 
                   MAX(r.occupancy) as peak_occupancy
            FROM shelters s
            JOIN reports r ON s.id = r.shelter_id
            GROUP BY s.id
        """)
        rows = cursor.fetchall()
        analytics = []
        for row in rows:
            analytics.append({
                "shelter_name": row[0],
                "capacity": row[1],
                "average_occupancy": row[2],
                "peak_occupancy": row[3]
            })
        return {"occupancy_analytics": analytics}
    except Exception as e:
        logger.error(f"Error fetching occupancy analytics: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching analytics")

@app.get("/analytics/resource-usage/")
def get_resource_analytics(db: sqlite3.Connection = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT resources_used FROM reports")
        rows = cursor.fetchall()
        resource_counts = {}
        
        for row in rows:
            resources = eval(row[0])  # Caution: eval can be dangerous with untrusted data
            for resource, quantity in resources.items():
                if resource in resource_counts:
                    resource_counts[resource] += quantity
                else:
                    resource_counts[resource] = quantity
        
        return {"resource_usage": resource_counts}
    except Exception as e:
        logger.error(f"Error fetching resource analytics: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching analytics")

# Health check endpoint
@app.get("/health/")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}
```
