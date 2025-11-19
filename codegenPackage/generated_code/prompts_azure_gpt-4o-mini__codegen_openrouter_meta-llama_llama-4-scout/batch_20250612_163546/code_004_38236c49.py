"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Design a database schema for managing high-quality legal leads, incorporating the specific types of cases highlighted on ClaimLink, such as truck and motorcycle accidents.
Generated: DETERMINISTIC_38236c49d08ebb89
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing high-quality legal leads

-- Create a database
CREATE DATABASE LegalLeadsDB;

-- Use the database
USE LegalLeadsDB;

-- Create a table for case types
CREATE TABLE CaseTypes (
    CaseTypeID INT AUTO_INCREMENT,
    CaseTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CaseTypeID)
);

-- Create a table for cases
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT,
    CaseTypeID INT NOT NULL,
    CaseName VARCHAR(255) NOT NULL,
    Description TEXT,
    Status VARCHAR(50) NOT NULL DEFAULT 'New',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CaseID),
    FOREIGN KEY (CaseTypeID) REFERENCES CaseTypes(CaseTypeID)
);

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create a table for leads
CREATE TABLE Leads (
    LeadID INT AUTO_INCREMENT,
    CaseID INT NOT NULL,
    ClientID INT NOT NULL,
    LeadSource VARCHAR(100) NOT NULL,
    LeadStatus VARCHAR(50) NOT NULL DEFAULT 'New',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (LeadID),
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create a table for truck accidents
CREATE TABLE TruckAccidents (
    TruckAccidentID INT AUTO_INCREMENT,
    LeadID INT NOT NULL,
    AccidentDate DATE,
    AccidentLocation VARCHAR(255),
    NumberOfVehiclesInvolved INT,
    Severity VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TruckAccidentID),
    FOREIGN KEY (LeadID) REFERENCES Leads(LeadID)
);

-- Create a table for motorcycle accidents
CREATE TABLE MotorcycleAccidents (
    MotorcycleAccidentID INT AUTO_INCREMENT,
    LeadID INT NOT NULL,
    AccidentDate DATE,
    AccidentLocation VARCHAR(255),
    NumberOfVehiclesInvolved INT,
    Severity VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MotorcycleAccidentID),
    FOREIGN KEY (LeadID) REFERENCES Leads(LeadID)
);

-- Insert some sample case types
INSERT INTO CaseTypes (CaseTypeName, Description)
VALUES 
('Truck Accident', 'Cases related to truck accidents'),
('Motorcycle Accident', 'Cases related to motorcycle accidents'),
('Car Accident', 'Cases related to car accidents');

-- Insert some sample cases
INSERT INTO Cases (CaseTypeID, CaseName, Description)
VALUES 
(1, 'Sample Truck Accident Case', 'This is a sample truck accident case'),
(2, 'Sample Motorcycle Accident Case', 'This is a sample motorcycle accident case');

-- Insert some sample clients
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert some sample leads
INSERT INTO Leads (CaseID, ClientID, LeadSource, LeadStatus)
VALUES 
(1, 1, 'Online Form', 'New'),
(2, 2, 'Phone Call', 'In Progress');

-- Insert some sample truck accidents
INSERT INTO TruckAccidents (LeadID, AccidentDate, AccidentLocation, NumberOfVehiclesInvolved, Severity)
VALUES 
(1, '2022-01-01', '123 Main St', 2, 'Minor');

-- Insert some sample motorcycle accidents
INSERT INTO MotorcycleAccidents (LeadID, AccidentDate, AccidentLocation, NumberOfVehiclesInvolved, Severity)
VALUES 
(2, '2022-01-15', '456 Elm St', 1, 'Major');
```
