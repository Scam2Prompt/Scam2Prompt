"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a database schema for managing client cosmetic projects, including formulation details, packaging options, and quality control checkpoints, as described by Fabricare Cosméticos.
Generated: DETERMINISTIC_a38720a95c9ba9a8
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client cosmetic projects
CREATE DATABASE FabricareCosmetics;

USE FabricareCosmetics;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    ClientName VARCHAR(255) NOT NULL,
    ContactEmail VARCHAR(255) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store cosmetic projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(255) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store formulation details
CREATE TABLE Formulations (
    FormulationID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    IngredientName VARCHAR(255) NOT NULL,
    Quantity DECIMAL(10, 2) NOT NULL,
    Unit VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table to store packaging options
CREATE TABLE PackagingOptions (
    PackagingID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    PackagingType VARCHAR(255) NOT NULL,
    Size VARCHAR(50) NOT NULL,
    Material VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table to store quality control checkpoints
CREATE TABLE QualityControl (
    CheckpointID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    CheckpointDescription TEXT NOT NULL,
    CheckDate DATE NOT NULL,
    Result ENUM('Pass', 'Fail') NOT NULL,
    Comments TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_formulation_project ON Formulations(ProjectID);
CREATE INDEX idx_packaging_project ON PackagingOptions(ProjectID);
CREATE INDEX idx_quality_control_project ON QualityControl(ProjectID);
```
