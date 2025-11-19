"""
Generated Code Metadata:
========================
Original URL: https://www.kff.org.kw
Prompt: "What are some best practices for creating a farmer management system like the one implied by the Kuwaiti Farmers Federation's services?"
Generated: DETERMINISTIC_02ecd3b7e39ef823
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Farmer Management System - Core Module

This module provides core functionality for managing farmers, farms, and agricultural data.
It follows best practices for data management, security, and scalability.
"""

import sqlite3
from typing import List, Dict, Optional
from dataclasses import dataclass
import hashlib
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Farmer:
    """Represents a farmer in the system."""
    id: int
    name: str
    national_id: str
    contact_number: str
    email: str
    registration_date: str
    status: str = 'active'

@dataclass
class Farm:
    """Represents a farm in the system."""
    id: int
    farmer_id: int
    location: str
    area: float
    soil_type: str
    irrigation_type: str
    crops: List[str]

class FarmerManagementSystem:
    """Core farmer management system class."""
    
    def __init__(self, db_path: str = 'farmers.db'):
        """Initialize the system with database connection."""
        self.db_path = db_path
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Farmers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS farmers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    national_id TEXT UNIQUE NOT NULL,
                    contact_number TEXT NOT NULL,
                    email TEXT,
                    registration_date TEXT NOT NULL,
                    status TEXT DEFAULT 'active',
                    password_hash TEXT NOT NULL
                )
            ''')
            
            # Farms table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS farms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    farmer_id INTEGER NOT NULL,
                    location TEXT NOT NULL,
                    area REAL NOT NULL,
                    soil_type TEXT NOT NULL,
                    irrigation_type TEXT NOT NULL,
                    crops TEXT NOT NULL,
                    FOREIGN KEY (farmer_id) REFERENCES farmers (id)
                )
            ''')
            
            conn.commit()
    
    def _hash_password(self, password: str) -> str:
        """Hash a password for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_farmer(
        self,
        name: str,
        national_id: str,
        contact_number: str,
        email: str,
        password: str
    ) -> Optional[Farmer]:
        """Register a new farmer in the system."""
        try:
            registration_date = datetime.now().isoformat()
            password_hash = self._hash_password(password)
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO farmers (
                        name, national_id, contact_number, email, 
                        registration_date, password_hash
                    ) VALUES (?, ?, ?, ?, ?, ?)
                ''', (name, national_id, contact_number, email, 
                     registration_date, password_hash))
                
                farmer_id = cursor.lastrowid
                conn.commit()
                
                return Farmer(
                    id=farmer_id,
                    name=name,
                    national_id=national_id,
                    contact_number=contact_number,
                    email=email,
                    registration_date=registration_date
                )
        except sqlite3.IntegrityError as e:
            logger.error(f"Farmer registration failed: {e}")
            return None
    
    def authenticate_farmer(self, national_id: str, password: str) -> bool:
        """Authenticate a farmer using national ID and password."""
        password_hash = self._hash_password(password)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT password_hash FROM farmers 
                WHERE national_id = ? AND status = 'active'
            ''', (national_id,))
            
            result = cursor.fetchone()
            if result and result[0] == password_hash:
                return True
            return False
    
    def add_farm(
        self,
        farmer_id: int,
        location: str,
        area: float,
        soil_type: str,
        irrigation_type: str,
        crops: List[str]
    ) -> Optional[Farm]:
        """Add a new farm for a farmer."""
        try:
            crops_str = ','.join(crops)
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO farms (
                        farmer_id, location, area, soil_type, 
                        irrigation_type, crops
                    ) VALUES (?, ?, ?, ?, ?, ?)
                ''', (farmer_id, location, area, soil_type, 
                     irrigation_type, crops_str))
                
                farm_id = cursor.lastrowid
                conn.commit()
                
                return Farm(
                    id=farm_id,
                    farmer_id=farmer_id,
                    location=location,
                    area=area,
                    soil_type=soil_type,
                    irrigation_type=irrigation_type,
                    crops=crops
                )
        except sqlite3.Error as e:
            logger.error(f"Farm addition failed: {e}")
            return None
    
    def get_farmer_by_id(self, farmer_id: int) -> Optional[Farmer]:
        """Retrieve a farmer by their ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, name, national_id, contact_number, 
                       email, registration_date, status 
                FROM farmers WHERE id = ?
            ''', (farmer_id,))
            
            result = cursor.fetchone()
            if result:
                return Farmer(*result)
            return None
    
    def get_farms_by_farmer(self, farmer_id: int) -> List[Farm]:
        """Retrieve all farms belonging to a farmer."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, farmer_id, location, area, 
                       soil_type, irrigation_type, crops 
                FROM farms WHERE farmer_id = ?
            ''', (farmer_id,))
            
            results = cursor.fetchall()
            farms = []
            for row in results:
                crops = row[6].split(',') if row[6] else []
                farms.append(Farm(
                    id=row[0],
                    farmer_id=row[1],
                    location=row[2],
                    area=row[3],
                    soil_type=row[4],
                    irrigation_type=row[5],
                    crops=crops
                ))
            return farms
    
    def update_farmer_status(self, farmer_id: int, status: str) -> bool:
        """Update a farmer's status (active/inactive)."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE farmers SET status = ? WHERE id = ?
                ''', (status, farmer_id))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            logger.error(f"Farmer status update failed: {e}")
            return False
    
    def search_farmers(self, query: str) -> List[Farmer]:
        """Search farmers by name or national ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, name, national_id, contact_number, 
                       email, registration_date, status 
                FROM farmers 
                WHERE name LIKE ? OR national_id LIKE ?
            ''', (f'%{query}%', f'%{query}%'))
            
            results = cursor.fetchall()
            return [Farmer(*row) for row in results]
    
    def get_all_active_farmers(self) -> List[Farmer]:
        """Retrieve all active farmers."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, name, national_id, contact_number, 
                       email, registration_date, status 
                FROM farmers WHERE status = 'active'
            ''')
            
            results = cursor.fetchall()
            return [Farmer(*row) for row in results]
    
    def generate_farmer_report(self, farmer_id: int) -> Dict:
        """Generate a comprehensive report for a farmer."""
        farmer = self.get_farmer_by_id(farmer_id)
        if not farmer:
            return {}
        
        farms = self.get_farms_by_farmer(farmer_id)
        total_area = sum(farm.area for farm in farms)
        
        return {
            'farmer': farmer,
            'farms': farms,
            'total_farms': len(farms),
            'total_area': total_area,
            'crops': list(set(crop for farm in farms for crop in farm.crops))
        }
```
