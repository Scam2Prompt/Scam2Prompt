"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lojaoficial.cloud
Prompt: Suggest a database schema for storing architectural project data, inspired by the Études Architect application’s functionality described on lojaoficial.cloud.
Generated: DETERMINISTIC_77e2f974dcdc95dd
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Architectural Project Data

-- Table to store information about architects
CREATE TABLE Architects (
    ArchitectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each architect
    FirstName VARCHAR(100) NOT NULL,           -- First name of the architect
    LastName VARCHAR(100) NOT NULL,            -- Last name of the architect
    Email VARCHAR(255) UNIQUE,                 -- Contact email
    PhoneNumber VARCHAR(20),                   -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store architectural projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    Description TEXT,                          -- Detailed description of the project
    StartDate DATE,                            -- Project start date
    EndDate DATE,                              -- Project end date (can be NULL for ongoing projects)
    ArchitectID INT NOT NULL,                  -- Foreign key linking to Architects table
    Budget DECIMAL(18, 2),                     -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed') DEFAULT 'Planned', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ArchitectID) REFERENCES Architects(ArchitectID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store project materials
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    MaterialName VARCHAR(255) NOT NULL,        -- Name of the material
    UnitCost DECIMAL(18, 2) NOT NULL,          -- Cost per unit of the material
    Quantity INT NOT NULL,                     -- Quantity of material used
    ProjectID INT NOT NULL,                    -- Foreign key linking to Projects table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store project activities/tasks
CREATE TABLE ProjectTasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each task
    TaskName VARCHAR(255) NOT NULL,            -- Name of the task
    Description TEXT,                          -- Detailed description of the task
    AssignedTo VARCHAR(255),                   -- Name or identifier of the person assigned to the task
    DueDate DATE,                              -- Due date for the task
    Status ENUM('Not Started', 'In Progress', 'Completed') DEFAULT 'Not Started', -- Current status of the task
    ProjectID INT NOT NULL,                    -- Foreign key linking to Projects table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store project documents (e.g., blueprints, reports)
CREATE TABLE ProjectDocuments (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each document
    DocumentName VARCHAR(255) NOT NULL,        -- Name of the document
    DocumentType ENUM('Blueprint', 'Report', 'Contract', 'Other') DEFAULT 'Other', -- Type of document
    FilePath VARCHAR(500) NOT NULL,            -- Path to the stored file
    UploadDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for file upload
    ProjectID INT NOT NULL,                    -- Foreign key linking to Projects table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,           -- First name of the client
    LastName VARCHAR(100) NOT NULL,            -- Last name of the client
    Email VARCHAR(255) UNIQUE,                 -- Contact email
    PhoneNumber VARCHAR(20),                   -- Contact phone number
    Address TEXT,                              -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store relationships between clients and projects
CREATE TABLE ClientProjects (
    ClientProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client-project relation
    ClientID INT NOT NULL,                          -- Foreign key linking to Clients table
    ProjectID INT NOT NULL,                         -- Foreign key linking to Projects table
    Role ENUM('Owner', 'Stakeholder', 'Other') DEFAULT 'Other', -- Role of the client in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Foreign key constraint
);
```
