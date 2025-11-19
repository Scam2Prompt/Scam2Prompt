"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Design a database schema to store information about clients, services, and employees for a facility management company like Ashvi Facility Management Services.
Generated: DETERMINISTIC_b664d1baa7ece98e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Facility Management Company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    company_name TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('active', 'inactive', 'suspended')) DEFAULT 'active',
    notes TEXT
);

-- Employees table
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    position TEXT NOT NULL,
    hire_date DATE NOT NULL,
    salary REAL CHECK(salary > 0),
    status TEXT CHECK(status IN ('active', 'on_leave', 'terminated')) DEFAULT 'active',
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    category TEXT NOT NULL,
    base_price REAL CHECK(base_price >= 0),
    hourly_rate REAL CHECK(hourly_rate >= 0),
    minimum_hours INTEGER CHECK(minimum_hours >= 0) DEFAULT 1
);

-- Service areas table
CREATE TABLE service_areas (
    area_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Employee skills junction table
CREATE TABLE employee_skills (
    employee_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    proficiency_level TEXT CHECK(proficiency_level IN ('beginner', 'intermediate', 'expert')),
    certification_date DATE,
    PRIMARY KEY (employee_id, service_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Contracts table
CREATE TABLE contracts (
    contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    contract_value REAL CHECK(contract_value >= 0),
    payment_terms TEXT,
    status TEXT CHECK(status IN ('active', 'expired', 'terminated')) DEFAULT 'active',
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Contract services junction table
CREATE TABLE contract_services (
    contract_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER CHECK(quantity > 0) DEFAULT 1,
    custom_price REAL CHECK(custom_price >= 0),
    frequency TEXT,
    PRIMARY KEY (contract_id, service_id),
    FOREIGN KEY (contract_id) REFERENCES contracts(contract_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Work orders table
CREATE TABLE work_orders (
    work_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    assigned_employee_id INTEGER,
    scheduled_date DATE NOT NULL,
    completion_date DATE,
    status TEXT CHECK(status IN ('scheduled', 'in_progress', 'completed', 'cancelled')) DEFAULT 'scheduled',
    hours_worked REAL CHECK(hours_worked >= 0),
    notes TEXT,
    FOREIGN KEY (contract_id) REFERENCES contracts(contract_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (assigned_employee_id) REFERENCES employees(employee_id) ON DELETE SET NULL,
    CHECK (completion_date IS NULL OR completion_date >= scheduled_date)
);

-- Service area coverage table
CREATE TABLE service_coverage (
    service_id INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    additional_charge REAL CHECK(additional_charge >= 0) DEFAULT 0,
    PRIMARY KEY (service_id, area_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (area_id) REFERENCES service_areas(area_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_id INTEGER NOT NULL,
    amount REAL CHECK(amount > 0) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method TEXT CHECK(payment_method IN ('cash', 'check', 'credit_card', 'bank_transfer', 'online')),
    transaction_reference TEXT,
    status TEXT CHECK(status IN ('pending', 'completed', 'failed', 'refunded')) DEFAULT 'completed',
    notes TEXT,
    FOREIGN KEY (contract_id) REFERENCES contracts(contract_id) ON DELETE CASCADE
);

-- Employee schedules table
CREATE TABLE employee_schedules (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    work_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT CHECK(status IN ('scheduled', 'completed', 'cancelled', 'no_show')) DEFAULT 'scheduled',
    notes TEXT,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    CHECK (end_time > start_time),
    UNIQUE (employee_id, work_date)
);

-- Create indexes for performance
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_employees_email ON employees(email);
CREATE INDEX idx_contracts_client ON contracts(client_id);
CREATE INDEX idx_work_orders_contract ON work_orders(contract_id);
CREATE INDEX idx_work_orders_employee ON work_orders(assigned_employee_id);
CREATE INDEX idx_work_orders_status ON work_orders(status);
CREATE INDEX idx_payments_contract ON payments(contract_id);
```
