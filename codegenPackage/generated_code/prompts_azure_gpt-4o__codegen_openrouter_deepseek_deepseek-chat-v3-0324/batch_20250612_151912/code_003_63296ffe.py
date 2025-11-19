"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Create a database schema for managing client cases in a law firm specializing in family law and criminal law, including tables for client information, case details, and modes of resolution (e.g., mediation, judicial representation) inspired by Majeli Avocat's practices.
Generated: DETERMINISTIC_63296ffeaac75f95
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for law firm case management system
-- Supports family law and criminal law cases with various resolution modes

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    address TEXT,
    city TEXT,
    postal_code TEXT,
    country TEXT DEFAULT 'Canada',
    phone_number TEXT NOT NULL,
    email TEXT,
    id_type TEXT CHECK(id_type IN ('Passport', 'Driver License', 'Health Card', 'Other')),
    id_number TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cases table
CREATE TABLE cases (
    case_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    case_type TEXT NOT NULL CHECK(case_type IN ('Family', 'Criminal')),
    case_subtype TEXT,
    case_status TEXT NOT NULL CHECK(case_status IN ('Open', 'Closed', 'Pending', 'Archived')),
    description TEXT,
    opened_date DATE NOT NULL,
    closed_date DATE,
    court_name TEXT,
    court_location TEXT,
    judge_name TEXT,
    opposing_party TEXT,
    opposing_counsel TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Case documents table
CREATE TABLE case_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    document_type TEXT CHECK(document_type IN ('Contract', 'Court Filing', 'Evidence', 'Correspondence', 'Other')),
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Case resolutions table
CREATE TABLE case_resolutions (
    resolution_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    resolution_type TEXT NOT NULL CHECK(resolution_type IN ('Mediation', 'Settlement', 'Trial', 'Dismissal', 'Appeal', 'Other')),
    resolution_date DATE NOT NULL,
    outcome TEXT NOT NULL,
    details TEXT,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    appointment_type TEXT CHECK(appointment_type IN ('Consultation', 'Court Date', 'Mediation', 'Follow-up', 'Other')),
    appointment_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER DEFAULT 60,
    location TEXT,
    notes TEXT,
    status TEXT DEFAULT 'Scheduled' CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Billing table
CREATE TABLE billing (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) DEFAULT 0.00,
    payment_status TEXT DEFAULT 'Pending' CHECK(payment_status IN ('Pending', 'Paid', 'Partial', 'Overdue', 'Cancelled')),
    payment_date DATE,
    payment_method TEXT CHECK(payment_method IN ('Cash', 'Check', 'Credit Card', 'Bank Transfer', 'Other')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Case notes table
CREATE TABLE case_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    author TEXT NOT NULL,
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    note_text TEXT NOT NULL,
    is_private BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Triggers for automatic timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_case_timestamp
AFTER UPDATE ON cases
FOR EACH ROW
BEGIN
    UPDATE cases SET updated_at = CURRENT_TIMESTAMP WHERE case_id = OLD.case_id;
END;

CREATE TRIGGER update_appointment_timestamp
AFTER UPDATE ON appointments
FOR EACH ROW
BEGIN
    UPDATE appointments SET updated_at = CURRENT_TIMESTAMP WHERE appointment_id = OLD.appointment_id;
END;

CREATE TRIGGER update_billing_timestamp
AFTER UPDATE ON billing
FOR EACH ROW
BEGIN
    UPDATE billing SET updated_at = CURRENT_TIMESTAMP WHERE invoice_id = OLD.invoice_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_cases_client_id ON cases(client_id);
CREATE INDEX idx_cases_case_status ON cases(case_status);
CREATE INDEX idx_case_documents_case_id ON case_documents(case_id);
CREATE INDEX idx_case_resolutions_case_id ON case_resolutions(case_id);
CREATE INDEX idx_appointments_case_id ON appointments(case_id);
CREATE INDEX idx_appointments_client_id ON appointments(client_id);
CREATE INDEX idx_billing_case_id ON billing(case_id);
CREATE INDEX idx_billing_client_id ON billing(client_id);
CREATE INDEX idx_case_notes_case_id ON case_notes(case_id);
```
