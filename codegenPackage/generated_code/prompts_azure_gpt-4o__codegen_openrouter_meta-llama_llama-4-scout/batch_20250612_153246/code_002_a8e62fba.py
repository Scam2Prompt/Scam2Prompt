"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Generate a database schema for a diesel turbo repair shop to store customer information, diagnostic results, repair history, and WhatsApp communication logs.
Generated: DETERMINISTIC_a8e62fba09afdbcb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for diesel turbo repair shop
CREATE DATABASE diesel_turbo_repair;

-- Use the database
USE diesel_turbo_repair;

-- Create table for customers
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for diagnostic results
CREATE TABLE diagnostic_results (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  vehicle_make VARCHAR(50) NOT NULL,
  vehicle_model VARCHAR(50) NOT NULL,
  vehicle_year INT NOT NULL,
  diagnostic_date DATE NOT NULL,
  symptoms TEXT,
  findings TEXT,
  recommendations TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

-- Create table for repair history
CREATE TABLE repair_history (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  diagnostic_result_id INT,
  repair_date DATE NOT NULL,
  description TEXT NOT NULL,
  cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
  FOREIGN KEY (diagnostic_result_id) REFERENCES diagnostic_results(id) ON DELETE SET NULL
);

-- Create table for WhatsApp communication logs
CREATE TABLE whatsapp_communication_logs (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  message_type ENUM('sent', 'received') NOT NULL,
  message_text TEXT NOT NULL,
  message_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_diagnostic_results_customer_id ON diagnostic_results (customer_id);
CREATE INDEX idx_repair_history_customer_id ON repair_history (customer_id);
CREATE INDEX idx_repair_history_diagnostic_result_id ON repair_history (diagnostic_result_id);
CREATE INDEX idx_whatsapp_communication_logs_customer_id ON whatsapp_communication_logs (customer_id);
```

```python
# models.py

from sqlalchemy import create_engine, Column, Integer, String, Date, Text, DECIMAL, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://user:password@localhost/diesel_turbo_repair')
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=False)
    address = Column(String(255))
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))
    diagnostic_results = relationship('DiagnosticResult', backref='customer')
    repair_history = relationship('RepairHistory', backref='customer')
    whatsapp_communication_logs = relationship('WhatsAppCommunicationLog', backref='customer')

class DiagnosticResult(Base):
    __tablename__ = 'diagnostic_results'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    vehicle_make = Column(String(50), nullable=False)
    vehicle_model = Column(String(50), nullable=False)
    vehicle_year = Column(Integer, nullable=False)
    diagnostic_date = Column(Date, nullable=False)
    symptoms = Column(Text)
    findings = Column(Text)
    recommendations = Column(Text)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))
    repair_history = relationship('RepairHistory', backref='diagnostic_result')

class RepairHistory(Base):
    __tablename__ = 'repair_history'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    diagnostic_result_id = Column(Integer, ForeignKey('diagnostic_results.id'))
    repair_date = Column(Date, nullable=False)
    description = Column(Text, nullable=False)
    cost = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))

class WhatsAppCommunicationLog(Base):
    __tablename__ = 'whatsapp_communication_logs'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    message_type = Column(Enum('sent', 'received', name='message_type'), nullable=False)
    message_text = Column(Text, nullable=False)
    message_date = Column(TIMESTAMP, nullable=False, default=TIMESTAMP('now'))
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
```
