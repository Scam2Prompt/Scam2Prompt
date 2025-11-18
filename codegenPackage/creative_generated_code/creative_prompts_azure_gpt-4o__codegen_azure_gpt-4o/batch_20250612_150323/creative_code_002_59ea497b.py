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
-- Database Schema for storing information about RIB fleets

-- Create the `boat_models` table to store distinct RIB boat models
CREATE TABLE boat_models (
    model_id SERIAL PRIMARY KEY,          -- Unique identifier for each boat model
    model_name VARCHAR(100) NOT NULL,     -- Name of the boat model (e.g., "Rock 36 Ionian")
    manufacturer VARCHAR(100),            -- Manufacturer name (e.g., "Rock Boats Ltd")
    capacity INT NOT NULL,                -- Maximum number of passengers the boat can carry
    length FLOAT NOT NULL,                -- Length of the boat in meters
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the model entry was created
);

-- Create the `equipment` table to store equipment details
CREATE TABLE equipment (
    equipment_id SERIAL PRIMARY KEY,      -- Unique identifier for equipment
    equipment_name VARCHAR(100) NOT NULL,-- Name of the equipment (e.g., "GPS", "Life Jackets")
    description TEXT,                     -- Additional details about the equipment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the equipment entry was created
);

-- Create a junction table `boat_equipment` to associate equipment with specific boat models
CREATE TABLE boat_equipment (
    boat_equipment_id SERIAL PRIMARY KEY, -- Unique identifier for the association
    model_id INT NOT NULL,                -- Foreign key referencing `boat_models.model_id`
    equipment_id INT NOT NULL,            -- Foreign key referencing `equipment.equipment_id`
    quantity INT NOT NULL,                -- Number of this equipment available in the boat
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the association entry was created
    FOREIGN KEY (model_id) REFERENCES boat_models(model_id) ON DELETE CASCADE,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE
);

-- Create the `boats` table to store individual boats in the fleet
CREATE TABLE boats (
    boat_id SERIAL PRIMARY KEY,           -- Unique identifier for each boat
    model_id INT NOT NULL,                -- Foreign key referencing `boat_models.model_id`
    registration_number VARCHAR(50) NOT NULL UNIQUE, -- Unique registration number for the boat
    availability_status BOOLEAN NOT NULL DEFAULT TRUE, -- Status of availability for chartering (true = available)
    location VARCHAR(100),                -- Current location in Greece
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the boat entry was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the entry was last updated
    FOREIGN KEY (model_id) REFERENCES boat_models(model_id) ON DELETE CASCADE
);

-- Create the `chartering_history` table to record chartering details
CREATE TABLE chartering_history (
    charter_id SERIAL PRIMARY KEY,        -- Unique identifier for each chartering record
    boat_id INT NOT NULL,                 -- Foreign key referencing `boats.boat_id`
    charter_start_date DATE NOT NULL,     -- Start date of the chartering period
    charter_end_date DATE NOT NULL,       -- End date of the chartering period
    customer_name VARCHAR(100) NOT NULL, -- Name of the customer who chartered the boat
    contact_info VARCHAR(150),           -- Contact details of the customer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the chartering record was created
    FOREIGN KEY (boat_id) REFERENCES boats(boat_id) ON DELETE CASCADE
);

-- Create indices to optimize queries (optional but recommended)
CREATE INDEX idx_boat_availability ON boats (availability_status);
CREATE INDEX idx_chartering_dates ON chartering_history (charter_start_date, charter_end_date);

-- Error Handling Example (Ensure Referential Integrity)
-- If any foreign key constraints fail, the system will throw an error. 
-- You can add try-catch mechanisms in application code to handle such cases.
```
