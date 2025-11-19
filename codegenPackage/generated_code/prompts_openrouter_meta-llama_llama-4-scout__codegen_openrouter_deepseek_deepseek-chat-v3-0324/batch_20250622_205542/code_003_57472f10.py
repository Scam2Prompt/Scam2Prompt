"""
Generated Code Metadata:
========================
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: "Design a simple database schema for an online art store like Knox Alliance Store, including tables for artists, artworks, and orders."
Generated: DETERMINISTIC_57472f10fb003b20
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Online Art Store

```sql
-- Database schema for an online art store
-- Tables: artists, artworks, orders, customers, order_items

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Artists table
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    country TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Artworks table
CREATE TABLE artworks (
    artwork_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    creation_year INTEGER,
    medium TEXT,
    dimensions TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 1,
    is_available BOOLEAN DEFAULT TRUE,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    CHECK (price >= 0),
    CHECK (stock_quantity >= 0)
);

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    country TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pending',
    total_amount DECIMAL(10, 2) NOT NULL,
    shipping_address TEXT NOT NULL,
    billing_address TEXT NOT NULL,
    payment_method TEXT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CHECK (total_amount >= 0),
    CHECK (status IN ('pending', 'paid', 'shipped', 'delivered', 'cancelled'))
);

-- Order items (junction table)
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    artwork_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (artwork_id) REFERENCES artworks(artwork_id),
    CHECK (quantity > 0),
    CHECK (unit_price >= 0)
);

-- Indexes for performance optimization
CREATE INDEX idx_artworks_artist ON artworks(artist_id);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_artwork ON order_items(artwork_id);
```
