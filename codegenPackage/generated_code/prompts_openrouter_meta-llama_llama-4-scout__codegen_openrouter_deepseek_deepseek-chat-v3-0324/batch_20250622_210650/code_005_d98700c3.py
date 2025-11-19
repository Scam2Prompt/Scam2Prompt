"""
Generated Code Metadata:
========================
Original URL: https://maraboutreconnu.com
Prompt: Design a database schema for storing client information, ritual or service details, and appointment schedules for a marabout service provider.
Generated: DETERMINISTIC_d98700c39bb310fd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Marabout Service Provider

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    country TEXT,
    postal_code TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Ritual/service types table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    status TEXT CHECK(status IN ('scheduled', 'completed', 'cancelled', 'no-show')) DEFAULT 'scheduled',
    price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT CHECK(payment_method IN ('cash', 'credit_card', 'bank_transfer', 'mobile_money')) NOT NULL,
    transaction_reference TEXT,
    status TEXT CHECK(status IN ('pending', 'completed', 'failed', 'refunded')) DEFAULT 'completed',
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE
);

-- Client notes/history table
CREATE TABLE client_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    note TEXT NOT NULL,
    created_by TEXT DEFAULT 'system',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_service_timestamp
AFTER UPDATE ON services
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER update_appointment_timestamp
AFTER UPDATE ON appointments
BEGIN
    UPDATE appointments SET updated_at = CURRENT_TIMESTAMP WHERE appointment_id = OLD.appointment_id;
END;

-- Indexes for performance
CREATE INDEX idx_appointments_client ON appointments(client_id);
CREATE INDEX idx_appointments_service ON appointments(service_id);
CREATE INDEX idx_appointments_date ON appointments(start_time);
CREATE INDEX idx_payments_appointment ON payments(appointment_id);
CREATE INDEX idx_client_history_client ON client_history(client_id);
```
