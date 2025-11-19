"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Generate a sample database schema for storing client information, counseling sessions, and therapist details for a counseling service like Dr. Rahileh Sadeghi's.
Generated: DETERMINISTIC_b5bb17b57354c0bd
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for counseling service management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    active BOOLEAN DEFAULT 1,
    CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Therapists table
CREATE TABLE therapists (
    therapist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    license_number TEXT UNIQUE NOT NULL,
    specialization TEXT,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT 1,
    CHECK (email LIKE '%@%.%')
);

-- Session types table
CREATE TABLE session_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    standard_fee DECIMAL(10,2) NOT NULL
);

-- Sessions table
CREATE TABLE sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    therapist_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    notes TEXT,
    status TEXT DEFAULT 'Scheduled' CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    fee DECIMAL(10,2) NOT NULL,
    payment_status TEXT DEFAULT 'Unpaid' CHECK(payment_status IN ('Paid', 'Unpaid', 'Partial')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES session_types(type_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT CHECK(payment_method IN ('Cash', 'Credit Card', 'Debit Card', 'Check', 'Bank Transfer', 'Other')),
    transaction_reference TEXT,
    notes TEXT,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
);

-- Client medical history table
CREATE TABLE client_medical_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    condition_name TEXT NOT NULL,
    diagnosis_date DATE,
    current_status TEXT,
    treatment TEXT,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Client insurance information
CREATE TABLE client_insurance (
    insurance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    provider_name TEXT NOT NULL,
    policy_number TEXT NOT NULL,
    group_number TEXT,
    coverage_start_date DATE NOT NULL,
    coverage_end_date DATE,
    copay_amount DECIMAL(10,2),
    deductible DECIMAL(10,2),
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (coverage_end_date IS NULL OR coverage_end_date > coverage_start_date)
);

-- Therapist availability
CREATE TABLE therapist_availability (
    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
    therapist_id INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL CHECK(day_of_week BETWEEN 0 AND 6), -- 0=Sunday, 6=Saturday
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Create indexes for performance
CREATE INDEX idx_client_name ON clients(last_name, first_name);
CREATE INDEX idx_therapist_name ON therapists(last_name, first_name);
CREATE INDEX idx_session_date ON sessions(session_date);
CREATE INDEX idx_session_client ON sessions(client_id);
CREATE INDEX idx_session_therapist ON sessions(therapist_id);
CREATE INDEX idx_payment_session ON payments(session_id);
```
