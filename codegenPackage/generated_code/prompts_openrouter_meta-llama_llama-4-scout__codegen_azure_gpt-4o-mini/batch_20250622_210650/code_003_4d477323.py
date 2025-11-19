"""
Generated Code Metadata:
========================
Original URL: https://reyesaluminio.com
Prompt: "Design a database schema to store information about aluminum carpentry projects, including client details, project types, and materials used."
Generated: DETERMINISTIC_4d477323df56b5a2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about aluminum carpentry projects

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS ProjectMaterials;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS ProjectTypes;

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Client's name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email (must be unique)
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store different types of projects
CREATE TABLE ProjectTypes (
    ProjectTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project type
    TypeName VARCHAR(100) NOT NULL UNIQUE,         -- Name of the project type (must be unique)
    Description TEXT                               -- Description of the project type
);

-- Table to store materials used in projects
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL UNIQUE,     -- Name of the material (must be unique)
    Description TEXT                               -- Description of the material
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each project
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    ProjectTypeID INT NOT NULL,                    -- Foreign key referencing ProjectTypes
    StartDate DATE NOT NULL,                       -- Project start date
    EndDate DATE,                                  -- Project end date (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending',  -- Project status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ProjectTypeID) REFERENCES ProjectTypes(ProjectTypeID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store materials used in each project
CREATE TABLE ProjectMaterials (
    ProjectMaterialID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project-material relationship
    ProjectID INT NOT NULL,                             -- Foreign key referencing Projects
    MaterialID INT NOT NULL,                           -- Foreign key referencing Materials
    Quantity DECIMAL(10, 2) NOT NULL,                 -- Quantity of the material used
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample data insertion (for testing purposes)
INSERT INTO Clients (Name, Email, Phone, Address) VALUES
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St, Springfield'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St, Springfield');

INSERT INTO ProjectTypes (TypeName, Description) VALUES
('Window Installation', 'Installation of aluminum windows'),
('Door Installation', 'Installation of aluminum doors');

INSERT INTO Materials (MaterialName, Description) VALUES
('Aluminum Frame', 'High-quality aluminum frame for construction'),
('Glass Panel', 'Tempered glass panel for windows and doors');

-- Note: The above sample data is for demonstration purposes and can be modified as needed.
```
