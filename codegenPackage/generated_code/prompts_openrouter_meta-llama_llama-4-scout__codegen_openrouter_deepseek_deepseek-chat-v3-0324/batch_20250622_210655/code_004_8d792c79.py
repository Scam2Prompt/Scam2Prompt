"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Based on the information provided about Pérez Bernalte Abogados' services in criminal law, civil law, and administrative law, create a simple database schema to organize client cases by legal area.
Generated: DETERMINISTIC_8d792c79b601b30d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Pérez Bernalte Abogados case management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Legal areas table
CREATE TABLE legal_areas (
    area_id INTEGER PRIMARY KEY AUTOINCREMENT,
    area_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Insert predefined legal areas
INSERT INTO legal_areas (area_name, description) VALUES 
    ('Criminal Law', 'Cases related to criminal offenses and defenses'),
    ('Civil Law', 'Cases involving private disputes between individuals or organizations'),
    ('Administrative Law', 'Cases concerning government agencies and public administration');

-- Cases table
CREATE TABLE cases (
    case_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    case_title TEXT NOT NULL,
    case_description TEXT,
    case_status TEXT DEFAULT 'Open' CHECK (case_status IN ('Open', 'In Progress', 'Closed', 'Archived')),
    opened_date DATE DEFAULT CURRENT_DATE,
    closed_date DATE,
    priority TEXT CHECK (priority IN ('Low', 'Medium', 'High', 'Urgent')),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (area_id) REFERENCES legal_areas(area_id),
    CHECK (closed_date IS NULL OR closed_date >= opened_date)
);

-- Documents table
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    document_type TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    appointment_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER DEFAULT 60 CHECK (duration_minutes > 0),
    notes TEXT,
    status TEXT DEFAULT 'Scheduled' CHECK (status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    CHECK (appointment_date > CURRENT_TIMESTAMP)
);

-- Trigger to update timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

-- Indexes for performance
CREATE INDEX idx_cases_client ON cases(client_id);
CREATE INDEX idx_cases_area ON cases(area_id);
CREATE INDEX idx_documents_case ON documents(case_id);
CREATE INDEX idx_appointments_case ON appointments(case_id);
```
