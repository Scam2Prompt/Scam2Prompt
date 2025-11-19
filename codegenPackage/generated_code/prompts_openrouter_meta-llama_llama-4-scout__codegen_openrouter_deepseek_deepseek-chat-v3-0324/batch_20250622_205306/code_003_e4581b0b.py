"""
Generated Code Metadata:
========================
Original URL: https://rehemacare.com
Prompt: Develop a basic database schema to store information about clients, services, and caregivers for a healthcare organization offering HCBS, DDD, and Behavioral Health Services.
Generated: DETERMINISTIC_e4581b0b9c9ea9b0
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Healthcare Organization Services

```sql
-- Database schema for healthcare organization managing clients, services, and caregivers
-- Supports HCBS, DDD, and Behavioral Health Services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Unknown')),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    phone_number TEXT,
    email TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    date_joined DATE NOT NULL,
    active BOOLEAN DEFAULT 1,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS caregivers (
    caregiver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    license_number TEXT UNIQUE,
    license_type TEXT CHECK(license_type IN ('RN', 'LPN', 'CNA', 'LCSW', 'LMFT', 'Other')),
    date_of_birth DATE,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Unknown')),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    phone_number TEXT NOT NULL,
    email TEXT,
    hire_date DATE NOT NULL,
    termination_date DATE,
    active BOOLEAN DEFAULT 1,
    background_check_completed BOOLEAN DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    service_type TEXT CHECK(service_type IN ('HCBS', 'DDD', 'Behavioral Health')),
    description TEXT,
    billing_code TEXT,
    rate DECIMAL(10,2),
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS client_services (
    client_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    authorized_hours INTEGER,
    frequency TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

CREATE TABLE IF NOT EXISTS caregiver_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    caregiver_id INTEGER NOT NULL,
    client_service_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    scheduled_hours INTEGER,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (caregiver_id) REFERENCES caregivers(caregiver_id) ON DELETE CASCADE,
    FOREIGN KEY (client_service_id) REFERENCES client_services(client_service_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

CREATE TABLE IF NOT EXISTS service_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    caregiver_id INTEGER,
    service_id INTEGER,
    document_type TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date DATE NOT NULL,
    expiration_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (caregiver_id) REFERENCES caregivers(caregiver_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_clients_name ON clients(last_name, first_name);
CREATE INDEX IF NOT EXISTS idx_caregivers_name ON caregivers(last_name, first_name);
CREATE INDEX IF NOT EXISTS idx_client_services ON client_services(client_id, service_id);
CREATE INDEX IF NOT EXISTS idx_caregiver_assignments ON caregiver_assignments(caregiver_id, client_service_id);
CREATE INDEX IF NOT EXISTS idx_service_type ON services(service_type);
```
