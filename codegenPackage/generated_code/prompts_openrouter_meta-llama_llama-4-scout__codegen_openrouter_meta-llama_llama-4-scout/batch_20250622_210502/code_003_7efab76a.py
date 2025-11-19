"""
Generated Code Metadata:
========================
Original URL: https://1marbleclassic.com
Prompt: "Create a SQL database schema to store information about home remodeling projects, including client details, project scope, and installation schedules, inspired by the services provided by 1Marble Classic."
Generated: DETERMINISTIC_7efab76a85425d13
Batch ID: 20250622_210502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for home remodeling projects

CREATE DATABASE HomeRemodelingDB;

USE HomeRemodelingDB;

-- Client table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    PRIMARY KEY (ClientID)
);

-- Project table to store project scope and details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(100) NOT NULL,
    ProjectDescription TEXT,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Status VARCHAR(50) NOT NULL DEFAULT 'Scheduled',
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- InstallationSchedule table to store installation schedules
CREATE TABLE InstallationSchedules (
    ScheduleID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    InstallationDate DATE NOT NULL,
    InstallationTime TIME NOT NULL,
    PRIMARY KEY (ScheduleID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Materials table to store materials used in projects
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT,
    MaterialName VARCHAR(100) NOT NULL,
    MaterialDescription TEXT,
    PRIMARY KEY (MaterialID)
);

-- ProjectMaterials table to store many-to-many relationship between projects and materials
CREATE TABLE ProjectMaterials (
    ProjectID INT NOT NULL,
    MaterialID INT NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (ProjectID, MaterialID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID)
);

-- Payments table to store payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Invoices table to store invoice information
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    InvoiceDate DATE NOT NULL,
    InvoiceAmount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (InvoiceID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_ClientID ON Projects (ClientID);
CREATE INDEX idx_ProjectID ON InstallationSchedules (ProjectID);
CREATE INDEX idx_ProjectID ON ProjectMaterials (ProjectID);
CREATE INDEX idx_MaterialID ON ProjectMaterials (MaterialID);
CREATE INDEX idx_ProjectID ON Payments (ProjectID);
CREATE INDEX idx_ProjectID ON Invoices (ProjectID);

-- Insert sample data
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO Projects (ClientID, ProjectName, ProjectDescription, StartDate, EndDate, Status)
VALUES 
(1, 'Kitchen Remodel', 'Kitchen renovation including cabinets, countertops, and appliances', '2022-01-01', '2022-03-01', 'In Progress'),
(2, 'Bathroom Remodel', 'Bathroom renovation including tile, fixtures, and vanity', '2022-04-01', '2022-06-01', 'Scheduled');

INSERT INTO InstallationSchedules (ProjectID, InstallationDate, InstallationTime)
VALUES 
(1, '2022-02-15', '08:00:00'),
(2, '2022-05-01', '09:00:00');

INSERT INTO Materials (MaterialName, MaterialDescription)
VALUES 
('Granite Countertops', 'High-quality granite countertops'),
('Stainless Steel Appliances', 'Energy-efficient stainless steel appliances'),
('Porcelain Tile', 'Durable and water-resistant porcelain tile');

INSERT INTO ProjectMaterials (ProjectID, MaterialID, Quantity)
VALUES 
(1, 1, 2),
(1, 2, 1),
(2, 3, 100);

INSERT INTO Payments (ProjectID, PaymentDate, PaymentAmount)
VALUES 
(1, '2022-01-15', 5000.00),
(2, '2022-04-15', 2000.00);

INSERT INTO Invoices (ProjectID, InvoiceDate, InvoiceAmount)
VALUES 
(1, '2022-03-15', 15000.00),
(2, '2022-06-15', 8000.00);
```
