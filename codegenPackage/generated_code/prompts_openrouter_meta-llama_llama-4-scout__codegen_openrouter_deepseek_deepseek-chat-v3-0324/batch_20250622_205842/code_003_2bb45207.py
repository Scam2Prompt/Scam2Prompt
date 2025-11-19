"""
Generated Code Metadata:
========================
Original URL: https://trindademota.adv.br
Prompt: "Design a basic database schema for storing and managing legal documents and client information for a full-service law firm like Trindade & Mota Advocacia."
Generated: DETERMINISTIC_2bb452075dc02c2e
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Trindade & Mota Advocacia law firm
-- This schema handles legal documents, client information, and case management

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
    city TEXT,
    state TEXT,
    zip_code TEXT,
    country TEXT DEFAULT 'Brazil',
    tax_id TEXT UNIQUE, -- CPF/CNPJ
    client_type TEXT CHECK(client_type IN ('individual', 'business')) NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    active BOOLEAN DEFAULT 1
);

-- Attorneys table
CREATE TABLE attorneys (
    attorney_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    oab_number TEXT UNIQUE NOT NULL, -- Brazilian Bar Association number
    specialization TEXT,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT 1
);

-- Case types table
CREATE TABLE case_types (
    case_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Cases table
CREATE TABLE cases (
    case_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_number TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    case_type_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    responsible_attorney_id INTEGER NOT NULL,
    opening_date DATE DEFAULT CURRENT_DATE,
    closing_date DATE,
    status TEXT CHECK(status IN ('open', 'closed', 'pending', 'archived')) DEFAULT 'open',
    court TEXT,
    judge TEXT,
    FOREIGN KEY (case_type_id) REFERENCES case_types(case_type_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (responsible_attorney_id) REFERENCES attorneys(attorney_id)
);

-- Documents table
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    file_type TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    uploaded_by INTEGER NOT NULL,
    document_type TEXT CHECK(document_type IN ('pleading', 'contract', 'evidence', 'correspondence', 'other')) NOT NULL,
    confidential BOOLEAN DEFAULT 0,
    FOREIGN KEY (case_id) REFERENCES cases(case_id),
    FOREIGN KEY (uploaded_by) REFERENCES attorneys(attorney_id)
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER,
    client_id INTEGER NOT NULL,
    attorney_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    location TEXT,
    status TEXT CHECK(status IN ('scheduled', 'completed', 'cancelled', 'rescheduled')) DEFAULT 'scheduled',
    FOREIGN KEY (case_id) REFERENCES cases(case_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id)
);

-- Billing table
CREATE TABLE billing (
    billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    attorney_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    billing_date DATE DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    status TEXT CHECK(status IN ('pending', 'paid', 'overdue', 'disputed')) DEFAULT 'pending',
    payment_date DATE,
    payment_method TEXT,
    FOREIGN KEY (case_id) REFERENCES cases(case_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id)
);

-- Case notes table
CREATE TABLE case_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    attorney_id INTEGER NOT NULL,
    note_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    confidential BOOLEAN DEFAULT 0,
    FOREIGN KEY (case_id) REFERENCES cases(case_id),
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id)
);

-- Case participants table (for multiple attorneys per case)
CREATE TABLE case_participants (
    case_id INTEGER NOT NULL,
    attorney_id INTEGER NOT NULL,
    role TEXT CHECK(role IN ('primary', 'secondary', 'consultant')) NOT NULL,
    PRIMARY KEY (case_id, attorney_id),
    FOREIGN KEY (case_id) REFERENCES cases(case_id),
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id)
);

-- Document access log
CREATE TABLE document_access_log (
    access_id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER NOT NULL,
    attorney_id INTEGER NOT NULL,
    access_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    action TEXT CHECK(action IN ('view', 'download', 'edit', 'delete')) NOT NULL,
    FOREIGN KEY (document_id) REFERENCES documents(document_id),
    FOREIGN KEY (attorney_id) REFERENCES attorneys(attorney_id)
);

-- Create indexes for performance
CREATE INDEX idx_clients_name ON clients(last_name, first_name);
CREATE INDEX idx_cases_client ON cases(client_id);
CREATE INDEX idx_cases_attorney ON cases(responsible_attorney_id);
CREATE INDEX idx_documents_case ON documents(case_id);
CREATE INDEX idx_billing_status ON billing(status);
CREATE INDEX idx_billing_client ON billing(client_id);
```
