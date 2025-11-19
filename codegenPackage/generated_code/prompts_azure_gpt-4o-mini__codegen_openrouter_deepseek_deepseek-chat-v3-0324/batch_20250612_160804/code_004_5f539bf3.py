"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: Illustrate how to implement a digital asset management system for local government using the e-Asset features mentioned on the BPKAD Lamongan website.
Generated: DETERMINISTIC_5f539bf3674309a8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Asset Management System for Local Government
Inspired by BPKAD Lamongan's e-Asset features
"""

import os
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import uuid

# Initialize FastAPI app
app = FastAPI(
    title="Local Government Digital Asset Management",
    description="System for managing government assets with e-Asset features",
    version="1.0.0"
)

# Database setup
DATABASE_NAME = "asset_management.db"

def init_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        location TEXT NOT NULL,
        acquisition_date TEXT NOT NULL,
        acquisition_value REAL NOT NULL,
        current_value REAL NOT NULL,
        condition TEXT NOT NULL,
        department TEXT NOT NULL,
        responsible_person TEXT NOT NULL,
        barcode TEXT UNIQUE,
        photo_path TEXT,
        last_updated TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS asset_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_id TEXT NOT NULL,
        change_date TEXT NOT NULL,
        change_type TEXT NOT NULL,
        changed_by TEXT NOT NULL,
        previous_value TEXT,
        new_value TEXT,
        FOREIGN KEY (asset_id) REFERENCES assets (id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS maintenance_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_id TEXT NOT NULL,
        maintenance_date TEXT NOT NULL,
        maintenance_type TEXT NOT NULL,
        cost REAL NOT NULL,
        description TEXT NOT NULL,
        performed_by TEXT NOT NULL,
        next_maintenance_date TEXT,
        FOREIGN KEY (asset_id) REFERENCES assets (id)
    )
    """)
    
    conn.commit()
    conn.close()

init_db()

# Models
class Asset(BaseModel):
    name: str = Field(..., example="Office Building A")
    category: str = Field(..., example="Building")
    location: str = Field(..., example="Jl. Pemuda No. 1")
    acquisition_date: str = Field(..., example="2020-01-15")
    acquisition_value: float = Field(..., example=500000000.0)
    current_value: float = Field(..., example=450000000.0)
    condition: str = Field(..., example="Good")
    department: str = Field(..., example="Public Works")
    responsible_person: str = Field(..., example="John Doe")
    barcode: Optional[str] = Field(None, example="GOV-ASSET-001")
    status: str = Field(..., example="Active")

class AssetUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    location: Optional[str] = None
    current_value: Optional[float] = None
    condition: Optional[str] = None
    department: Optional[str] = None
    responsible_person: Optional[str] = None
    status: Optional[str] = None

class MaintenanceRecord(BaseModel):
    maintenance_date: str = Field(..., example="2023-05-10")
    maintenance_type: str = Field(..., example="Routine")
    cost: float = Field(..., example=5000000.0)
    description: str = Field(..., example="Painting and minor repairs")
    performed_by: str = Field(..., example="PT Jasa Bangun")
    next_maintenance_date: Optional[str] = Field(None, example="2024-05-10")

class AssetHistory(BaseModel):
    change_date: str
    change_type: str
    changed_by: str
    previous_value: Optional[str] = None
    new_value: Optional[str] = None

# Utility functions
def get_db_connection():
    """Get a database connection"""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def log_asset_history(asset_id: str, change_type: str, changed_by: str, previous_value: str = None, new_value: str = None):
    """Log changes to asset in history table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO asset_history (asset_id, change_date, change_type, changed_by, previous_value, new_value)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (asset_id, datetime.now().isoformat(), change_type, changed_by, previous_value, new_value))
    
    conn.commit()
    conn.close()

# API Endpoints
@app.post("/assets/", response_model=Dict)
async def create_asset(
    asset: Asset,
    photo: UploadFile = File(None),
    changed_by: str = Form(...)
):
    """Create a new asset"""
    asset_id = str(uuid.uuid4())
    photo_path = None
    
    if photo:
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)
        photo_path = os.path.join(upload_dir, f"{asset_id}_{photo.filename}")
        with open(photo_path, "wb") as buffer:
            buffer.write(await photo.read())
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO assets (
            id, name, category, location, acquisition_date, acquisition_value,
            current_value, condition, department, responsible_person, barcode,
            photo_path, last_updated, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            asset_id,
            asset.name,
            asset.category,
            asset.location,
            asset.acquisition_date,
            asset.acquisition_value,
            asset.current_value,
            asset.condition,
            asset.department,
            asset.responsible_person,
            asset.barcode,
            photo_path,
            datetime.now().isoformat(),
            asset.status
        ))
        
        log_asset_history(
            asset_id=asset_id,
            change_type="CREATE",
            changed_by=changed_by,
            new_value=str(asset.dict())
        )
        
        conn.commit()
        return {"id": asset_id, "message": "Asset created successfully"}
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()

@app.get("/assets/", response_model=List[Dict])
def list_assets():
    """List all assets"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM assets")
    assets = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return assets

@app.get("/assets/{asset_id}", response_model=Dict)
def get_asset(asset_id: str):
    """Get asset details"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM assets WHERE id = ?", (asset_id,))
    asset = cursor.fetchone()
    
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    conn.close()
    return dict(asset)

@app.put("/assets/{asset_id}", response_model=Dict)
async def update_asset(
    asset_id: str,
    asset_update: AssetUpdate,
    changed_by: str
):
    """Update asset information"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get current asset data
    cursor.execute("SELECT * FROM assets WHERE id = ?", (asset_id,))
    current_asset = cursor.fetchone()
    
    if not current_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    current_asset_dict = dict(current_asset)
    update_data = asset_update.dict(exclude_unset=True)
    
    # Prepare update query
    set_clause = ", ".join(f"{key} = ?" for key in update_data.keys())
    values = list(update_data.values())
    values.append(asset_id)
    
    try:
        cursor.execute(f"""
        UPDATE assets 
        SET {set_clause}, last_updated = ?
        WHERE id = ?
        """, (*values, datetime.now().isoformat(), asset_id))
        
        # Log changes
        for field, new_value in update_data.items():
            old_value = current_asset_dict.get(field)
            if old_value != new_value:
                log_asset_history(
                    asset_id=asset_id,
                    change_type="UPDATE",
                    changed_by=changed_by,
                    previous_value=str({field: old_value}),
                    new_value=str({field: new_value})
                )
        
        conn.commit()
        return {"message": "Asset updated successfully"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()

@app
