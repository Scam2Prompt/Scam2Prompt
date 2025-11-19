"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Design a simple database schema to store information about customers, furniture, and moving services offered by آل البيت.
Generated: DETERMINISTIC_d37c5d965319423e
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for آل البيت moving services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    email TEXT,
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Furniture categories table
CREATE TABLE furniture_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Furniture items table
CREATE TABLE furniture_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    weight_kg REAL NOT NULL CHECK(weight_kg > 0),
    dimensions TEXT NOT NULL, -- Format: "LxWxH" in cm
    fragile BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (category_id) REFERENCES furniture_categories(category_id) ON DELETE RESTRICT
);

-- Moving services table
CREATE TABLE moving_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    base_price REAL NOT NULL CHECK(base_price >= 0),
    price_per_km REAL CHECK(price_per_km >= 0),
    min_distance_km REAL DEFAULT 0 CHECK(min_distance_km >= 0),
    max_distance_km REAL CHECK(max_distance_km >= min_distance_km)
);

-- Orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    pickup_address TEXT NOT NULL,
    destination_address TEXT NOT NULL,
    distance_km REAL NOT NULL CHECK(distance_km > 0),
    total_price REAL NOT NULL CHECK(total_price >= 0),
    status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'confirmed', 'in_progress', 'completed', 'cancelled')),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    scheduled_date TIMESTAMP NOT NULL,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    FOREIGN KEY (service_id) REFERENCES moving_services(service_id) ON DELETE RESTRICT
);

-- Order items junction table
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1 CHECK(quantity > 0),
    special_instructions TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES furniture_items(item_id) ON DELETE RESTRICT
);

-- Create indexes for performance
CREATE INDEX idx_customers_phone ON customers(phone_number);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_order_items_order ON order_items(order_id);
```
