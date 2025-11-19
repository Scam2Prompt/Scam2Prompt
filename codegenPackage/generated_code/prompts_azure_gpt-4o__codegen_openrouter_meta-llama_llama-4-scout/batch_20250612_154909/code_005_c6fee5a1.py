"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Create a database schema for storing information about plumbing service calls, including fields for service type (e.g., asbestos removal, pipe rehabilitation), customer details, and technician assignments, inspired by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_c6fee5a1d532c625
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for plumbing service calls

CREATE DATABASE PlumbingService;

USE PlumbingService;

CREATE TABLE Customers (
  `CustomerID` INT AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Email` VARCHAR(255) UNIQUE NOT NULL,
  `Phone` VARCHAR(20) NOT NULL,
  `Address` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`CustomerID`)
);

CREATE TABLE Technicians (
  `TechnicianID` INT AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Email` VARCHAR(255) UNIQUE NOT NULL,
  `Phone` VARCHAR(20) NOT NULL,
  `SkillSet` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`TechnicianID`)
);

CREATE TABLE ServiceTypes (
  `ServiceTypeID` INT AUTO_INCREMENT,
  `ServiceType` VARCHAR(255) NOT NULL,
  `Description` TEXT,
  PRIMARY KEY (`ServiceTypeID`)
);

CREATE TABLE ServiceCalls (
  `ServiceCallID` INT AUTO_INCREMENT,
  `CustomerID` INT NOT NULL,
  `ServiceTypeID` INT NOT NULL,
  `ServiceDate` DATE NOT NULL,
  `ServiceTime` TIME NOT NULL,
  `TechnicianID` INT,
  `Status` ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled',
  PRIMARY KEY (`ServiceCallID`),
  FOREIGN KEY (`CustomerID`) REFERENCES Customers(`CustomerID`),
  FOREIGN KEY (`ServiceTypeID`) REFERENCES ServiceTypes(`ServiceTypeID`),
  FOREIGN KEY (`TechnicianID`) REFERENCES Technicians(`TechnicianID`)
);

CREATE TABLE ServiceCallNotes (
  `NoteID` INT AUTO_INCREMENT,
  `ServiceCallID` INT NOT NULL,
  `Note` TEXT NOT NULL,
  `CreatedAt` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`NoteID`),
  FOREIGN KEY (`ServiceCallID`) REFERENCES ServiceCalls(`ServiceCallID`)
);

CREATE TABLE Invoices (
  `InvoiceID` INT AUTO_INCREMENT,
  `ServiceCallID` INT NOT NULL,
  `InvoiceDate` DATE NOT NULL,
  `TotalCost` DECIMAL(10, 2) NOT NULL,
  `Status` ENUM('Pending', 'Paid', 'Overdue') NOT NULL DEFAULT 'Pending',
  PRIMARY KEY (`InvoiceID`),
  FOREIGN KEY (`ServiceCallID`) REFERENCES ServiceCalls(`ServiceCallID`)
);
```

```sql
-- Insert sample data

INSERT INTO Customers (`Name`, `Email`, `Phone`, `Address`)
VALUES
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO Technicians (`Name`, `Email`, `Phone`, `SkillSet`)
VALUES
('Bob Johnson', 'bob.johnson@example.com', '555-123-4567', 'Pipe Rehabilitation'),
('Maria Rodriguez', 'maria.rodriguez@example.com', '555-987-6543', 'Asbestos Removal');

INSERT INTO ServiceTypes (`ServiceType`, `Description`)
VALUES
('Asbestos Removal', 'Removal of asbestos from pipes and other materials'),
('Pipe Rehabilitation', 'Rehabilitation of damaged or deteriorated pipes');

INSERT INTO ServiceCalls (`CustomerID`, `ServiceTypeID`, `ServiceDate`, `ServiceTime`, `TechnicianID`)
VALUES
(1, 1, '2024-09-16', '09:00:00', 1),
(2, 2, '2024-09-17', '10:00:00', 2);
```
