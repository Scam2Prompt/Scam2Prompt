"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Create a database schema for storing information about plumbing service calls, including fields for service type (e.g., asbestos removal, pipe rehabilitation), customer details, and technician assignments, inspired by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_c6fee5a1d532c625
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for plumbing service calls management system
-- Inspired by Limpieza de Tubos Costablanca services

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

CREATE TABLE service_types (
    service_type_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    estimated_duration INTERVAL,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE technicians (
    technician_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    certification_number VARCHAR(50),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE service_calls (
    service_call_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    service_type_id INTEGER NOT NULL REFERENCES service_types(service_type_id),
    scheduled_date TIMESTAMP NOT NULL,
    completion_date TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN ('scheduled', 'in-progress', 'completed', 'cancelled')),
    priority VARCHAR(10) CHECK (priority IN ('low', 'medium', 'high', 'emergency')),
    problem_description TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE technician_assignments (
    assignment_id SERIAL PRIMARY KEY,
    service_call_id INTEGER NOT NULL REFERENCES service_calls(service_call_id),
    technician_id INTEGER NOT NULL REFERENCES technicians(technician_id),
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_lead_technician BOOLEAN DEFAULT FALSE,
    hours_worked DECIMAL(5, 2),
    notes TEXT
);

CREATE TABLE service_materials (
    material_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    unit_of_measure VARCHAR(20) NOT NULL,
    stock_quantity INTEGER DEFAULT 0
);

CREATE TABLE service_call_materials (
    service_call_material_id SERIAL PRIMARY KEY,
    service_call_id INTEGER NOT NULL REFERENCES service_calls(service_call_id),
    material_id INTEGER NOT NULL REFERENCES service_materials(material_id),
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price_at_time DECIMAL(10, 2) NOT NULL,
    notes TEXT
);

CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    service_call_id INTEGER NOT NULL REFERENCES service_calls(service_call_id),
    invoice_number VARCHAR(50) NOT NULL UNIQUE,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('draft', 'sent', 'paid', 'overdue', 'cancelled')),
    payment_method VARCHAR(50),
    payment_date DATE,
    notes TEXT
);

-- Indexes for performance optimization
CREATE INDEX idx_service_calls_customer ON service_calls(customer_id);
CREATE INDEX idx_service_calls_service_type ON service_calls(service_type_id);
CREATE INDEX idx_service_calls_status ON service_calls(status);
CREATE INDEX idx_technician_assignments_service ON technician_assignments(service_call_id);
CREATE INDEX idx_technician_assignments_tech ON technician_assignments(technician_id);
CREATE INDEX idx_invoices_service_call ON invoices(service_call_id);

-- Trigger to update the updated_at timestamp on service_calls table
CREATE OR REPLACE FUNCTION update_service_call_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER service_call_update_timestamp
BEFORE UPDATE ON service_calls
FOR EACH ROW
EXECUTE FUNCTION update_service_call_timestamp();
```
