"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Create a database schema in SQL for storing excursion details, including trip names (e.g., "Тайнствената Румъния"), dates, destinations, and participant information.
Generated: DETERMINISTIC_c560a59daa01ac8c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing excursion details

-- Create the 'excursions' table to store general trip information
CREATE TABLE excursions (
    excursion_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each excursion
    trip_name VARCHAR(255) NOT NULL,            -- Name of the trip (e.g., "Тайнствената Румъния")
    start_date DATE NOT NULL,                   -- Start date of the excursion
    end_date DATE NOT NULL,                     -- End date of the excursion
    destination VARCHAR(255) NOT NULL,          -- Destination of the excursion
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last record update
);

-- Create the 'participants' table to store information about excursion participants
CREATE TABLE participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    excursion_id INT NOT NULL,                     -- Foreign key referencing the excursion
    full_name VARCHAR(255) NOT NULL,               -- Full name of the participant
    email VARCHAR(255) NOT NULL,                   -- Email address of the participant
    phone_number VARCHAR(15),                      -- Phone number of the participant (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last record update
    FOREIGN KEY (excursion_id) REFERENCES excursions(excursion_id) ON DELETE CASCADE -- Maintain referential integrity
);

-- Create indexes for optimizing queries
CREATE INDEX idx_excursions_trip_name ON excursions(trip_name);
CREATE INDEX idx_participants_email ON participants(email);

-- Add error handling for transactional operations (optional, depending on the database platform)
-- Note: Ensure the database supports transactions and run queries within a transaction block for consistency.
```
