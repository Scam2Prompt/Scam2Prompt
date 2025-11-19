"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: "Design a simple database schema for storing client information, audit reports, and tax consultancy services provided by a firm like Experts Consulting Group."
Generated: DETERMINISTIC_e2f6fb97db180150
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Experts Consulting Group

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
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
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('active', 'inactive', 'prospect')) DEFAULT 'prospect',
    notes TEXT
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    duration_days INTEGER NOT NULL
);

-- Consultants table
CREATE TABLE consultants (
    consultant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    specialization TEXT NOT NULL,
    hire_date DATE NOT NULL,
    status TEXT CHECK(status IN ('active', 'inactive', 'on_leave')) DEFAULT 'active'
);

-- Client services (many-to-many relationship)
CREATE TABLE client_services (
    client_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    consultant_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    actual_price DECIMAL(10, 2) NOT NULL,
    status TEXT CHECK(status IN ('pending', 'in_progress', 'completed', 'cancelled')) DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (consultant_id) REFERENCES consultants(consultant_id) ON DELETE CASCADE,
    UNIQUE(client_id, service_id, consultant_id, start_date)
);

-- Audit reports table
CREATE TABLE audit_reports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    consultant_id INTEGER NOT NULL,
    report_date DATE NOT NULL,
    report_type TEXT NOT NULL,
    findings TEXT NOT NULL,
    recommendations TEXT NOT NULL,
    status TEXT CHECK(status IN ('draft', 'finalized', 'delivered')) DEFAULT 'draft',
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (consultant_id) REFERENCES consultants(consultant_id) ON DELETE CASCADE
);

-- Tax filings table
CREATE TABLE tax_filings (
    filing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    consultant_id INTEGER NOT NULL,
    tax_year INTEGER NOT NULL,
    filing_type TEXT NOT NULL,
    submission_date DATE,
    status TEXT CHECK(status IN ('preparation', 'review', 'filed', 'rejected', 'accepted')) DEFAULT 'preparation',
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (consultant_id) REFERENCES consultants(consultant_id) ON DELETE CASCADE,
    UNIQUE(client_id, tax_year, filing_type)
);

-- Documents table (for storing various documents)
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    consultant_id INTEGER,
    document_type TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (consultant_id) REFERENCES consultants(consultant_id) ON DELETE SET NULL
);

-- Indexes for performance optimization
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_client_services_status ON client_services(status);
CREATE INDEX idx_audit_reports_client ON audit_reports(client_id);
CREATE INDEX idx_tax_filings_client_year ON tax_filings(client_id, tax_year);
```
