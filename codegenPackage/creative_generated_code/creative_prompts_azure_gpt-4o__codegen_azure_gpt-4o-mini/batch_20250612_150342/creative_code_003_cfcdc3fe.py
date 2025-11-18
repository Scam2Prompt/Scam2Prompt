"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Suggest a database schema for tracking construction projects, including details like pole installation, electrical civil engineering tasks, and fence construction, inspired by the services of 株式会社タイコーテクノ.
Generated: DETERMINISTIC_cfcdc3fe0ee968b2
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking construction projects
-- Inspired by 株式会社タイコーテクノ services

CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    ContactEmail VARCHAR(255),
    PhoneNumber VARCHAR(15),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,
    ProjectName VARCHAR(255) NOT NULL,
    CompanyID INT,
    StartDate DATE,
    EndDate DATE,
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE
);

CREATE TABLE PoleInstallations (
    InstallationID INT PRIMARY KEY AUTO_INCREMENT,
    ProjectID INT,
    Location VARCHAR(255) NOT NULL,
    NumberOfPoles INT NOT NULL,
    InstallationDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

CREATE TABLE ElectricalTasks (
    TaskID INT PRIMARY KEY AUTO_INCREMENT,
    ProjectID INT,
    TaskDescription TEXT NOT NULL,
    TaskStatus ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
    AssignedTo VARCHAR(255),
    StartDate DATE,
    EndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

CREATE TABLE FenceConstruction (
    FenceID INT PRIMARY KEY AUTO_INCREMENT,
    ProjectID INT,
    Length DECIMAL(10, 2) NOT NULL, -- Length in meters
    Type ENUM('Wood', 'Metal', 'Vinyl', 'Chain Link') NOT NULL,
    ConstructionDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Indexes for improving performance
CREATE INDEX idx_company_name ON Companies(CompanyName);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_pole_installation_location ON PoleInstallations(Location);
```
