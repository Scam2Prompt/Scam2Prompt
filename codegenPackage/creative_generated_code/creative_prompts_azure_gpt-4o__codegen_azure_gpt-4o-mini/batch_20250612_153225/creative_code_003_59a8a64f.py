"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Create a database schema for managing housing options in a Kallimos-style community, including compact houses, tiny homes, studio apartments, and shared spaces like Kallimos Commons.
Generated: DETERMINISTIC_59a8a64fc983dfef
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing housing options in a Kallimos-style community

-- Drop existing tables if they exist for a clean setup
DROP TABLE IF EXISTS HousingOptions;
DROP TABLE IF EXISTS HousingTypes;
DROP TABLE IF EXISTS Residents;
DROP TABLE IF EXISTS Amenities;

-- Table for different types of housing
CREATE TABLE HousingTypes (
    id SERIAL PRIMARY KEY,  -- Unique identifier for each housing type
    type_name VARCHAR(50) NOT NULL UNIQUE,  -- Name of the housing type (e.g., Compact House, Tiny Home)
    description TEXT,  -- Description of the housing type
    max_occupancy INT CHECK (max_occupancy > 0)  -- Maximum number of residents allowed
);

-- Table for housing options available in the community
CREATE TABLE HousingOptions (
    id SERIAL PRIMARY KEY,  -- Unique identifier for each housing option
    housing_type_id INT REFERENCES HousingTypes(id) ON DELETE CASCADE,  -- Foreign key referencing HousingTypes
    address VARCHAR(255) NOT NULL,  -- Address of the housing option
    total_units INT CHECK (total_units > 0),  -- Total units available
    available_units INT CHECK (available_units >= 0),  -- Units currently available
    price DECIMAL(10, 2) CHECK (price >= 0),  -- Price per unit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Table for residents who live in the housing options
CREATE TABLE Residents (
    id SERIAL PRIMARY KEY,  -- Unique identifier for each resident
    name VARCHAR(100) NOT NULL,  -- Resident's name
    housing_option_id INT REFERENCES HousingOptions(id) ON DELETE SET NULL,  -- Foreign key referencing HousingOptions
    move_in_date DATE NOT NULL,  -- Date the resident moved in
    move_out_date DATE,  -- Date the resident moved out (optional)
    UNIQUE (name, housing_option_id)  -- Ensure one resident per housing option
);

-- Table for amenities provided in the community
CREATE TABLE Amenities (
    id SERIAL PRIMARY KEY,  -- Unique identifier for each amenity
    name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the amenity (e.g., Swimming Pool, Gym)
    description TEXT  -- Description of the amenity
);

-- Table for linking housing options with their amenities
CREATE TABLE HousingAmenities (
    housing_option_id INT REFERENCES HousingOptions(id) ON DELETE CASCADE,  -- Foreign key referencing HousingOptions
    amenity_id INT REFERENCES Amenities(id) ON DELETE CASCADE,  -- Foreign key referencing Amenities
    PRIMARY KEY (housing_option_id, amenity_id)  -- Composite primary key to ensure uniqueness
);

-- Insert predefined housing types
INSERT INTO HousingTypes (type_name, description, max_occupancy) VALUES
('Compact House', 'A small house designed for efficiency and comfort.', 4),
('Tiny Home', 'A very small home that maximizes minimal living.', 2),
('Studio Apartment', 'An apartment that combines living and sleeping areas.', 2),
('Kallimos Commons', 'Shared community space with facilities for residents.', 20);

-- Error handling and logging can be added in application logic when interacting with these tables.
```
