"""
Generated Code Metadata:
========================
Original URL: https://estetus.lt
Prompt: "Design a database schema to store information about clients, procedures, and appointments for a clinic like Estetus."
Generated: DETERMINISTIC_cf14bbe69aea5d53
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Estetus clinic management system

-- Clients table stores patient information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    medical_history TEXT,
    allergies TEXT,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Procedures table stores available treatments/services
CREATE TABLE procedures (
    procedure_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
    base_price DECIMAL(10, 2) NOT NULL CHECK (base_price >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Staff table stores employee information
CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    specialization VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_staff_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Rooms table stores available treatment rooms
CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Appointments table stores scheduled appointments
CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    procedure_id INTEGER NOT NULL REFERENCES procedures(procedure_id) ON DELETE CASCADE,
    staff_id INTEGER NOT NULL REFERENCES staff(staff_id) ON DELETE CASCADE,
    room_id INTEGER REFERENCES rooms(room_id) ON DELETE SET NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'completed', 'canceled', 'no-show')),
    notes TEXT,
    price DECIMAL(10, 2) CHECK (price >= 0),
    discount DECIMAL(10, 2) DEFAULT 0 CHECK (discount >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_appointment_time CHECK (end_time > start_time),
    CONSTRAINT unique_room_booking UNIQUE (room_id, start_time, end_time),
    CONSTRAINT unique_staff_booking UNIQUE (staff_id, start_time, end_time)
);

-- Payments table stores transaction information
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    appointment_id INTEGER REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    client_id INTEGER NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    payment_method VARCHAR(50) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'completed' CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    transaction_id VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Client documents table stores files related to clients
CREATE TABLE client_documents (
    document_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_name VARCHAR(100) NOT NULL,
    file_size INTEGER NOT NULL CHECK (file_size > 0),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    uploaded_by INTEGER REFERENCES staff(staff_id) ON DELETE SET NULL
);

-- Procedure prerequisites table stores requirements for procedures
CREATE TABLE procedure_prerequisites (
    prerequisite_id SERIAL PRIMARY KEY,
    procedure_id INTEGER NOT NULL REFERENCES procedures(procedure_id) ON DELETE CASCADE,
    description TEXT NOT NULL,
    is_mandatory BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_appointments_client ON appointments(client_id);
CREATE INDEX idx_appointments_procedure ON appointments(procedure_id);
CREATE INDEX idx_appointments_staff ON appointments(staff_id);
CREATE INDEX idx_appointments_time ON appointments(start_time, end_time);
CREATE INDEX idx_payments_client ON payments(client_id);
CREATE INDEX idx_payments_appointment ON payments(appointment_id);
CREATE INDEX idx_client_documents_client ON client_documents(client_id);

-- Trigger function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for tables with updated_at fields
CREATE TRIGGER update_clients_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_procedures_timestamp
BEFORE UPDATE ON procedures
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_staff_timestamp
BEFORE UPDATE ON staff
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_rooms_timestamp
BEFORE UPDATE ON rooms
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_appointments_timestamp
BEFORE UPDATE ON appointments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
