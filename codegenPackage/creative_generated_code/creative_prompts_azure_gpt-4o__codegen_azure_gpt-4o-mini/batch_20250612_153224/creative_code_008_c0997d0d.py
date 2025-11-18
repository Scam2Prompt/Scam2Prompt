"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Design a database schema to store dumpster rental information, including service areas, dumpster sizes, and pricing, as described on the Purple Dumpster website.
Generated: DETERMINISTIC_c0997d0df564cfa2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for dumpster rental information

-- Drop existing tables if they exist to start fresh
DROP TABLE IF EXISTS Pricing;
DROP TABLE IF EXISTS DumpsterSizes;
DROP TABLE IF EXISTS ServiceAreas;
DROP TABLE IF EXISTS Dumpsters;

-- Table to store service area information
CREATE TABLE ServiceAreas (
    id SERIAL PRIMARY KEY, -- Unique identifier for each service area
    name VARCHAR(255) NOT NULL, -- Name of the service area
    description TEXT, -- Description of the service area (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store different dumpster sizes
CREATE TABLE DumpsterSizes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each dumpster size
    size VARCHAR(50) NOT NULL, -- Size of the dumpster (e.g., "10 yard", "20 yard")
    volume INTEGER NOT NULL, -- Volume in cubic yards
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store pricing information for dumpster rentals
CREATE TABLE Pricing (
    id SERIAL PRIMARY KEY, -- Unique identifier for each pricing record
    dumpster_size_id INT NOT NULL, -- Foreign key referencing DumpsterSizes
    service_area_id INT NOT NULL, -- Foreign key referencing ServiceAreas
    base_price DECIMAL(10, 2) NOT NULL, -- Base price for the dumpster rental
    daily_rate DECIMAL(10, 2) NOT NULL, -- Daily rate after the initial rental period
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (dumpster_size_id) REFERENCES DumpsterSizes(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (service_area_id) REFERENCES ServiceAreas(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about individual dumpster rentals
CREATE TABLE Dumpsters (
    id SERIAL PRIMARY KEY, -- Unique identifier for each dumpster
    dumpster_size_id INT NOT NULL, -- Foreign key referencing DumpsterSizes
    service_area_id INT NOT NULL, -- Foreign key referencing ServiceAreas
    rental_date TIMESTAMP NOT NULL, -- Date the dumpster was rented
    return_date TIMESTAMP, -- Date the dumpster was returned (nullable)
    total_price DECIMAL(10, 2), -- Total price for the rental (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (dumpster_size_id) REFERENCES DumpsterSizes(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (service_area_id) REFERENCES ServiceAreas(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Example data insertion
INSERT INTO ServiceAreas (name, description) VALUES 
('Downtown', 'Central business district with high rental demand'),
('Suburbs', 'Residential areas with moderate rental demand');

INSERT INTO DumpsterSizes (size, volume) VALUES 
('10 yard', 10),
('20 yard', 20),
('30 yard', 30);

INSERT INTO Pricing (dumpster_size_id, service_area_id, base_price, daily_rate) VALUES 
(1, 1, 200.00, 30.00),  -- Pricing for a 10 yard dumpster in Downtown
(2, 1, 300.00, 40.00),  -- Pricing for a 20 yard dumpster in Downtown
(1, 2, 180.00, 25.00),  -- Pricing for a 10 yard dumpster in Suburbs
(2, 2, 280.00, 35.00);  -- Pricing for a 20 yard dumpster in Suburbs

-- Ensure to handle errors in your application logic when interacting with these tables.
```
