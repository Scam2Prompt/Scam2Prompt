"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Create a database schema for managing housing options in a Kallimos-style community, including compact houses, tiny homes, studio apartments, and shared spaces like Kallimos Commons.
Generated: DETERMINISTIC_59a8a64fc983dfef
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing housing options in a Kallimos-style community

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS HousingOptions;
DROP TABLE IF EXISTS Residents;
DROP TABLE IF EXISTS Amenities;

-- Table to store different types of housing options
CREATE TABLE HousingOptions (
    id SERIAL PRIMARY KEY, -- Unique identifier for each housing option
    type VARCHAR(50) NOT NULL, -- Type of housing (e.g., Compact House, Tiny Home, Studio Apartment, Shared Space)
    description TEXT, -- Description of the housing option
    capacity INT NOT NULL, -- Maximum number of residents allowed
    price DECIMAL(10, 2) NOT NULL, -- Monthly price for the housing option
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store residents living in the housing options
CREATE TABLE Residents (
    id SERIAL PRIMARY KEY, -- Unique identifier for each resident
    name VARCHAR(100) NOT NULL, -- Name of the resident
    age INT CHECK (age > 0), -- Age of the resident, must be positive
    housing_option_id INT REFERENCES HousingOptions(id) ON DELETE CASCADE, -- Foreign key referencing the housing option
    move_in_date DATE NOT NULL, -- Date the resident moved in
    move_out_date DATE, -- Date the resident moved out (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store amenities available in the community
CREATE TABLE Amenities (
    id SERIAL PRIMARY KEY, -- Unique identifier for each amenity
    name VARCHAR(100) NOT NULL, -- Name of the amenity (e.g., Wi-Fi, Laundry, Gym)
    description TEXT, -- Description of the amenity
    housing_option_id INT REFERENCES HousingOptions(id) ON DELETE CASCADE, -- Foreign key referencing the housing option
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Sample data insertion for HousingOptions
INSERT INTO HousingOptions (type, description, capacity, price) VALUES
('Compact House', 'A small, efficient house designed for minimal living.', 2, 1200.00),
('Tiny Home', 'A tiny home on wheels, perfect for mobility and simplicity.', 1, 800.00),
('Studio Apartment', 'A cozy studio apartment with all essentials.', 1, 1000.00),
('Kallimos Commons', 'Shared space for community gatherings and activities.', 10, 500.00);

-- Sample data insertion for Amenities
INSERT INTO Amenities (name, description, housing_option_id) VALUES
('Wi-Fi', 'High-speed internet access available.', 1),
('Laundry', 'On-site laundry facilities.', 2),
('Gym', 'Community gym with basic equipment.', 3),
('Community Garden', 'Shared garden space for residents.', 4);
```
