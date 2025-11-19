"""
Generated Code Metadata:
========================
Original URL: https://www.aspuddensstad.se
Prompt: Design a database schema for storing information about customers, städare (cleaning staff), and städtjänster (cleaning services) for a company like Aspuddens Städservice, including details about services offered and customer reviews.
Generated: DETERMINISTIC_09336a699712103c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Aspuddens Städservice

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    city TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%_@__%.__%')
);

CREATE TABLE IF NOT EXISTS cleaning_staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    city TEXT NOT NULL,
    hire_date DATE NOT NULL,
    hourly_rate DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%_@__%.__%'),
    CHECK (hourly_rate > 0)
);

CREATE TABLE IF NOT EXISTS service_types (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10,2) NOT NULL,
    duration_minutes INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (base_price > 0),
    CHECK (duration_minutes > 0)
);

CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    staff_id INTEGER,
    booking_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending', -- pending, confirmed, completed, cancelled
    special_instructions TEXT,
    price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service_types(service_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES cleaning_staff(staff_id) ON DELETE SET NULL,
    CHECK (status IN ('pending', 'confirmed', 'completed', 'cancelled')),
    CHECK (price > 0),
    CHECK (end_time > start_time)
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL UNIQUE,
    customer_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES cleaning_staff(staff_id) ON DELETE CASCADE,
    CHECK (rating BETWEEN 1 AND 5)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_customers_email ON customers(email);
CREATE INDEX IF NOT EXISTS idx_staff_email ON cleaning_staff(email);
CREATE INDEX IF NOT EXISTS idx_bookings_customer ON bookings(customer_id);
CREATE INDEX IF NOT EXISTS idx_bookings_staff ON bookings(staff_id);
CREATE INDEX IF NOT EXISTS idx_bookings_date ON bookings(booking_date);
CREATE INDEX IF NOT EXISTS idx_reviews_staff ON reviews(staff_id);
CREATE INDEX IF NOT EXISTS idx_reviews_customer ON reviews(customer_id);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_customer_timestamp
AFTER UPDATE ON customers
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = NEW.customer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_staff_timestamp
AFTER UPDATE ON cleaning_staff
BEGIN
    UPDATE cleaning_staff SET updated_at = CURRENT_TIMESTAMP WHERE staff_id = NEW.staff_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_timestamp
AFTER UPDATE ON service_types
BEGIN
    UPDATE service_types SET updated_at = CURRENT_TIMESTAMP WHERE service_id = NEW.service_id;
END;

CREATE TRIGGER IF NOT EXISTS update_booking_timestamp
AFTER UPDATE ON bookings
BEGIN
    UPDATE bookings SET updated_at = CURRENT_TIMESTAMP WHERE booking_id = NEW.booking_id;
END;
```
