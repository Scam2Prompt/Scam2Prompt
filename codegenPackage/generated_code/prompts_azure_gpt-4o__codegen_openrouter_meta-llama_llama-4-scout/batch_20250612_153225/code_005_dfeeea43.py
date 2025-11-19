"""
Generated Code Metadata:
========================
Original URL: https://olgastepanova.com.ua
Prompt: Create a database schema for storing client health data, including lab results, dietary preferences, and consultation history, inspired by the personalized approach described on Olga Stepanova's website.
Generated: DETERMINISTIC_dfeeea4391ce6451
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing client health data
CREATE DATABASE ClientHealthDB;

-- Use the created database
USE ClientHealthDB;

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create a table for lab results
CREATE TABLE LabResults (
    LabResultID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    LabName VARCHAR(255) NOT NULL,
    ResultValue VARCHAR(255) NOT NULL,
    ResultUnit VARCHAR(20) NOT NULL,
    TestDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (LabResultID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create a table for dietary preferences
CREATE TABLE DietaryPreferences (
    DietaryPreferenceID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    FoodPreference VARCHAR(255) NOT NULL,
    FoodDislike VARCHAR(255),
    SpecialDiet VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DietaryPreferenceID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create a table for consultation history
CREATE TABLE Consultations (
    ConsultationID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ConsultationDate DATE NOT NULL,
    Symptoms VARCHAR(255),
    Diagnosis VARCHAR(255),
    Treatment VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ConsultationID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create a table for consultation notes
CREATE TABLE ConsultationNotes (
    NoteID INT AUTO_INCREMENT,
    ConsultationID INT NOT NULL,
    NoteText TEXT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (NoteID),
    FOREIGN KEY (ConsultationID) REFERENCES Consultations(ConsultationID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_ClientID ON LabResults(ClientID);
CREATE INDEX idx_ClientID ON DietaryPreferences(ClientID);
CREATE INDEX idx_ClientID ON Consultations(ClientID);
CREATE INDEX idx_ConsultationID ON ConsultationNotes(ConsultationID);

-- Example insert statements
INSERT INTO Clients (FirstName, LastName, DateOfBirth, Email, Phone, Address)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO LabResults (ClientID, LabName, ResultValue, ResultUnit, TestDate)
VALUES (1, 'Blood Pressure', '120/80', 'mmHg', '2022-01-01');

INSERT INTO DietaryPreferences (ClientID, FoodPreference, FoodDislike, SpecialDiet)
VALUES (1, 'Vegetarian', 'Shellfish', 'Gluten-free');

INSERT INTO Consultations (ClientID, ConsultationDate, Symptoms, Diagnosis, Treatment)
VALUES (1, '2022-01-01', 'Headache', 'Tension Headache', 'Rest and hydration');

INSERT INTO ConsultationNotes (ConsultationID, NoteText)
VALUES (1, 'Client reported stress and fatigue.');
```
