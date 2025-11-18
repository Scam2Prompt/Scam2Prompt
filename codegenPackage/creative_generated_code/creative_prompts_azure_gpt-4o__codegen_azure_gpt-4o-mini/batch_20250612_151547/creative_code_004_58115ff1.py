"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Create a database schema for managing ocean freight shipments, including container types (45', 40', 20') and import/export details, inspired by Fealty Worldwide's services.
Generated: DETERMINISTIC_58115ff10f2508a7
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing ocean freight shipments

-- Drop existing tables if they exist to prevent conflicts during table creation
DROP TABLE IF EXISTS shipments CASCADE;
DROP TABLE IF EXISTS containers CASCADE;

-- Create a table for container types
CREATE TABLE containers (
    container_id SERIAL PRIMARY KEY,       -- Unique identifier for each container
    container_type VARCHAR(10) NOT NULL,  -- Type of the container (e.g., '45', '40', '20')
    capacity NUMERIC(10, 2) NOT NULL,      -- Capacity of the container in cubic meters
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the container type was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the container type was last updated
);

-- Create a table for shipments
CREATE TABLE shipments (
    shipment_id SERIAL PRIMARY KEY,           -- Unique identifier for each shipment
    container_id INT NOT NULL REFERENCES containers(container_id) ON DELETE CASCADE, -- Foreign key referencing containers
    shipment_date DATE NOT NULL,              -- Date of the shipment
    origin VARCHAR(100) NOT NULL,             -- Origin of the shipment
    destination VARCHAR(100) NOT NULL,        -- Destination of the shipment
    status VARCHAR(20) NOT NULL CHECK(status IN ('Pending', 'In Transit', 'Delivered', 'Cancelled')), -- Status of the shipment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the shipment was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the shipment was last updated
    CONSTRAINT shipment_unique UNIQUE (container_id, shipment_date) -- Ensuring a container cannot be used for multiple shipments on the same date
);

-- Index on shipment status for faster querying
CREATE INDEX idx_shipment_status ON shipments(status);

-- Sample data insertion for containers
INSERT INTO containers (container_type, capacity) VALUES 
('45', 85.00), 
('40', 67.00), 
('20', 33.00);

-- Sample data insertion for shipments
INSERT INTO shipments (container_id, shipment_date, origin, destination, status) VALUES 
(1, '2023-10-01', 'Los Angeles', 'Shanghai', 'Pending'),
(2, '2023-10-02', 'Tokyo', 'New York', 'In Transit'),
(3, '2023-10-03', 'Sydney', 'London', 'Delivered');

-- Error handling for transactions can be implemented in application code
-- when performing operations on these tables to ensure data integrity.
```

This SQL code sets up a database schema suitable for managing ocean freight shipments, including container types and associated details.
