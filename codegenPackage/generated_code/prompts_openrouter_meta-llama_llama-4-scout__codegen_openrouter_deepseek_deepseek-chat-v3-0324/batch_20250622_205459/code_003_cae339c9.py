"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: "Design a database schema to store information about waste collection, recycling, and renewable product sales for a company like Clibiya, including fields for tracking waste types and quantities."
Generated: DETERMINISTIC_cae339c9a99e17b2
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for waste management and recycling tracking system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Waste types table
CREATE TABLE IF NOT EXISTS waste_types (
    waste_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL CHECK (category IN ('organic', 'plastic', 'paper', 'metal', 'glass', 'electronic', 'hazardous', 'other')),
    is_recyclable BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Collection points table
CREATE TABLE IF NOT EXISTS collection_points (
    point_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    contact_person TEXT,
    contact_phone TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Waste collection records table
CREATE TABLE IF NOT EXISTS waste_collections (
    collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    point_id INTEGER NOT NULL,
    collection_date DATE NOT NULL,
    collected_by TEXT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (point_id) REFERENCES collection_points(point_id) ON DELETE CASCADE
);

-- Waste collection details (quantities by type)
CREATE TABLE IF NOT EXISTS collection_details (
    detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection_id INTEGER NOT NULL,
    waste_type_id INTEGER NOT NULL,
    quantity REAL NOT NULL CHECK (quantity > 0),
    unit TEXT NOT NULL DEFAULT 'kg' CHECK (unit IN ('kg', 'liter', 'piece')),
    FOREIGN KEY (collection_id) REFERENCES waste_collections(collection_id) ON DELETE CASCADE,
    FOREIGN KEY (waste_type_id) REFERENCES waste_types(waste_type_id) ON DELETE CASCADE,
    UNIQUE(collection_id, waste_type_id)
);

-- Recycling centers table
CREATE TABLE IF NOT EXISTS recycling_centers (
    center_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    contact_person TEXT,
    contact_phone TEXT,
    accepted_waste_types TEXT NOT NULL, -- Comma-separated list of waste_type_ids
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Recycling transactions table
CREATE TABLE IF NOT EXISTS recycling_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    center_id INTEGER NOT NULL,
    transaction_date DATE NOT NULL,
    processed_by TEXT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (center_id) REFERENCES recycling_centers(center_id) ON DELETE CASCADE
);

-- Recycling transaction details
CREATE TABLE IF NOT EXISTS recycling_details (
    detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id INTEGER NOT NULL,
    waste_type_id INTEGER NOT NULL,
    quantity_received REAL NOT NULL CHECK (quantity_received > 0),
    quantity_processed REAL NOT NULL CHECK (quantity_processed >= 0),
    processing_method TEXT,
    unit TEXT NOT NULL DEFAULT 'kg' CHECK (unit IN ('kg', 'liter', 'piece')),
    FOREIGN KEY (transaction_id) REFERENCES recycling_transactions(transaction_id) ON DELETE CASCADE,
    FOREIGN KEY (waste_type_id) REFERENCES waste_types(waste_type_id) ON DELETE CASCADE,
    UNIQUE(transaction_id, waste_type_id)
);

-- Renewable products table
CREATE TABLE IF NOT EXISTS renewable_products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL CHECK (category IN ('recycled', 'upcycled', 'biodegradable', 'compost', 'other')),
    unit_price REAL NOT NULL CHECK (unit_price > 0),
    unit TEXT NOT NULL DEFAULT 'piece' CHECK (unit IN ('piece', 'kg', 'liter', 'set')),
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product sales table
CREATE TABLE IF NOT EXISTS product_sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    customer_name TEXT,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL CHECK (unit_price > 0),
    discount REAL DEFAULT 0 CHECK (discount >= 0),
    payment_method TEXT CHECK (payment_method IN ('cash', 'card', 'online', 'other')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES renewable_products(product_id) ON DELETE CASCADE
);

-- Waste processing methods table
CREATE TABLE IF NOT EXISTS processing_methods (
    method_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    efficiency REAL CHECK (efficiency >= 0 AND efficiency <= 100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Waste to product mapping table
CREATE TABLE IF NOT EXISTS waste_to_product (
    mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
    waste_type_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    conversion_rate REAL NOT NULL CHECK (conversion_rate > 0),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (waste_type_id) REFERENCES waste_types(waste_type_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES renewable_products(product_id) ON DELETE CASCADE,
    UNIQUE(waste_type_id, product_id)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_waste_collections_date ON waste_collections(collection_date);
CREATE INDEX IF NOT EXISTS idx_collection_details_type ON collection_details(waste_type_id);
CREATE INDEX IF NOT EXISTS idx_recycling_transactions_date ON recycling_transactions(transaction_date);
CREATE INDEX IF NOT EXISTS idx_product_sales_date ON product_sales(sale_date);
CREATE INDEX IF NOT EXISTS idx_product_sales_product ON product_sales(product_id);
```
