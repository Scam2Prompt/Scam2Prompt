"""
Generated Code Metadata:
========================
Original URL: https://bgalpina.com
Prompt: "Create a SQL database schema to store information about hiking excursions, including columns for destination, date, and description."
Generated: DETERMINISTIC_b5836778b018b43f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for hiking excursions

-- Create a database for hiking excursions
CREATE DATABASE HikingExcursions;

-- Use the HikingExcursions database
USE HikingExcursions;

-- Create a table to store hiking excursion information
CREATE TABLE Excursions (
    -- Unique identifier for each excursion
    ExcursionID INT AUTO_INCREMENT,
    
    -- Destination of the hiking excursion
    Destination VARCHAR(255) NOT NULL,
    
    -- Date of the hiking excursion
    ExcursionDate DATE NOT NULL,
    
    -- Description of the hiking excursion
    Description TEXT,
    
    -- Timestamp for when the excursion was created
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Timestamp for when the excursion was last updated
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    PRIMARY KEY (ExcursionID)
);

-- Create a table to store user information for excursions
CREATE TABLE Users (
    -- Unique identifier for each user
    UserID INT AUTO_INCREMENT,
    
    -- Name of the user
    Name VARCHAR(255) NOT NULL,
    
    -- Email of the user
    Email VARCHAR(255) UNIQUE NOT NULL,
    
    -- Timestamp for when the user was created
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Timestamp for when the user was last updated
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    PRIMARY KEY (UserID)
);

-- Create a table to store user participation in excursions
CREATE TABLE ExcursionParticipants (
    -- Unique identifier for each participant
    ParticipantID INT AUTO_INCREMENT,
    
    -- Foreign key referencing the Excursions table
    ExcursionID INT NOT NULL,
    
    -- Foreign key referencing the Users table
    UserID INT NOT NULL,
    
    -- Timestamp for when the user joined the excursion
    JoinedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (ParticipantID),
    
    -- Establish relationships between tables
    FOREIGN KEY (ExcursionID) REFERENCES Excursions(ExcursionID) ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Example usage:
-- Insert a new excursion
INSERT INTO Excursions (Destination, ExcursionDate, Description)
VALUES ('Mount Everest', '2024-09-01', 'A challenging hike to the summit of Mount Everest');

-- Insert a new user
INSERT INTO Users (Name, Email)
VALUES ('John Doe', 'john@example.com');

-- Add a user to an excursion
INSERT INTO ExcursionParticipants (ExcursionID, UserID)
VALUES (1, 1);
```
