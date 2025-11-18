"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a database schema for managing client cosmetic projects, including formulation details, packaging options, and quality control checkpoints, as described by Fabricare Cosméticos.
Generated: DETERMINISTIC_a38720a95c9ba9a8
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Client Cosmetic Projects
CREATE DATABASE FabricareCosmetics;

USE FabricareCosmetics;

-- Table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    ClientName VARCHAR(100) NOT NULL,
    ContactEmail VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for storing cosmetic projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(100) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table for storing formulation details
CREATE TABLE Formulations (
    FormulationID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    IngredientName VARCHAR(100) NOT NULL,
    Quantity DECIMAL(10, 2) NOT NULL,
    Unit VARCHAR(50) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table for storing packaging options
CREATE TABLE PackagingOptions (
    PackagingID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    PackagingType VARCHAR(100) NOT NULL,
    Volume DECIMAL(10, 2) NOT NULL,
    Material VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table for quality control checkpoints
CREATE TABLE QualityControl (
    CheckpointID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    CheckpointDescription TEXT NOT NULL,
    CheckpointDate DATE NOT NULL,
    Status ENUM('Passed', 'Failed', 'Pending') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Indexes for efficient querying
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_formulation_project ON Formulations(ProjectID);
CREATE INDEX idx_packaging_project ON PackagingOptions(ProjectID);
CREATE INDEX idx_quality_control_project ON QualityControl(ProjectID);

-- Ensure that all newly created tables have consistent data types and constraints
-- Additional constraints and triggers can be added as per business logic requirements
```
