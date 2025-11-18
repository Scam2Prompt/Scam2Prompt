"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixelverse-combo.ru
Prompt: Design a database schema for storing PixelVerse robot attributes, evolution history, and user ownership data.
Generated: DETERMINISTIC_f8f58c8ab5a8e083
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for PixelVerse Robot Management

-- Table: Users
-- Stores information about users who own robots.
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username for login or identification
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: Robots
-- Stores information about individual robots and their attributes.
CREATE TABLE Robots (
    RobotID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the robot
    Name VARCHAR(50) NOT NULL,              -- Name of the robot
    Model VARCHAR(50) NOT NULL,             -- Robot model type
    Attributes JSON NOT NULL,               -- JSON to store dynamic attributes (e.g., speed, power, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Robot creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    OwnerID INT NOT NULL,                   -- Foreign key referencing the owner of the robot
    FOREIGN KEY (OwnerID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table: RobotEvolutionHistory
-- Stores the evolution history of robots (modifications, upgrades, etc.).
CREATE TABLE RobotEvolutionHistory (
    EvolutionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the evolution record
    RobotID INT NOT NULL,                       -- Foreign key referencing the robot
    ChangeDescription TEXT NOT NULL,            -- Description of the change (e.g., upgraded speed to 50)
    ChangedAttributes JSON NOT NULL,            -- JSON to store attributes that were changed
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the change
    FOREIGN KEY (RobotID) REFERENCES Robots(RobotID) ON DELETE CASCADE -- Cascade delete if robot is deleted
);

-- Indexes for better query performance
CREATE INDEX idx_username ON Users(Username);
CREATE INDEX idx_robot_owner ON Robots(OwnerID);
CREATE INDEX idx_evolution_robot ON RobotEvolutionHistory(RobotID);
```
