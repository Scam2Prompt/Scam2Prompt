"""
Generated Code Metadata:
========================
Original URL: https://www.atletismomg.org.br
Prompt: Develop a simple database schema to store information about athletic clubs, teams, and athletes, inspired by the structures used on the FMA website.
Generated: DETERMINISTIC_cbf91aed6cbd9db5
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for athletic clubs, teams, and athletes

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Athletes;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS Clubs;

-- Create a table to store information about athletic clubs
CREATE TABLE Clubs (
    ClubID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each club
    ClubName VARCHAR(100) NOT NULL,         -- Name of the club
    Location VARCHAR(100),                   -- Location of the club
    EstablishedYear INT,                     -- Year the club was established
    ContactEmail VARCHAR(100)                -- Contact email for the club
);

-- Create a table to store information about teams
CREATE TABLE Teams (
    TeamID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each team
    TeamName VARCHAR(100) NOT NULL,         -- Name of the team
    ClubID INT,                              -- Foreign key referencing Clubs
    Sport VARCHAR(50),                       -- Sport associated with the team
    FOREIGN KEY (ClubID) REFERENCES Clubs(ClubID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store information about athletes
CREATE TABLE Athletes (
    AthleteID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each athlete
    FirstName VARCHAR(50) NOT NULL,          -- Athlete's first name
    LastName VARCHAR(50) NOT NULL,            -- Athlete's last name
    DateOfBirth DATE,                         -- Athlete's date of birth
    TeamID INT,                               -- Foreign key referencing Teams
    Position VARCHAR(50),                     -- Position or role of the athlete in the team
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE SET NULL  -- Ensures referential integrity
);

-- Sample data insertion (optional)
INSERT INTO Clubs (ClubName, Location, EstablishedYear, ContactEmail) VALUES
('City Athletic Club', 'New York', 1990, 'contact@cityathleticclub.com'),
('Mountain Sports Club', 'Denver', 1985, 'info@mountainsportsclub.com');

INSERT INTO Teams (TeamName, ClubID, Sport) VALUES
('City Runners', 1, 'Running'),
('Mountain Climbers', 2, 'Climbing');

INSERT INTO Athletes (FirstName, LastName, DateOfBirth, TeamID, Position) VALUES
('John', 'Doe', '1995-05-15', 1, 'Runner'),
('Jane', 'Smith', '1992-08-22', 2, 'Climber');
```
