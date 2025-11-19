"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Create a SQL database schema to store information about carpet types, repair services, customer testimonials, and contact details, similar to Perfect Melbourne Carpet's database.
Generated: DETERMINISTIC_3b3abe6a4de95858
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Carpet Services Company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Carpet Types Table
CREATE TABLE IF NOT EXISTS carpet_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    material TEXT NOT NULL,
    durability_rating INTEGER CHECK(durability_rating BETWEEN 1 AND 5),
    price_per_sqm DECIMAL(10, 2) NOT NULL,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Repair Services Table
CREATE TABLE IF NOT EXISTS repair_services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    description TEXT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    estimated_duration_minutes INTEGER NOT NULL,
    is_available BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Customers Table
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    address TEXT,
    suburb TEXT,
    postcode TEXT CHECK(length(postcode) = 4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Testimonials Table
CREATE TABLE IF NOT EXISTS testimonials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    is_approved BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

-- Contact Submissions Table
CREATE TABLE IF NOT EXISTS contact_submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Appointments Table
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'confirmed', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES repair_services(id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_carpet_types_timestamp
AFTER UPDATE ON carpet_types
FOR EACH ROW
BEGIN
    UPDATE carpet_types SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER IF NOT EXISTS update_repair_services_timestamp
AFTER UPDATE ON repair_services
FOR EACH ROW
BEGIN
    UPDATE repair_services SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER IF NOT EXISTS update_customers_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER IF NOT EXISTS update_appointments_timestamp
AFTER UPDATE ON appointments
FOR EACH ROW
BEGIN
    UPDATE appointments SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_carpet_types_name ON carpet_types(name);
CREATE INDEX IF NOT EXISTS idx_repair_services_name ON repair_services(service_name);
CREATE INDEX IF NOT EXISTS idx_customers_email ON customers(email);
CREATE INDEX IF NOT EXISTS idx_appointments_date ON appointments(appointment_date);
CREATE INDEX IF NOT EXISTS idx_appointments_customer ON appointments(customer_id);
```
