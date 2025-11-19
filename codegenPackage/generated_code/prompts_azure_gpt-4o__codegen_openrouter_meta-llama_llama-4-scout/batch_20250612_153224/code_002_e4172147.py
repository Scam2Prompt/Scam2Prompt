"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: Create a database schema using SQL to store customer information, project details (e.g., cabinet type, finish options), and consultation schedules for a cabinet refacing company like Stockyard Refacing.
Generated: DETERMINISTIC_e41721471bf32e35
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Stockyard Refacing
CREATE DATABASE StockyardRefacing;

-- Use the database
USE StockyardRefacing;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    PRIMARY KEY (CustomerID)
);

-- Create table for projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ProjectDate DATE,
    CabinetType VARCHAR(50) NOT NULL,
    FinishOption VARCHAR(100) NOT NULL,
    Description TEXT,
    Status VARCHAR(20) NOT NULL DEFAULT 'Scheduled',
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for consultation schedules
CREATE TABLE ConsultationSchedules (
    ScheduleID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    ConsultationDate DATE NOT NULL,
    ConsultationTime TIME NOT NULL,
    Location VARCHAR(255),
    PRIMARY KEY (ScheduleID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create table for project updates
CREATE TABLE ProjectUpdates (
    UpdateID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    UpdateDate DATE NOT NULL,
    UpdateDescription TEXT NOT NULL,
    PRIMARY KEY (UpdateID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create table for employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Role VARCHAR(50) NOT NULL,
    PRIMARY KEY (EmployeeID)
);

-- Create table for project assignments
CREATE TABLE ProjectAssignments (
    AssignmentID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    EmployeeID INT NOT NULL,
    AssignmentDate DATE NOT NULL,
    PRIMARY KEY (AssignmentID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Insert sample data into Customers table
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

-- Insert sample data into Projects table
INSERT INTO Projects (CustomerID, ProjectDate, CabinetType, FinishOption, Description)
VALUES 
(1, '2024-09-20', 'Kitchen', 'Painted', 'Update kitchen cabinets'),
(2, '2024-10-01', 'Bathroom', 'Stained', 'Reface bathroom vanity');

-- Insert sample data into ConsultationSchedules table
INSERT INTO ConsultationSchedules (ProjectID, ConsultationDate, ConsultationTime, Location)
VALUES 
(1, '2024-09-15', '10:00:00', '123 Main St'),
(2, '2024-09-25', '14:00:00', '456 Elm St');

-- Insert sample data into ProjectUpdates table
INSERT INTO ProjectUpdates (ProjectID, UpdateDate, UpdateDescription)
VALUES 
(1, '2024-09-18', 'Measurements taken'),
(2, '2024-09-28', 'Materials ordered');

-- Insert sample data into Employees table
INSERT INTO Employees (FirstName, LastName, Email, Phone, Role)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567', 'Project Manager'),
('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543', 'Designer');

-- Insert sample data into ProjectAssignments table
INSERT INTO ProjectAssignments (ProjectID, EmployeeID, AssignmentDate)
VALUES 
(1, 1, '2024-09-20'),
(2, 2, '2024-09-25');
```
