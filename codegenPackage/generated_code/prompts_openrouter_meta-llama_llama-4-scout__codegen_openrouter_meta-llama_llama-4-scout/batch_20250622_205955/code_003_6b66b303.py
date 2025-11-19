"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: "Design a database schema for a construction company's customer relationship management (CRM) system, including tables for clients, projects, and services offered, such as groundworks solutions and health and safety consulting."
Generated: DETERMINISTIC_6b66b303866727dd
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for construction company's CRM system
CREATE DATABASE ConstructionCRM;

-- Use the database
USE ConstructionCRM;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactFirstName VARCHAR(100) NOT NULL,
    ContactLastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(255) NOT NULL,
    ProjectDescription TEXT,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Status VARCHAR(50) NOT NULL DEFAULT 'In Progress',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create table for services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    ServiceDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create table for project services
CREATE TABLE ProjectServices (
    ProjectID INT NOT NULL,
    ServiceID INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ProjectID, ServiceID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Insert sample services
INSERT INTO Services (ServiceName, ServiceDescription)
VALUES 
('Groundworks Solutions', 'Groundworks solutions for construction projects'),
('Health and Safety Consulting', 'Health and safety consulting services for construction projects'),
('Structural Engineering', 'Structural engineering services for construction projects');

-- Create table for service providers
CREATE TABLE ServiceProviders (
    ServiceProviderID INT AUTO_INCREMENT,
    ServiceProviderName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceProviderID)
);

-- Create table for service provider services
CREATE TABLE ServiceProviderServices (
    ServiceProviderID INT NOT NULL,
    ServiceID INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceProviderID, ServiceID),
    FOREIGN KEY (ServiceProviderID) REFERENCES ServiceProviders(ServiceProviderID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_Projects_ClientID ON Projects (ClientID);
CREATE INDEX idx_ProjectServices_ProjectID ON ProjectServices (ProjectID);
CREATE INDEX idx_ProjectServices_ServiceID ON ProjectServices (ServiceID);
CREATE INDEX idx_ServiceProviderServices_ServiceProviderID ON ServiceProviderServices (ServiceProviderID);
CREATE INDEX idx_ServiceProviderServices_ServiceID ON ServiceProviderServices (ServiceID);
```
