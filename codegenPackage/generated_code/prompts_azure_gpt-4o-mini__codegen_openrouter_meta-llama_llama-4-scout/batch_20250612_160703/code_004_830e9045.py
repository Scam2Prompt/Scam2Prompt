"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: Create a sample database schema for managing therapy sessions and outcomes based on the ICON Foundation's outcome-based mindset in clinical practice.
Generated: DETERMINISTIC_830e9045a059c4c2
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing therapy sessions and outcomes

-- Create a database
CREATE DATABASE TherapyManagement;

-- Use the database
USE TherapyManagement;

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    ContactInformation VARCHAR(255) NOT NULL,
    PRIMARY KEY (ClientID)
);

-- Create a table for therapists
CREATE TABLE Therapists (
    TherapistID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Credentials VARCHAR(255) NOT NULL,
    ContactInformation VARCHAR(255) NOT NULL,
    PRIMARY KEY (TherapistID)
);

-- Create a table for sessions
CREATE TABLE Sessions (
    SessionID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    TherapistID INT NOT NULL,
    SessionDate DATE NOT NULL,
    SessionType VARCHAR(255) NOT NULL,
    PRIMARY KEY (SessionID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID)
);

-- Create a table for outcomes
CREATE TABLE Outcomes (
    OutcomeID INT AUTO_INCREMENT,
    SessionID INT NOT NULL,
    OutcomeMeasure VARCHAR(255) NOT NULL,
    OutcomeScore DECIMAL(3,2) NOT NULL,
    PRIMARY KEY (OutcomeID),
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID)
);

-- Create a table for goals
CREATE TABLE Goals (
    GoalID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    GoalDescription VARCHAR(255) NOT NULL,
    GoalStatus VARCHAR(255) NOT NULL,
    PRIMARY KEY (GoalID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create a table for interventions
CREATE TABLE Interventions (
    InterventionID INT AUTO_INCREMENT,
    SessionID INT NOT NULL,
    InterventionDescription VARCHAR(255) NOT NULL,
    PRIMARY KEY (InterventionID),
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID)
);

-- Create a table for progress notes
CREATE TABLE ProgressNotes (
    NoteID INT AUTO_INCREMENT,
    SessionID INT NOT NULL,
    NoteText TEXT NOT NULL,
    PRIMARY KEY (NoteID),
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID)
);

-- Example insert statements
INSERT INTO Clients (FirstName, LastName, DateOfBirth, ContactInformation)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com');

INSERT INTO Therapists (FirstName, LastName, Credentials, ContactInformation)
VALUES ('Jane', 'Smith', 'LCSW', 'jane.smith@example.com');

INSERT INTO Sessions (ClientID, TherapistID, SessionDate, SessionType)
VALUES (1, 1, '2022-01-01', 'Individual');

INSERT INTO Outcomes (SessionID, OutcomeMeasure, OutcomeScore)
VALUES (1, 'GAD-7', 10.00);

INSERT INTO Goals (ClientID, GoalDescription, GoalStatus)
VALUES (1, 'Reduce anxiety symptoms', 'In Progress');

INSERT INTO Interventions (SessionID, InterventionDescription)
VALUES (1, 'Cognitive-behavioral therapy');

INSERT INTO ProgressNotes (SessionID, NoteText)
VALUES (1, 'Client reported reduced anxiety symptoms.');
```
