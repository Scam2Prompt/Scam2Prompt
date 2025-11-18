"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danceanatolia.com
Prompt: Suggest a database schema for storing participant information for Anatolian folk dance courses, including fields for age groups (e.g., "Kinder," "Teen," "Adult") and dance styles like Zeybek, as outlined on danceanatolia.com.
Generated: DETERMINISTIC_d6b8a56def4ce892
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Anatolian Folk Dance Courses Participant Information

-- Table: AgeGroups
-- Stores predefined age group categories for participants
CREATE TABLE AgeGroups (
    AgeGroupID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each age group
    Name VARCHAR(50) NOT NULL,                 -- Name of the age group (e.g., "Kinder", "Teen", "Adult")
    Description TEXT                           -- Optional description for the age group
);

-- Table: DanceStyles
-- Stores predefined dance styles offered in the courses
CREATE TABLE DanceStyles (
    DanceStyleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each dance style
    Name VARCHAR(50) NOT NULL,                   -- Name of the dance style (e.g., "Zeybek")
    Description TEXT                             -- Optional description for the dance style
);

-- Table: Participants
-- Stores participant information
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    FirstName VARCHAR(100) NOT NULL,              -- First name of the participant
    LastName VARCHAR(100) NOT NULL,               -- Last name of the participant
    DateOfBirth DATE NOT NULL,                    -- Date of birth of the participant
    AgeGroupID INT NOT NULL,                      -- Foreign key linking to AgeGroups table
    DanceStyleID INT NOT NULL,                    -- Foreign key linking to DanceStyles table
    Email VARCHAR(150),                           -- Contact email address of the participant
    PhoneNumber VARCHAR(20),                      -- Contact phone number of the participant
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of registration
    Notes TEXT,                                   -- Optional notes about the participant
    FOREIGN KEY (AgeGroupID) REFERENCES AgeGroups(AgeGroupID) ON DELETE CASCADE,
    FOREIGN KEY (DanceStyleID) REFERENCES DanceStyles(DanceStyleID) ON DELETE CASCADE
);

-- Indexes can be added for performance optimization
-- Adding index for quick lookup by AgeGroupID
CREATE INDEX idx_participants_agegroup ON Participants (AgeGroupID);

-- Adding index for quick lookup by DanceStyleID
CREATE INDEX idx_participants_dancestyle ON Participants (DanceStyleID);

-- Sample Error Handling: Ensure database constraints
-- Verify AgeGroup and DanceStyle entries exist before inserting Participants
```
