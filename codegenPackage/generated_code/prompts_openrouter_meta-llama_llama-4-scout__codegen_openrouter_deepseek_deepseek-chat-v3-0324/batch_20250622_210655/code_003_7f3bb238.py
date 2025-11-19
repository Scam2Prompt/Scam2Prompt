"""
Generated Code Metadata:
========================
Original URL: https://eveningdesertsafaridxb.ae
Prompt: "Design a database schema to store information about desert safari tour packages, including package details, activities, and customer bookings."
Generated: DETERMINISTIC_7f3bb238ca46dffd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Desert Safari Tour Packages

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Package Types Table
CREATE TABLE package_types (
    package_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Activities Table
CREATE TABLE activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    duration_minutes INTEGER,
    minimum_age INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Packages Table
CREATE TABLE packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    duration_hours DECIMAL(4, 1) NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (package_type_id) REFERENCES package_types(package_type_id)
);

-- Package Activities Junction Table
CREATE TABLE package_activities (
    package_id INTEGER NOT NULL,
    activity_id INTEGER NOT NULL,
    sequence_number INTEGER NOT NULL,
    PRIMARY KEY (package_id, activity_id),
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE
);

-- Customers Table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    country TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bookings Table
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tour_date DATE NOT NULL,
    number_of_people INTEGER NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    special_requests TEXT,
    status TEXT DEFAULT 'confirmed' CHECK(status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (package_id) REFERENCES packages(package_id)
);

-- Payments Table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT NOT NULL,
    transaction_id TEXT,
    status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'failed', 'refunded')),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_package_types
AFTER UPDATE ON package_types
FOR EACH ROW
BEGIN
    UPDATE package_types SET updated_at = CURRENT_TIMESTAMP WHERE package_type_id = OLD.package_type_id;
END;

CREATE TRIGGER update_activities
AFTER UPDATE ON activities
FOR EACH ROW
BEGIN
    UPDATE activities SET updated_at = CURRENT_TIMESTAMP WHERE activity_id = OLD.activity_id;
END;

CREATE TRIGGER update_packages
AFTER UPDATE ON packages
FOR EACH ROW
BEGIN
    UPDATE packages SET updated_at = CURRENT_TIMESTAMP WHERE package_id = OLD.package_id;
END;

CREATE TRIGGER update_customers
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER update_bookings
AFTER UPDATE ON bookings
FOR EACH ROW
BEGIN
    UPDATE bookings SET updated_at = CURRENT_TIMESTAMP WHERE booking_id = OLD.booking_id;
END;
```
