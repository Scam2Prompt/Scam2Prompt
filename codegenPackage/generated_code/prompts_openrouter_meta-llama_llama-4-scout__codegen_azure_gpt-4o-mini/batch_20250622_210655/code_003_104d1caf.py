"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Design a database schema to store information about educational programs, such as those offered by Sophia Loisirs & Vie, including details about their " STUDIO DE REPETITION" and "Cyberkiosc" services.
Generated: DETERMINISTIC_104d1cafaa36dc7e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for educational programs offered by Sophia Loisirs & Vie

-- Create a table to store information about educational programs
CREATE TABLE EducationalPrograms (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,         -- Name of the program
    Description TEXT,                           -- Detailed description of the program
    StartDate DATE,                            -- Start date of the program
    EndDate DATE,                              -- End date of the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store information about services offered within the programs
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service
    ProgramID INT,                              -- Foreign key referencing the EducationalPrograms table
    ServiceName VARCHAR(255) NOT NULL,         -- Name of the service
    Description TEXT,                           -- Detailed description of the service
    Price DECIMAL(10, 2),                       -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the service was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store information about participants in the programs
CREATE TABLE Participants (
    ParticipantID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each participant
    ProgramID INT,                                 -- Foreign key referencing the EducationalPrograms table
    FullName VARCHAR(255) NOT NULL,               -- Full name of the participant
    Email VARCHAR(255) NOT NULL UNIQUE,           -- Email of the participant (must be unique)
    PhoneNumber VARCHAR(15),                       -- Phone number of the participant
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the participant registered
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store feedback from participants about the programs
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each feedback entry
    ProgramID INT,                                 -- Foreign key referencing the EducationalPrograms table
    ParticipantID INT,                             -- Foreign key referencing the Participants table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the participant (1 to 5 scale)
    Comments TEXT,                                 -- Additional comments from the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the feedback was created
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_program_name ON EducationalPrograms(ProgramName);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_participant_email ON Participants(Email);
```
