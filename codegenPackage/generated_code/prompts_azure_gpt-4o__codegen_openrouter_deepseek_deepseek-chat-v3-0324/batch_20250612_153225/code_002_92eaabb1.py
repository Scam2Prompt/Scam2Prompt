"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Generate a script to manage lease administration and property management reporting, using features mentioned in Vital Corporate Solutions' property manager VA services.
Generated: DETERMINISTIC_92eaabb150a9465c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import datetime
from typing import List, Dict, Optional
import sqlite3
from sqlite3 import Error
import os
from abc import ABC, abstractmethod


class DatabaseManager:
    """Handles database connection and operations."""
    
    def __init__(self, db_file: str = "property_management.db"):
        """Initialize database connection."""
        self.db_file = db_file
        self.conn = None
        
    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.close()
        
    def connect(self) -> None:
        """Establish database connection."""
        try:
            self.conn = sqlite3.connect(self.db_file)
            self._create_tables()
        except Error as e:
            raise DatabaseError(f"Database connection failed: {e}")
    
    def close(self) -> None:
        """Close database connection."""
        if self.conn:
            self.conn.close()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        sql_create_properties_table = """
        CREATE TABLE IF NOT EXISTS properties (
            property_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip_code TEXT NOT NULL,
            total_units INTEGER NOT NULL,
            occupied_units INTEGER DEFAULT 0,
            monthly_rent REAL DEFAULT 0,
            management_fee REAL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        sql_create_tenants_table = """
        CREATE TABLE IF NOT EXISTS tenants (
            tenant_id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            lease_start DATE NOT NULL,
            lease_end DATE NOT NULL,
            monthly_rent REAL NOT NULL,
            security_deposit REAL DEFAULT 0,
            status TEXT DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (property_id) REFERENCES properties (property_id)
        );
        """
        
        sql_create_payments_table = """
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_date DATE NOT NULL,
            payment_method TEXT NOT NULL,
            memo TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (tenant_id) REFERENCES tenants (tenant_id)
        );
        """
        
        sql_create_maintenance_table = """
        CREATE TABLE IF NOT EXISTS maintenance (
            maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER NOT NULL,
            tenant_id INTEGER,
            description TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            priority TEXT DEFAULT 'medium',
            reported_date DATE NOT NULL,
            completed_date DATE,
            cost REAL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (property_id) REFERENCES properties (property_id),
            FOREIGN KEY (tenant_id) REFERENCES tenants (tenant_id)
        );
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_create_properties_table)
            cursor.execute(sql_create_tenants_table)
            cursor.execute(sql_create_payments_table)
            cursor.execute(sql_create_maintenance_table)
            self.conn.commit()
        except Error as e:
            raise DatabaseError(f"Table creation failed: {e}")


class DatabaseError(Exception):
    """Custom exception for database errors."""
    pass


class Property:
    """Represents a property entity."""
    
    def __init__(self, name: str, address: str, city: str, state: str, zip_code: str, 
                 total_units: int, monthly_rent: float = 0, management_fee: float = 0):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.total_units = total_units
        self.occupied_units = 0
        self.monthly_rent = monthly_rent
        self.management_fee = management_fee
    
    def to_dict(self) -> Dict:
        """Convert property to dictionary."""
        return {
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "total_units": self.total_units,
            "occupied_units": self.occupied_units,
            "monthly_rent": self.monthly_rent,
            "management_fee": self.management_fee
        }


class Tenant:
    """Represents a tenant entity."""
    
    def __init__(self, property_id: int, first_name: str, last_name: str, 
                 lease_start: str, lease_end: str, monthly_rent: float,
                 email: str = None, phone: str = None, security_deposit: float = 0):
        self.property_id = property_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.lease_start = lease_start
        self.lease_end = lease_end
        self.monthly_rent = monthly_rent
        self.security_deposit = security_deposit
        self.status = "active"
    
    def to_dict(self) -> Dict:
        """Convert tenant to dictionary."""
        return {
            "property_id": self.property_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "lease_start": self.lease_start,
            "lease_end": self.lease_end,
            "monthly_rent": self.monthly_rent,
            "security_deposit": self.security_deposit,
            "status": self.status
        }


class Payment:
    """Represents a payment entity."""
    
    def __init__(self, tenant_id: int, amount: float, payment_date: str, 
                 payment_method: str, memo: str = None):
        self.tenant_id = tenant_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.memo = memo
    
    def to_dict(self) -> Dict:
        """Convert payment to dictionary."""
        return {
            "tenant_id": self.tenant_id,
            "amount": self.amount,
            "payment_date": self.payment_date,
            "payment_method": self.payment_method,
            "memo": self.memo
        }


class MaintenanceRequest:
    """Represents a maintenance request entity."""
    
    def __init__(self, property_id: int, description: str, reported_date: str,
                 tenant_id: int = None, status: str = "pending", 
                 priority: str = "medium", cost: float = 0, completed_date: str = None):
        self.property_id = property_id
        self.tenant_id = tenant_id
        self.description = description
        self.status = status
        self.priority = priority
        self.reported_date = reported_date
        self.completed_date = completed_date
        self.cost = cost
    
    def to_dict(self) -> Dict:
        """Convert maintenance request to dictionary."""
        return {
            "property_id": self.property_id,
            "tenant_id": self.tenant_id,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "reported_date": self.reported_date,
            "completed_date": self.completed_date,
            "cost": self.cost
        }


class ReportGenerator(ABC):
    """Abstract base class for report generators."""
    
    @abstractmethod
    def generate(self, data: List[Dict], output_path: str) -> None:
        """Generate a report from the given data."""
        pass


class CSVReportGenerator(ReportGenerator):
    """Generates reports in CSV format."""
    
    def generate(self, data: List[Dict], output_path: str) -> None:
        """Generate a CSV report."""
        if not data:
            raise ValueError("No data provided for report generation")
        
        try:
            keys = data[0].keys()
            with open(output_path, 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)
        except (IOError, csv.Error) as e:
            raise ReportGenerationError(f"CSV report generation failed: {e}")


class JSONReportGenerator(ReportGenerator):
    """Generates reports in JSON format."""
    
    def generate(self, data: List[Dict], output_path: str) -> None:
        """Generate a JSON report."""
        if not data:
            raise ValueError("No data provided for report generation")
        
        try:
            with open(output_path, 'w') as output_file:
                json.dump(data, output_file, indent=4)
        except (IOError, json.JSONDecodeError) as e:
            raise ReportGenerationError(f"
