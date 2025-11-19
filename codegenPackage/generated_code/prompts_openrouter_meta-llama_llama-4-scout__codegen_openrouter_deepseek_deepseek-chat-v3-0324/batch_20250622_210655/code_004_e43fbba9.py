"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: "Design a database schema to store customer information, service requests, and appointment schedules for a plumbing and heating business like Flammedeauinc."
Generated: DETERMINISTIC_e43fbba985122e8c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Flammedeauinc Plumbing and Heating Business

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CHECK (email LIKE '%_@__%.__%' OR email IS NULL),
    CHECK (LENGTH(phone) >= 10)
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    estimated_duration_minutes INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1
);

-- Technicians table
CREATE TABLE technicians (
    technician_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    specialization TEXT,
    CHECK (email LIKE '%_@__%.__%'),
    CHECK (LENGTH(phone) >= 10)
);

-- Service requests table
CREATE TABLE service_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    urgency_level TEXT CHECK(urgency_level IN ('low', 'medium', 'high', 'emergency')),
    status TEXT CHECK(status IN ('pending', 'assigned', 'in_progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE SET NULL
);

-- Appointments table
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    technician_id INTEGER NOT NULL,
    scheduled_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT CHECK(status IN ('scheduled', 'in_progress', 'completed', 'cancelled', 'no_show')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (technician_id) REFERENCES technicians(technician_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Invoice table
CREATE TABLE invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0,
    payment_status TEXT CHECK(payment_status IN ('pending', 'partial', 'paid', 'overdue')),
    due_date DATE NOT NULL,
    issued_date DATE DEFAULT CURRENT_DATE,
    notes TEXT,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE
);

-- Invoice line items
CREATE TABLE invoice_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Payment records
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT CHECK(payment_method IN ('cash', 'check', 'credit_card', 'debit_card', 'bank_transfer')),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_reference TEXT,
    notes TEXT,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE
);

-- Customer equipment table
CREATE TABLE customer_equipment (
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    equipment_type TEXT NOT NULL,
    brand TEXT,
    model TEXT,
    serial_number TEXT,
    installation_date DATE,
    last_service_date DATE,
    warranty_expiration DATE,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_customers_name ON customers(last_name, first_name);
CREATE INDEX idx_service_requests_customer ON service_requests(customer_id);
CREATE INDEX idx_service_requests_status ON service_requests(status);
CREATE INDEX idx_appointments_date ON appointments(scheduled_date);
CREATE INDEX idx_appointments_technician ON appointments(technician_id);
CREATE INDEX idx_invoices_appointment ON invoices(appointment_id);
CREATE INDEX idx_invoices_status ON invoices(payment_status);
```
