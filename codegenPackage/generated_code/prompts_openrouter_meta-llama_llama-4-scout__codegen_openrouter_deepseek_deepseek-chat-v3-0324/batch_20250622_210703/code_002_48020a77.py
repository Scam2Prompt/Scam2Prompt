"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Generate a construction plan for a healthcare center using SQL and database management principles."
Generated: DETERMINISTIC_48020a77fe5b2e45
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Script for Healthcare Center Construction Plan Database
-- This script creates a database schema to manage construction plans for a healthcare center

-- Create the database
CREATE DATABASE HealthcareConstruction;
GO

USE HealthcareConstruction;
GO

-- Enable error handling
SET XACT_ABORT ON;
GO

-- Create tables with proper constraints and relationships

-- Table for construction projects
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY IDENTITY(1,1),
    ProjectName VARCHAR(100) NOT NULL,
    Description VARCHAR(500),
    StartDate DATE NOT NULL,
    TargetCompletionDate DATE NOT NULL,
    Budget DECIMAL(15,2) NOT NULL,
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Planning', 'In Progress', 'On Hold', 'Completed')),
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME DEFAULT GETDATE(),
    CONSTRAINT CHK_Dates CHECK (TargetCompletionDate > StartDate)
);

-- Table for building sections/units
CREATE TABLE BuildingSections (
    SectionID INT PRIMARY KEY IDENTITY(1,1),
    ProjectID INT NOT NULL,
    SectionName VARCHAR(100) NOT NULL,
    Purpose VARCHAR(200) NOT NULL,
    FloorCount INT NOT NULL,
    AreaSqFt DECIMAL(10,2) NOT NULL,
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Not Started', 'In Progress', 'Completed')),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table for construction phases
CREATE TABLE ConstructionPhases (
    PhaseID INT PRIMARY KEY IDENTITY(1,1),
    SectionID INT NOT NULL,
    PhaseName VARCHAR(100) NOT NULL,
    Description VARCHAR(300),
    StartDate DATE,
    EndDate DATE,
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Pending', 'In Progress', 'Completed', 'Delayed')),
    FOREIGN KEY (SectionID) REFERENCES BuildingSections(SectionID) ON DELETE CASCADE,
    CONSTRAINT CHK_PhaseDates CHECK (EndDate IS NULL OR EndDate >= StartDate)
);

-- Table for contractors
CREATE TABLE Contractors (
    ContractorID INT PRIMARY KEY IDENTITY(1,1),
    CompanyName VARCHAR(100) NOT NULL,
    Specialization VARCHAR(100) NOT NULL,
    ContactPerson VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    LicenseNumber VARCHAR(50),
    IsActive BIT DEFAULT 1
);

-- Table for contractor assignments
CREATE TABLE ContractorAssignments (
    AssignmentID INT PRIMARY KEY IDENTITY(1,1),
    PhaseID INT NOT NULL,
    ContractorID INT NOT NULL,
    AssignedDate DATE NOT NULL DEFAULT GETDATE(),
    CompletionDate DATE,
    ContractAmount DECIMAL(12,2) NOT NULL,
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Assigned', 'In Progress', 'Completed', 'Terminated')),
    FOREIGN KEY (PhaseID) REFERENCES ConstructionPhases(PhaseID) ON DELETE CASCADE,
    FOREIGN KEY (ContractorID) REFERENCES Contractors(ContractorID),
    CONSTRAINT CHK_AssignmentDates CHECK (CompletionDate IS NULL OR CompletionDate >= AssignedDate)
);

-- Table for materials
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100) NOT NULL,
    Description VARCHAR(200),
    Unit VARCHAR(20) NOT NULL,
    UnitCost DECIMAL(10,2) NOT NULL,
    Supplier VARCHAR(100)
);

-- Table for material requirements
CREATE TABLE MaterialRequirements (
    RequirementID INT PRIMARY KEY IDENTITY(1,1),
    PhaseID INT NOT NULL,
    MaterialID INT NOT NULL,
    Quantity DECIMAL(10,2) NOT NULL,
    DateRequired DATE NOT NULL,
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Pending', 'Ordered', 'Delivered', 'Used')),
    FOREIGN KEY (PhaseID) REFERENCES ConstructionPhases(PhaseID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID)
);

-- Table for inspections
CREATE TABLE Inspections (
    InspectionID INT PRIMARY KEY IDENTITY(1,1),
    PhaseID INT NOT NULL,
    InspectionDate DATE NOT NULL,
    InspectorName VARCHAR(100) NOT NULL,
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Passed', 'Failed', 'Pending')),
    Notes VARCHAR(500),
    FOREIGN KEY (PhaseID) REFERENCES ConstructionPhases(PhaseID) ON DELETE CASCADE
);

-- Table for permits
CREATE TABLE Permits (
    PermitID INT PRIMARY KEY IDENTITY(1,1),
    ProjectID INT NOT NULL,
    PermitType VARCHAR(100) NOT NULL,
    IssuingAuthority VARCHAR(100) NOT NULL,
    IssueDate DATE NOT NULL,
    ExpiryDate DATE,
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Applied', 'Issued', 'Expired', 'Revoked')),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    CONSTRAINT CHK_PermitDates CHECK (ExpiryDate IS NULL OR ExpiryDate > IssueDate)
);

-- Table for budget tracking
CREATE TABLE BudgetTransactions (
    TransactionID INT PRIMARY KEY IDENTITY(1,1),
    ProjectID INT NOT NULL,
    TransactionDate DATE NOT NULL DEFAULT GETDATE(),
    Amount DECIMAL(12,2) NOT NULL,
    TransactionType VARCHAR(20) NOT NULL CHECK (TransactionType IN ('Income', 'Expense')),
    Description VARCHAR(200) NOT NULL,
    RelatedEntityType VARCHAR(50),
    RelatedEntityID INT,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX IX_BuildingSections_ProjectID ON BuildingSections(ProjectID);
CREATE INDEX IX_ConstructionPhases_SectionID ON ConstructionPhases(SectionID);
CREATE INDEX IX_ContractorAssignments_PhaseID ON ContractorAssignments(PhaseID);
CREATE INDEX IX_ContractorAssignments_ContractorID ON ContractorAssignments(ContractorID);
CREATE INDEX IX_MaterialRequirements_PhaseID ON MaterialRequirements(PhaseID);
CREATE INDEX IX_MaterialRequirements_MaterialID ON MaterialRequirements(MaterialID);
CREATE INDEX IX_Inspections_PhaseID ON Inspections(PhaseID);
CREATE INDEX IX_Permits_ProjectID ON Permits(ProjectID);
CREATE INDEX IX_BudgetTransactions_ProjectID ON BudgetTransactions(ProjectID);

-- Create a view for project progress
CREATE VIEW ProjectProgress AS
SELECT 
    p.ProjectID,
    p.ProjectName,
    p.StartDate,
    p.TargetCompletionDate,
    p.Status AS ProjectStatus,
    COUNT(DISTINCT bs.SectionID) AS TotalSections,
    SUM(CASE WHEN bs.Status = 'Completed' THEN 1 ELSE 0 END) AS CompletedSections,
    COUNT(DISTINCT cp.PhaseID) AS TotalPhases,
    SUM(CASE WHEN cp.Status = 'Completed' THEN 1 ELSE 0 END) AS CompletedPhases,
    (SUM(CASE WHEN cp.Status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(DISTINCT cp.PhaseID), 0)) AS CompletionPercentage
FROM 
    Projects p
LEFT JOIN 
    BuildingSections bs ON p.ProjectID = bs.ProjectID
LEFT JOIN 
    ConstructionPhases cp ON bs.SectionID = cp.SectionID
GROUP BY 
    p.ProjectID, p.ProjectName, p.StartDate, p.TargetCompletionDate, p.Status;

-- Create a stored procedure to update project status
CREATE PROCEDURE UpdateProjectStatus
    @ProjectID INT,
    @NewStatus VARCHAR(20)
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- Validate status
        IF @NewStatus NOT IN ('Planning', 'In Progress', 'On Hold', 'Completed')
        BEGIN
            RAISERROR('Invalid status value', 16, 1);
        END
        
        -- Update project status
        UPDATE Projects 
        SET Status = @NewStatus, 
            UpdatedAt = GETDATE()
        WHERE ProjectID = @ProjectID;
        
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;
        
        THROW;
    END CATCH
END;
GO

-- Create a trigger to update timestamps
CREATE TRIGGER TR_Projects_UpdateTimestamp
ON Projects
AFTER UPDATE
AS
BEGIN
    UPDATE Projects
    SET UpdatedAt = GETDATE()
    WHERE ProjectID IN (SELECT ProjectID FROM inserted);
END;
GO

-- Create a function to calculate remaining budget
CREATE FUNCTION CalculateRemainingBudget(@ProjectID INT)
RETURNS DECIMAL(15,2)
AS
BEGIN
    DECLARE @TotalBudget DECIMAL(15,2);
    DECLARE @TotalExpenses DECIMAL(15,2);
    
    SELECT @TotalBudget = Budget FROM Projects WHERE ProjectID = @ProjectID;
    
    SELECT @TotalExpenses = SUM(Amount)
    FROM BudgetTransactions
    WHERE ProjectID = @ProjectID AND TransactionType = 'Expense';
    
    RETURN @TotalBudget - ISNULL(@TotalExpenses, 0);
END;
GO
```
