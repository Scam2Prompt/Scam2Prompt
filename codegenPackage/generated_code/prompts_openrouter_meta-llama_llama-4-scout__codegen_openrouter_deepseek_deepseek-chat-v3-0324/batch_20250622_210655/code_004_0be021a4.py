"""
Generated Code Metadata:
========================
Original URL: https://www.albertozofrea.it
Prompt: Suggest a suitable database schema for storing client information, appointments, and services offered by a professional Shiatsu operator like Alberto Zofrea.
Generated: DETERMINISTIC_0be021a4e06c1b28
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Shiatsu practitioner management system

-- Clients table stores basic client information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    birth_date DATE,
    gender VARCHAR(20),
    health_notes TEXT,
    preferences TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Services table lists all available shiatsu services
CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Practitioners table (in case there are multiple practitioners)
CREATE TABLE practitioners (
    practitioner_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    bio TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Appointments table tracks all scheduled sessions
CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(client_id),
    practitioner_id INTEGER NOT NULL REFERENCES practitioners(practitioner_id),
    service_id INTEGER NOT NULL REFERENCES services(service_id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'scheduled' CHECK (
        status IN ('scheduled', 'completed', 'cancelled', 'no-show')
    ),
    notes TEXT,
    price DECIMAL(10, 2) NOT NULL,
    discount DECIMAL(10, 2) DEFAULT 0.00,
    payment_status VARCHAR(20) DEFAULT 'pending' CHECK (
        payment_status IN ('pending', 'paid', 'partial', 'refunded')
    ),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT end_after_start CHECK (end_time > start_time)
);

-- Client health history table
CREATE TABLE client_health_history (
    history_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(client_id),
    entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    practitioner_id INTEGER REFERENCES practitioners(practitioner_id),
    notes TEXT NOT NULL,
    concerns TEXT,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_notes TEXT
);

-- Payments table tracks financial transactions
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    appointment_id INTEGER REFERENCES appointments(appointment_id),
    client_id INTEGER NOT NULL REFERENCES clients(client_id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_reference VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_appointments_client ON appointments(client_id);
CREATE INDEX idx_appointments_practitioner ON appointments(practitioner_id);
CREATE INDEX idx_appointments_date ON appointments(start_time);
CREATE INDEX idx_client_health_history ON client_health_history(client_id);
CREATE INDEX idx_payments_client ON payments(client_id);
CREATE INDEX idx_payments_appointment ON payments(appointment_id);

-- Trigger to update the updated_at timestamp when records are modified
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_clients_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_services_timestamp
BEFORE UPDATE ON services
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_practitioners_timestamp
BEFORE UPDATE ON practitioners
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_appointments_timestamp
BEFORE UPDATE ON appointments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
