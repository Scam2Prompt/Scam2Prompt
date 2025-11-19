"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: "Design a database schema for storing information about clients, talent profiles, and recruitment processes for a consulting firm that offers international talent selection services."
Generated: DETERMINISTIC_f271192a4acb8ed8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for consulting firm

CREATE DATABASE ConsultingFirm;

USE ConsultingFirm;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    Industry VARCHAR(100) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for talent profiles
CREATE TABLE TalentProfiles (
    TalentID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Nationality VARCHAR(100) NOT NULL,
    Skills VARCHAR(255) NOT NULL,
    ExperienceYears INT NOT NULL,
    Education VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TalentID)
);

-- Create table for recruitment processes
CREATE TABLE RecruitmentProcesses (
    ProcessID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    TalentID INT,
    JobTitle VARCHAR(255) NOT NULL,
    JobDescription TEXT NOT NULL,
    Status ENUM('Open', 'In Progress', 'Closed') NOT NULL DEFAULT 'Open',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProcessID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (TalentID) REFERENCES TalentProfiles(TalentID) ON DELETE SET NULL
);

-- Create table for interviews
CREATE TABLE Interviews (
    InterviewID INT AUTO_INCREMENT,
    ProcessID INT NOT NULL,
    InterviewDate DATE NOT NULL,
    InterviewType ENUM('Phone', 'Video', 'In Person') NOT NULL,
    Result ENUM('Passed', 'Failed', 'Pending') NOT NULL DEFAULT 'Pending',
    Feedback TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InterviewID),
    FOREIGN KEY (ProcessID) REFERENCES RecruitmentProcesses(ProcessID) ON DELETE CASCADE
);

-- Create table for offers
CREATE TABLE Offers (
    OfferID INT AUTO_INCREMENT,
    ProcessID INT NOT NULL,
    OfferDate DATE NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL,
    Benefits TEXT,
    Status ENUM('Pending', 'Accepted', 'Rejected') NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OfferID),
    FOREIGN KEY (ProcessID) REFERENCES RecruitmentProcesses(ProcessID) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_ClientID ON RecruitmentProcesses (ClientID);
CREATE INDEX idx_TalentID ON RecruitmentProcesses (TalentID);
CREATE INDEX idx_ProcessID ON Interviews (ProcessID);
CREATE INDEX idx_ProcessID ON Offers (ProcessID);
```
