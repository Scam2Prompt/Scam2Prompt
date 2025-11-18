"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fodyem.com
Prompt: Generate a database schema for managing travel packages, including fields for destinations like "Abidjan" and "Maroc & CAN," pricing, and availability.
Generated: DETERMINISTIC_c66b0a91b99c12ff
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing travel packages

CREATE TABLE Destinations (
    id SERIAL PRIMARY KEY, -- Unique identifier for each destination
    name VARCHAR(255) NOT NULL, -- Name of the destination
    region VARCHAR(255), -- Region of the destination (e.g., Africa, Europe)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE TravelPackages (
    id SERIAL PRIMARY KEY, -- Unique identifier for each travel package
    destination_id INT NOT NULL, -- Foreign key referencing the Destinations table
    package_name VARCHAR(255) NOT NULL, -- Name of the travel package
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Package price with a check constraint for non-negative values
    availability INT NOT NULL CHECK (availability >= 0), -- Number of available spots, non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (destination_id) REFERENCES Destinations(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Example insert statements for the Destinations table

INSERT INTO Destinations (name, region) VALUES
('Abidjan', 'West Africa'),
('Maroc', 'North Africa'),
('CAN', 'North America'); -- Assuming CAN refers to a specific destination

-- Example insert statement for the TravelPackages table

INSERT INTO TravelPackages (destination_id, package_name, price, availability) VALUES
(1, 'Abidjan Getaway', 499.99, 10),
(2, 'Explore Maroc', 599.00, 5),
(3, 'Canadian Adventures', 799.50, 8);

-- Note: Adjust the insert values as needed based on actual business requirements.
```
