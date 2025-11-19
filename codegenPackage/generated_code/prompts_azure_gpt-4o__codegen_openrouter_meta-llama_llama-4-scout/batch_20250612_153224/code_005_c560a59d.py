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
-- excursion_database_schema.sql

-- Create database
CREATE DATABASE ExcursionDB;

-- Use database
USE ExcursionDB;

-- Create table for destinations
CREATE TABLE Destinations (
    DestinationID INT AUTO_INCREMENT,
    DestinationName VARCHAR(255) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    PRIMARY KEY (DestinationID)
);

-- Create table for excursions
CREATE TABLE Excursions (
    ExcursionID INT AUTO_INCREMENT,
    TripName VARCHAR(255) NOT NULL,
    ExcursionDate DATE NOT NULL,
    DestinationID INT,
    Description TEXT,
    PRIMARY KEY (ExcursionID),
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID)
);

-- Create table for participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    PRIMARY KEY (ParticipantID)
);

-- Create table for excursion participants
CREATE TABLE ExcursionParticipants (
    ExcursionID INT,
    ParticipantID INT,
    PRIMARY KEY (ExcursionID, ParticipantID),
    FOREIGN KEY (ExcursionID) REFERENCES Excursions(ExcursionID),
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID)
);

-- Create indexes for foreign keys
CREATE INDEX idx_excursions_destination_id ON Excursions (DestinationID);
CREATE INDEX idx_excursion_participants_excursion_id ON ExcursionParticipants (ExcursionID);
CREATE INDEX idx_excursion_participants_participant_id ON ExcursionParticipants (ParticipantID);

-- Example data
INSERT INTO Destinations (DestinationName, Country, City, Address)
VALUES 
('Bran Castle', 'Romania', 'Bran', 'Str. Sighiştarilor 1, 507025 Bran, Romania'),
('Rasnov Citadel', 'Romania', 'Rasnov', 'Str. Cetății 1, 505400 Brașov, Romania');

INSERT INTO Excursions (TripName, ExcursionDate, DestinationID, Description)
VALUES 
('Тайнствената Румъния', '2024-09-20', 1, 'Explore the mystical side of Romania'),
('Medieval Transylvania', '2024-09-22', 2, 'Discover the medieval towns of Transylvania');

INSERT INTO Participants (FirstName, LastName, Email, Phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '+1 123 456 7890'),
('Jane', 'Smith', 'jane.smith@example.com', '+1 987 654 3210');

INSERT INTO ExcursionParticipants (ExcursionID, ParticipantID)
VALUES 
(1, 1),
(1, 2),
(2, 1);
```
