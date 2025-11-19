"""
Generated Code Metadata:
========================
Original URL: https://bgalpina.com
Prompt: Create a database schema in SQL for storing excursion details, including trip names (e.g., "Тайнствената Румъния"), dates, destinations, and participant information.
Generated: DETERMINISTIC_c560a59daa01ac8c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing excursion details

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Participants;
DROP TABLE IF EXISTS Destinations;
DROP TABLE IF EXISTS Excursions;

-- Table to store excursion details
CREATE TABLE Excursions (
    excursion_id SERIAL PRIMARY KEY, -- Unique identifier for each excursion
    trip_name VARCHAR(255) NOT NULL, -- Name of the trip (e.g., "Тайнствената Румъния")
    start_date DATE NOT NULL,         -- Start date of the excursion
    end_date DATE NOT NULL,           -- End date of the excursion
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the excursion was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store destinations for each excursion
CREATE TABLE Destinations (
    destination_id SERIAL PRIMARY KEY, -- Unique identifier for each destination
    excursion_id INT NOT NULL,          -- Foreign key referencing the excursion
    destination_name VARCHAR(255) NOT NULL, -- Name of the destination
    FOREIGN KEY (excursion_id) REFERENCES Excursions(excursion_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store participant information
CREATE TABLE Participants (
    participant_id SERIAL PRIMARY KEY, -- Unique identifier for each participant
    excursion_id INT NOT NULL,          -- Foreign key referencing the excursion
    participant_name VARCHAR(255) NOT NULL, -- Name of the participant
    email VARCHAR(255) UNIQUE NOT NULL, -- Unique email for each participant
    phone_number VARCHAR(20),           -- Optional phone number for the participant
    FOREIGN KEY (excursion_id) REFERENCES Excursions(excursion_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_excursion_trip_name ON Excursions(trip_name);
CREATE INDEX idx_destination_name ON Destinations(destination_name);
CREATE INDEX idx_participant_email ON Participants(email);
```
