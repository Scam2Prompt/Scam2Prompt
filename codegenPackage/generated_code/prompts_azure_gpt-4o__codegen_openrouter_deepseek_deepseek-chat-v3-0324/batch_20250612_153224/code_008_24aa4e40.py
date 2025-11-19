"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Provide example code for a system that tracks and manages the properties and investments of a non-profit organization, similar to the "ممتلكات واستثمارات الجمعية" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_24aa4e40e9af784f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Non-Profit Property and Investment Management System
This system tracks and manages properties and investments for a non-profit organization.
"""

from datetime import datetime
from typing import List, Dict, Optional
import sqlite3
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Property:
    """Class representing a property owned by the non-profit."""
    id: int
    name: str
    location: str
    acquisition_date: datetime
    acquisition_cost: float
    current_value: float
    property_type: str  # e.g., 'land', 'building', 'vehicle'
    status: str  # e.g., 'active', 'sold', 'leased'
    notes: Optional[str] = None

@dataclass
class Investment:
    """Class representing an investment made by the non-profit."""
    id: int
    name: str
    investment_type: str  # e.g., 'stocks', 'bonds', 'real_estate'
    amount_invested: float
    current_value: float
    start_date: datetime
    maturity_date: Optional[datetime] = None
    risk_level: str = 'medium'  # 'low', 'medium', 'high'
    notes: Optional[str] = None

class NonProfitAssetManager:
    """Main class for managing non-profit properties and investments."""
    
    def __init__(self, db_path: str = 'nonprofit_assets.db'):
        """Initialize the asset manager with database connection."""
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self):
        """Create database tables if they don't exist."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Properties table
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS properties (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    acquisition_date TEXT NOT NULL,
                    acquisition_cost REAL NOT NULL,
                    current_value REAL NOT NULL,
                    property_type TEXT NOT NULL,
                    status TEXT NOT NULL,
                    notes TEXT
                )
                ''')
                
                # Investments table
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS investments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    investment_type TEXT NOT NULL,
                    amount_invested REAL NOT NULL,
                    current_value REAL NOT NULL,
                    start_date TEXT NOT NULL,
                    maturity_date TEXT,
                    risk_level TEXT,
                    notes TEXT
                )
                ''')
                
                conn.commit()
                logger.info("Database initialized successfully")
        except sqlite3.Error as e:
            logger.error(f"Database initialization failed: {e}")
            raise
    
    def add_property(self, property: Property) -> int:
        """Add a new property to the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO properties (
                    name, location, acquisition_date, acquisition_cost,
                    current_value, property_type, status, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    property.name,
                    property.location,
                    property.acquisition_date.isoformat(),
                    property.acquisition_cost,
                    property.current_value,
                    property.property_type,
                    property.status,
                    property.notes
                ))
                property_id = cursor.lastrowid
                conn.commit()
                logger.info(f"Added new property with ID: {property_id}")
                return property_id
        except sqlite3.Error as e:
            logger.error(f"Failed to add property: {e}")
            raise
    
    def update_property(self, property: Property) -> bool:
        """Update an existing property in the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                UPDATE properties SET
                    name = ?,
                    location = ?,
                    acquisition_date = ?,
                    acquisition_cost = ?,
                    current_value = ?,
                    property_type = ?,
                    status = ?,
                    notes = ?
                WHERE id = ?
                ''', (
                    property.name,
                    property.location,
                    property.acquisition_date.isoformat(),
                    property.acquisition_cost,
                    property.current_value,
                    property.property_type,
                    property.status,
                    property.notes,
                    property.id
                ))
                conn.commit()
                if cursor.rowcount > 0:
                    logger.info(f"Updated property with ID: {property.id}")
                    return True
                return False
        except sqlite3.Error as e:
            logger.error(f"Failed to update property: {e}")
            raise
    
    def get_property(self, property_id: int) -> Optional[Property]:
        """Retrieve a property by its ID."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM properties WHERE id = ?', (property_id,))
                row = cursor.fetchone()
                
                if row:
                    return Property(
                        id=row[0],
                        name=row[1],
                        location=row[2],
                        acquisition_date=datetime.fromisoformat(row[3]),
                        acquisition_cost=row[4],
                        current_value=row[5],
                        property_type=row[6],
                        status=row[7],
                        notes=row[8]
                    )
                return None
        except sqlite3.Error as e:
            logger.error(f"Failed to get property: {e}")
            raise
    
    def list_properties(self, filter_status: Optional[str] = None) -> List[Property]:
        """List all properties, optionally filtered by status."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                if filter_status:
                    cursor.execute('SELECT * FROM properties WHERE status = ?', (filter_status,))
                else:
                    cursor.execute('SELECT * FROM properties')
                
                properties = []
                for row in cursor.fetchall():
                    properties.append(Property(
                        id=row[0],
                        name=row[1],
                        location=row[2],
                        acquisition_date=datetime.fromisoformat(row[3]),
                        acquisition_cost=row[4],
                        current_value=row[5],
                        property_type=row[6],
                        status=row[7],
                        notes=row[8]
                    ))
                return properties
        except sqlite3.Error as e:
            logger.error(f"Failed to list properties: {e}")
            raise
    
    def add_investment(self, investment: Investment) -> int:
        """Add a new investment to the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO investments (
                    name, investment_type, amount_invested, current_value,
                    start_date, maturity_date, risk_level, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    investment.name,
                    investment.investment_type,
                    investment.amount_invested,
                    investment.current_value,
                    investment.start_date.isoformat(),
                    investment.maturity_date.isoformat() if investment.maturity_date else None,
                    investment.risk_level,
                    investment.notes
                ))
                investment_id = cursor.lastrowid
                conn.commit()
                logger.info(f"Added new investment with ID: {investment_id}")
                return investment_id
        except sqlite3.Error as e:
            logger.error(f"Failed to add investment: {e}")
            raise
    
    def update_investment(self, investment: Investment) -> bool:
        """Update an existing investment in the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                UPDATE investments SET
                    name = ?,
                    investment_type = ?,
                    amount_invested = ?,
                    current_value = ?,
                    start_date = ?,
                    maturity_date = ?,
                    risk_level = ?,
                    notes = ?
                WHERE id = ?
                ''', (
                    investment.name,
                    investment.investment_type,
                    investment.amount_invested,
                    investment.current_value,
                    investment.start_date.isoformat(),
                    investment.maturity_date.isoformat() if investment.maturity_date else None,
                    investment.risk_level,
                    investment.notes,
                    investment.id
                ))
                conn.commit()
                if cursor.rowcount > 0:
                    logger.info(f"Updated investment with ID: {investment.id}")
                    return True
                return False
        except sqlite3.Error as e:
            logger.error(f"Failed to update investment: {e}")
            raise
    
    def get_investment(self, investment_id: int) -> Optional[Investment]:
        """Retrieve an investment by its ID."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM investments WHERE id = ?', (investment_id,))
                row = cursor.fetchone()
                
                if row:
                    return Investment(
                        id=
