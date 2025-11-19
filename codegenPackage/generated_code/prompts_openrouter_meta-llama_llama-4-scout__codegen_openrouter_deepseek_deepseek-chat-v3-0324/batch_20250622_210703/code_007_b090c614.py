"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Design a database schema to store information about hair services, products, and client appointments for a beauty salon management system.
Generated: DETERMINISTIC_b090c6143f9b728d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Beauty Salon Management System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    birth_date DATE,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT email_or_phone CHECK (email IS NOT NULL OR phone IS NOT NULL)
);

-- Services table to store available salon services
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CHECK (duration_minutes > 0),
    CHECK (price >= 0)
);

-- Stylists table to store employee information
CREATE TABLE stylists (
    stylist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    specialization TEXT,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Products table to store salon products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    brand TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    quantity_in_stock INTEGER NOT NULL DEFAULT 0,
    reorder_threshold INTEGER DEFAULT 5,
    is_active BOOLEAN DEFAULT TRUE,
    CHECK (price >= cost),
    CHECK (quantity_in_stock >= 0),
    CHECK (reorder_threshold >= 0)
);

-- Appointments table to track client bookings
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    stylist_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    status TEXT NOT NULL DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'completed', 'cancelled', 'no-show')),
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (stylist_id) REFERENCES stylists(stylist_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Junction table for appointment products (many-to-many relationship)
CREATE TABLE appointment_products (
    appointment_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    price_at_time DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (appointment_id, product_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CHECK (quantity > 0)
);

-- Client service history
CREATE TABLE service_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    stylist_id INTEGER NOT NULL,
    appointment_id INTEGER,
    service_date DATETIME NOT NULL,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (stylist_id) REFERENCES stylists(stylist_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
);

-- Inventory transactions
CREATE TABLE inventory_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    transaction_type TEXT NOT NULL CHECK (transaction_type IN ('purchase', 'sale', 'adjustment', 'return')),
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_appointments_client ON appointments(client_id);
CREATE INDEX idx_appointments_stylist ON appointments(stylist_id);
CREATE INDEX idx_appointments_time ON appointments(start_time, end_time);
CREATE INDEX idx_service_history_client ON service_history(client_id);
CREATE INDEX idx_inventory_product ON inventory_transactions(product_id);
```
