"""
Generated Code Metadata:
========================
Original URL: https://cocula.gob.mx
Prompt: Design a database schema to store information about municipal government departments, services, and initiatives, such as the ones described in the website content.
Generated: DETERMINISTIC_0730fb145f56f513
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about municipal government departments, services, and initiatives

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Initiatives;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Departments;

-- Table to store information about government departments
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each department
    Name VARCHAR(255) NOT NULL,                   -- Name of the department
    Description TEXT,                              -- Description of the department's responsibilities
    ContactEmail VARCHAR(255),                     -- Contact email for the department
    PhoneNumber VARCHAR(20),                       -- Contact phone number for the department
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about services offered by departments
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each service
    DepartmentID INT,                              -- Foreign key referencing Departments
    Name VARCHAR(255) NOT NULL,                    -- Name of the service
    Description TEXT,                              -- Description of the service
    Availability VARCHAR(255),                     -- Availability details (e.g., hours of operation)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about initiatives undertaken by departments
CREATE TABLE Initiatives (
    InitiativeID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each initiative
    DepartmentID INT,                               -- Foreign key referencing Departments
    Title VARCHAR(255) NOT NULL,                    -- Title of the initiative
    Description TEXT,                               -- Description of the initiative
    StartDate DATE,                                -- Start date of the initiative
    EndDate DATE,                                  -- End date of the initiative
    Status ENUM('Planned', 'Ongoing', 'Completed') NOT NULL, -- Current status of the initiative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes can be added for performance optimization if necessary
CREATE INDEX idx_department_name ON Departments(Name);
CREATE INDEX idx_service_name ON Services(Name);
CREATE INDEX idx_initiative_title ON Initiatives(Title);
```
