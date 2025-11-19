"""
Generated Code Metadata:
========================
Original URL: https://carehelpers.pt
Prompt: Design a database schema in SQL for managing client information and service requests for a home care provider like CARE HELPERS, focusing on activities of daily living and technical aids.
Generated: DETERMINISTIC_3c4bff9a0b0ea223
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for home care provider
CREATE DATABASE CareHelpers;

-- Use the database
USE CareHelpers;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for caregivers
CREATE TABLE Caregivers (
    CaregiverID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CaregiverID)
);

-- Create table for activities of daily living (ADLs)
CREATE TABLE ADLs (
    ADLID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    CaregiverID INT,
    Activity VARCHAR(100) NOT NULL,
    Description TEXT,
    Date DATE NOT NULL,
    Completed BOOLEAN DEFAULT FALSE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ADLID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID)
);

-- Create table for technical aids
CREATE TABLE TechnicalAids (
    AidID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    AidType VARCHAR(100) NOT NULL,
    Description TEXT,
    InstallationDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AidID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create table for service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    CaregiverID INT,
    RequestDate DATE NOT NULL,
    RequestType VARCHAR(100) NOT NULL,
    Description TEXT,
    Status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (RequestID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID)
);

-- Create table for medication reminders
CREATE TABLE MedicationReminders (
    ReminderID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    MedicationName VARCHAR(100) NOT NULL,
    Dosage VARCHAR(50) NOT NULL,
    Frequency VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReminderID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create indexes for faster queries
CREATE INDEX idx_ClientID ON ADLs(ClientID);
CREATE INDEX idx_CaregiverID ON ADLs(CaregiverID);
CREATE INDEX idx_ClientID ON ServiceRequests(ClientID);
CREATE INDEX idx_CaregiverID ON ServiceRequests(CaregiverID);
CREATE INDEX idx_ClientID ON TechnicalAids(ClientID);
CREATE INDEX idx_ClientID ON MedicationReminders(ClientID);
```
