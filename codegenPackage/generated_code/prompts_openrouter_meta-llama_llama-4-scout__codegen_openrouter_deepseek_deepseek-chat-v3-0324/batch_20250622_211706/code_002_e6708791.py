"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: "Generate a sample database schema for storing client information, horse details, and appointment schedules for an equine care provider like Martin Godwin."
Generated: DETERMINISTIC_e670879136b35fd7
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Equine Care Provider Database

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT CHECK(email LIKE '%_@__%.__%'),
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(email)
);

-- Horses table to store horse details
CREATE TABLE horses (
    horse_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    breed TEXT,
    color TEXT,
    birth_year INTEGER,
    gender TEXT CHECK(gender IN ('Stallion', 'Mare', 'Gelding')),
    registration_number TEXT,
    health_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Services table to store available services
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT 1
);

-- Staff table to store employee information
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT CHECK(email LIKE '%_@__%.__%'),
    phone TEXT NOT NULL,
    role TEXT NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(email)
);

-- Appointments table to schedule horse care
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    horse_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT CHECK(status IN ('Scheduled', 'Completed', 'Cancelled')) DEFAULT 'Scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (horse_id) REFERENCES horses(horse_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    UNIQUE(horse_id, appointment_date, start_time)
);

-- Payments table to track financial transactions
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    appointment_id INTEGER,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT CHECK(payment_method IN ('Cash', 'Check', 'Credit Card', 'Bank Transfer')),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('Pending', 'Completed', 'Failed', 'Refunded')) DEFAULT 'Completed',
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
);

-- Create indexes for performance optimization
CREATE INDEX idx_horses_client ON horses(client_id);
CREATE INDEX idx_appointments_horse ON appointments(horse_id);
CREATE INDEX idx_appointments_staff ON appointments(staff_id);
CREATE INDEX idx_appointments_date ON appointments(appointment_date);
CREATE INDEX idx_payments_client ON payments(client_id);
CREATE INDEX idx_payments_appointment ON payments(appointment_id);

-- Trigger to update timestamp on record updates
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_horse_timestamp
AFTER UPDATE ON horses
BEGIN
    UPDATE horses SET updated_at = CURRENT_TIMESTAMP WHERE horse_id = OLD.horse_id;
END;

CREATE TRIGGER update_appointment_timestamp
AFTER UPDATE ON appointments
BEGIN
    UPDATE appointments SET updated_at = CURRENT_TIMESTAMP WHERE appointment_id = OLD.appointment_id;
END;
```
