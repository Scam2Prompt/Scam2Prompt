"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Design a database schema for a home services management system that tracks customer requests for services like air conditioning cleaning and water leakage detection, as offered by شركة انجاز.
Generated: DETERMINISTIC_64e59ad3c1dd6ab9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a home services management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    email TEXT,
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Services table
CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price REAL NOT NULL,
    estimated_duration_minutes INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Service requests table
CREATE TABLE IF NOT EXISTS service_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    preferred_date DATE NOT NULL,
    preferred_time_slot TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'in_progress', 'completed', 'cancelled')),
    special_instructions TEXT,
    urgency_level TEXT DEFAULT 'normal' CHECK (urgency_level IN ('low', 'normal', 'high', 'emergency')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Technicians table
CREATE TABLE IF NOT EXISTS technicians (
    technician_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    email TEXT,
    specialization TEXT,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Service assignments table
CREATE TABLE IF NOT EXISTS service_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    technician_id INTEGER NOT NULL,
    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_date TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (technician_id) REFERENCES technicians(technician_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_method TEXT NOT NULL CHECK (payment_method IN ('cash', 'credit_card', 'bank_transfer', 'online')),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    transaction_reference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE
);

-- Service materials table (for tracking materials used in services)
CREATE TABLE IF NOT EXISTS service_materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_name TEXT NOT NULL,
    description TEXT,
    unit_price REAL NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Materials used in service requests
CREATE TABLE IF NOT EXISTS request_materials (
    request_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity_used INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES service_materials(material_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_customers_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_services_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_requests_timestamp
AFTER UPDATE ON service_requests
FOR EACH ROW
BEGIN
    UPDATE service_requests SET updated_at = CURRENT_TIMESTAMP WHERE request_id = OLD.request_id;
END;

CREATE TRIGGER IF NOT EXISTS update_technicians_timestamp
AFTER UPDATE ON technicians
FOR EACH ROW
BEGIN
    UPDATE technicians SET updated_at = CURRENT_TIMESTAMP WHERE technician_id = OLD.technician_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_assignments_timestamp
AFTER UPDATE ON service_assignments
FOR EACH ROW
BEGIN
    UPDATE service_assignments SET updated_at = CURRENT_TIMESTAMP WHERE assignment_id = OLD.assignment_id;
END;

CREATE TRIGGER IF NOT EXISTS update_payments_timestamp
AFTER UPDATE ON payments
FOR EACH ROW
BEGIN
    UPDATE payments SET updated_at = CURRENT_TIMESTAMP WHERE payment_id = OLD.payment_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_materials_timestamp
AFTER UPDATE ON service_materials
FOR EACH ROW
BEGIN
    UPDATE service_materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER IF NOT EXISTS update_request_materials_timestamp
AFTER UPDATE ON request_materials
FOR EACH ROW
BEGIN
    UPDATE request_materials SET updated_at = CURRENT_TIMESTAMP WHERE request_material_id = OLD.request_material_id;
END;

-- Initial data insertion for services
INSERT OR IGNORE INTO services (service_name, description, base_price, estimated_duration_minutes) VALUES
('Air Conditioning Cleaning', 'Professional cleaning of AC units', 200.00, 120),
('Water Leakage Detection', 'Detection and location of water leaks in pipes', 150.00, 90),
('Electrical Maintenance', 'General electrical system maintenance', 180.00, 120),
('Plumbing Services', 'Fixing and maintaining plumbing systems', 170.00, 90);
```
