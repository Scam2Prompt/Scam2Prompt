"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safetransfreight.com
Prompt: Create a database schema to manage warehousing, storage, and distribution services offered by Safetrans Freight Solutions, including flexible storage solutions.
Generated: DETERMINISTIC_b66918bfd2b6f701
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Safetrans Freight Solutions to manage warehousing, storage, and distribution services.
-- This includes flexible storage solutions.

-- Create a database named safetrans_warehouse
CREATE DATABASE safetrans_warehouse;

-- Switch to the newly created database
USE safetrans_warehouse;

-- Table to store information about warehouses
CREATE TABLE warehouses (
    warehouse_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each warehouse
    name VARCHAR(255) NOT NULL,                 -- Name of the warehouse
    location VARCHAR(255) NOT NULL,             -- Location of the warehouse
    capacity INT NOT NULL,                      -- Maximum storage capacity of the warehouse (in units)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the warehouse record was created
);

-- Table to store information about stored goods
CREATE TABLE goods (
    goods_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each stored goods item
    name VARCHAR(255) NOT NULL,                 -- Name of the goods
    description TEXT,                           -- Description of the goods
    quantity INT NOT NULL,                      -- Quantity of the goods in storage
    warehouse_id INT NOT NULL,                  -- Foreign key referencing the warehouse where the goods are stored
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the goods record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update of the goods record
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to store information about clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each client
    name VARCHAR(255) NOT NULL,                 -- Name of the client
    email VARCHAR(255) NOT NULL UNIQUE,         -- Email address of the client (must be unique)
    phone_number VARCHAR(15),                   -- Phone number of the client
    address VARCHAR(255),                       -- Address of the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client record was created
);

-- Table to track distribution transactions
CREATE TABLE distributions (
    distribution_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each distribution transaction
    client_id INT NOT NULL,                         -- Foreign key referencing the client involved in the transaction
    goods_id INT NOT NULL,                          -- Foreign key referencing the goods being distributed
    quantity INT NOT NULL,                          -- Quantity of the goods being distributed
    distribution_date DATE NOT NULL,                -- Date of the distribution
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the distribution record was created
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (goods_id) REFERENCES goods(goods_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to manage flexible storage solutions (e.g., temporary storage)
CREATE TABLE flexible_storage (
    storage_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each flexible storage record
    client_id INT NOT NULL,                    -- Foreign key referencing the client using the storage
    warehouse_id INT NOT NULL,                 -- Foreign key referencing the warehouse providing storage
    goods_id INT,                              -- Optional foreign key referencing stored goods (can be NULL for empty storage)
    start_date DATE NOT NULL,                  -- Start date for the storage
    end_date DATE,                             -- End date for the storage (can be NULL for ongoing storage)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the storage record was created
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (goods_id) REFERENCES goods(goods_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Indexing for performance optimization
CREATE INDEX idx_goods_warehouse ON goods (warehouse_id);
CREATE INDEX idx_distributions_client_goods ON distributions (client_id, goods_id);
CREATE INDEX idx_flexible_storage_dates ON flexible_storage (start_date, end_date);

-- Commit the schema changes
COMMIT;
```
