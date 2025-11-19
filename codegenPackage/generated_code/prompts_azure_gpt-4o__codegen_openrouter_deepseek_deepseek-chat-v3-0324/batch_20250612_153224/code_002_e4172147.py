"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: Create a database schema using SQL to store customer information, project details (e.g., cabinet type, finish options), and consultation schedules for a cabinet refacing company like Stockyard Refacing.
Generated: DETERMINISTIC_e41721471bf32e35
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Stockyard Refacing company
-- Creates tables for customer information, project details, and consultation schedules

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE CHECK(email LIKE '%_@__%.__%'),
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cabinet types table
CREATE TABLE IF NOT EXISTS cabinet_types (
    cabinet_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL CHECK(base_price >= 0)
);

-- Finish options table
CREATE TABLE IF NOT EXISTS finish_options (
    finish_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    price_modifier DECIMAL(10, 2) DEFAULT 0.00
);

-- Hardware options table
CREATE TABLE IF NOT EXISTS hardware_options (
    hardware_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    price_modifier DECIMAL(10, 2) DEFAULT 0.00
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    cabinet_type_id INTEGER NOT NULL,
    finish_id INTEGER NOT NULL,
    hardware_id INTEGER,
    project_name TEXT NOT NULL,
    description TEXT,
    total_price DECIMAL(10, 2) NOT NULL CHECK(total_price >= 0),
    start_date DATE,
    estimated_completion_date DATE,
    status TEXT NOT NULL DEFAULT 'Pending' CHECK(status IN ('Pending', 'In Progress', 'Completed', 'Cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (cabinet_type_id) REFERENCES cabinet_types(cabinet_type_id),
    FOREIGN KEY (finish_id) REFERENCES finish_options(finish_id),
    FOREIGN KEY (hardware_id) REFERENCES hardware_options(hardware_id)
);

-- Consultations table
CREATE TABLE IF NOT EXISTS consultations (
    consultation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    project_id INTEGER,
    consultant_name TEXT NOT NULL,
    consultation_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    notes TEXT,
    status TEXT NOT NULL DEFAULT 'Scheduled' CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL,
    CHECK (end_time > start_time)
);

-- Project images table
CREATE TABLE IF NOT EXISTS project_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    description TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_timestamp
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER IF NOT EXISTS update_consultation_timestamp
AFTER UPDATE ON consultations
FOR EACH ROW
BEGIN
    UPDATE consultations SET updated_at = CURRENT_TIMESTAMP WHERE consultation_id = OLD.consultation_id;
END;
```
