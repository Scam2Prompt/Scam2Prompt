"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Develop a database schema for managing real estate assets and rental services, inspired by the operations of Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_1be63a220719483b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for real estate asset and rental management system
-- Inspired by Lao Tai Trading - Investment Group operations

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS tenants;
DROP TABLE IF EXISTS leases;
DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS units;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS maintenance_requests;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS property_managers;

-- Owners table
CREATE TABLE owners (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT,
    address TEXT,
    tax_id TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Properties table
CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    property_type TEXT NOT NULL CHECK (property_type IN ('Residential', 'Commercial', 'Industrial', 'Mixed-Use')),
    year_built INTEGER,
    total_units INTEGER DEFAULT 0,
    parking_spaces INTEGER DEFAULT 0,
    amenities TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE
);

-- Units table
CREATE TABLE units (
    unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    unit_number TEXT NOT NULL,
    bedrooms INTEGER NOT NULL,
    bathrooms REAL NOT NULL,
    square_footage REAL NOT NULL,
    unit_type TEXT NOT NULL CHECK (unit_type IN ('Apartment', 'Office', 'Retail', 'Warehouse', 'Other')),
    status TEXT NOT NULL CHECK (status IN ('Vacant', 'Occupied', 'Under Maintenance', 'Reserved')),
    monthly_rent REAL NOT NULL,
    deposit_amount REAL NOT NULL,
    features TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    UNIQUE (property_id, unit_number)
);

-- Tenants table
CREATE TABLE tenants (
    tenant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT,
    employer TEXT,
    emergency_contact_name TEXT,
    emergency_contact_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Leases table
CREATE TABLE leases (
    lease_id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id INTEGER NOT NULL,
    tenant_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    monthly_rent REAL NOT NULL,
    deposit_amount REAL NOT NULL,
    lease_status TEXT NOT NULL CHECK (lease_status IN ('Active', 'Expired', 'Terminated', 'Renewed')),
    late_fee REAL DEFAULT 0,
    grace_period INTEGER DEFAULT 5,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES units(unit_id) ON DELETE CASCADE,
    FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id) ON DELETE CASCADE,
    CHECK (end_date > start_date)
);

-- Employees table
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT NOT NULL,
    hire_date DATE NOT NULL,
    salary REAL,
    status TEXT NOT NULL CHECK (status IN ('Active', 'On Leave', 'Terminated')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Property managers table (junction table between properties and employees)
CREATE TABLE property_managers (
    property_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (property_id, employee_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);

-- Maintenance requests table
CREATE TABLE maintenance_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id INTEGER NOT NULL,
    tenant_id INTEGER NOT NULL,
    employee_id INTEGER,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_date TIMESTAMP,
    issue_type TEXT NOT NULL CHECK (issue_type IN ('Plumbing', 'Electrical', 'HVAC', 'Structural', 'Appliance', 'Other')),
    description TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Submitted', 'In Progress', 'Completed', 'Cancelled')),
    priority TEXT NOT NULL CHECK (priority IN ('Low', 'Medium', 'High', 'Emergency')),
    cost REAL DEFAULT 0,
    FOREIGN KEY (unit_id) REFERENCES units(unit_id) ON DELETE CASCADE,
    FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE SET NULL
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    lease_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_date DATE NOT NULL,
    payment_method TEXT NOT NULL CHECK (payment_method IN ('Cash', 'Check', 'Credit Card', 'Bank Transfer', 'Online Payment')),
    transaction_reference TEXT,
    payment_type TEXT NOT NULL CHECK (payment_type IN ('Rent', 'Deposit', 'Late Fee', 'Maintenance', 'Other')),
    status TEXT NOT NULL CHECK (status IN ('Pending', 'Completed', 'Failed', 'Refunded')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lease_id) REFERENCES leases(lease_id) ON DELETE CASCADE
);

-- Triggers for automatic updates
CREATE TRIGGER update_owner_timestamp
AFTER UPDATE ON owners
FOR EACH ROW
BEGIN
    UPDATE owners SET updated_at = CURRENT_TIMESTAMP WHERE owner_id = old.owner_id;
END;

CREATE TRIGGER update_property_timestamp
AFTER UPDATE ON properties
FOR EACH ROW
BEGIN
    UPDATE properties SET updated_at = CURRENT_TIMESTAMP WHERE property_id = old.property_id;
END;

CREATE TRIGGER update_unit_timestamp
AFTER UPDATE ON units
FOR EACH ROW
BEGIN
    UPDATE units SET updated_at = CURRENT_TIMESTAMP WHERE unit_id = old.unit_id;
END;

CREATE TRIGGER update_tenant_timestamp
AFTER UPDATE ON tenants
FOR EACH ROW
BEGIN
    UPDATE tenants SET updated_at = CURRENT_TIMESTAMP WHERE tenant_id = old.tenant_id;
END;

CREATE TRIGGER update_lease_timestamp
AFTER UPDATE ON leases
FOR EACH ROW
BEGIN
    UPDATE leases SET updated_at = CURRENT_TIMESTAMP WHERE lease_id = old.lease_id;
END;

CREATE TRIGGER update_employee_timestamp
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    UPDATE employees SET updated_at = CURRENT_TIMESTAMP WHERE employee_id = old.employee_id;
END;

-- Trigger to update unit status when lease is created
CREATE TRIGGER update_unit_status_on_lease
AFTER INSERT ON leases
FOR EACH ROW
BEGIN
    UPDATE units SET status = 'Occupied' WHERE unit_id = NEW.unit_id;
END;

-- Trigger to update unit status when lease ends
CREATE TRIGGER update_unit_status_on_lease_end
AFTER UPDATE OF lease_status ON leases
FOR EACH ROW
WHEN NEW.lease_status IN ('Expired', 'Terminated')
BEGIN
    UPDATE units SET status = 'Vacant' WHERE unit_id = NEW.unit_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_properties_city ON properties(city);
CREATE INDEX idx_properties_owner ON properties(owner_id);
CREATE INDEX idx_units_property ON units(property_id);
CREATE INDEX idx_leases_tenant ON leases(tenant_id);
CREATE INDEX idx_leases_unit ON leases(unit_id);
CREATE INDEX idx_payments_lease ON payments(lease_id);
CREATE INDEX idx_maintenance_unit ON maintenance_requests(unit_id);
CREATE INDEX idx_maintenance_status ON maintenance_requests(status);
```
