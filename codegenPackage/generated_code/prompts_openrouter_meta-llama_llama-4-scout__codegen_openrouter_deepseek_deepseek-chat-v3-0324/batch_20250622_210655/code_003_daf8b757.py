"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Create a SQL database schema for storing information about moving services, customers, and employees for a company like Şanlı Nakliye.
Generated: DETERMINISTIC_daf8b757419409cb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Şanlı Nakliye moving services company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    UNIQUE(phone, email)
);

-- Employees table
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    position TEXT NOT NULL,
    hire_date DATE NOT NULL,
    salary REAL NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('active', 'on_leave', 'terminated')),
    UNIQUE(phone, email)
);

-- Vehicles table
CREATE TABLE vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_plate TEXT NOT NULL UNIQUE,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    capacity_kg REAL NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('available', 'in_use', 'maintenance')),
    last_maintenance_date DATE
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price REAL NOT NULL,
    price_per_km REAL,
    minimum_hours INTEGER DEFAULT 1
);

-- Moves table (main orders)
CREATE TABLE moves (
    move_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    move_date DATE NOT NULL,
    start_time TIME NOT NULL,
    estimated_duration_hours REAL NOT NULL,
    origin_address TEXT NOT NULL,
    destination_address TEXT NOT NULL,
    distance_km REAL NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('scheduled', 'in_progress', 'completed', 'cancelled')),
    total_price REAL NOT NULL,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT
);

-- Move services junction table
CREATE TABLE move_services (
    move_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    move_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    FOREIGN KEY (move_id) REFERENCES moves(move_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE RESTRICT,
    UNIQUE(move_id, service_id)
);

-- Move assignments (employees assigned to moves)
CREATE TABLE move_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    move_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    vehicle_id INTEGER,
    role TEXT NOT NULL CHECK(role IN ('driver', 'helper', 'supervisor')),
    FOREIGN KEY (move_id) REFERENCES moves(move_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE RESTRICT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE SET NULL,
    UNIQUE(move_id, employee_id)
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    move_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('cash', 'credit_card', 'bank_transfer')),
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'refunded', 'failed')),
    transaction_reference TEXT,
    FOREIGN KEY (move_id) REFERENCES moves(move_id) ON DELETE RESTRICT
);

-- Inventory items table
CREATE TABLE inventory_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    quantity INTEGER NOT NULL DEFAULT 0,
    unit TEXT NOT NULL,
    last_restock_date DATE
);

-- Move inventory usage
CREATE TABLE move_inventory_usage (
    usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    move_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity_used INTEGER NOT NULL,
    FOREIGN KEY (move_id) REFERENCES moves(move_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES inventory_items(item_id) ON DELETE RESTRICT
);

-- Create indexes for better performance
CREATE INDEX idx_customers_phone ON customers(phone);
CREATE INDEX idx_employees_phone ON employees(phone);
CREATE INDEX idx_moves_customer ON moves(customer_id);
CREATE INDEX idx_moves_date ON moves(move_date);
CREATE INDEX idx_move_assignments_move ON move_assignments(move_id);
CREATE INDEX idx_move_assignments_employee ON move_assignments(employee_id);
CREATE INDEX idx_payments_move ON payments(move_id);
```
