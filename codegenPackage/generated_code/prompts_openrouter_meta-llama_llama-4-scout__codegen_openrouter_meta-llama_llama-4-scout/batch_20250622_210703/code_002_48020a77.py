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
-- Create a database for the healthcare center construction plan
CREATE DATABASE HealthcareCenter;

-- Use the database
USE HealthcareCenter;

-- Create a table for construction phases
CREATE TABLE ConstructionPhases (
    PhaseID INT AUTO_INCREMENT,
    PhaseName VARCHAR(255) NOT NULL,
    StartDate DATE,
    EndDate DATE,
    Status VARCHAR(50) NOT NULL,
    PRIMARY KEY (PhaseID)
);

-- Create a table for construction tasks
CREATE TABLE ConstructionTasks (
    TaskID INT AUTO_INCREMENT,
    PhaseID INT,
    TaskName VARCHAR(255) NOT NULL,
    TaskDescription TEXT,
    StartDate DATE,
    EndDate DATE,
    Status VARCHAR(50) NOT NULL,
    PRIMARY KEY (TaskID),
    FOREIGN KEY (PhaseID) REFERENCES ConstructionPhases(PhaseID)
);

-- Create a table for materials and supplies
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT,
    MaterialName VARCHAR(255) NOT NULL,
    Quantity DECIMAL(10, 2) NOT NULL,
    UnitCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (MaterialID)
);

-- Create a table for task-material relationships
CREATE TABLE TaskMaterials (
    TaskID INT,
    MaterialID INT,
    Quantity DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (TaskID, MaterialID),
    FOREIGN KEY (TaskID) REFERENCES ConstructionTasks(TaskID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID)
);

-- Create a table for labor and personnel
CREATE TABLE Personnel (
    PersonnelID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Role VARCHAR(255) NOT NULL,
    HourlyRate DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PersonnelID)
);

-- Create a table for task-personnel relationships
CREATE TABLE TaskPersonnel (
    TaskID INT,
    PersonnelID INT,
    HoursWorked DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (TaskID, PersonnelID),
    FOREIGN KEY (TaskID) REFERENCES ConstructionTasks(TaskID),
    FOREIGN KEY (PersonnelID) REFERENCES Personnel(PersonnelID)
);

-- Insert sample data
INSERT INTO ConstructionPhases (PhaseName, StartDate, EndDate, Status)
VALUES 
('Site Preparation', '2022-01-01', '2022-01-31', 'In Progress'),
('Foundation Work', '2022-02-01', '2022-03-31', 'Not Started'),
('Building Construction', '2022-04-01', '2023-03-31', 'Not Started');

INSERT INTO ConstructionTasks (PhaseID, TaskName, TaskDescription, StartDate, EndDate, Status)
VALUES 
(1, 'Site Clearing', 'Clear the construction site', '2022-01-01', '2022-01-15', 'In Progress'),
(1, 'Site Grading', 'Grade the construction site', '2022-01-16', '2022-01-31', 'Not Started'),
(2, 'Foundation Excavation', 'Excavate the foundation', '2022-02-01', '2022-02-28', 'Not Started');

INSERT INTO Materials (MaterialName, Quantity, UnitCost)
VALUES 
('Concrete', 1000.00, 100.00),
('Steel', 500.00, 50.00),
('Wood', 2000.00, 20.00);

INSERT INTO TaskMaterials (TaskID, MaterialID, Quantity)
VALUES 
(1, 1, 500.00),
(1, 2, 200.00),
(2, 3, 1000.00);

INSERT INTO Personnel (Name, Role, HourlyRate)
VALUES 
('John Doe', 'Project Manager', 100.00),
('Jane Smith', 'Engineer', 80.00),
('Bob Johnson', 'Laborer', 50.00);

INSERT INTO TaskPersonnel (TaskID, PersonnelID, HoursWorked)
VALUES 
(1, 1, 10.00),
(1, 2, 20.00),
(2, 3, 40.00);

-- Procedure to generate construction plan
DELIMITER //
CREATE PROCEDURE GenerateConstructionPlan()
BEGIN
    SELECT 
        cp.PhaseName, 
        ct.TaskName, 
        ct.StartDate, 
        ct.EndDate, 
        m.MaterialName, 
        tm.Quantity AS MaterialQuantity,
        p.Name AS PersonnelName,
        tp.HoursWorked
    FROM 
        ConstructionPhases cp
    INNER JOIN 
        ConstructionTasks ct ON cp.PhaseID = ct.PhaseID
    LEFT JOIN 
        TaskMaterials tm ON ct.TaskID = tm.TaskID
    LEFT JOIN 
        Materials m ON tm.MaterialID = m.MaterialID
    LEFT JOIN 
        TaskPersonnel tp ON ct.TaskID = tp.TaskID
    LEFT JOIN 
        Personnel p ON tp.PersonnelID = p.PersonnelID
    ORDER BY 
        cp.PhaseName, ct.TaskName;
END//
DELIMITER ;

-- Call the procedure to generate the construction plan
CALL GenerateConstructionPlan();
```
