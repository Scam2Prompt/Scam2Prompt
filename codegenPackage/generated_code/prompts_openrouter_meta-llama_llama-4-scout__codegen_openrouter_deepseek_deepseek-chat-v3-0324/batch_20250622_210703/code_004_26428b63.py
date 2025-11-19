"""
Generated Code Metadata:
========================
Original URL: https://healthcareventure.nl
Prompt: Develop a simple database schema to store information about clients, employees, and services provided by a youth mental healthcare company, considering the need for superior client-focused care.
Generated: DETERMINISTIC_26428b63e4d0423d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for youth mental healthcare company
-- Tables for clients, employees, services, and appointments

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Non-binary', 'Other', 'Prefer not to say')),
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    emergency_contact_name TEXT NOT NULL,
    emergency_contact_phone TEXT NOT NULL,
    insurance_provider TEXT,
    insurance_policy_number TEXT,
    registration_date DATE DEFAULT CURRENT_DATE,
    notes TEXT,
    active BOOLEAN DEFAULT TRUE,
    CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Employees table
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Therapist', 'Psychiatrist', 'Counselor', 'Case Manager', 'Administrator')),
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    license_number TEXT,
    specialization TEXT,
    hire_date DATE DEFAULT CURRENT_DATE,
    active BOOLEAN DEFAULT TRUE,
    CHECK (email LIKE '%@%.%')
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    active BOOLEAN DEFAULT TRUE
);

-- Employee-service junction table (many-to-many relationship)
CREATE TABLE employee_services (
    employee_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (employee_id, service_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT NOT NULL DEFAULT 'Scheduled' CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    CHECK (end_time > start_time)
);

-- Client progress notes table
CREATE TABLE progress_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    appointment_id INTEGER,
    note_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
);

-- Create indexes for performance
CREATE INDEX idx_appointments_client ON appointments(client_id);
CREATE INDEX idx_appointments_employee ON appointments(employee_id);
CREATE INDEX idx_appointments_date ON appointments(appointment_date);
CREATE INDEX idx_progress_notes_client ON progress_notes(client_id);
```
