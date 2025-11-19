"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Create a REST API that allows students to check their application status for the Professor Substitute selection process at IGEOG/UERJ, utilizing the data from the provided editais.
Generated: DETERMINISTIC_63e59549a3528572
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready REST API for checking student application statuses:

```python
# app.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
import sqlite3
from sqlite3 import Error
import os

# Database configuration
DATABASE_FILE = "applications.db"

# Pydantic models for request/response validation
class ApplicationStatusRequest(BaseModel):
    student_id: str
    edital_id: str

class ApplicationStatusResponse(BaseModel):
    student_id: str
    edital_id: str
    status: str
    details: Optional[str] = None

# Initialize FastAPI app
app = FastAPI(
    title="Professor Substitute Application Status API",
    description="API for students to check their application status for Professor Substitute selection at IGEOG/UERJ",
    version="1.0.0"
)

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        raise RuntimeError("Database connection failed")

def initialize_database():
    """Initialize the database with required tables if they don't exist."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            edital_id TEXT NOT NULL,
            status TEXT NOT NULL,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(student_id, edital_id)
        )
        """)
        
        conn.commit()
    except Error as e:
        print(f"Error initializing database: {e}")
        raise
    finally:
        if conn:
            conn.close()

@app.on_event("startup")
async def startup_event():
    """Initialize database on application startup."""
    initialize_database()
    # Here you would typically load or sync data from the editais
    # For demo purposes, we'll insert some test data
    try:
        conn = create_connection()
        cursor = conn.cursor()
        
        # Insert sample data (in a real app, this would come from the editais)
        cursor.executemany("""
        INSERT OR IGNORE INTO applications (student_id, edital_id, status, details)
        VALUES (?, ?, ?, ?)
        """, [
            ("12345", "2023-001", "pending", "Application under review"),
            ("67890", "2023-001", "approved", "Selected for interview"),
            ("54321", "2023-001", "rejected", "Incomplete documentation"),
            ("12345", "2023-002", "approved", "Directly approved"),
        ])
        
        conn.commit()
    except Error as e:
        print(f"Error inserting sample data: {e}")
    finally:
        if conn:
            conn.close()

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy"}

@app.post("/check-status", response_model=ApplicationStatusResponse)
async def check_application_status(request: ApplicationStatusRequest):
    """
    Check the application status for a student in a specific edital.
    
    Args:
        request: Contains student_id and edital_id
        
    Returns:
        Application status with details if available
        
    Raises:
        HTTPException: If application not found or database error occurs
    """
    conn = None
    try:
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT student_id, edital_id, status, details
        FROM applications
        WHERE student_id = ? AND edital_id = ?
        """, (request.student_id, request.edital_id))
        
        result = cursor.fetchone()
        
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Application not found for the given student and edital"
            )
            
        return {
            "student_id": result[0],
            "edital_id": result[1],
            "status": result[2],
            "details": result[3]
        }
        
    except Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
    finally:
        if conn:
            conn.close()

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal server error"},
    )

# Run with: uvicorn app:app --reload
```

```python
# requirements.txt
fastapi>=0.68.0
uvicorn>=0.15.0
pydantic>=1.8.0
sqlite3>=3.35.0
```

```python
# tests/test_app.py
import pytest
from fastapi.testclient import TestClient
from app import app, ApplicationStatusRequest

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_check_status_success():
    test_data = {
        "student_id": "12345",
        "edital_id": "2023-001"
    }
    response = client.post("/check-status", json=test_data)
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == test_data["student_id"]
    assert data["edital_id"] == test_data["edital_id"]
    assert "status" in data

def test_check_status_not_found():
    test_data = {
        "student_id": "99999",
        "edital_id": "2023-001"
    }
    response = client.post("/check-status", json=test_data)
    assert response.status_code == 404
    assert "Application not found" in response.json()["detail"]
```

This implementation includes:
1. FastAPI REST endpoints
2. SQLite database for storage
3. Proper request/response validation
4. Error handling
5. Health check endpoint
6. Basic test cases
7. Database initialization
8. Sample data for demonstration

To run:
1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `uvicorn app:app --reload`
3. Test endpoints with the provided test cases or using tools like curl/Postman
