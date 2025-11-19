"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Create a database schema to manage customer orders, equipment rentals, and repair services for a company like SARL VERDIER, which specializes in agricultural and irrigation equipment.
Generated: DETERMINISTIC_b9994a7a72503b8d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SARL VERDIER - Agricultural and Irrigation Equipment Management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    company_name TEXT,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL,
    tax_id TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CHECK (email LIKE '%@%.%')
);

-- Equipment categories
CREATE TABLE equipment_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Equipment inventory
CREATE TABLE equipment (
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    model TEXT NOT NULL,
    serial_number TEXT UNIQUE,
    purchase_date DATE,
    purchase_price DECIMAL(10,2),
    current_value DECIMAL(10,2),
    status TEXT NOT NULL CHECK (status IN ('available', 'rented', 'maintenance', 'retired')),
    location TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (category_id) REFERENCES equipment_categories(category_id)
);

-- Rental rates
CREATE TABLE rental_rates (
    rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER NOT NULL,
    daily_rate DECIMAL(10,2) NOT NULL,
    weekly_rate DECIMAL(10,2) NOT NULL,
    monthly_rate DECIMAL(10,2) NOT NULL,
    minimum_rental_period INTEGER NOT NULL, -- in days
    deposit_amount DECIMAL(10,2),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

-- Orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK (status IN ('pending', 'confirmed', 'shipped', 'delivered', 'cancelled')),
    total_amount DECIMAL(10,2) NOT NULL,
    tax_amount DECIMAL(10,2) NOT NULL,
    discount_amount DECIMAL(10,2) DEFAULT 0,
    payment_method TEXT NOT NULL CHECK (payment_method IN ('cash', 'credit_card', 'bank_transfer', 'check')),
    payment_status TEXT NOT NULL CHECK (payment_status IN ('unpaid', 'partially_paid', 'paid')),
    delivery_address TEXT,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order items (products sold)
CREATE TABLE order_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    equipment_id INTEGER,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL,
    discount DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

-- Rental contracts
CREATE TABLE rental_contracts (
    contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    expected_return_date DATE NOT NULL,
    actual_return_date DATE,
    status TEXT NOT NULL CHECK (status IN ('active', 'completed', 'overdue', 'cancelled')),
    total_amount DECIMAL(10,2) NOT NULL,
    deposit_amount DECIMAL(10,2) NOT NULL,
    deposit_returned BOOLEAN DEFAULT FALSE,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CHECK (end_date >= start_date),
    CHECK (expected_return_date >= start_date)
);

-- Rental contract items
CREATE TABLE rental_items (
    rental_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_id INTEGER NOT NULL,
    equipment_id INTEGER NOT NULL,
    rate_id INTEGER NOT NULL,
    rental_period_days INTEGER NOT NULL,
    rate_applied DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (contract_id) REFERENCES rental_contracts(contract_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    FOREIGN KEY (rate_id) REFERENCES rental_rates(rate_id)
);

-- Repair services
CREATE TABLE repair_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    standard_duration INTEGER, -- in hours
    standard_cost DECIMAL(10,2)
);

-- Repair orders
CREATE TABLE repair_orders (
    repair_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    equipment_id INTEGER NOT NULL,
    reported_issue TEXT NOT NULL,
    diagnosis TEXT,
    status TEXT NOT NULL CHECK (status IN ('received', 'diagnosed', 'in_progress', 'waiting_parts', 'completed', 'cancelled')),
    start_date DATETIME,
    completion_date DATETIME,
    estimated_cost DECIMAL(10,2),
    actual_cost DECIMAL(10,2),
    warranty_covered BOOLEAN DEFAULT FALSE,
    payment_status TEXT NOT NULL CHECK (payment_status IN ('unpaid', 'partially_paid', 'paid')),
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

-- Repair order services
CREATE TABLE repair_order_services (
    repair_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    repair_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1 CHECK (quantity > 0),
    unit_cost DECIMAL(10,2) NOT NULL,
    duration_hours DECIMAL(5,2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (repair_id) REFERENCES repair_orders(repair_id),
    FOREIGN KEY (service_id) REFERENCES repair_services(service_id)
);

-- Repair parts used
CREATE TABLE repair_parts (
    part_id INTEGER PRIMARY KEY AUTOINCREMENT,
    repair_id INTEGER NOT NULL,
    part_name TEXT NOT NULL,
    part_number TEXT,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_cost DECIMAL(10,2) NOT NULL,
    supplier TEXT,
    warranty_info TEXT,
    FOREIGN KEY (repair_id) REFERENCES repair_orders(repair_id)
);

-- Maintenance schedule
CREATE TABLE maintenance_schedule (
    maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER NOT NULL,
    maintenance_type TEXT NOT NULL,
    frequency_days INTEGER NOT NULL,
    last_performed DATE,
    next_due DATE NOT NULL,
    assigned_technician TEXT,
    notes TEXT,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

-- Maintenance history
CREATE TABLE maintenance_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    maintenance_id INTEGER NOT NULL,
    performed_date DATE NOT NULL,
    technician TEXT NOT NULL,
    description TEXT NOT NULL,
    parts_used TEXT,
    cost DECIMAL(10,2),
    FOREIGN KEY (maintenance_id) REFERENCES maintenance_schedule(maintenance_id)
);

-- Payments
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK (payment_method IN ('cash', 'credit_card', 'bank_transfer', 'check')),
    reference_number TEXT,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Payment allocations (for invoices)
CREATE TABLE payment_allocations (
    allocation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    payment_id INTEGER NOT NULL,
    order_id INTEGER,
    contract_id INTEGER,
    repair_id INTEGER,
    amount DECIMAL(10,2) NOT NULL,
    allocation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (payment_id) REFERENCES payments(payment_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (contract_id) REFERENCES rental_contracts(contract_id),
    FOREIGN KEY (repair_id) REFERENCES repair_orders(repair_id),
    CHECK (
        (order_id IS NOT NULL AND contract_id IS NULL AND repair_id IS NULL) OR
        (order_id IS NULL AND contract_id IS NOT NULL AND repair_id IS NULL) OR
        (order_id IS NULL AND contract_id IS NULL AND repair_id IS NOT NULL)
    )
);

-- Create indexes for performance
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_equipment_status ON equipment(status);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_rental_contracts_customer ON rental_contracts(customer_id);
CREATE INDEX idx_rental_contracts_status ON rental_contracts(status);
CREATE INDEX idx_repair_orders_customer ON repair_orders(customer_id);
CREATE INDEX idx_repair_orders_status ON repair_orders(status);
CREATE INDEX idx_maintenance_schedule_equipment ON maintenance_schedule(equipment_id);
CREATE INDEX idx_maintenance_schedule_next_due ON maintenance_schedule(next_due);
