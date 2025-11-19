"""
Generated Code Metadata:
========================
Original URL: https://sembradordevidaac.org
Prompt: Design a simple database schema to store information about community groups, their members, and their activities, using Sembrador de Vida as a use case example.
Generated: DETERMINISTIC_bfe25b546eedfd5f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about community groups, their members, and their activities

-- Create a database for the community groups
CREATE DATABASE CommunityGroupsDB;

-- Use the created database
USE CommunityGroupsDB;

-- Table to store information about community groups
CREATE TABLE Groups (
    GroupID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each group
    GroupName VARCHAR(100) NOT NULL,          -- Name of the community group
    Description TEXT,                          -- Description of the group
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the group was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store information about members
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each member
    GroupID INT NOT NULL,                      -- Foreign key referencing the group
    MemberName VARCHAR(100) NOT NULL,         -- Name of the member
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email of the member (must be unique)
    JoinedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the member joined
    FOREIGN KEY (GroupID) REFERENCES Groups(GroupID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store information about activities
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each activity
    GroupID INT NOT NULL,                       -- Foreign key referencing the group
    ActivityName VARCHAR(100) NOT NULL,        -- Name of the activity
    ActivityDate DATETIME NOT NULL,            -- Date and time of the activity
    Location VARCHAR(255),                      -- Location of the activity
    Description TEXT,                           -- Description of the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the activity was created
    FOREIGN KEY (GroupID) REFERENCES Groups(GroupID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Example of inserting data into the Groups table
INSERT INTO Groups (GroupName, Description) VALUES 
('Sembrador de Vida', 'A community group focused on sustainable living and environmental awareness.');

-- Example of inserting data into the Members table
INSERT INTO Members (GroupID, MemberName, Email) VALUES 
(1, 'John Doe', 'john.doe@example.com'),
(1, 'Jane Smith', 'jane.smith@example.com');

-- Example of inserting data into the Activities table
INSERT INTO Activities (GroupID, ActivityName, ActivityDate, Location, Description) VALUES 
(1, 'Tree Planting Day', '2023-11-15 09:00:00', 'Community Park', 'A day dedicated to planting trees in the local park.');

-- Ensure proper error handling in your application code when interacting with the database
-- Example: Check for unique constraints, handle foreign key violations, etc.
```
