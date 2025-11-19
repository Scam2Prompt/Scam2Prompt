"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Create a database schema for managing roofing projects, including fields for roof type (tile, shingle, metal, flat), client details, and warranty information, inspired by King Roofing's services.
Generated: DETERMINISTIC_ddf9b1c3ec6a04fb
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing roofing projects

-- Define the database
CREATE DATABASE RoofingProjects;

-- Use the database
USE RoofingProjects;

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    PRIMARY KEY (ClientID)
);

-- Create a table for roof types
CREATE TABLE RoofTypes (
    RoofTypeID INT AUTO_INCREMENT,
    RoofType ENUM('tile', 'shingle', 'metal', 'flat') NOT NULL,
    Description TEXT,
    PRIMARY KEY (RoofTypeID)
);

-- Create a table for roofing projects
CREATE TABLE RoofingProjects (
    ProjectID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    RoofTypeID INT NOT NULL,
    ProjectDate DATE NOT NULL,
    ProjectStatus ENUM('pending', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'pending',
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (RoofTypeID) REFERENCES RoofTypes(RoofTypeID)
);

-- Create a table for warranty information
CREATE TABLE Warranties (
    WarrantyID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    WarrantyType ENUM('manufacturer', 'contractor') NOT NULL,
    WarrantyDuration INT NOT NULL, -- in years
    WarrantyStartDate DATE NOT NULL,
    WarrantyEndDate DATE,
    PRIMARY KEY (WarrantyID),
    FOREIGN KEY (ProjectID) REFERENCES RoofingProjects(ProjectID)
);

-- Create a table for project updates
CREATE TABLE ProjectUpdates (
    UpdateID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    UpdateDate DATE NOT NULL,
    UpdateDescription TEXT NOT NULL,
    PRIMARY KEY (UpdateID),
    FOREIGN KEY (ProjectID) REFERENCES RoofingProjects(ProjectID)
);

-- Example data insertion
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345');

INSERT INTO RoofTypes (RoofType, Description)
VALUES 
('shingle', 'Asphalt shingle roofing'),
('metal', 'Metal roofing');

INSERT INTO RoofingProjects (ClientID, RoofTypeID, ProjectDate)
VALUES 
(1, 1, '2022-01-01');

INSERT INTO Warranties (ProjectID, WarrantyType, WarrantyDuration, WarrantyStartDate)
VALUES 
(1, 'contractor', 5, '2022-01-01');

INSERT INTO ProjectUpdates (ProjectID, UpdateDate, UpdateDescription)
VALUES 
(1, '2022-01-15', 'Project started'),
(1, '2022-02-01', 'Project completed');
```
