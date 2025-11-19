"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Create a SQL database schema to store information about building projects, including client details, project status, and architectural designs, similar to what Remas Engineering Consultants might use to manage their projects.
Generated: DETERMINISTIC_c1ce34c271df3f38
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for building projects
CREATE DATABASE BuildingProjects;

-- Use the database
USE BuildingProjects;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    ClientName VARCHAR(255) NOT NULL,
    ClientEmail VARCHAR(255) UNIQUE NOT NULL,
    ClientPhone VARCHAR(20) NOT NULL,
    ClientAddress VARCHAR(255) NOT NULL,
    PRIMARY KEY (ClientID)
);

-- Create table for project status
CREATE TABLE ProjectStatus (
    StatusID INT AUTO_INCREMENT,
    StatusName VARCHAR(50) NOT NULL,
    StatusDescription VARCHAR(255),
    PRIMARY KEY (StatusID)
);

-- Create table for projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(255) NOT NULL,
    ProjectDescription VARCHAR(255),
    ProjectStartDate DATE,
    ProjectEndDate DATE,
    StatusID INT NOT NULL DEFAULT 1,
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (StatusID) REFERENCES ProjectStatus(StatusID)
);

-- Create table for architectural designs
CREATE TABLE ArchitecturalDesigns (
    DesignID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    DesignName VARCHAR(255) NOT NULL,
    DesignDescription VARCHAR(255),
    DesignFile BLOB,
    PRIMARY KEY (DesignID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create table for project updates
CREATE TABLE ProjectUpdates (
    UpdateID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    UpdateDate DATE NOT NULL,
    UpdateDescription VARCHAR(255) NOT NULL,
    StatusID INT NOT NULL,
    PRIMARY KEY (UpdateID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (StatusID) REFERENCES ProjectStatus(StatusID)
);

-- Insert initial project statuses
INSERT INTO ProjectStatus (StatusID, StatusName, StatusDescription)
VALUES 
(1, 'New', 'New project initiated'),
(2, 'In Progress', 'Project is in progress'),
(3, 'On Hold', 'Project is on hold'),
(4, 'Completed', 'Project is completed'),
(5, 'Cancelled', 'Project is cancelled');

-- Create indexes for foreign keys
CREATE INDEX idx_ClientID ON Projects (ClientID);
CREATE INDEX idx_StatusID ON Projects (StatusID);
CREATE INDEX idx_ProjectID ON ArchitecturalDesigns (ProjectID);
CREATE INDEX idx_ProjectID ON ProjectUpdates (ProjectID);
CREATE INDEX idx_StatusID ON ProjectUpdates (StatusID);
```
