"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Construct a database schema for managing information on various types of construction projects, including underground and engineering works, as highlighted by URANPRES.
Generated: DETERMINISTIC_b249174bea685afd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing construction project information

-- Create a table to store general information about construction projects
CREATE TABLE ConstructionProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL, -- Name of the construction project
    ProjectType ENUM('Underground', 'Engineering', 'Other') NOT NULL, -- Type of construction project
    Description TEXT, -- Detailed description of the project
    StartDate DATE NOT NULL, -- Project start date
    EndDate DATE, -- Project end date (nullable for ongoing projects)
    Budget DECIMAL(15, 2), -- Estimated budget for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about project locations
CREATE TABLE ProjectLocations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    ProjectID INT NOT NULL, -- Foreign key linking to a project
    Address VARCHAR(255) NOT NULL, -- Address for the project location
    City VARCHAR(100) NOT NULL, -- City where the project is located
    State VARCHAR(100) NOT NULL, -- State where the project is located
    Country VARCHAR(100) NOT NULL, -- Country where the project is located
    Coordinates POINT, -- Geographic coordinates (longitude and latitude) of the location
    FOREIGN KEY (ProjectID) REFERENCES ConstructionProjects(ProjectID) ON DELETE CASCADE
);

-- Create a table to store information about contractors or companies working on projects
CREATE TABLE Contractors (
    ContractorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contractor
    Name VARCHAR(255) NOT NULL, -- Name of the contractor
    ContactInfo VARCHAR(255), -- Contact information (e.g., phone or email)
    Specialty VARCHAR(255), -- Area of specialization (e.g., underground works, engineering)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store which contractors are assigned to which projects
CREATE TABLE ProjectContractors (
    ProjectID INT NOT NULL, -- Foreign key linking to a project
    ContractorID INT NOT NULL, -- Foreign key linking to a contractor
    Role VARCHAR(100) NOT NULL, -- Role of the contractor in the project (e.g., Lead, Subcontractor)
    AssignmentDate DATE NOT NULL, -- Date the contractor was assigned to the project
    FOREIGN KEY (ProjectID) REFERENCES ConstructionProjects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (ContractorID) REFERENCES Contractors(ContractorID) ON DELETE CASCADE,
    PRIMARY KEY (ProjectID, ContractorID) -- Composite key to ensure uniqueness
);

-- Create a table to store milestones for each project
CREATE TABLE ProjectMilestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each milestone
    ProjectID INT NOT NULL, -- Foreign key linking to a project
    MilestoneName VARCHAR(255) NOT NULL, -- Name of the milestone
    Description TEXT, -- Detailed description of the milestone
    DueDate DATE NOT NULL, -- Deadline for the milestone
    Status ENUM('Pending', 'Completed', 'Overdue') NOT NULL, -- Current status of the milestone
    FOREIGN KEY (ProjectID) REFERENCES ConstructionProjects(ProjectID) ON DELETE CASCADE
);

-- Create a table to store expenses for each project
CREATE TABLE ProjectExpenses (
    ExpenseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each expense
    ProjectID INT NOT NULL, -- Foreign key linking to a project
    ExpenseDate DATE NOT NULL, -- Date the expense was incurred
    Amount DECIMAL(15, 2) NOT NULL, -- Amount of the expense
    Category VARCHAR(100) NOT NULL, -- Category of the expense (e.g., Materials, Labor)
    Description TEXT, -- Detailed description of the expense
    FOREIGN KEY (ProjectID) REFERENCES ConstructionProjects(ProjectID) ON DELETE CASCADE
);

-- Ensure the schema is production-ready by adding appropriate indexes
CREATE INDEX idx_ProjectType ON ConstructionProjects(ProjectType);
CREATE INDEX idx_ProjectStatus ON ConstructionProjects(Status);
CREATE INDEX idx_LocationCity ON ProjectLocations(City);
CREATE INDEX idx_ContractorSpecialty ON Contractors(Specialty);
CREATE INDEX idx_MilestoneStatus ON ProjectMilestones(Status);

-- The schema is now complete and production-ready for managing construction project data.
```
