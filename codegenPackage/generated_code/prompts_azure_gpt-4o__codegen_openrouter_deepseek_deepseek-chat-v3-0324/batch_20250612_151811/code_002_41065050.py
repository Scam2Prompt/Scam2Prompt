"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: Generate code to create a database schema for storing client information, service details (e.g., company creation, auditing), and deadlines, based on the offerings of Hub Experts.
Generated: DETERMINISTIC_410650504a9d6ec0
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Hub Experts client management system
-- This schema supports client information, service details, and deadline tracking

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table - stores basic client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    company_name TEXT,
    registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'prospect')),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Services table - catalog of available services
CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    estimated_duration_days INTEGER,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Client services table - tracks services assigned to clients
CREATE TABLE IF NOT EXISTS client_services (
    client_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'in_progress', 'completed', 'cancelled')),
    actual_price DECIMAL(10, 2),
    assigned_to TEXT,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE RESTRICT
);

-- Deadlines table - tracks important dates for client services
CREATE TABLE IF NOT EXISTS deadlines (
    deadline_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_service_id INTEGER NOT NULL,
    deadline_name TEXT NOT NULL,
    deadline_date DATE NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'met', 'missed', 'rescheduled')),
    notes TEXT,
    reminder_sent BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_service_id) REFERENCES client_services(client_service_id) ON DELETE CASCADE
);

-- Documents table - stores documents related to clients and services
CREATE TABLE IF NOT EXISTS documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    client_service_id INTEGER,
    document_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date DATE NOT NULL DEFAULT CURRENT_DATE,
    document_type TEXT,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (client_service_id) REFERENCES client_services(client_service_id) ON DELETE SET NULL
);

-- Audit log table - tracks important changes in the system
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT NOT NULL,
    record_id INTEGER NOT NULL,
    action TEXT NOT NULL CHECK (action IN ('create', 'update', 'delete')),
    old_values TEXT,
    new_values TEXT,
    changed_by TEXT NOT NULL,
    changed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Trigger to update the updated_at timestamp when client records are modified
CREATE TRIGGER IF NOT EXISTS update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

-- Trigger to update the updated_at timestamp when client services are modified
CREATE TRIGGER IF NOT EXISTS update_client_service_timestamp
AFTER UPDATE ON client_services
FOR EACH ROW
BEGIN
    UPDATE client_services SET updated_at = CURRENT_TIMESTAMP WHERE client_service_id = OLD.client_service_id;
END;

-- Trigger to update the updated_at timestamp when deadlines are modified
CREATE TRIGGER IF NOT EXISTS update_deadline_timestamp
AFTER UPDATE ON deadlines
FOR EACH ROW
BEGIN
    UPDATE deadlines SET updated_at = CURRENT_TIMESTAMP WHERE deadline_id = OLD.deadline_id;
END;

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_client_email ON clients(email);
CREATE INDEX IF NOT EXISTS idx_client_status ON clients(status);
CREATE INDEX IF NOT EXISTS idx_client_service_status ON client_services(status);
CREATE INDEX IF NOT EXISTS idx_deadline_date ON deadlines(deadline_date);
CREATE INDEX IF NOT EXISTS idx_deadline_status ON deadlines(status);
```
