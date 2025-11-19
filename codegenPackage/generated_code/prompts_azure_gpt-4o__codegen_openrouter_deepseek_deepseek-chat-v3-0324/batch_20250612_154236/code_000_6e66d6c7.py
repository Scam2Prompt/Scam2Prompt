"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Write a Python script to automate scheduling repair services for BPL appliances, including ACs, refrigerators, and washing machines, using location-based filtering for Delhi, Noida, Gurgaon, and Faridabad.
Generated: DETERMINISTIC_6e66d6c7edc4f76b
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional
import sqlite3
from sqlite3 import Error

# Database setup and connection
def create_connection(db_file: str) -> Optional[sqlite3.Connection]:
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables(conn: sqlite3.Connection) -> None:
    """Create necessary tables if they don't exist"""
    try:
        c = conn.cursor()
        
        # Customers table
        c.execute('''CREATE TABLE IF NOT EXISTS customers
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      phone TEXT NOT NULL,
                      email TEXT,
                      address TEXT NOT NULL,
                      city TEXT NOT NULL CHECK(city IN ('Delhi', 'Noida', 'Gurgaon', 'Faridabad')),
                      pincode TEXT)''')
        
        # Appliances table
        c.execute('''CREATE TABLE IF NOT EXISTS appliances
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      customer_id INTEGER NOT NULL,
                      type TEXT NOT NULL CHECK(type IN ('AC', 'Refrigerator', 'Washing Machine')),
                      brand TEXT NOT NULL,
                      model TEXT NOT NULL,
                      purchase_date TEXT,
                      warranty_status BOOLEAN,
                      FOREIGN KEY (customer_id) REFERENCES customers (id))''')
        
        # Service requests table
        c.execute('''CREATE TABLE IF NOT EXISTS service_requests
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      appliance_id INTEGER NOT NULL,
                      issue_description TEXT NOT NULL,
                      request_date TEXT NOT NULL,
                      preferred_date TEXT NOT NULL,
                      preferred_time TEXT NOT NULL,
                      status TEXT DEFAULT 'Pending' CHECK(status IN ('Pending', 'Assigned', 'Completed', 'Cancelled')),
                      technician_id INTEGER,
                      FOREIGN KEY (appliance_id) REFERENCES appliances (id),
                      FOREIGN KEY (technician_id) REFERENCES technicians (id))''')
        
        # Technicians table
        c.execute('''CREATE TABLE IF NOT EXISTS technicians
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      phone TEXT NOT NULL,
                      email TEXT,
                      specialization TEXT CHECK(specialization IN ('AC', 'Refrigerator', 'Washing Machine', 'General')),
                      cities_served TEXT NOT NULL)''')
        
        conn.commit()
    except Error as e:
        print(e)

# Data models
class Customer:
    def __init__(self, name: str, phone: str, address: str, city: str, email: str = None, pincode: str = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.pincode = pincode
    
    def save(self, conn: sqlite3.Connection) -> int:
        """Save customer to database and return customer ID"""
        sql = '''INSERT INTO customers(name, phone, email, address, city, pincode)
                 VALUES(?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, (self.name, self.phone, self.email, self.address, self.city, self.pincode))
        conn.commit()
        return cur.lastrowid

class Appliance:
    def __init__(self, customer_id: int, appliance_type: str, brand: str, model: str, 
                 purchase_date: str = None, warranty_status: bool = False):
        self.customer_id = customer_id
        self.type = appliance_type
        self.brand = brand
        self.model = model
        self.purchase_date = purchase_date
        self.warranty_status = warranty_status
    
    def save(self, conn: sqlite3.Connection) -> int:
        """Save appliance to database and return appliance ID"""
        sql = '''INSERT INTO appliances(customer_id, type, brand, model, purchase_date, warranty_status)
                 VALUES(?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, (self.customer_id, self.type, self.brand, self.model, 
                          self.purchase_date, self.warranty_status))
        conn.commit()
        return cur.lastrowid

class ServiceRequest:
    def __init__(self, appliance_id: int, issue_description: str, preferred_date: str, 
                 preferred_time: str, request_date: str = None):
        self.appliance_id = appliance_id
        self.issue_description = issue_description
        self.preferred_date = preferred_date
        self.preferred_time = preferred_time
        self.request_date = request_date or datetime.datetime.now().strftime("%Y-%m-%d")
    
    def save(self, conn: sqlite3.Connection) -> int:
        """Save service request to database and return request ID"""
        sql = '''INSERT INTO service_requests(appliance_id, issue_description, request_date, 
                 preferred_date, preferred_time)
                 VALUES(?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, (self.appliance_id, self.issue_description, self.request_date, 
                          self.preferred_date, self.preferred_time))
        conn.commit()
        return cur.lastrowid

class Technician:
    def __init__(self, name: str, phone: str, specialization: str, cities_served: List[str], email: str = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.specialization = specialization
        self.cities_served = ",".join(cities_served)
    
    def save(self, conn: sqlite3.Connection) -> int:
        """Save technician to database and return technician ID"""
        sql = '''INSERT INTO technicians(name, phone, email, specialization, cities_served)
                 VALUES(?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, (self.name, self.phone, self.email, self.specialization, self.cities_served))
        conn.commit()
        return cur.lastrowid

# Service functions
def get_available_technicians(conn: sqlite3.Connection, city: str, appliance_type: str, 
                             service_date: str) -> List[Dict]:
    """Get available technicians for a given city, appliance type and date"""
    try:
        cur = conn.cursor()
        
        # Check if service_date is a valid date
        try:
            datetime.datetime.strptime(service_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")
        
        # Get technicians who serve the city and specialize in the appliance type
        query = '''SELECT id, name, phone, specialization 
                   FROM technicians 
                   WHERE cities_served LIKE ? 
                   AND (specialization = ? OR specialization = 'General')'''
        cur.execute(query, (f'%{city}%', appliance_type))
        technicians = cur.fetchall()
        
        # Filter technicians who have less than 5 appointments on the given date
        available_techs = []
        for tech in technicians:
            tech_id = tech[0]
            query = '''SELECT COUNT(*) 
                       FROM service_requests 
                       WHERE technician_id = ? 
                       AND preferred_date = ? 
                       AND status != 'Cancelled''''
            cur.execute(query, (tech_id, service_date))
            count = cur.fetchone()[0]
            if count < 5:  # Max 5 appointments per day per technician
                available_techs.append({
                    'id': tech_id,
                    'name': tech[1],
                    'phone': tech[2],
                    'specialization': tech[3]
                })
        
        return available_techs
    except Error as e:
        print(e)
        return []

def schedule_service(conn: sqlite3.Connection, request_id: int, technician_id: int) -> bool:
    """Assign a technician to a service request"""
    try:
        cur = conn.cursor()
        sql = '''UPDATE service_requests 
                 SET status = 'Assigned', technician_id = ? 
                 WHERE id = ?'''
        cur.execute(sql, (technician_id, request_id))
        conn.commit()
        return cur.rowcount > 0
    except Error as e:
        print(e)
        return False

def get_service_requests_by_city(conn: sqlite3.Connection, city: str) -> List[Dict]:
    """Get all service requests for a specific city"""
    try:
        cur = conn.cursor()
        query = '''SELECT sr.id, c.name, c.phone, a.type, a.brand, sr.issue_description, 
                          sr.preferred_date, sr.preferred_time, sr.status
                   FROM service_requests sr
                   JOIN appliances a ON sr.appliance_id = a.id
                   JOIN customers c ON a.customer_id = c.id
                   WHERE c.city = ?'''
        cur.execute(query, (city,))
        rows = cur.fetchall()
        
        requests = []
        for row in rows:
            requests.append({
                'request_id': row[0],
                'customer_name': row[1],
                'customer_phone': row[2],
