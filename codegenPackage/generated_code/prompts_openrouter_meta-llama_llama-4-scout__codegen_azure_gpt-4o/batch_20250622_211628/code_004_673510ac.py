"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Design a database schema for storing information about sports coaches, trainers, and athletes, inspired by the team of dedicated coaches at L-Zero, including details about their experience, qualifications, and services offered.
Generated: DETERMINISTIC_673510ac56ff88ad
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about sports coaches, trainers, and athletes

-- Table to store information about individuals (coaches, trainers, athletes)
CREATE TABLE Individuals (
    IndividualID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each individual
    FirstName VARCHAR(50) NOT NULL,              -- First name of the individual
    LastName VARCHAR(50) NOT NULL,               -- Last name of the individual
    Role ENUM('Coach', 'Trainer', 'Athlete') NOT NULL, -- Role of the individual
    DateOfBirth DATE,                            -- Date of birth of the individual
    Email VARCHAR(100) UNIQUE,                   -- Email address (must be unique)
    PhoneNumber VARCHAR(15),                     -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store qualifications and certifications for coaches and trainers
CREATE TABLE Qualifications (
    QualificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each qualification
    IndividualID INT NOT NULL,                      -- Foreign key referencing Individuals table
    QualificationName VARCHAR(100) NOT NULL,        -- Name of the qualification or certification
    Institution VARCHAR(100),                       -- Institution that issued the qualification
    DateObtained DATE,                              -- Date the qualification was obtained
    ValidUntil DATE,                                -- Expiration date (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (IndividualID) REFERENCES Individuals(IndividualID) ON DELETE CASCADE
);

-- Table to store services offered by coaches and trainers
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each service
    IndividualID INT NOT NULL,                      -- Foreign key referencing Individuals table
    ServiceName VARCHAR(100) NOT NULL,              -- Name of the service offered
    Description TEXT,                               -- Detailed description of the service
    Price DECIMAL(10, 2),                           -- Price of the service (if applicable)
    DurationInMinutes INT,                          -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (IndividualID) REFERENCES Individuals(IndividualID) ON DELETE CASCADE
);

-- Table to store athlete profiles
CREATE TABLE AthleteProfiles (
    AthleteProfileID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each athlete profile
    IndividualID INT NOT NULL,                       -- Foreign key referencing Individuals table
    Sport VARCHAR(50) NOT NULL,                      -- Sport the athlete is involved in
    SkillLevel ENUM('Beginner', 'Intermediate', 'Advanced', 'Professional') NOT NULL, -- Skill level of the athlete
    Achievements TEXT,                               -- List of achievements (if any)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (IndividualID) REFERENCES Individuals(IndividualID) ON DELETE CASCADE
);

-- Table to store relationships between coaches/trainers and athletes
CREATE TABLE Relationships (
    RelationshipID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each relationship
    CoachTrainerID INT NOT NULL,                    -- Foreign key referencing Individuals table (Coach/Trainer)
    AthleteID INT NOT NULL,                         -- Foreign key referencing Individuals table (Athlete)
    RelationshipType ENUM('Coach', 'Trainer') NOT NULL, -- Type of relationship
    StartDate DATE NOT NULL,                        -- Start date of the relationship
    EndDate DATE,                                   -- End date of the relationship (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CoachTrainerID) REFERENCES Individuals(IndividualID) ON DELETE CASCADE,
    FOREIGN KEY (AthleteID) REFERENCES Individuals(IndividualID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_individual_role ON Individuals(Role);
CREATE INDEX idx_service_individual ON Services(IndividualID);
CREATE INDEX idx_relationship_coach_trainer ON Relationships(CoachTrainerID);
CREATE INDEX idx_relationship_athlete ON Relationships(AthleteID);
```
