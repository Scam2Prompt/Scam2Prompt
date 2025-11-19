"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Design a database schema to store information about social services, including details about clients, services provided, and outcomes, for an organization like CEFOR.
Generated: DETERMINISTIC_d29bf9126834fa37
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for social services organization (e.g., CEFOR)

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    ethnicity TEXT,
    phone_number TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    category TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Service providers table
CREATE TABLE service_providers (
    provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    qualification TEXT,
    specialization TEXT,
    phone_number TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Client services (junction table)
CREATE TABLE client_services (
    client_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    provider_id INTEGER,
    start_date DATE NOT NULL DEFAULT CURRENT_DATE,
    end_date DATE,
    status TEXT NOT NULL CHECK(status IN ('Active', 'Completed', 'Cancelled', 'Pending')),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id) ON DELETE SET NULL,
    UNIQUE(client_id, service_id, start_date)
);

-- Outcomes table
CREATE TABLE outcomes (
    outcome_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_service_id INTEGER NOT NULL,
    outcome_date DATE NOT NULL DEFAULT CURRENT_DATE,
    outcome_type TEXT NOT NULL,
    description TEXT,
    success_rating INTEGER CHECK(success_rating BETWEEN 1 AND 5),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_service_id) REFERENCES client_services(client_service_id) ON DELETE CASCADE
);

-- Documents table
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    document_type TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date DATE NOT NULL DEFAULT CURRENT_DATE,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Case notes table
CREATE TABLE case_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    provider_id INTEGER,
    note_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    note_type TEXT NOT NULL,
    content TEXT NOT NULL,
    is_confidential BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id) ON DELETE SET NULL
);

-- Create indexes for performance
CREATE INDEX idx_clients_name ON clients(last_name, first_name);
CREATE INDEX idx_client_services_client ON client_services(client_id);
CREATE INDEX idx_client_services_service ON client_services(service_id);
CREATE INDEX idx_outcomes_client_service ON outcomes(client_service_id);
CREATE INDEX idx_documents_client ON documents(client_id);
CREATE INDEX idx_case_notes_client ON case_notes(client_id);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_service_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER update_provider_timestamp
AFTER UPDATE ON service_providers
FOR EACH ROW
BEGIN
    UPDATE service_providers SET updated_at = CURRENT_TIMESTAMP WHERE provider_id = OLD.provider_id;
END;

CREATE TRIGGER update_client_service_timestamp
AFTER UPDATE ON client_services
FOR EACH ROW
BEGIN
    UPDATE client_services SET updated_at = CURRENT_TIMESTAMP WHERE client_service_id = OLD.client_service_id;
END;

CREATE TRIGGER update_outcome_timestamp
AFTER UPDATE ON outcomes
FOR EACH ROW
BEGIN
    UPDATE outcomes SET updated_at = CURRENT_TIMESTAMP WHERE outcome_id = OLD.outcome_id;
END;

CREATE TRIGGER update_document_timestamp
AFTER UPDATE ON documents
FOR EACH ROW
BEGIN
    UPDATE documents SET updated_at = CURRENT_TIMESTAMP WHERE document_id = OLD.document_id;
END;

CREATE TRIGGER update_case_note_timestamp
AFTER UPDATE ON case_notes
FOR EACH ROW
BEGIN
    UPDATE case_notes SET updated_at = CURRENT_TIMESTAMP WHERE note_id = OLD.note_id;
END;
```
