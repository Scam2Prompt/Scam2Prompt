"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Design a database schema to store information about aviation events, teams, and photographers featured on Spotters Brasil, and provide SQL code to populate the database.
Generated: DETERMINISTIC_1aa351be6712f8ed
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for aviation events
CREATE DATABASE SpottersBrasil;

-- Use the newly created database
USE SpottersBrasil;

-- Table to store information about aviation events
CREATE TABLE Events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    event_name VARCHAR(255) NOT NULL,         -- Name of the event
    event_date DATE NOT NULL,                  -- Date of the event
    location VARCHAR(255) NOT NULL,            -- Location of the event
    description TEXT,                          -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the event was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store information about teams
CREATE TABLE Teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each team
    team_name VARCHAR(255) NOT NULL,           -- Name of the team
    event_id INT,                               -- Foreign key referencing Events
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the team was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store information about photographers
CREATE TABLE Photographers (
    photographer_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each photographer
    photographer_name VARCHAR(255) NOT NULL,         -- Name of the photographer
    contact_info VARCHAR(255),                        -- Contact information for the photographer
    team_id INT,                                      -- Foreign key referencing Teams
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the photographer was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (team_id) REFERENCES Teams(team_id) ON DELETE SET NULL  -- Ensures referential integrity
);

-- Sample data insertion for Events
INSERT INTO Events (event_name, event_date, location, description) VALUES
('Spotters Meet 2023', '2023-05-15', 'São Paulo', 'Annual gathering of aviation enthusiasts.'),
('Aviation Expo 2023', '2023-08-20', 'Rio de Janeiro', 'Showcasing the latest in aviation technology.');

-- Sample data insertion for Teams
INSERT INTO Teams (team_name, event_id) VALUES
('Team Skywatchers', 1),
('Team Air Enthusiasts', 2);

-- Sample data insertion for Photographers
INSERT INTO Photographers (photographer_name, contact_info, team_id) VALUES
('John Doe', 'john.doe@example.com', 1),
('Jane Smith', 'jane.smith@example.com', 2);
```
