"""
Generated Code Metadata:
========================
Original URL: https://tari.ee
Prompt: Create a database schema for managing architectural projects, including fields for client needs and rational solutions, as outlined on Tari.ee.
Generated: DETERMINISTIC_15cd99cba158f819
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing architectural projects

CREATE DATABASE IF NOT EXISTS ArchitecturalProjects;

USE ArchitecturalProjects;

-- Table to store client information
CREATE TABLE IF NOT EXISTS Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ContactEmail VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store project information
CREATE TABLE IF NOT EXISTS Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(100) NOT NULL,
    Description TEXT,
    StartDate DATE,
    EndDate DATE,
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store client needs for each project
CREATE TABLE IF NOT EXISTS ClientNeeds (
    NeedID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    NeedDescription TEXT NOT NULL,
    Priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table to store rational solutions for each project
CREATE TABLE IF NOT EXISTS RationalSolutions (
    SolutionID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    SolutionDescription TEXT NOT NULL,
    EffectivenessRating INT CHECK (EffectivenessRating BETWEEN 1 AND 10),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(ContactEmail);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_project_priority ON ClientNeeds(Priority);
CREATE INDEX idx_solution_rating ON RationalSolutions(EffectivenessRating);
```
