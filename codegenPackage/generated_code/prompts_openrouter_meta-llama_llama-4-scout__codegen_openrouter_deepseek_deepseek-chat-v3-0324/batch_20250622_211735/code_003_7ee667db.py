"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: "Design a database schema for storing information about PG properties, tenants, and rent payments, inspired by Moms PG's features."
Generated: DETERMINISTIC_7ee667db818cbe9d
Batch ID: 20250622_211735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for PG (Paying Guest) property management system
-- Inspired by Moms PG's features

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store PG property information
CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    pincode TEXT NOT NULL,
    total_rooms INTEGER NOT NULL CHECK(total_rooms > 0),
    available_rooms INTEGER NOT NULL CHECK(available_rooms >= 0),
    amenities TEXT, -- JSON string or comma-separated list of amenities
    monthly_rent REAL NOT NULL CHECK(monthly_rent > 0),
    security_deposit REAL NOT NULL CHECK(security_deposit >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    CONSTRAINT chk_available CHECK (available_rooms <= total_rooms)
);

-- Table to store tenant information
CREATE TABLE tenants (
    tenant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    aadhar_number TEXT UNIQUE,
    emergency_contact_name TEXT,
    emergency_contact_number TEXT,
    check_in_date DATE NOT NULL,
    check_out_date DATE,
    room_number TEXT NOT NULL,
    monthly_rent REAL NOT NULL CHECK(monthly_rent > 0),
    security_deposit_paid REAL NOT NULL CHECK(security_deposit_paid >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    CONSTRAINT chk_dates CHECK (check_out_date IS NULL OR check_out_date > check_in_date)
);

-- Table to store rent payment records
CREATE TABLE rent_payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tenant_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK(amount > 0),
    payment_date DATE NOT NULL,
    payment_method TEXT NOT NULL, -- cash, bank transfer, UPI, etc.
    transaction_reference TEXT,
    month INTEGER NOT NULL CHECK(month BETWEEN 1 AND 12),
    year INTEGER NOT NULL CHECK(year BETWEEN 2000 AND 2100),
    received_by TEXT, -- staff member who received payment
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    UNIQUE(tenant_id, month, year) -- Ensure one payment per tenant per month
);

-- Table to store maintenance requests
CREATE TABLE maintenance_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    tenant_id INTEGER NOT NULL,
    room_number TEXT NOT NULL,
    request_type TEXT NOT NULL, -- plumbing, electrical, cleaning, etc.
    description TEXT NOT NULL,
    status TEXT DEFAULT 'pending', -- pending, in_progress, completed, cancelled
    priority TEXT DEFAULT 'medium', -- low, medium, high
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
);

-- Table to store expense records
CREATE TABLE expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    category TEXT NOT NULL, -- maintenance, utilities, staff, etc.
    amount REAL NOT NULL CHECK(amount > 0),
    description TEXT,
    expense_date DATE NOT NULL,
    payment_method TEXT,
    receipt_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

-- Table to store staff information
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role TEXT NOT NULL, -- manager, cleaner, cook, security, etc.
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    salary REAL CHECK(salary >= 0),
    joining_date DATE NOT NULL,
    leaving_date DATE,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    CONSTRAINT chk_staff_dates CHECK (leaving_date IS NULL OR leaving_date > joining_date)
);

-- Create indexes for better performance
CREATE INDEX idx_tenants_property ON tenants(property_id);
CREATE INDEX idx_payments_tenant ON rent_payments(tenant_id);
CREATE INDEX idx_payments_property ON rent_payments(property_id);
CREATE INDEX idx_maintenance_property ON maintenance_requests(property_id);
CREATE INDEX idx_maintenance_tenant ON maintenance_requests(tenant_id);
CREATE INDEX idx_expenses_property ON expenses(property_id);
CREATE INDEX idx_staff_property ON staff(property_id);

-- Trigger to update available rooms when tenant checks in/out
CREATE TRIGGER update_available_rooms
AFTER INSERT ON tenants
BEGIN
    UPDATE properties 
    SET available_rooms = available_rooms - 1 
    WHERE property_id = NEW.property_id AND NEW.is_active = 1;
END;

CREATE TRIGGER update_available_rooms_checkout
AFTER UPDATE ON tenants
WHEN NEW.is_active = 0 AND OLD.is_active = 1
BEGIN
    UPDATE properties 
    SET available_rooms = available_rooms + 1 
    WHERE property_id = NEW.property_id;
END;

-- Trigger to update timestamp on row update
CREATE TRIGGER update_timestamp_properties
AFTER UPDATE ON properties
BEGIN
    UPDATE properties 
    SET updated_at = CURRENT_TIMESTAMP 
    WHERE property_id = OLD.property_id;
END;

CREATE TRIGGER update_timestamp_tenants
AFTER UPDATE ON tenants
BEGIN
    UPDATE tenants 
    SET updated_at = CURRENT_TIMESTAMP 
    WHERE tenant_id = OLD.tenant_id;
END;

CREATE TRIGGER update_timestamp_staff
AFTER UPDATE ON staff
BEGIN
    UPDATE staff 
    SET updated_at = CURRENT_TIMESTAMP 
    WHERE staff_id = OLD.staff_id;
END;
```
