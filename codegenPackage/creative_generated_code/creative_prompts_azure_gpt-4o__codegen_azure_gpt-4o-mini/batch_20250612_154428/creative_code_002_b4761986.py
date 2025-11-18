"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Create a database schema in SQL for managing PG properties, including fields for location, price, room type, amenities (e.g., "CCTV," "24/7 security guard"), and tenant details, inspired by the Moms PG property listings.
Generated: DETERMINISTIC_b4761986ab1272a6
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL schema for managing PG properties

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Tenant CASCADE;
DROP TABLE IF EXISTS Property CASCADE;

-- Table to store PG Property details
CREATE TABLE Property (
    property_id SERIAL PRIMARY KEY,      -- Unique identifier for the property
    location VARCHAR(255) NOT NULL,      -- Location of the property
    price DECIMAL(10, 2) NOT NULL,       -- Monthly rental price
    room_type VARCHAR(50) NOT NULL,      -- Type of room (e.g., single, double, etc.)
    amenities TEXT[],                     -- Array of amenities available (e.g., CCTV, 24/7 security)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of property listing creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store tenant details
CREATE TABLE Tenant (
    tenant_id SERIAL PRIMARY KEY,         -- Unique identifier for the tenant
    property_id INT NOT NULL,             -- Foreign key referencing Property
    name VARCHAR(100) NOT NULL,           -- Tenant's name
    contact_number VARCHAR(15) NOT NULL,  -- Tenant's contact number
    move_in_date DATE NOT NULL,           -- Date when the tenant moved in
    move_out_date DATE,                   -- Optional: Date when the tenant moved out
    FOREIGN KEY (property_id) REFERENCES Property(property_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Index for quick lookup of properties based on location and price
CREATE INDEX idx_property_location_price ON Property(location, price);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO Property (location, price, room_type, amenities)
VALUES 
    ('Bangalore', 15000.00, 'Single', ARRAY['CCTV', '24/7 security guard']),
    ('Delhi', 12000.00, 'Double', ARRAY['CCTV', 'Wi-Fi']),
    ('Mumbai', 18000.00, 'Shared', ARRAY['24/7 security guard']);

INSERT INTO Tenant (property_id, name, contact_number, move_in_date)
VALUES 
    (1, 'John Doe', '9876543210', '2023-09-01'),
    (2, 'Jane Smith', '9123456789', '2023-09-10');
```
