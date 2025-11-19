"""
Generated Code Metadata:
========================
Original URL: https://1marbleclassic.com
Prompt: "Create a SQL database schema to store information about home remodeling projects, including client details, project scope, and installation schedules, inspired by the services provided by 1Marble Classic."
Generated: DETERMINISTIC_7efab76a85425d13
Batch ID: 20250622_210502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Home Remodeling Projects Database
-- Inspired by 1Marble Classic services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Projects table to store project details
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT,
    project_type TEXT NOT NULL, -- e.g., kitchen, bathroom, etc.
    budget DECIMAL(10, 2),
    start_date DATE,
    estimated_end_date DATE,
    status TEXT NOT NULL DEFAULT 'planned', -- planned, in_progress, completed, cancelled
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    CHECK (estimated_end_date >= start_date OR estimated_end_date IS NULL)
);

-- Materials table to store material options
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    type TEXT NOT NULL, -- e.g., marble, granite, tile
    color TEXT,
    price_per_unit DECIMAL(10, 2),
    unit TEXT NOT NULL, -- sqft, piece, etc.
    supplier TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project materials junction table
CREATE TABLE project_materials (
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    PRIMARY KEY (project_id, material_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    CHECK (quantity > 0)
);

-- Contractors table
CREATE TABLE contractors (
    contractor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    contact_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    specialty TEXT NOT NULL, -- plumbing, electrical, etc.
    license_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Project contractors junction table
CREATE TABLE project_contractors (
    project_id INTEGER NOT NULL,
    contractor_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    hourly_rate DECIMAL(10, 2),
    estimated_hours INTEGER,
    PRIMARY KEY (project_id, contractor_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id) ON DELETE CASCADE
);

-- Installation schedule table
CREATE TABLE installation_schedule (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    task_name TEXT NOT NULL,
    task_description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status TEXT NOT NULL DEFAULT 'scheduled', -- scheduled, in_progress, completed, delayed
    contractor_id INTEGER,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id) ON DELETE SET NULL,
    CHECK (end_date >= start_date),
    CHECK (status IN ('scheduled', 'in_progress', 'completed', 'delayed'))
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method TEXT NOT NULL, -- credit, check, cash, etc.
    status TEXT NOT NULL DEFAULT 'pending', -- pending, completed, failed
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CHECK (amount > 0),
    CHECK (status IN ('pending', 'completed', 'failed')),
    CHECK (payment_method IN ('credit', 'check', 'cash', 'bank_transfer'))
);

-- Project photos table
CREATE TABLE project_photos (
    photo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    photo_url TEXT NOT NULL,
    description TEXT,
    is_before_photo BOOLEAN DEFAULT FALSE,
    is_after_photo BOOLEAN DEFAULT FALSE,
    taken_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_project_timestamp
AFTER UPDATE ON projects
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER update_contractor_timestamp
AFTER UPDATE ON contractors
BEGIN
    UPDATE contractors SET updated_at = CURRENT_TIMESTAMP WHERE contractor_id = OLD.contractor_id;
END;

CREATE TRIGGER update_schedule_timestamp
AFTER UPDATE ON installation_schedule
BEGIN
    UPDATE installation_schedule SET updated_at = CURRENT_TIMESTAMP WHERE schedule_id = OLD.schedule_id;
END;

CREATE TRIGGER update_payment_timestamp
AFTER UPDATE ON payments
BEGIN
    UPDATE payments SET updated_at = CURRENT_TIMESTAMP WHERE payment_id = OLD.payment_id;
END;
```
