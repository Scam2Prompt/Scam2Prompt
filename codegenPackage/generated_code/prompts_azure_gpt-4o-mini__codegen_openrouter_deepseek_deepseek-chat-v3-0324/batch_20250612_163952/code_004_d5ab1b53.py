"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: Design a database schema for managing client information and appointment scheduling for an equine care service, taking cues from the organizational structure of Martin Godwin Equine Services.
Generated: DETERMINISTIC_d5ab1b53594d67ff
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Equine Care Service

```sql
-- Database schema for equine care service management system
-- Inspired by Martin Godwin Equine Services organizational structure

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(30),
    zip_code VARCHAR(20),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT email_or_phone_not_null CHECK (email IS NOT NULL OR phone IS NOT NULL)
);

CREATE TABLE horses (
    horse_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    registered_name VARCHAR(100),
    barn_name VARCHAR(50) NOT NULL,
    breed VARCHAR(50),
    color VARCHAR(50),
    birth_year INTEGER,
    gender VARCHAR(10) CHECK (gender IN ('Stallion', 'Mare', 'Gelding', 'Colt', 'Filly')),
    microchip_number VARCHAR(50) UNIQUE,
    passport_number VARCHAR(50) UNIQUE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    role VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    horse_id INTEGER NOT NULL REFERENCES horses(horse_id) ON DELETE CASCADE,
    service_id INTEGER NOT NULL REFERENCES services(service_id) ON DELETE RESTRICT,
    staff_id INTEGER NOT NULL REFERENCES staff(staff_id) ON DELETE RESTRICT,
    scheduled_start TIMESTAMP WITH TIME ZONE NOT NULL,
    scheduled_end TIMESTAMP WITH TIME ZONE NOT NULL,
    actual_start TIMESTAMP WITH TIME ZONE,
    actual_end TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) NOT NULL DEFAULT 'Scheduled' CHECK (status IN ('Scheduled', 'Completed', 'Cancelled', 'No-Show')),
    notes TEXT,
    price DECIMAL(10, 2),
    payment_status VARCHAR(20) DEFAULT 'Unpaid' CHECK (payment_status IN ('Unpaid', 'Partial', 'Paid', 'Refunded')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_appointment_time CHECK (scheduled_end > scheduled_start)
);

CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(client_id) ON DELETE RESTRICT,
    invoice_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending' CHECK (status IN ('Pending', 'Paid', 'Overdue', 'Cancelled')),
    total_amount DECIMAL(10, 2) NOT NULL,
    amount_paid DECIMAL(10, 2) DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_due_date CHECK (due_date >= invoice_date),
    CONSTRAINT valid_payment CHECK (amount_paid <= total_amount)
);

CREATE TABLE invoice_items (
    item_id SERIAL PRIMARY KEY,
    invoice_id INTEGER NOT NULL REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    appointment_id INTEGER REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    description TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    tax_rate DECIMAL(5, 2) DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_quantity CHECK (quantity > 0),
    CONSTRAINT positive_price CHECK (unit_price >= 0)
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    invoice_id INTEGER NOT NULL REFERENCES invoices(invoice_id) ON DELETE RESTRICT,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(20) NOT NULL CHECK (payment_method IN ('Cash', 'Check', 'Credit Card', 'Bank Transfer', 'Other')),
    transaction_reference VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_amount CHECK (amount > 0)
);

CREATE TABLE medical_records (
    record_id SERIAL PRIMARY KEY,
    horse_id INTEGER NOT NULL REFERENCES horses(horse_id) ON DELETE CASCADE,
    record_date DATE NOT NULL DEFAULT CURRENT_DATE,
    record_type VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    veterinarian VARCHAR(100),
    notes TEXT,
    attachment_path VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE staff_availability (
    availability_id SERIAL PRIMARY KEY,
    staff_id INTEGER NOT NULL REFERENCES staff(staff_id) ON DELETE CASCADE,
    day_of_week INTEGER NOT NULL CHECK (day_of_week BETWEEN 0 AND 6), -- 0=Sunday, 6=Saturday
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    available BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_availability_time CHECK (end_time > start_time),
    UNIQUE(staff_id, day_of_week)
);

-- Indexes for performance optimization
CREATE INDEX idx_appointments_horse_id ON appointments(horse_id);
CREATE INDEX idx_appointments_staff_id ON appointments(staff_id);
CREATE INDEX idx_appointments_date ON appointments(scheduled_start);
CREATE INDEX idx_horses_client_id ON horses(client_id);
CREATE INDEX idx_invoices_client_id ON invoices(client_id);
CREATE INDEX idx_invoice_items_invoice_id ON invoice_items(invoice_id);
CREATE INDEX idx_medical_records_horse_id ON medical_records(horse_id);

-- Triggers for automatic updated_at timestamps
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

CREATE TRIGGER update_horses_timestamp
BEFORE UPDATE ON horses
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_services_timestamp
BEFORE UPDATE ON services
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_staff_timestamp
BEFORE UPDATE ON staff
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_appointments_timestamp
BEFORE UPDATE ON appointments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_invoices_timestamp
BEFORE UPDATE ON invoices
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_medical_records_timestamp
BEFORE UPDATE ON medical_records
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_staff_availability_timestamp
BEFORE UPDATE ON staff_availability
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
