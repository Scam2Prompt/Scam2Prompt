"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Design a database schema for storing information about legal consultations and cases, inspired by the practices of Fachri Ahyani as an advocate.
Generated: DETERMINISTIC_26a6c5000aaeab9b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for legal consultations and cases management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    date_of_birth DATE,
    id_number TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Case categories table
CREATE TABLE IF NOT EXISTS case_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Cases table
CREATE TABLE IF NOT EXISTS cases (
    case_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    case_number TEXT UNIQUE,
    filing_date DATE,
    status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'closed', 'pending', 'dismissed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES case_categories(category_id)
);

-- Consultations table
CREATE TABLE IF NOT EXISTS consultations (
    consultation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER,
    client_id INTEGER NOT NULL,
    consultation_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
    notes TEXT,
    fee DECIMAL(10, 2) CHECK (fee >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE SET NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Documents table
CREATE TABLE IF NOT EXISTS documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    file_path TEXT NOT NULL UNIQUE,
    document_type TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Court hearings table
CREATE TABLE IF NOT EXISTS court_hearings (
    hearing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    hearing_date TIMESTAMP NOT NULL,
    location TEXT NOT NULL,
    judge TEXT,
    outcome TEXT,
    notes TEXT,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Tasks table for case-related tasks
CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    due_date TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'overdue')),
    priority TEXT NOT NULL DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    case_id INTEGER,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL,
    description TEXT,
    receipt_number TEXT UNIQUE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE SET NULL
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER IF NOT EXISTS update_case_timestamp
AFTER UPDATE ON cases
FOR EACH ROW
BEGIN
    UPDATE cases SET updated_at = CURRENT_TIMESTAMP WHERE case_id = OLD.case_id;
END;

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_cases_client_id ON cases(client_id);
CREATE INDEX IF NOT EXISTS idx_cases_status ON cases(status);
CREATE INDEX IF NOT EXISTS idx_consultations_case_id ON consultations(case_id);
CREATE INDEX IF NOT EXISTS idx_consultations_client_id ON consultations(client_id);
CREATE INDEX IF NOT EXISTS idx_documents_case_id ON documents(case_id);
CREATE INDEX IF NOT EXISTS idx_hearings_case_id ON court_hearings(case_id);
CREATE INDEX IF NOT EXISTS idx_tasks_case_id ON tasks(case_id);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);
CREATE INDEX IF NOT EXISTS idx_payments_client_id ON payments(client_id);
CREATE INDEX IF NOT EXISTS idx_payments_case_id ON payments(case_id);
```
