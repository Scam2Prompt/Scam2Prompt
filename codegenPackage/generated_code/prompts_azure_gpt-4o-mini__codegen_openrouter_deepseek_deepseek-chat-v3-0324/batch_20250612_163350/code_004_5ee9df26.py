"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Design a database schema for managing dumpster rental services, including fields for customer inquiries and service areas, based on the structure used by Junk in The Box ATL.
Generated: DETERMINISTIC_5ee9df261a42344c
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Dumpster Rental Services Management System
-- Inspired by Junk in The Box ATL structure

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    CHECK (LENGTH(phone) >= 10)
);

-- Service areas table
CREATE TABLE IF NOT EXISTS service_areas (
    area_id INTEGER PRIMARY KEY AUTOINCREMENT,
    area_name TEXT NOT NULL UNIQUE,
    zip_codes TEXT NOT NULL,  -- Comma-separated list of zip codes
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Dumpster sizes table
CREATE TABLE IF NOT EXISTS dumpster_sizes (
    size_id INTEGER PRIMARY KEY AUTOINCREMENT,
    size_name TEXT NOT NULL UNIQUE,  -- e.g., "10-yard", "20-yard"
    dimensions TEXT NOT NULL,
    capacity TEXT NOT NULL,
    price_per_day DECIMAL(10, 2) NOT NULL,
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Rentals table
CREATE TABLE IF NOT EXISTS rentals (
    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    size_id INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    delivery_address TEXT NOT NULL,
    delivery_instructions TEXT,
    status TEXT DEFAULT 'pending',  -- pending, confirmed, delivered, picked_up, cancelled
    total_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (size_id) REFERENCES dumpster_sizes(size_id),
    FOREIGN KEY (area_id) REFERENCES service_areas(area_id),
    CHECK (end_date > start_date),
    CHECK (status IN ('pending', 'confirmed', 'delivered', 'picked_up', 'cancelled'))
);

-- Inquiries table
CREATE TABLE IF NOT EXISTS inquiries (
    inquiry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    message TEXT NOT NULL,
    preferred_size_id INTEGER,
    preferred_dates TEXT,  -- JSON string or text description
    status TEXT DEFAULT 'new',  -- new, contacted, converted, rejected
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL,
    FOREIGN KEY (preferred_size_id) REFERENCES dumpster_sizes(size_id),
    CHECK (email LIKE '%@%.%'),
    CHECK (LENGTH(phone) >= 10),
    CHECK (status IN ('new', 'contacted', 'converted', 'rejected'))
);

-- Triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_rental_timestamp
AFTER UPDATE ON rentals
FOR EACH ROW
BEGIN
    UPDATE rentals SET updated_at = CURRENT_TIMESTAMP WHERE rental_id = OLD.rental_id;
END;

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_customers_email ON customers(email);
CREATE INDEX IF NOT EXISTS idx_rentals_customer ON rentals(customer_id);
CREATE INDEX IF NOT EXISTS idx_rentals_dates ON rentals(start_date, end_date);
CREATE INDEX IF NOT EXISTS idx_inquiries_status ON inquiries(status);
```
