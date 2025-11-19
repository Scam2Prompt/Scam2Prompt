"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: Create a database schema for tracking waste collection, recycling, and sales processes, incorporating Clibiya's focus on used oil, edible fats, rejected plastic, and organic waste.
Generated: DETERMINISTIC_37af51ba0e51e2ce
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Clibiya's waste management system
-- Tracks collection, recycling, and sales processes for various waste types

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Waste types table
CREATE TABLE waste_types (
    waste_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    unit_of_measure TEXT NOT NULL,
    is_hazardous BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Suppliers table
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT,
    tax_id TEXT,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Collection points table
CREATE TABLE collection_points (
    point_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    contact_phone TEXT,
    latitude REAL,
    longitude REAL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Collection records table
CREATE TABLE collections (
    collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    point_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    waste_type_id INTEGER NOT NULL,
    quantity REAL NOT NULL,
    collection_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (point_id) REFERENCES collection_points(point_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (waste_type_id) REFERENCES waste_types(waste_type_id)
);

-- Processing facilities table
CREATE TABLE processing_facilities (
    facility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    contact_phone TEXT,
    capacity REAL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Processing records table
CREATE TABLE processing (
    processing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    facility_id INTEGER NOT NULL,
    waste_type_id INTEGER NOT NULL,
    input_quantity REAL NOT NULL,
    output_quantity REAL NOT NULL,
    output_product TEXT,
    processing_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (facility_id) REFERENCES processing_facilities(facility_id),
    FOREIGN KEY (waste_type_id) REFERENCES waste_types(waste_type_id)
);

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT,
    tax_id TEXT,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sales records table
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_type TEXT NOT NULL,
    quantity REAL NOT NULL,
    unit_price REAL NOT NULL,
    total_amount REAL NOT NULL,
    sale_date DATE NOT NULL,
    invoice_number TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Inventory table
CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_type TEXT NOT NULL,
    quantity REAL NOT NULL,
    unit_of_measure TEXT NOT NULL,
    location TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transportation records table
CREATE TABLE transportation (
    transport_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id INTEGER NOT NULL,
    destination_id INTEGER NOT NULL,
    waste_type_id INTEGER NOT NULL,
    quantity REAL NOT NULL,
    transport_date DATE NOT NULL,
    vehicle_details TEXT,
    driver_details TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (waste_type_id) REFERENCES waste_types(waste_type_id)
);

-- Quality control records table
CREATE TABLE quality_control (
    qc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id INTEGER NOT NULL,
    waste_type_id INTEGER NOT NULL,
    test_type TEXT NOT NULL,
    test_result TEXT NOT NULL,
    test_date DATE NOT NULL,
    conducted_by TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (waste_type_id) REFERENCES waste_types(waste_type_id)
);

-- Insert initial waste types
INSERT INTO waste_types (name, description, unit_of_measure, is_hazardous)
VALUES 
    ('Used Oil', 'Waste lubricating oil from vehicles and machinery', 'liters', 1),
    ('Edible Fats', 'Used cooking oil and food industry fats', 'liters', 0),
    ('Rejected Plastic', 'Non-recyclable plastic waste', 'kilograms', 0),
    ('Organic Waste', 'Food waste and other biodegradable materials', 'kilograms', 0);

-- Create indexes for performance
CREATE INDEX idx_collections_date ON collections(collection_date);
CREATE INDEX idx_sales_date ON sales(sale_date);
CREATE INDEX idx_processing_date ON processing(processing_date);
CREATE INDEX idx_transportation_date ON transportation(transport_date);
```
