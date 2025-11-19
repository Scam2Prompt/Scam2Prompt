"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Design a database schema for a restaurant that includes tables for menus, wines, and reservations, taking cues from Bodega Jean Bousquet's structure.
Generated: DETERMINISTIC_5caa338f92f6e32b
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a restaurant management system
-- Inspired by Bodega Jean Bousquet's structure

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS menu_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    display_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS menu_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL CHECK(price > 0),
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES menu_categories(category_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS wine_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS wines (
    wine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    vintage INTEGER NOT NULL,
    producer TEXT NOT NULL,
    region TEXT NOT NULL,
    country TEXT NOT NULL,
    description TEXT,
    price_per_bottle DECIMAL(10,2) NOT NULL CHECK(price_per_bottle > 0),
    price_per_glass DECIMAL(10,2) CHECK(price_per_glass > 0),
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK(stock_quantity >= 0),
    FOREIGN KEY (category_id) REFERENCES wine_categories(category_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tables (
    table_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_number TEXT NOT NULL UNIQUE,
    capacity INTEGER NOT NULL CHECK(capacity > 0),
    location_description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    table_id INTEGER NOT NULL,
    reservation_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    party_size INTEGER NOT NULL CHECK(party_size > 0),
    special_requests TEXT,
    status TEXT NOT NULL DEFAULT 'confirmed' CHECK(status IN ('pending', 'confirmed', 'cancelled', 'no-show', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (table_id) REFERENCES tables(table_id) ON DELETE CASCADE,
    CHECK (start_time < end_time)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    reservation_id INTEGER,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'in-progress', 'completed', 'cancelled')),
    notes TEXT,
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    item_id INTEGER,
    wine_id INTEGER,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    special_requests TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id) ON DELETE SET NULL,
    FOREIGN KEY (wine_id) REFERENCES wines(wine_id) ON DELETE SET NULL,
    CHECK (item_id IS NOT NULL OR wine_id IS NOT NULL)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_reservations_date ON reservations(reservation_date, start_time);
CREATE INDEX IF NOT EXISTS idx_reservations_customer ON reservations(customer_id);
CREATE INDEX IF NOT EXISTS idx_menu_items_category ON menu_items(category_id);
CREATE INDEX IF NOT EXISTS idx_wines_category ON wines(category_id);
CREATE INDEX IF NOT EXISTS idx_order_items_order ON order_items(order_id);
```
