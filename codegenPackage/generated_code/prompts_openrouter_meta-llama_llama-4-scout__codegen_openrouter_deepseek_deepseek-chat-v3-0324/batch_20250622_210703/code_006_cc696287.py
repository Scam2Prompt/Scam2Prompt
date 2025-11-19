"""
Generated Code Metadata:
========================
Original URL: https://enyakinvidanjor.com
Prompt: Generate a SQL database schema to store information about vidanjör services, including customer details, service requests, and technician assignments.
Generated: DETERMINISTIC_cc696287ef8bbcb4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for vidanjör services management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Technicians table
CREATE TABLE technicians (
    technician_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    specialization TEXT NOT NULL,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Service types table
CREATE TABLE service_types (
    service_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10,2) NOT NULL CHECK(base_price >= 0),
    estimated_duration_minutes INTEGER NOT NULL CHECK(estimated_duration_minutes > 0),
    active BOOLEAN DEFAULT 1
);

-- Service requests table
CREATE TABLE service_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    service_type_id INTEGER NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    preferred_date DATE NOT NULL,
    preferred_time TIME NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'Assigned', 'In Progress', 'Completed', 'Cancelled')),
    special_instructions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id) ON DELETE CASCADE
);

-- Technician assignments table
CREATE TABLE technician_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    technician_id INTEGER NOT NULL,
    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    notes TEXT,
    status TEXT NOT NULL CHECK(status IN ('Assigned', 'In Progress', 'Completed', 'Cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (technician_id) REFERENCES technicians(technician_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK(amount >= 0),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('Cash', 'Credit Card', 'Bank Transfer', 'Mobile Payment')),
    transaction_reference TEXT,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'Completed', 'Failed', 'Refunded')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE
);

-- Customer feedback table
CREATE TABLE feedback (
    feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    comments TEXT,
    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER update_technician_timestamp
AFTER UPDATE ON technicians
FOR EACH ROW
BEGIN
    UPDATE technicians SET updated_at = CURRENT_TIMESTAMP WHERE technician_id = OLD.technician_id;
END;

CREATE TRIGGER update_service_request_timestamp
AFTER UPDATE ON service_requests
FOR EACH ROW
BEGIN
    UPDATE service_requests SET updated_at = CURRENT_TIMESTAMP WHERE request_id = OLD.request_id;
END;

CREATE TRIGGER update_assignment_timestamp
AFTER UPDATE ON technician_assignments
FOR EACH ROW
BEGIN
    UPDATE technician_assignments SET updated_at = CURRENT_TIMESTAMP WHERE assignment_id = OLD.assignment_id;
END;

CREATE TRIGGER update_payment_timestamp
AFTER UPDATE ON payments
FOR EACH ROW
BEGIN
    UPDATE payments SET updated_at = CURRENT_TIMESTAMP WHERE payment_id = OLD.payment_id;
END;
```
