"""
Generated Code Metadata:
========================
Original URL: https://pooltyme.app
Prompt: Design a database schema for a pool maintenance management app like Pooltyme, including tables for logs, users, and pool information.
Generated: DETERMINISTIC_3f875f8c55c94730
Batch ID: 20250622_205053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Pool Maintenance Management App

-- Users table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'technician', 'customer')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Customer addresses table
CREATE TABLE customer_addresses (
    address_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    street_address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) DEFAULT 'United States',
    is_primary BOOLEAN DEFAULT TRUE
);

-- Pool information table
CREATE TABLE pools (
    pool_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    address_id INTEGER REFERENCES customer_addresses(address_id) ON DELETE SET NULL,
    pool_name VARCHAR(100) NOT NULL,
    pool_type VARCHAR(50) CHECK (pool_type IN ('residential', 'commercial')),
    pool_size_gallons INTEGER,
    pool_surface_type VARCHAR(50) CHECK (pool_surface_type IN ('plaster', 'vinyl', 'fiberglass', 'tile')),
    has_spa BOOLEAN DEFAULT FALSE,
    spa_size_gallons INTEGER,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Maintenance services table
CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    duration_minutes INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Service visits table
CREATE TABLE service_visits (
    visit_id SERIAL PRIMARY KEY,
    pool_id INTEGER REFERENCES pools(pool_id) ON DELETE CASCADE,
    technician_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    scheduled_date TIMESTAMP WITH TIME ZONE NOT NULL,
    completed_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('scheduled', 'in-progress', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Visit services junction table
CREATE TABLE visit_services (
    visit_service_id SERIAL PRIMARY KEY,
    visit_id INTEGER REFERENCES service_visits(visit_id) ON DELETE CASCADE,
    service_id INTEGER REFERENCES services(service_id) ON DELETE CASCADE,
    actual_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    UNIQUE(visit_id, service_id)
);

-- Pool chemical logs table
CREATE TABLE chemical_logs (
    log_id SERIAL PRIMARY KEY,
    pool_id INTEGER REFERENCES pools(pool_id) ON DELETE CASCADE,
    visit_id INTEGER REFERENCES service_visits(visit_id) ON DELETE SET NULL,
    technician_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    log_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    chlorine_level DECIMAL(5, 2),
    ph_level DECIMAL(4, 2),
    alkalinity_level INTEGER,
    calcium_hardness_level INTEGER,
    cyanuric_acid_level INTEGER,
    total_dissolved_solids INTEGER,
    temperature_fahrenheit DECIMAL(5, 2),
    notes TEXT
);

-- Equipment table
CREATE TABLE equipment (
    equipment_id SERIAL PRIMARY KEY,
    pool_id INTEGER REFERENCES pools(pool_id) ON DELETE CASCADE,
    equipment_type VARCHAR(50) NOT NULL,
    model VARCHAR(100),
    serial_number VARCHAR(100),
    installation_date DATE,
    last_service_date DATE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Maintenance tasks table
CREATE TABLE maintenance_tasks (
    task_id SERIAL PRIMARY KEY,
    equipment_id INTEGER REFERENCES equipment(equipment_id) ON DELETE CASCADE,
    task_name VARCHAR(100) NOT NULL,
    frequency_days INTEGER NOT NULL,
    last_performed_date DATE,
    next_due_date DATE,
    notes TEXT
);

-- Billing information table
CREATE TABLE billing_information (
    billing_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    payment_method_type VARCHAR(50) NOT NULL CHECK (payment_method_type IN ('credit_card', 'debit_card', 'bank_account')),
    card_last_four VARCHAR(4),
    card_exp_month VARCHAR(2),
    card_exp_year VARCHAR(4),
    bank_name VARCHAR(100),
    billing_address_id INTEGER REFERENCES customer_addresses(address_id) ON DELETE SET NULL,
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Invoices table
CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    billing_id INTEGER REFERENCES billing_information(billing_id) ON DELETE SET NULL,
    invoice_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    due_date TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('draft', 'sent', 'paid', 'overdue', 'cancelled')),
    subtotal DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    notes TEXT
);

-- Invoice items table
CREATE TABLE invoice_items (
    item_id SERIAL PRIMARY KEY,
    invoice_id INTEGER REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    service_id INTEGER REFERENCES services(service_id) ON DELETE SET NULL,
    visit_id INTEGER REFERENCES service_visits(visit_id) ON DELETE SET NULL,
    description TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL
);

-- Payments table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    invoice_id INTEGER REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    billing_id INTEGER REFERENCES billing_information(billing_id) ON DELETE SET NULL,
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    transaction_id VARCHAR(100),
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    notes TEXT
);

-- Create indexes for performance
CREATE INDEX idx_pools_user_id ON pools(user_id);
CREATE INDEX idx_service_visits_pool_id ON service_visits(pool_id);
CREATE INDEX idx_service_visits_technician_id ON service_visits(technician_id);
CREATE INDEX idx_chemical_logs_pool_id ON chemical_logs(pool_id);
CREATE INDEX idx_chemical_logs_visit_id ON chemical_logs(visit_id);
CREATE INDEX idx_invoices_user_id ON invoices(user_id);
CREATE INDEX idx_invoice_items_invoice_id ON invoice_items(invoice_id);
```
