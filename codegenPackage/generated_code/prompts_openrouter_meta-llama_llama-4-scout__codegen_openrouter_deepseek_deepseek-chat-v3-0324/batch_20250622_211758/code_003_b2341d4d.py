"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Design a simple database schema to store information about wood products, including their applications, advantages, and treatment processes, similar to those described on the Trattar Madeiras website."
Generated: DETERMINISTIC_b2341d4da1332be3
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for wood products information
-- Tables include products, applications, advantages, and treatment processes

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create Products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    species TEXT NOT NULL,
    density REAL,
    hardness TEXT,
    durability TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Applications table
CREATE TABLE IF NOT EXISTS applications (
    application_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    application_type TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create Advantages table
CREATE TABLE IF NOT EXISTS advantages (
    advantage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    advantage TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create Treatment Processes table
CREATE TABLE IF NOT EXISTS treatment_processes (
    process_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    process_name TEXT NOT NULL,
    description TEXT,
    duration TEXT,
    effectiveness TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create Images table for product images
CREATE TABLE IF NOT EXISTS product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create trigger to update timestamps on row modification
CREATE TRIGGER IF NOT EXISTS update_product_timestamp
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

CREATE TRIGGER IF NOT EXISTS update_application_timestamp
AFTER UPDATE ON applications
BEGIN
    UPDATE applications SET updated_at = CURRENT_TIMESTAMP WHERE application_id = OLD.application_id;
END;

CREATE TRIGGER IF NOT EXISTS update_advantage_timestamp
AFTER UPDATE ON advantages
BEGIN
    UPDATE advantages SET updated_at = CURRENT_TIMESTAMP WHERE advantage_id = OLD.advantage_id;
END;

CREATE TRIGGER IF NOT EXISTS update_process_timestamp
AFTER UPDATE ON treatment_processes
BEGIN
    UPDATE treatment_processes SET updated_at = CURRENT_TIMESTAMP WHERE process_id = OLD.process_id;
END;

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_products_name ON products(name);
CREATE INDEX IF NOT EXISTS idx_products_species ON products(species);
CREATE INDEX IF NOT EXISTS idx_applications_product ON applications(product_id);
CREATE INDEX IF NOT EXISTS idx_advantages_product ON advantages(product_id);
CREATE INDEX IF NOT EXISTS idx_processes_product ON treatment_processes(product_id);
CREATE INDEX IF NOT EXISTS idx_images_product ON product_images(product_id);
```
