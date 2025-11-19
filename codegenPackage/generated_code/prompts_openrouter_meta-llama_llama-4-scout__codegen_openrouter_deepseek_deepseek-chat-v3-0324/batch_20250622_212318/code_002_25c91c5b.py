"""
Generated Code Metadata:
========================
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: "Generate a sample database schema to store information about therapy sessions, including treatment types, therapist schedules, and client bookings, inspired by the services provided by Equilibri-Bio."
Generated: DETERMINISTIC_25c91c5b37dc72eb
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Equilibri-Bio therapy management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables for therapy types
CREATE TABLE IF NOT EXISTS therapy_types (
    therapy_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (duration_minutes > 0),
    CHECK (base_price >= 0)
);

-- Create tables for therapists
CREATE TABLE IF NOT EXISTS therapists (
    therapist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    specialization TEXT,
    bio TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Junction table for therapist-therapy type relationships
CREATE TABLE IF NOT EXISTS therapist_therapy_types (
    therapist_id INTEGER NOT NULL,
    therapy_type_id INTEGER NOT NULL,
    PRIMARY KEY (therapist_id, therapy_type_id),
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE,
    FOREIGN KEY (therapy_type_id) REFERENCES therapy_types(therapy_type_id) ON DELETE CASCADE
);

-- Create tables for clients
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    date_of_birth DATE,
    medical_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Create tables for therapist availability
CREATE TABLE IF NOT EXISTS therapist_availability (
    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
    therapist_id INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL, -- 0=Sunday, 1=Monday, etc.
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_recurring BOOLEAN DEFAULT TRUE,
    valid_from DATE DEFAULT CURRENT_DATE,
    valid_to DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE,
    CHECK (day_of_week BETWEEN 0 AND 6),
    CHECK (end_time > start_time),
    CHECK (valid_to IS NULL OR valid_to >= valid_from)
);

-- Create tables for therapy sessions
CREATE TABLE IF NOT EXISTS therapy_sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    therapist_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    therapy_type_id INTEGER NOT NULL,
    scheduled_start TIMESTAMP NOT NULL,
    scheduled_end TIMESTAMP NOT NULL,
    status TEXT DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'completed', 'cancelled', 'no-show')),
    notes TEXT,
    price DECIMAL(10, 2) NOT NULL,
    payment_status TEXT DEFAULT 'pending' CHECK (payment_status IN ('pending', 'paid', 'refunded', 'partial')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (therapy_type_id) REFERENCES therapy_types(therapy_type_id),
    CHECK (scheduled_end > scheduled_start),
    CHECK (price >= 0)
);

-- Create tables for session notes
CREATE TABLE IF NOT EXISTS session_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    note_type TEXT CHECK (note_type IN ('progress', 'observation', 'recommendation')),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES therapy_sessions(session_id) ON DELETE CASCADE
);

-- Create tables for payments
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT CHECK (payment_method IN ('cash', 'card', 'insurance', 'bank_transfer')),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'completed' CHECK (status IN ('completed', 'pending', 'failed', 'refunded')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES therapy_sessions(session_id),
    CHECK (amount > 0)
);

-- Create index for performance optimization
CREATE INDEX IF NOT EXISTS idx_therapy_sessions_therapist ON therapy_sessions(therapist_id);
CREATE INDEX IF NOT EXISTS idx_therapy_sessions_client ON therapy_sessions(client_id);
CREATE INDEX IF NOT EXISTS idx_therapy_sessions_date ON therapy_sessions(scheduled_start);
CREATE INDEX IF NOT EXISTS idx_therapist_availability ON therapist_availability(therapist_id, day_of_week);
```
