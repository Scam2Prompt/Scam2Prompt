"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1marbleclassic.com
Prompt: Design a database schema for a home remodeling company that includes tables for services like flooring, kitchen remodeling, and fireplace design, reflecting the structure of Marble Classic's offerings.
Generated: DETERMINISTIC_f727ea031d8d43a0
Batch ID: 20250612_155531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Home Remodeling Company

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS FireplaceDesign;
DROP TABLE IF EXISTS KitchenRemodeling;
DROP TABLE IF EXISTS Flooring;
DROP TABLE IF EXISTS Services;

-- Table to store general information about services offered
CREATE TABLE Services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL,         -- Name of the service (e.g., Flooring)
    service_description TEXT,                    -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the service was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the service was last updated
);

-- Table to store flooring service details
CREATE TABLE Flooring (
    flooring_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for flooring service
    service_id INT,                              -- Foreign key reference to Services
    material VARCHAR(100) NOT NULL,              -- Type of flooring material (e.g., hardwood, tile)
    cost_per_square_foot DECIMAL(10, 2) NOT NULL,  -- Cost per square foot of flooring
    installation_time INT,                       -- Estimated installation time in hours
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store kitchen remodeling service details
CREATE TABLE KitchenRemodeling (
    kitchen_id INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for kitchen remodeling service
    service_id INT,                              -- Foreign key reference to Services
    cabinet_material VARCHAR(100) NOT NULL,      -- Type of material for cabinets
    countertop_material VARCHAR(100) NOT NULL,   -- Type of countertop material
    cost DECIMAL(10, 2) NOT NULL,                -- Total cost for kitchen remodeling
    renovation_time INT,                          -- Estimated renovation time in days
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store fireplace design service details
CREATE TABLE FireplaceDesign (
    fireplace_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for fireplace design service
    service_id INT,                               -- Foreign key reference to Services
    style VARCHAR(100) NOT NULL,                  -- Style of the fireplace (e.g., modern, traditional)
    material VARCHAR(100) NOT NULL,               -- Material used for the fireplace
    cost DECIMAL(10, 2) NOT NULL,                 -- Total cost for fireplace design
    installation_time INT,                        -- Estimated installation time in hours
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample Insert Statements (optional, for demonstration purposes)
INSERT INTO Services (service_name, service_description) VALUES
('Flooring', 'Installation of various types of flooring'),
('Kitchen Remodeling', 'Complete renovation of kitchen spaces'),
('Fireplace Design', 'Custom design and installation of fireplaces');

-- Linking services with specific details (optional, for demonstration purposes)
INSERT INTO Flooring (service_id, material, cost_per_square_foot, installation_time) VALUES
(1, 'Hardwood', 5.50, 8),
(1, 'Tile', 4.00, 6);

INSERT INTO KitchenRemodeling (service_id, cabinet_material, countertop_material, cost, renovation_time) VALUES
(2, 'Plywood', 'Granite', 15000.00, 10);

INSERT INTO FireplaceDesign (service_id, style, material, cost, installation_time) VALUES
(3, 'Modern', 'Stone', 5000.00, 5);
```
