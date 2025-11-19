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
-- Create a database schema for storing information about sports coaches, trainers, and athletes

CREATE DATABASE SportsTeam;

USE SportsTeam;

-- Create a table for coaches
CREATE TABLE Coaches (
    CoachID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    ExperienceYears INT,
    Qualifications TEXT,
    ServicesOffered TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CoachID)
);

-- Create a table for trainers
CREATE TABLE Trainers (
    TrainerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    ExperienceYears INT,
    Qualifications TEXT,
    ServicesOffered TEXT,
    CoachID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TrainerID),
    FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID) ON DELETE SET NULL
);

-- Create a table for athletes
CREATE TABLE Athletes (
    AthleteID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Sport VARCHAR(255),
    CoachID INT,
    TrainerID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AthleteID),
    FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID) ON DELETE SET NULL,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE SET NULL
);

-- Create a table for coach services
CREATE TABLE CoachServices (
    ServiceID INT AUTO_INCREMENT,
    CoachID INT,
    ServiceName VARCHAR(255) NOT NULL,
    ServiceDescription TEXT,
    Price DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID) ON DELETE CASCADE
);

-- Create a table for trainer services
CREATE TABLE TrainerServices (
    ServiceID INT AUTO_INCREMENT,
    TrainerID INT,
    ServiceName VARCHAR(255) NOT NULL,
    ServiceDescription TEXT,
    Price DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE
);

-- Create a table for athlete training sessions
CREATE TABLE TrainingSessions (
    SessionID INT AUTO_INCREMENT,
    AthleteID INT,
    CoachID INT,
    TrainerID INT,
    SessionDate DATE,
    SessionTime TIME,
    SessionDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SessionID),
    FOREIGN KEY (AthleteID) REFERENCES Athletes(AthleteID) ON DELETE CASCADE,
    FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID) ON DELETE SET NULL,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE SET NULL
);

-- Insert sample data
INSERT INTO Coaches (FirstName, LastName, Email, Phone, ExperienceYears, Qualifications, ServicesOffered)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 10, 'Certified Coach', 'Personal Training, Team Coaching');

INSERT INTO Trainers (FirstName, LastName, Email, Phone, ExperienceYears, Qualifications, ServicesOffered, CoachID)
VALUES 
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', 5, 'Certified Trainer', 'Strength Training, Conditioning', 1);

INSERT INTO Athletes (FirstName, LastName, Email, Phone, Sport, CoachID, TrainerID)
VALUES 
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567', 'Basketball', 1, 1);

INSERT INTO CoachServices (CoachID, ServiceName, ServiceDescription, Price)
VALUES 
(1, 'Personal Training', 'One-on-one training sessions', 50.00);

INSERT INTO TrainerServices (TrainerID, ServiceName, ServiceDescription, Price)
VALUES 
(1, 'Strength Training', 'Group strength training sessions', 30.00);

INSERT INTO TrainingSessions (AthleteID, CoachID, TrainerID, SessionDate, SessionTime, SessionDescription)
VALUES 
(1, 1, 1, '2024-09-16', '10:00:00', 'Training session for basketball skills');
```
