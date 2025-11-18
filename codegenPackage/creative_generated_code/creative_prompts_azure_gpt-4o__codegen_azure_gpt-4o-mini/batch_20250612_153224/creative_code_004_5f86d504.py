"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Create a database schema in SQL to store information about horse riding tours, including tour names like "Moonshine Ride" and "Rari Discovery Ride," participant details, and preferred tour dates.
Generated: DETERMINISTIC_5f86d5049dd07084
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for horse riding tours

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS HorseRidingTours;

-- Switch to the created database
USE HorseRidingTours;

-- Table to store information about the tours
CREATE TABLE IF NOT EXISTS Tours (
    TourID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each tour
    TourName VARCHAR(255) NOT NULL,         -- Name of the tour
    TourDescription TEXT,                    -- Description of the tour
    TourDate DATE NOT NULL,                  -- Preferred date for the tour
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record update
);

-- Table to store participant information
CREATE TABLE IF NOT EXISTS Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each participant
    TourID INT NOT NULL,                          -- Foreign key referencing Tours
    ParticipantName VARCHAR(255) NOT NULL,        -- Name of the participant
    ParticipantEmail VARCHAR(255) NOT NULL UNIQUE, -- Email of the participant
    PhoneNumber VARCHAR(20),                      -- Optional phone number
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when participant registered
    FOREIGN KEY (TourID) REFERENCES Tours(TourID) ON DELETE CASCADE  -- Foreign key constraint
);

-- Sample data insertion for Tours table
INSERT INTO Tours (TourName, TourDescription, TourDate) VALUES
    ('Moonshine Ride', 'An adventurous ride under the moonlight.', '2023-11-01'),
    ('Rari Discovery Ride', 'A scenic ride through Rari landscapes.', '2023-11-15');

-- Sample data insertion for Participants table
INSERT INTO Participants (TourID, ParticipantName, ParticipantEmail, PhoneNumber) VALUES
    (1, 'John Doe', 'john.doe@example.com', '123-456-7890'),
    (1, 'Jane Smith', 'jane.smith@example.com', '098-765-4321'),
    (2, 'Alice Johnson', 'alice.johnson@example.com', NULL);
```
