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
-- Database schema for storing excursion details

-- Create the main table for excursions
CREATE TABLE Excursions (
    excursion_id SERIAL PRIMARY KEY, -- Unique identifier for each excursion
    trip_name VARCHAR(255) NOT NULL,  -- Name of the trip (e.g., "Тайнствената Румъния")
    excursion_date DATE NOT NULL,       -- Date of the excursion
    destination VARCHAR(255) NOT NULL   -- Destination of the excursion
);

-- Create a table for participants
CREATE TABLE Participants (
    participant_id SERIAL PRIMARY KEY,  -- Unique identifier for each participant
    excursion_id INT NOT NULL,          -- Reference to the associated excursion
    participant_name VARCHAR(255) NOT NULL, -- Name of the participant
    participant_email VARCHAR(255),      -- Email of the participant (optional)
    participant_phone VARCHAR(20),       -- Phone number of the participant (optional)
    
    -- Foreign key constraint to ensure referential integrity
    FOREIGN KEY (excursion_id) REFERENCES Excursions(excursion_id) 
    ON DELETE CASCADE -- Automatically remove participants if the excursion is deleted
);

-- Create a table for excursion itineraries (optional)
CREATE TABLE Itineraries (
    itinerary_id SERIAL PRIMARY KEY,    -- Unique identifier for each itinerary entry
    excursion_id INT NOT NULL,          -- Reference to the associated excursion
    stop_order INT NOT NULL,            -- Order of the stop in the itinerary
    stop_description TEXT NOT NULL,     -- Description of the stop
    
    -- Foreign key constraint to ensure referential integrity
    FOREIGN KEY (excursion_id) REFERENCES Excursions(excursion_id) 
    ON DELETE CASCADE -- Automatically remove itineraries if the excursion is deleted
);

-- Create an index on excursion dates for faster queries
CREATE INDEX idx_excursion_date ON Excursions(excursion_date);
```
