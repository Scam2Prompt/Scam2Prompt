"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Generate code for a financial disclosure system that allows non-profits to publish annual financial reports, inspired by the "التقارير المالية الإفصاح 2023" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_c3a549bfe5ed6e07
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
import sqlite3
from sqlite3 import Error

# Database setup
DB_FILE = "financial_disclosure.db"

def create_connection():
    """Create a database connection to SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        raise

def initialize_database():
    """Initialize database tables"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        
        # Organizations table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS organizations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            registration_number TEXT UNIQUE NOT NULL,
            contact_email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Financial reports table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS financial_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            organization_id INTEGER NOT NULL,
            year INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            file_path TEXT NOT NULL,
            is_published BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            published_at TIMESTAMP,
            FOREIGN KEY (organization_id) REFERENCES organizations (id),
            UNIQUE(organization_id, year)
        )
        """)
        
        conn.commit()
    except Error as e:
        print(f"Error initializing database: {e}")
        raise
    finally:
        if conn:
            conn.close()

# Models
class Organization(BaseModel):
    name: str
    registration_number: str
    contact_email: str

    @validator('contact_email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v

class FinancialReport(BaseModel):
    organization_id: int
    year: int
    title: str
    description: Optional[str] = None
    is_published: bool = False

    @validator('year')
    def validate_year(cls, v):
        current_year = datetime.now().year
        if v < 2000 or v > current_year + 1:
            raise ValueError(f'Year must be between 2000 and {current_year + 1}')
        return v

class FinancialReportResponse(FinancialReport):
    id: int
    file_path: str
    created_at: datetime
    published_at: Optional[datetime] = None

class PublishedReport(BaseModel):
    id: int
    organization_name: str
    year: int
    title: str
    description: Optional[str]
    file_path: str
    published_at: datetime

# API setup
app = FastAPI(
    title="Non-Profit Financial Disclosure System",
    description="System for non-profits to publish annual financial reports",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File storage configuration
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Helper functions
def save_uploaded_file(file: UploadFile) -> str:
    """Save uploaded file to disk and return its path"""
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path

def get_organization(conn, organization_id: int) -> Dict:
    """Get organization by ID"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM organizations WHERE id = ?", (organization_id,))
    return cursor.fetchone()

# API endpoints
@app.post("/organizations/", response_model=Dict)
def create_organization(organization: Organization):
    """Register a new non-profit organization"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO organizations (name, registration_number, contact_email) VALUES (?, ?, ?)",
            (organization.name, organization.registration_number, organization.contact_email)
        )
        conn.commit()
        return {"message": "Organization registered successfully", "id": cursor.lastrowid}
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Registration number already exists")
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()

@app.post("/reports/", response_model=FinancialReportResponse)
def upload_financial_report(
    organization_id: int = Form(...),
    year: int = Form(...),
    title: str = Form(...),
    description: Optional[str] = Form(None),
    file: UploadFile = File(...)
):
    """Upload a financial report for an organization"""
    conn = create_connection()
    try:
        # Verify organization exists
        org = get_organization(conn, organization_id)
        if not org:
            raise HTTPException(status_code=404, detail="Organization not found")
        
        # Save file
        file_path = save_uploaded_file(file)
        
        # Insert report
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO financial_reports 
            (organization_id, year, title, description, file_path) 
            VALUES (?, ?, ?, ?, ?)
            """,
            (organization_id, year, title, description, file_path)
        )
        conn.commit()
        
        # Return created report
        cursor.execute(
            "SELECT * FROM financial_reports WHERE id = ?", 
            (cursor.lastrowid,)
        )
        report = cursor.fetchone()
        return FinancialReportResponse(
            id=report[0],
            organization_id=report[1],
            year=report[2],
            title=report[3],
            description=report[4],
            file_path=report[5],
            is_published=bool(report[6]),
            created_at=report[7],
            published_at=report[8]
        )
    except sqlite3.IntegrityError as e:
        raise HTTPException(
            status_code=400, 
            detail="A report already exists for this organization and year"
        )
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()

@app.put("/reports/{report_id}/publish", response_model=FinancialReportResponse)
def publish_report(report_id: int):
    """Publish a financial report"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        
        # Get current report status
        cursor.execute("SELECT * FROM financial_reports WHERE id = ?", (report_id,))
        report = cursor.fetchone()
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        
        if report[6]:  # is_published
            raise HTTPException(status_code=400, detail="Report is already published")
        
        # Update report status
        current_time = datetime.now().isoformat()
        cursor.execute(
            "UPDATE financial_reports SET is_published = TRUE, published_at = ? WHERE id = ?",
            (current_time, report_id)
        )
        conn.commit()
        
        # Return updated report
        cursor.execute("SELECT * FROM financial_reports WHERE id = ?", (report_id,))
        updated_report = cursor.fetchone()
        return FinancialReportResponse(
            id=updated_report[0],
            organization_id=updated_report[1],
            year=updated_report[2],
            title=updated_report[3],
            description=updated_report[4],
            file_path=updated_report[5],
            is_published=bool(updated_report[6]),
            created_at=updated_report[7],
            published_at=updated_report[8]
        )
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()

@app.get("/reports/published", response_model=List[PublishedReport])
def get_published_reports():
    """Get all published financial reports"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT fr.id, o.name, fr.year, fr.title, fr.description, fr.file_path, fr.published_at
            FROM financial_reports fr
            JOIN organizations o ON fr.organization_id = o.id
            WHERE fr.is_published = TRUE
            ORDER BY fr.published_at DESC
        """)
        reports = cursor.fetchall()
        return [
            PublishedReport(
                id=report[0],
                organization_name=report[1],
                year=report[2],
                title=report[3],
                description=report[4],
                file_path=report[5],
                published_at=report[6
