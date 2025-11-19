"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Generate a database schema for storing information about RIB fleets, including attributes like boat model (e.g., "Rock 36 Ionian"), equipment details, and availability status for chartering in Greece.
Generated: DETERMINISTIC_59ea497b9093d148
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for RIB fleets
CREATE DATABASE rib_fleet;

-- Use the rib_fleet database
USE rib_fleet;

-- Create a table for boat models
CREATE TABLE boat_models (
  id INT AUTO_INCREMENT,
  model_name VARCHAR(255) NOT NULL,
  manufacturer VARCHAR(100) NOT NULL,
  length DECIMAL(4, 2) NOT NULL,  -- in meters
  beam DECIMAL(3, 2) NOT NULL,    -- in meters
  draft DECIMAL(3, 2) NOT NULL,   -- in meters
  max_speed DECIMAL(5, 2) NOT NULL,  -- in knots
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (model_name)
);

-- Create a table for equipment details
CREATE TABLE equipment_details (
  id INT AUTO_INCREMENT,
  boat_model_id INT NOT NULL,
  engine_type VARCHAR(100) NOT NULL,
  engine_power INT NOT NULL,  -- in horsepower
  fuel_capacity DECIMAL(6, 2) NOT NULL,  -- in liters
  navigation_equipment JSON,  -- e.g., GPS, VHF, etc.
  safety_equipment JSON,      -- e.g., life jackets, flares, etc.
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (boat_model_id) REFERENCES boat_models(id) ON DELETE CASCADE
);

-- Create a table for RIB fleet information
CREATE TABLE rib_fleets (
  id INT AUTO_INCREMENT,
  boat_model_id INT NOT NULL,
  fleet_name VARCHAR(255) NOT NULL,
  fleet_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (boat_model_id) REFERENCES boat_models(id) ON DELETE CASCADE
);

-- Create a table for charter availability
CREATE TABLE charter_availability (
  id INT AUTO_INCREMENT,
  rib_fleet_id INT NOT NULL,
  charter_date DATE NOT NULL,
  is_available BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (rib_fleet_id) REFERENCES rib_fleets(id) ON DELETE CASCADE
);

-- Create a table for charter bookings
CREATE TABLE charter_bookings (
  id INT AUTO_INCREMENT,
  rib_fleet_id INT NOT NULL,
  charter_date DATE NOT NULL,
  customer_name VARCHAR(255) NOT NULL,
  booking_status ENUM('pending', 'confirmed', 'cancelled') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (rib_fleet_id) REFERENCES rib_fleets(id) ON DELETE CASCADE,
  UNIQUE KEY (rib_fleet_id, charter_date)
);

-- Create indexes for efficient querying
CREATE INDEX idx_boat_models_model_name ON boat_models (model_name);
CREATE INDEX idx_equipment_details_boat_model_id ON equipment_details (boat_model_id);
CREATE INDEX idx_rib_fleets_boat_model_id ON rib_fleets (boat_model_id);
CREATE INDEX idx_charter_availability_rib_fleet_id ON charter_availability (rib_fleet_id);
CREATE INDEX idx_charter_bookings_rib_fleet_id ON charter_bookings (rib_fleet_id);
```

```sql
-- sample_data.sql

-- Insert sample data into the database
INSERT INTO boat_models (model_name, manufacturer, length, beam, draft, max_speed)
VALUES
  ('Rock 36 Ionian', 'Sunseeker', 10.97, 3.35, 0.95, 35.00),
  ('Predator 34', 'Sunseeker', 10.36, 3.20, 0.90, 30.00),
  ('Riviera 35', 'Riviera', 10.67, 3.40, 0.92, 32.00);

INSERT INTO equipment_details (boat_model_id, engine_type, engine_power, fuel_capacity, navigation_equipment, safety_equipment)
VALUES
  (1, 'Diesel', 2 * 260, 550.00, '{"GPS": true, "VHF": true}', '{"life_jackets": 8, "flares": 6}'),
  (2, 'Diesel', 2 * 200, 450.00, '{"GPS": true, "VHF": true}', '{"life_jackets": 6, "flares": 4}'),
  (3, 'Diesel', 2 * 220, 500.00, '{"GPS": true, "VHF": true}', '{"life_jackets": 7, "flares": 5}');

INSERT INTO rib_fleets (boat_model_id, fleet_name, fleet_description)
VALUES
  (1, 'Greece RIB Fleet', 'RIB fleet based in Greece'),
  (2, 'Aegean Sea Fleet', 'RIB fleet operating in the Aegean Sea'),
  (3, 'Ionian Sea Fleet', 'RIB fleet operating in the Ionian Sea');

INSERT INTO charter_availability (rib_fleet_id, charter_date, is_available)
VALUES
  (1, '2024-09-16', TRUE),
  (1, '2024-09-17', FALSE),
  (2, '2024-09-16', TRUE),
  (2, '2024-09-18', TRUE),
  (3, '2024-09-17', TRUE),
  (3, '2024-09-19', FALSE);

INSERT INTO charter_bookings (rib_fleet_id, charter_date, customer_name, booking_status)
VALUES
  (1, '2024-09-17', 'John Doe', 'pending'),
  (2, '2024-09-16', 'Jane Smith', 'confirmed'),
  (3, '2024-09-19', 'Bob Johnson', 'cancelled');
```
