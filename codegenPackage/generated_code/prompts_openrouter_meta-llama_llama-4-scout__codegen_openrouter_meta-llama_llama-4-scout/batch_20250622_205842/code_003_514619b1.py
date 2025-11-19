"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Design a database schema to store information about beneficiaries, volunteers, and projects for an organization like Rakhshanda Memorial, focusing on psychological health and financial independence initiatives.
Generated: DETERMINISTIC_514619b18bc5a19f
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Rakhshanda Memorial organization

-- Create database
CREATE DATABASE RakhshandaMemorial;

-- Use database
USE RakhshandaMemorial;

-- Create table for beneficiaries
CREATE TABLE Beneficiaries (
    BeneficiaryID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE,
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    PsychologicalHealthStatus VARCHAR(100),
    FinancialStatus VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (BeneficiaryID)
);

-- Create table for volunteers
CREATE TABLE Volunteers (
    VolunteerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE,
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    Skills VARCHAR(255),
    Availability VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VolunteerID)
);

-- Create table for projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    ProjectName VARCHAR(255) NOT NULL,
    Description TEXT,
    StartDate DATE,
    EndDate DATE,
    Budget DECIMAL(10, 2),
    PsychologicalHealthFocus BOOLEAN,
    FinancialIndependenceFocus BOOLEAN,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProjectID)
);

-- Create table for beneficiary project associations
CREATE TABLE BeneficiaryProjects (
    BeneficiaryID INT,
    ProjectID INT,
    AssociationDate DATE,
    PRIMARY KEY (BeneficiaryID, ProjectID),
    FOREIGN KEY (BeneficiaryID) REFERENCES Beneficiaries(BeneficiaryID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create table for volunteer project associations
CREATE TABLE VolunteerProjects (
    VolunteerID INT,
    ProjectID INT,
    AssociationDate DATE,
    PRIMARY KEY (VolunteerID, ProjectID),
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create table for project outcomes
CREATE TABLE ProjectOutcomes (
    OutcomeID INT AUTO_INCREMENT,
    ProjectID INT,
    OutcomeDate DATE,
    Description TEXT,
    PsychologicalHealthImpact VARCHAR(100),
    FinancialIndependenceImpact VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OutcomeID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create table for donations
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT,
    DonorName VARCHAR(255),
    DonationDate DATE,
    Amount DECIMAL(10, 2),
    ProjectID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DonationID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_beneficiaries_email ON Beneficiaries (Email);
CREATE INDEX idx_volunteers_email ON Volunteers (Email);
CREATE INDEX idx_projects_name ON Projects (ProjectName);
```

```sql
-- Example usage:

-- Insert beneficiaries
INSERT INTO Beneficiaries (FirstName, LastName, DateOfBirth, Email, Phone, Address, PsychologicalHealthStatus, FinancialStatus)
VALUES 
('John', 'Doe', '1990-01-01', 'john.doe@example.com', '1234567890', '123 Main St', 'Good', 'Fair');

-- Insert volunteers
INSERT INTO Volunteers (FirstName, LastName, DateOfBirth, Email, Phone, Address, Skills, Availability)
VALUES 
('Jane', 'Doe', '1995-01-01', 'jane.doe@example.com', '0987654321', '456 Elm St', 'Counseling', 'Full-time');

-- Insert projects
INSERT INTO Projects (ProjectName, Description, StartDate, EndDate, Budget, PsychologicalHealthFocus, FinancialIndependenceFocus)
VALUES 
('Mental Health Initiative', 'Provide counseling services to beneficiaries', '2022-01-01', '2022-12-31', 10000.00, TRUE, FALSE);

-- Associate beneficiary with project
INSERT INTO BeneficiaryProjects (BeneficiaryID, ProjectID, AssociationDate)
VALUES 
(1, 1, '2022-01-01');

-- Associate volunteer with project
INSERT INTO VolunteerProjects (VolunteerID, ProjectID, AssociationDate)
VALUES 
(1, 1, '2022-01-01');
```
