"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Design a database schema to store information about franchise systems, including their stage of development, services offered, and client details, similar to how Franchise Teacher manages its clients.
Generated: DETERMINISTIC_4e50d55c1c0cbe26
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- franchise_systems.sql

-- Create a database schema for franchise systems
CREATE DATABASE FranchiseSystems;

-- Use the FranchiseSystems database
USE FranchiseSystems;

-- Create a table for franchise stages
CREATE TABLE FranchiseStages (
  StageID INT AUTO_INCREMENT,
  StageName VARCHAR(255) NOT NULL,
  StageDescription TEXT,
  PRIMARY KEY (StageID)
);

-- Create a table for services offered
CREATE TABLE Services (
  ServiceID INT AUTO_INCREMENT,
  ServiceName VARCHAR(255) NOT NULL,
  ServiceDescription TEXT,
  PRIMARY KEY (ServiceID)
);

-- Create a table for franchise systems
CREATE TABLE FranchiseSystems (
  FranchiseID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Description TEXT,
  StageID INT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (FranchiseID),
  FOREIGN KEY (StageID) REFERENCES FranchiseStages(StageID)
);

-- Create a table for franchise system services
CREATE TABLE FranchiseSystemServices (
  FranchiseID INT,
  ServiceID INT,
  PRIMARY KEY (FranchiseID, ServiceID),
  FOREIGN KEY (FranchiseID) REFERENCES FranchiseSystems(FranchiseID),
  FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create a table for clients
CREATE TABLE Clients (
  ClientID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20),
  Address TEXT,
  FranchiseID INT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ClientID),
  FOREIGN KEY (FranchiseID) REFERENCES FranchiseSystems(FranchiseID)
);

-- Create a table for client contacts
CREATE TABLE ClientContacts (
  ContactID INT AUTO_INCREMENT,
  ClientID INT,
  ContactName VARCHAR(255) NOT NULL,
  ContactEmail VARCHAR(255) NOT NULL,
  ContactPhone VARCHAR(20) NOT NULL,
  PRIMARY KEY (ContactID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Insert sample data into FranchiseStages
INSERT INTO FranchiseStages (StageName, StageDescription)
VALUES 
('Development', 'Franchise system in development stage'),
('Launch', 'Franchise system launched and operational'),
('Growth', 'Franchise system growing and expanding');

-- Insert sample data into Services
INSERT INTO Services (ServiceName, ServiceDescription)
VALUES 
('Training', 'Training services for franchisees'),
('Marketing', 'Marketing services for franchisees'),
('Operations', 'Operational support for franchisees');

-- Insert sample data into FranchiseSystems
INSERT INTO FranchiseSystems (Name, Description, StageID)
VALUES 
('Franchise Teacher', 'Franchise system for educational services', 2),
('Franchise Business', 'Franchise system for business services', 1);

-- Insert sample data into FranchiseSystemServices
INSERT INTO FranchiseSystemServices (FranchiseID, ServiceID)
VALUES 
(1, 1),
(1, 2),
(2, 3);

-- Insert sample data into Clients
INSERT INTO Clients (Name, Email, Phone, Address, FranchiseID)
VALUES 
('Client 1', 'client1@example.com', '123-456-7890', '123 Main St', 1),
('Client 2', 'client2@example.com', '987-654-3210', '456 Elm St', 2);

-- Insert sample data into ClientContacts
INSERT INTO ClientContacts (ClientID, ContactName, ContactEmail, ContactPhone)
VALUES 
(1, 'John Doe', 'john.doe@example.com', '111-222-3333'),
(2, 'Jane Smith', 'jane.smith@example.com', '444-555-6666');
```
