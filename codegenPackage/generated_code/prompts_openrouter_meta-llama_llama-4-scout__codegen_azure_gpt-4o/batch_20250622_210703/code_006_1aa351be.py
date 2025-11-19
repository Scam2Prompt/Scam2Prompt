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
-- Create a database schema for Spotters Brasil

-- Create table for aviation events
CREATE TABLE AviationEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the event
    EventName VARCHAR(255) NOT NULL,        -- Name of the aviation event
    EventDate DATE NOT NULL,                -- Date of the event
    Location VARCHAR(255) NOT NULL,         -- Location of the event
    Description TEXT                        -- Optional description of the event
);

-- Create table for teams
CREATE TABLE Teams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the team
    TeamName VARCHAR(255) NOT NULL,        -- Name of the team
    Country VARCHAR(100),                  -- Country of origin for the team
    FoundedYear INT,                       -- Year the team was founded
    Description TEXT                       -- Optional description of the team
);

-- Create table for photographers
CREATE TABLE Photographers (
    PhotographerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the photographer
    FullName VARCHAR(255) NOT NULL,                -- Full name of the photographer
    Email VARCHAR(255) UNIQUE NOT NULL,            -- Email address of the photographer
    PhoneNumber VARCHAR(20),                       -- Optional phone number
    Bio TEXT                                       -- Optional biography of the photographer
);

-- Create table to associate photographers with aviation events
CREATE TABLE EventPhotographers (
    EventID INT NOT NULL,                          -- Foreign key to AviationEvents
    PhotographerID INT NOT NULL,                  -- Foreign key to Photographers
    PRIMARY KEY (EventID, PhotographerID),        -- Composite primary key
    FOREIGN KEY (EventID) REFERENCES AviationEvents(EventID) ON DELETE CASCADE,
    FOREIGN KEY (PhotographerID) REFERENCES Photographers(PhotographerID) ON DELETE CASCADE
);

-- Create table to associate teams with aviation events
CREATE TABLE EventTeams (
    EventID INT NOT NULL,                          -- Foreign key to AviationEvents
    TeamID INT NOT NULL,                           -- Foreign key to Teams
    PRIMARY KEY (EventID, TeamID),                 -- Composite primary key
    FOREIGN KEY (EventID) REFERENCES AviationEvents(EventID) ON DELETE CASCADE,
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE
);

-- Insert sample data into AviationEvents
INSERT INTO AviationEvents (EventName, EventDate, Location, Description)
VALUES
('Airshow Brazil 2023', '2023-11-15', 'São Paulo, Brazil', 'Annual airshow featuring aerobatic teams and aircraft displays'),
('Rio Aviation Expo', '2023-12-10', 'Rio de Janeiro, Brazil', 'Aviation expo showcasing the latest in aircraft technology');

-- Insert sample data into Teams
INSERT INTO Teams (TeamName, Country, FoundedYear, Description)
VALUES
('Blue Falcons Aerobatic Team', 'USA', 1995, 'Renowned aerobatic team known for precision flying'),
('Brazilian Sky Masters', 'Brazil', 2005, 'Local aerobatic team showcasing Brazilian talent');

-- Insert sample data into Photographers
INSERT INTO Photographers (FullName, Email, PhoneNumber, Bio)
VALUES
('Carlos Silva', 'carlos.silva@example.com', '555-1234', 'Professional aviation photographer with 10 years of experience'),
('Ana Pereira', 'ana.pereira@example.com', '555-5678', 'Award-winning photographer specializing in airshows');

-- Associate photographers with events
INSERT INTO EventPhotographers (EventID, PhotographerID)
VALUES
(1, 1), -- Carlos Silva covering Airshow Brazil 2023
(2, 2); -- Ana Pereira covering Rio Aviation Expo

-- Associate teams with events
INSERT INTO EventTeams (EventID, TeamID)
VALUES
(1, 1), -- Blue Falcons participating in Airshow Brazil 2023
(2, 2); -- Brazilian Sky Masters participating in Rio Aviation Expo
```
