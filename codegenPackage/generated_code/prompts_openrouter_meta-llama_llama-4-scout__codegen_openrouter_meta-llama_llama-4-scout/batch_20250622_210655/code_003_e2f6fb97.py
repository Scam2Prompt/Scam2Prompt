"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: "Design a simple database schema for storing client information, audit reports, and tax consultancy services provided by a firm like Experts Consulting Group."
Generated: DETERMINISTIC_e2f6fb97db180150
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Experts Consulting Group
CREATE DATABASE ExpertsConsultingGroup;

-- Use the database
USE ExpertsConsultingGroup;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for audit reports
CREATE TABLE AuditReports (
    ReportID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ReportDate DATE NOT NULL,
    ReportType VARCHAR(100) NOT NULL,
    ReportDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReportID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create table for tax consultancy services
CREATE TABLE TaxConsultancyServices (
    ServiceID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ServiceType VARCHAR(100) NOT NULL,
    ServiceDate DATE NOT NULL,
    ServiceDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create table for consultancy service providers
CREATE TABLE Consultants (
    ConsultantID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ConsultantID)
);

-- Create table for service provider assignments
CREATE TABLE ConsultantAssignments (
    AssignmentID INT AUTO_INCREMENT,
    ServiceID INT NOT NULL,
    ConsultantID INT NOT NULL,
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (AssignmentID),
    FOREIGN KEY (ServiceID) REFERENCES TaxConsultancyServices(ServiceID) ON DELETE CASCADE,
    FOREIGN KEY (ConsultantID) REFERENCES Consultants(ConsultantID) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO AuditReports (ClientID, ReportDate, ReportType, ReportDescription)
VALUES 
(1, '2022-01-01', 'Annual Audit', 'Annual audit report for John Doe'),
(2, '2022-06-01', 'Interim Audit', 'Interim audit report for Jane Doe');

INSERT INTO TaxConsultancyServices (ClientID, ServiceType, ServiceDate, ServiceDescription)
VALUES 
(1, 'Tax Return', '2022-03-01', 'Tax return preparation for John Doe'),
(2, 'Tax Planning', '2022-09-01', 'Tax planning services for Jane Doe');

INSERT INTO Consultants (FirstName, LastName, Email, Phone)
VALUES 
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-987-6543');

INSERT INTO ConsultantAssignments (ServiceID, ConsultantID)
VALUES 
(1, 1),
(2, 2);
```
