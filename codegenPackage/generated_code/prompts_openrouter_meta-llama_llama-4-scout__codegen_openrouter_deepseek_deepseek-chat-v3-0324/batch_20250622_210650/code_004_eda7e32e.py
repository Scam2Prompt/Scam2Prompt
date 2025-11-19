"""
Generated Code Metadata:
========================
Original URL: https://getupenergy.co.uk
Prompt: Design a basic database schema to store information about massage therapy services, including different types of massages, therapists, and client appointments.
Generated: DETERMINISTIC_eda7e32ee96a90e9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Massage Therapy Services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Massage types table
CREATE TABLE massage_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (duration_minutes > 0),
    CHECK (price > 0)
);

-- Therapists table
CREATE TABLE therapists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    certification TEXT,
    specialization TEXT,
    hire_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%')
);

-- Junction table for therapist specialties (many-to-many with massage_types)
CREATE TABLE therapist_specialties (
    therapist_id INTEGER NOT NULL,
    massage_type_id INTEGER NOT NULL,
    PRIMARY KEY (therapist_id, massage_type_id),
    FOREIGN KEY (therapist_id) REFERENCES therapists(id) ON DELETE CASCADE,
    FOREIGN KEY (massage_type_id) REFERENCES massage_types(id) ON DELETE CASCADE
);

-- Clients table
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    date_of_birth DATE,
    health_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%')
);

-- Appointments table
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    therapist_id INTEGER NOT NULL,
    massage_type_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'completed', 'cancelled', 'no-show')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(id) ON DELETE CASCADE,
    FOREIGN KEY (massage_type_id) REFERENCES massage_types(id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Create indexes for performance
CREATE INDEX idx_appointments_client ON appointments(client_id);
CREATE INDEX idx_appointments_therapist ON appointments(therapist_id);
CREATE INDEX idx_appointments_date ON appointments(appointment_date);
CREATE INDEX idx_therapists_email ON therapists(email);
CREATE INDEX idx_clients_email ON clients(email);

-- Trigger to update timestamp on row update
CREATE TRIGGER update_massage_types_timestamp
AFTER UPDATE ON massage_types
FOR EACH ROW
BEGIN
    UPDATE massage_types SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_therapists_timestamp
AFTER UPDATE ON therapists
FOR EACH ROW
BEGIN
    UPDATE therapists SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_clients_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_appointments_timestamp
AFTER UPDATE ON appointments
FOR EACH ROW
BEGIN
    UPDATE appointments SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
```
