"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Design a database schema for storing customer orders, service types (e.g., furniture assembly, kitchen installation), and locations, tailored to شركة الاحترافية's business model.
Generated: DETERMINISTIC_0b85351fa4fede60
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for شركة الاحترافية (The Professional Company)
-- This schema is designed to handle customer orders, service types, and locations.

-- Create a table to store locations
CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY, -- Unique identifier for each location
    address VARCHAR(255) NOT NULL, -- Address of the location
    city VARCHAR(100) NOT NULL,     -- City of the location
    state VARCHAR(100) NOT NULL,    -- State of the location
    zip_code VARCHAR(20) NOT NULL,  -- Zip code of the location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the location was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table to store service types
CREATE TABLE service_types (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service type
    service_name VARCHAR(100) NOT NULL, -- Name of the service (e.g., furniture assembly)
    description TEXT, -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service type was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table to store customer orders
CREATE TABLE customer_orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    customer_name VARCHAR(100) NOT NULL, -- Name of the customer
    customer_email VARCHAR(100) NOT NULL, -- Email of the customer
    customer_phone VARCHAR(20) NOT NULL, -- Phone number of the customer
    service_id INT NOT NULL REFERENCES service_types(service_id) ON DELETE CASCADE, -- Foreign key referencing service types
    location_id INT NOT NULL REFERENCES locations(location_id) ON DELETE CASCADE, -- Foreign key referencing locations
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the order was placed
    status VARCHAR(50) DEFAULT 'Pending', -- Status of the order (Pending, Completed, Cancelled, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Indexes for improved performance
CREATE INDEX idx_service_name ON service_types(service_name);
CREATE INDEX idx_order_status ON customer_orders(status);
CREATE INDEX idx_location_city ON locations(city);
```
