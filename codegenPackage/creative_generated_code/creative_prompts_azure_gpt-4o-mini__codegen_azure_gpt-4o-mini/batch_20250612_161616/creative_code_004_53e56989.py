"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Illustrate how to implement a database schema for storing information about construction projects and equipment hire, taking cues from the comprehensive services offered by Ntalo Investments.
Generated: DETERMINISTIC_53e5698916cb472f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information related to construction projects and equipment hire

-- Drop existing tables if they exist to avoid conflicts during development
DROP TABLE IF EXISTS Equipment;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Rentals;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    ContactEmail VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store construction project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(100) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Budget DECIMAL(15, 2) NOT NULL,
    Status ENUM('Pending', 'Ongoing', 'Completed') NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store equipment details
CREATE TABLE Equipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT,
    EquipmentName VARCHAR(100) NOT NULL,
    EquipmentType VARCHAR(50) NOT NULL,
    DailyRate DECIMAL(10, 2) NOT NULL,
    Availability BOOLEAN NOT NULL DEFAULT TRUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to keep track of equipment rentals
CREATE TABLE Rentals (
    RentalID INT PRIMARY KEY AUTO_INCREMENT,
    EquipmentID INT NOT NULL,
    ProjectID INT NOT NULL,
    RentalStartDate DATE NOT NULL,
    RentalEndDate DATE NOT NULL,
    TotalCost DECIMAL(15, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Indexes for improving query performance
CREATE INDEX idx_client_name ON Clients(Name);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_equipment_availability ON Equipment(Availability);
```
