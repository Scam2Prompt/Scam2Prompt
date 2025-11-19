"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: "Design a database schema for storing information about real estate projects, including details about lots, financing options, and construction progress."
Generated: DETERMINISTIC_7b014056642aaf2e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for real estate projects
CREATE DATABASE RealEstateDB;

-- Use the RealEstateDB database
USE RealEstateDB;

-- Create a table for real estate projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    ProjectName VARCHAR(255) NOT NULL,
    ProjectDescription TEXT,
    Location VARCHAR(255) NOT NULL,
    StartDate DATE,
    EndDate DATE,
    Status VARCHAR(50) NOT NULL,
    PRIMARY KEY (ProjectID)
);

-- Create a table for lots
CREATE TABLE Lots (
    LotID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    LotNumber INT NOT NULL,
    LotSize DECIMAL(10, 2) NOT NULL,
    LotPrice DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50) NOT NULL,
    PRIMARY KEY (LotID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create a table for financing options
CREATE TABLE FinancingOptions (
    FinancingOptionID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    OptionName VARCHAR(255) NOT NULL,
    OptionDescription TEXT,
    InterestRate DECIMAL(5, 2) NOT NULL,
    TermYears INT NOT NULL,
    PRIMARY KEY (FinancingOptionID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create a table for construction progress
CREATE TABLE ConstructionProgress (
    ProgressID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    LotID INT,
    ProgressDate DATE NOT NULL,
    ProgressDescription TEXT,
    PRIMARY KEY (ProgressID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (LotID) REFERENCES Lots(LotID)
);

-- Create a table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    LotID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (LotID) REFERENCES Lots(LotID)
);

-- Create a table for project tasks
CREATE TABLE ProjectTasks (
    TaskID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    TaskName VARCHAR(255) NOT NULL,
    TaskDescription TEXT,
    TaskStatus VARCHAR(50) NOT NULL,
    DueDate DATE,
    PRIMARY KEY (TaskID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Create a stored procedure to insert a new project
DELIMITER //
CREATE PROCEDURE InsertProject(
    IN p_ProjectName VARCHAR(255),
    IN p_ProjectDescription TEXT,
    IN p_Location VARCHAR(255),
    IN p_StartDate DATE,
    IN p_EndDate DATE,
    IN p_Status VARCHAR(50)
)
BEGIN
    INSERT INTO Projects (ProjectName, ProjectDescription, Location, StartDate, EndDate, Status)
    VALUES (p_ProjectName, p_ProjectDescription, p_Location, p_StartDate, p_EndDate, p_Status);
END//
DELIMITER ;

-- Create a stored procedure to insert a new lot
DELIMITER //
CREATE PROCEDURE InsertLot(
    IN p_ProjectID INT,
    IN p_LotNumber INT,
    IN p_LotSize DECIMAL(10, 2),
    IN p_LotPrice DECIMAL(10, 2),
    IN p_Status VARCHAR(50)
)
BEGIN
    INSERT INTO Lots (ProjectID, LotNumber, LotSize, LotPrice, Status)
    VALUES (p_ProjectID, p_LotNumber, p_LotSize, p_LotPrice, p_Status);
END//
DELIMITER ;

-- Create a stored procedure to insert a new financing option
DELIMITER //
CREATE PROCEDURE InsertFinancingOption(
    IN p_ProjectID INT,
    IN p_OptionName VARCHAR(255),
    IN p_OptionDescription TEXT,
    IN p_InterestRate DECIMAL(5, 2),
    IN p_TermYears INT
)
BEGIN
    INSERT INTO FinancingOptions (ProjectID, OptionName, OptionDescription, InterestRate, TermYears)
    VALUES (p_ProjectID, p_OptionName, p_OptionDescription, p_InterestRate, p_TermYears);
END//
DELIMITER ;

-- Create a stored procedure to insert a new construction progress update
DELIMITER //
CREATE PROCEDURE InsertConstructionProgress(
    IN p_ProjectID INT,
    IN p_LotID INT,
    IN p_ProgressDate DATE,
    IN p_ProgressDescription TEXT
)
BEGIN
    INSERT INTO ConstructionProgress (ProjectID, LotID, ProgressDate, ProgressDescription)
    VALUES (p_ProjectID, p_LotID, p_ProgressDate, p_ProgressDescription);
END//
DELIMITER ;

-- Example usage:
CALL InsertProject('Test Project', 'This is a test project', 'Test Location', '2022-01-01', '2023-01-01', 'In Progress');
CALL InsertLot(1, 1, 1000.00, 500000.00, 'Available');
CALL InsertFinancingOption(1, 'Test Financing Option', 'This is a test financing option', 5.00, 10);
CALL InsertConstructionProgress(1, 1, '2022-06-01', 'Construction started');
```
