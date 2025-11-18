"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Create a database schema in SQL to store information about automotive parts (e.g., brake calipers, pivots) and their associated service center locations, such as Santa Cruz do Sul and São José.
Generated: DETERMINISTIC_def88ad723a18bd2
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for automotive parts and service centers

-- Create a database for automotive parts
CREATE DATABASE AutomotivePartsDB;

-- Use the created database
USE AutomotivePartsDB;

-- Table to store information about automotive parts
CREATE TABLE Parts (
    part_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each part
    part_name VARCHAR(100) NOT NULL,          -- Name of the automotive part
    part_description TEXT,                     -- Description of the automotive part
    part_price DECIMAL(10, 2) NOT NULL,       -- Price of the automotive part
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the part was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table to store service center locations
CREATE TABLE ServiceCenters (
    center_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service center
    center_name VARCHAR(100) NOT NULL,         -- Name of the service center
    address VARCHAR(255) NOT NULL,             -- Address of the service center
    city VARCHAR(100) NOT NULL,                -- City of the service center
    state VARCHAR(100) NOT NULL,               -- State of the service center
    zip_code VARCHAR(10) NOT NULL,             -- ZIP/Postal code
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the center was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table to associate parts with service centers
CREATE TABLE PartServiceCenter (
    part_service_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each association
    part_id INT NOT NULL,                             -- Foreign key referencing Parts
    center_id INT NOT NULL,                           -- Foreign key referencing ServiceCenters
    stock_quantity INT NOT NULL DEFAULT 0,           -- Quantity of the part in stock at this service center
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the association was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (part_id) REFERENCES Parts(part_id) ON DELETE CASCADE,  -- Establish foreign key relationship
    FOREIGN KEY (center_id) REFERENCES ServiceCenters(center_id) ON DELETE CASCADE -- Establish foreign key relationship
);

-- Sample data insertion (commented out for production readiness)
-- INSERT INTO Parts (part_name, part_description, part_price) VALUES
-- ('Brake Caliper', 'A device that houses the brake pads and pushes them against the disc.', 150.00),
-- ('Pivot', 'A rotating point for mechanical components.', 25.00);

-- INSERT INTO ServiceCenters (center_name, address, city, state, zip_code) VALUES
-- ('Santa Cruz do Sul Service Center', '123 Main St', 'Santa Cruz do Sul', 'RS', '96830-000'),
-- ('São José Service Center', '456 Elm St', 'São José', 'SC', '88101-000');

-- INSERT INTO PartServiceCenter (part_id, center_id, stock_quantity) VALUES
-- (1, 1, 10),  -- 10 Brake Calipers available at Santa Cruz do Sul
-- (2, 2, 5);   -- 5 Pivots available at São José
```
