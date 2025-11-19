"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: "Design a database schema to store information about villas, including details like location (e.g., distance to Myrtos beach), amenities (e.g., swimming pool, table tennis), and capacity, inspired by the villa listings on villaandreas.gr."
Generated: DETERMINISTIC_e03f62ecfdc43519
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about villas

CREATE TABLE villas (
    villa_id SERIAL PRIMARY KEY, -- Unique identifier for each villa
    name VARCHAR(255) NOT NULL, -- Name of the villa
    location VARCHAR(255) NOT NULL, -- Location description
    distance_to_beach DECIMAL(5, 2) NOT NULL, -- Distance to Myrtos beach in kilometers
    capacity INT NOT NULL, -- Maximum capacity of the villa
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of villa creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE amenities (
    amenity_id SERIAL PRIMARY KEY, -- Unique identifier for each amenity
    name VARCHAR(100) NOT NULL UNIQUE -- Name of the amenity
);

CREATE TABLE villa_amenities (
    villa_id INT NOT NULL, -- Foreign key referencing villas
    amenity_id INT NOT NULL, -- Foreign key referencing amenities
    PRIMARY KEY (villa_id, amenity_id), -- Composite primary key
    FOREIGN KEY (villa_id) REFERENCES villas(villa_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for amenities
INSERT INTO amenities (name) VALUES 
('Swimming Pool'),
('Table Tennis'),
('Wi-Fi'),
('Air Conditioning'),
('Parking');

-- Note: Ensure to handle errors during data insertion and updates in application code.
-- Use transactions where necessary to maintain data integrity.
```
