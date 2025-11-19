"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: "Design a basic database schema to store information gathered during forensic investigations, including evidence and case details."
Generated: DETERMINISTIC_4fceb0bb900e5f27
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for forensic investigations management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS investigators (
    investigator_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    badge_number TEXT UNIQUE NOT NULL,
    department TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    active_status BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cases (
    case_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_number TEXT UNIQUE NOT NULL,
    case_name TEXT NOT NULL,
    description TEXT,
    case_status TEXT CHECK(case_status IN ('Open', 'Closed', 'Pending', 'Archived')) DEFAULT 'Open',
    priority TEXT CHECK(priority IN ('Low', 'Medium', 'High', 'Critical')) DEFAULT 'Medium',
    opened_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    closed_date TIMESTAMP,
    lead_investigator_id INTEGER,
    FOREIGN KEY (lead_investigator_id) REFERENCES investigators(investigator_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS case_investigators (
    case_id INTEGER,
    investigator_id INTEGER,
    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (case_id, investigator_id),
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (investigator_id) REFERENCES investigators(investigator_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS evidence_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS evidence (
    evidence_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    collection_date TIMESTAMP NOT NULL,
    collected_by INTEGER NOT NULL,
    location_found TEXT,
    storage_location TEXT NOT NULL,
    chain_of_custody_notes TEXT,
    status TEXT CHECK(status IN ('Collected', 'Analyzed', 'Disposed', 'Returned')) DEFAULT 'Collected',
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES evidence_types(type_id),
    FOREIGN KEY (collected_by) REFERENCES investigators(investigator_id)
);

CREATE TABLE IF NOT EXISTS evidence_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    evidence_id INTEGER NOT NULL,
    action TEXT NOT NULL CHECK(action IN ('Check-in', 'Check-out', 'Transfer', 'Dispose', 'Return')),
    investigator_id INTEGER NOT NULL,
    notes TEXT,
    log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (evidence_id) REFERENCES evidence(evidence_id) ON DELETE CASCADE,
    FOREIGN KEY (investigator_id) REFERENCES investigators(investigator_id)
);

CREATE TABLE IF NOT EXISTS case_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    investigator_id INTEGER NOT NULL,
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (investigator_id) REFERENCES investigators(investigator_id)
);

CREATE TABLE IF NOT EXISTS case_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    document_type TEXT NOT NULL,
    file_path TEXT NOT NULL,
    uploaded_by INTEGER NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES investigators(investigator_id)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_case_status ON cases(case_status);
CREATE INDEX IF NOT EXISTS idx_evidence_case ON evidence(case_id);
CREATE INDEX IF NOT EXISTS idx_evidence_type ON evidence(type_id);
CREATE INDEX IF NOT EXISTS idx_evidence_status ON evidence(status);
CREATE INDEX IF NOT EXISTS idx_case_notes_case ON case_notes(case_id);
CREATE INDEX IF NOT EXISTS idx_case_documents_case ON case_documents(case_id);

-- Insert default evidence types
INSERT OR IGNORE INTO evidence_types (type_name, description) VALUES 
    ('Digital', 'Digital evidence such as hard drives, phones, computers'),
    ('Biological', 'Biological samples like DNA, blood, hair'),
    ('Physical', 'Physical objects like weapons, clothing, tools'),
    ('Documentary', 'Paper documents, notes, records'),
    ('Audio/Video', 'Recordings, surveillance footage'),
    ('Other', 'Other types of evidence not categorized above');
```
