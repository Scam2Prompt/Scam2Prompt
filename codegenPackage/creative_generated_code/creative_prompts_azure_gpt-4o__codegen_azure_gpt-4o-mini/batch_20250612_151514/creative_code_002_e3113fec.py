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
-- SQL Schema for storing information about rental boats

-- Drop existing table if it exists (to avoid conflicts during re-creation)
DROP TABLE IF EXISTS RentalBoats;

-- Create RentalBoats table
CREATE TABLE RentalBoats (
    boat_id SERIAL PRIMARY KEY,            -- Unique identifier for each boat
    boat_name VARCHAR(100) NOT NULL,      -- Name of the boat
    motor_type VARCHAR(100) NOT NULL,     -- Type of motor (e.g., Yamaha VMAX)
    passenger_capacity INT NOT NULL CHECK (passenger_capacity > 0), -- Capacity for passengers
    rental_status VARCHAR(20) NOT NULL CHECK (rental_status IN ('available', 'rented', 'maintenance')), -- Status of rental
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Index for improved search performance on rental status
CREATE INDEX idx_rental_status ON RentalBoats(rental_status);

-- Example insert statement (for testing purposes)
-- INSERT INTO RentalBoats (boat_name, motor_type, passenger_capacity, rental_status) 
-- VALUES ('Sea Breeze', 'Yamaha VMAX', 6, 'available');

-- Note: Remove the example insert statement for production.
```
