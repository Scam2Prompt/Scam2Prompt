"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Create a database schema in SQL for storing renovation project details, including design specifications, cost estimates, and client contact information, based on the services offered on the webpage.
Generated: DETERMINISTIC_f6e5b748322f8302
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for renovation projects
CREATE DATABASE RenovationProjects;

-- Use the RenovationProjects database
USE RenovationProjects;

-- Create a table for clients
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

-- Create a table for services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(100) NOT NULL,
    ServiceDescription TEXT,
    PRIMARY KEY (ServiceID)
);

-- Create a table for project status
CREATE TABLE ProjectStatus (
    StatusID INT AUTO_INCREMENT,
    StatusName VARCHAR(50) NOT NULL,
    StatusDescription TEXT,
    PRIMARY KEY (StatusID)
);

-- Create a table for renovation projects
CREATE TABLE RenovationProjects (
    ProjectID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(255) NOT NULL,
    ProjectDescription TEXT,
    StartDate DATE,
    EndDate DATE,
    StatusID INT NOT NULL DEFAULT 1,
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (StatusID) REFERENCES ProjectStatus(StatusID)
);

-- Create a table for design specifications
CREATE TABLE DesignSpecifications (
    SpecificationID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    ServiceID INT NOT NULL,
    SpecificationDetails TEXT NOT NULL,
    PRIMARY KEY (SpecificationID),
    FOREIGN KEY (ProjectID) REFERENCES RenovationProjects(ProjectID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create a table for cost estimates
CREATE TABLE CostEstimates (
    EstimateID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    ServiceID INT NOT NULL,
    EstimatedCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (EstimateID),
    FOREIGN KEY (ProjectID) REFERENCES RenovationProjects(ProjectID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create a table for project updates
CREATE TABLE ProjectUpdates (
    UpdateID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    UpdateDate DATE NOT NULL,
    UpdateDescription TEXT NOT NULL,
    PRIMARY KEY (UpdateID),
    FOREIGN KEY (ProjectID) REFERENCES RenovationProjects(ProjectID)
);

-- Insert default services
INSERT INTO Services (ServiceName, ServiceDescription)
VALUES 
('Kitchen Renovation', 'Renovation of kitchen area'),
('Bathroom Renovation', 'Renovation of bathroom area'),
('Flooring Installation', 'Installation of new flooring');

-- Insert default project status
INSERT INTO ProjectStatus (StatusName, StatusDescription)
VALUES 
('New', 'New project'),
('In Progress', 'Project in progress'),
('Completed', 'Project completed'),
('Cancelled', 'Project cancelled');
```
