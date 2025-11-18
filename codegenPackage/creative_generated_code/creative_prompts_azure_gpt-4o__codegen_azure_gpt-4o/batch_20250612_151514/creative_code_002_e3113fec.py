"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Create a database schema using SQL for storing information about rental boats, including attributes like boat name, motor type (e.g., Yamaha VMAX), passenger capacity, and rental status.
Generated: DETERMINISTIC_e3113fece2f1e393
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing information about rental boats.
-- This schema includes attributes like boat name, motor type, passenger capacity, and rental status.

-- Create the table 'rental_boats' to store boat information.
CREATE TABLE rental_boats (
    boat_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each boat.
    boat_name VARCHAR(100) NOT NULL,              -- Name of the boat.
    motor_type VARCHAR(100) NOT NULL,             -- Type of motor (e.g., Yamaha VMAX).
    passenger_capacity INT NOT NULL CHECK (passenger_capacity > 0), -- Maximum passenger capacity (must be > 0).
    rental_status ENUM('Available', 'Rented', 'Maintenance') NOT NULL DEFAULT 'Available', -- Rental status of the boat.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp.
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last updated timestamp.
);

-- Add an index to optimize searches based on rental status.
CREATE INDEX idx_rental_status ON rental_boats (rental_status);

-- Insert sample data into the table for testing purposes.
INSERT INTO rental_boats (boat_name, motor_type, passenger_capacity, rental_status) VALUES
('Sea Breeze', 'Yamaha VMAX', 8, 'Available'),
('Ocean Explorer', 'Honda BF200', 10, 'Maintenance'),
('Wave Rider', 'Mercury FourStroke', 6, 'Rented'),
('Lake Cruiser', 'Suzuki DF250', 12, 'Available');

-- Query to test the schema.
-- SELECT * FROM rental_boats WHERE rental_status = 'Available';

-- To ensure best practices, it's advisable to set up proper backups and monitor the database for performance.
```
