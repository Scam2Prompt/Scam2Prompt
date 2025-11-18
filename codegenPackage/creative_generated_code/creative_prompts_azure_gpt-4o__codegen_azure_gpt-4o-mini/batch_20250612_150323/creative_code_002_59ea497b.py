"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Generate a database schema for storing information about RIB fleets, including attributes like boat model (e.g., "Rock 36 Ionian"), equipment details, and availability status for chartering in Greece.
Generated: DETERMINISTIC_59ea497b9093d148
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about RIB fleets
CREATE DATABASE rib_fleet_management;

USE rib_fleet_management;

-- Table to store information about boat models
CREATE TABLE BoatModels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model_name VARCHAR(255) NOT NULL UNIQUE, -- Unique name for each boat model
    manufacturer VARCHAR(255),                -- Manufacturer of the boat
    length DECIMAL(5,2),                      -- Length of the boat in meters
    beam DECIMAL(5,2),                        -- Beam of the boat in meters
    weight DECIMAL(10,2),                     -- Weight of the boat in kilograms
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store equipment details for each boat model
CREATE TABLE Equipment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    boat_model_id INT NOT NULL,               -- Foreign key referencing BoatModels
    equipment_name VARCHAR(255) NOT NULL,    -- Name of the equipment
    quantity INT DEFAULT 1,                   -- Quantity of this equipment
    FOREIGN KEY (boat_model_id) REFERENCES BoatModels(id) ON DELETE CASCADE -- Delete equipment if boat model is deleted
);

-- Table to store availability status for chartering
CREATE TABLE CharterAvailability (
    id INT AUTO_INCREMENT PRIMARY KEY,
    boat_model_id INT NOT NULL,               -- Foreign key referencing BoatModels
    availability_date DATE NOT NULL,          -- Date of availability
    is_available BOOLEAN NOT NULL DEFAULT TRUE, -- Availability status
    FOREIGN KEY (boat_model_id) REFERENCES BoatModels(id) ON DELETE CASCADE, -- Delete availability if boat model is deleted
    UNIQUE(boat_model_id, availability_date) -- Ensure no duplicate availability entries for the same date and boat model
);

-- Sample insertion of a boat model
INSERT INTO BoatModels (model_name, manufacturer, length, beam, weight) 
VALUES ('Rock 36 Ionian', 'Rock Boats', 11.0, 3.6, 3500);

-- Sample insertion of equipment for the boat model
INSERT INTO Equipment (boat_model_id, equipment_name, quantity) 
VALUES (LAST_INSERT_ID(), 'GPS Navigation', 1),
       (LAST_INSERT_ID(), 'Life Jackets', 10),
       (LAST_INSERT_ID(), 'Anchor', 1);

-- Sample insertion of availability status for chartering
INSERT INTO CharterAvailability (boat_model_id, availability_date, is_available) 
VALUES (LAST_INSERT_ID(), '2023-10-01', TRUE),
       (LAST_INSERT_ID(), '2023-10-02', FALSE);
```
