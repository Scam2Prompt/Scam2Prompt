"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Provide an example of a database schema for storing information about construction projects, including fields for project name, location, client, number of apartments, and hours worked, as detailed in INARO S.A.S.'s project descriptions.
Generated: DETERMINISTIC_38be978432942b16
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- construction_projects_schema.sql

-- Create a database schema for storing information about construction projects

-- Create a table for clients
CREATE TABLE Clients (
  ClientID INT AUTO_INCREMENT,
  ClientName VARCHAR(255) NOT NULL,
  ClientContact VARCHAR(255) NOT NULL,
  ClientEmail VARCHAR(255) UNIQUE NOT NULL,
  PRIMARY KEY (ClientID)
);

-- Create a table for construction projects
CREATE TABLE ConstructionProjects (
  ProjectID INT AUTO_INCREMENT,
  ProjectName VARCHAR(255) NOT NULL,
  Location VARCHAR(255) NOT NULL,
  ClientID INT NOT NULL,
  NumberOfApartments INT NOT NULL,
  ProjectDescription TEXT,
  ProjectStartDate DATE NOT NULL,
  ProjectEndDate DATE,
  PRIMARY KEY (ProjectID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create a table for project hours worked
CREATE TABLE ProjectHours (
  HourID INT AUTO_INCREMENT,
  ProjectID INT NOT NULL,
  WorkDate DATE NOT NULL,
  HoursWorked DECIMAL(10, 2) NOT NULL,
  EmployeeID INT NOT NULL,
  PRIMARY KEY (HourID),
  FOREIGN KEY (ProjectID) REFERENCES ConstructionProjects(ProjectID)
);

-- Create a table for employees
CREATE TABLE Employees (
  EmployeeID INT AUTO_INCREMENT,
  EmployeeName VARCHAR(255) NOT NULL,
  EmployeeEmail VARCHAR(255) UNIQUE NOT NULL,
  PRIMARY KEY (EmployeeID)
);

-- Example insert statements
INSERT INTO Clients (ClientName, ClientContact, ClientEmail)
VALUES 
('INARO S.A.S.', 'John Doe', 'john.doe@inaro.com'),
('ABC Corporation', 'Jane Smith', 'jane.smith@abccorp.com');

INSERT INTO ConstructionProjects (ProjectName, Location, ClientID, NumberOfApartments, ProjectStartDate)
VALUES 
('INARO Project 1', 'New York', 1, 100, '2022-01-01'),
('ABC Project 1', 'Los Angeles', 2, 50, '2022-06-01');

INSERT INTO Employees (EmployeeName, EmployeeEmail)
VALUES 
('John Smith', 'john.smith@example.com'),
('Jane Doe', 'jane.doe@example.com');

INSERT INTO ProjectHours (ProjectID, WorkDate, HoursWorked, EmployeeID)
VALUES 
(1, '2022-01-01', 8.00, 1),
(1, '2022-01-02', 7.50, 1),
(2, '2022-06-01', 8.00, 2);
```
