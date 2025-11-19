"""
Generated Code Metadata:
========================
Original URL: https://t528.com
Prompt: Illustrate how to use the data from 星飞园 to create a database schema for storing aircraft cargo specifications, including fields for aircraft type, cargo dimensions, and container capacity.
Generated: DETERMINISTIC_50d16bc5c9ca975e
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing aircraft cargo specifications
-- This schema is designed to store information about aircraft type, cargo dimensions, and container capacity.

-- Create a table to store aircraft cargo specifications
CREATE TABLE AircraftCargoSpecifications (
    id SERIAL PRIMARY KEY, -- Unique identifier for each record
    aircraft_type VARCHAR(100) NOT NULL, -- Type of aircraft (e.g., Boeing 747, Airbus A320)
    cargo_length DECIMAL(10, 2) NOT NULL, -- Length of the cargo area in meters
    cargo_width DECIMAL(10, 2) NOT NULL, -- Width of the cargo area in meters
    cargo_height DECIMAL(10, 2) NOT NULL, -- Height of the cargo area in meters
    container_capacity INT NOT NULL, -- Maximum number of containers the aircraft can hold
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store container specifications
CREATE TABLE ContainerSpecifications (
    id SERIAL PRIMARY KEY, -- Unique identifier for each container specification
    container_type VARCHAR(100) NOT NULL, -- Type of container (e.g., ULD, LD3)
    container_length DECIMAL(10, 2) NOT NULL, -- Length of the container in meters
    container_width DECIMAL(10, 2) NOT NULL, -- Width of the container in meters
    container_height DECIMAL(10, 2) NOT NULL, -- Height of the container in meters
    max_weight DECIMAL(10, 2) NOT NULL, -- Maximum weight the container can hold in kilograms
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to map aircraft to container types
CREATE TABLE AircraftContainerMapping (
    id SERIAL PRIMARY KEY, -- Unique identifier for each mapping
    aircraft_id INT NOT NULL, -- Foreign key referencing AircraftCargoSpecifications
    container_id INT NOT NULL, -- Foreign key referencing ContainerSpecifications
    FOREIGN KEY (aircraft_id) REFERENCES AircraftCargoSpecifications (id) ON DELETE CASCADE,
    FOREIGN KEY (container_id) REFERENCES ContainerSpecifications (id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the mapping was created
);

-- Indexes for optimizing queries
CREATE INDEX idx_aircraft_type ON AircraftCargoSpecifications (aircraft_type);
CREATE INDEX idx_container_type ON ContainerSpecifications (container_type);

-- Example error handling: Ensure cargo dimensions are positive
CREATE TRIGGER validate_cargo_dimensions
BEFORE INSERT OR UPDATE ON AircraftCargoSpecifications
FOR EACH ROW
BEGIN
    IF NEW.cargo_length <= 0 OR NEW.cargo_width <= 0 OR NEW.cargo_height <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cargo dimensions must be positive values.';
    END IF;
END;

-- Example error handling: Ensure container dimensions are positive
CREATE TRIGGER validate_container_dimensions
BEFORE INSERT OR UPDATE ON ContainerSpecifications
FOR EACH ROW
BEGIN
    IF NEW.container_length <= 0 OR NEW.container_width <= 0 OR NEW.container_height <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Container dimensions must be positive values.';
    END IF;
END;
```
