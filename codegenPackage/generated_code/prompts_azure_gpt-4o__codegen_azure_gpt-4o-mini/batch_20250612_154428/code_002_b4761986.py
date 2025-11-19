"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: Create a database schema in SQL for managing PG properties, including fields for location, price, room type, amenities (e.g., "CCTV," "24/7 security guard"), and tenant details, inspired by the Moms PG property listings.
Generated: DETERMINISTIC_b4761986ab1272a6
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing PG properties

-- Create a table for storing property details
CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY, -- Unique identifier for each property
    location VARCHAR(255) NOT NULL, -- Location of the property
    price DECIMAL(10, 2) NOT NULL, -- Monthly rental price
    room_type VARCHAR(100) NOT NULL, -- Type of room (e.g., single, double, shared)
    amenities TEXT[], -- Array of amenities available at the property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table for storing tenant details
CREATE TABLE tenants (
    tenant_id SERIAL PRIMARY KEY, -- Unique identifier for each tenant
    name VARCHAR(100) NOT NULL, -- Name of the tenant
    age INT CHECK (age > 0), -- Age of the tenant
    phone_number VARCHAR(15) UNIQUE NOT NULL, -- Unique phone number of the tenant
    email VARCHAR(255) UNIQUE NOT NULL, -- Unique email address of the tenant
    property_id INT REFERENCES properties(property_id) ON DELETE CASCADE, -- Foreign key referencing the property
    move_in_date DATE NOT NULL, -- Date the tenant moves in
    move_out_date DATE, -- Date the tenant moves out (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the tenant was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create an index on the properties table for faster location searches
CREATE INDEX idx_location ON properties(location);

-- Create an index on the tenants table for faster phone number searches
CREATE INDEX idx_phone_number ON tenants(phone_number);
```
