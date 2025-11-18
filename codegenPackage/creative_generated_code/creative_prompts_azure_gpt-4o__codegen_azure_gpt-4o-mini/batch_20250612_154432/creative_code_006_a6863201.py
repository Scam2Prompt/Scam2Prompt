"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeg-group.com
Prompt: Create a database schema to manage project details for residential and commercial outdoor environments, inspired by the project categories listed on the Outdoor Environments Group website.
Generated: DETERMINISTIC_a6863201e6f3b705
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing project details for residential and commercial outdoor environments

CREATE DATABASE OutdoorEnvironments;

USE OutdoorEnvironments;

-- Table to store project categories (residential and commercial)
CREATE TABLE ProjectCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectName VARCHAR(255) NOT NULL,
    CategoryID INT NOT NULL,
    StartDate DATE,
    EndDate DATE,
    Budget DECIMAL(10, 2) CHECK (Budget >= 0),
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES ProjectCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store project details
CREATE TABLE ProjectDetails (
    DetailID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    DetailDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table to store team members involved in the projects
CREATE TABLE TeamMembers (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    MemberName VARCHAR(255) NOT NULL,
    Role VARCHAR(100),
    ContactEmail VARCHAR(255) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to link team members with projects
CREATE TABLE ProjectTeamMembers (
    ProjectID INT NOT NULL,
    MemberID INT NOT NULL,
    PRIMARY KEY (ProjectID, MemberID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (MemberID) REFERENCES TeamMembers(MemberID) ON DELETE CASCADE
);

-- Table to store project locations
CREATE TABLE ProjectLocations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    ZipCode VARCHAR(20) NOT NULL,
    Latitude DECIMAL(9, 6),
    Longitude DECIMAL(9, 6),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Sample data insertion for categories
INSERT INTO ProjectCategories (CategoryName, Description) VALUES
('Residential', 'Projects related to residential outdoor environments'),
('Commercial', 'Projects related to commercial outdoor environments');

-- Sample data insertion for projects
INSERT INTO Projects (ProjectName, CategoryID, StartDate, EndDate, Budget, Status) VALUES
('Backyard Landscaping', 1, '2023-05-01', '2023-08-01', 15000.00, 'In Progress'),
('Office Park Development', 2, '2023-03-01', '2023-07-01', 50000.00, 'Pending');

-- Sample data insertion for team members
INSERT INTO TeamMembers (MemberName, Role, ContactEmail) VALUES
('Alice Johnson', 'Project Manager', 'alice.johnson@example.com'),
('Bob Smith', 'Landscape Architect', 'bob.smith@example.com');

-- Sample data insertion for project details
INSERT INTO ProjectDetails (ProjectID, DetailDescription) VALUES
(1, 'Design layout for plants and hardscaping'),
(2, 'Create blueprints for office park development');

-- Sample data insertion for project locations
INSERT INTO ProjectLocations (ProjectID, Address, City, State, ZipCode, Latitude, Longitude) VALUES
(1, '123 Main St', 'Springfield', 'IL', '62701', 39.7817, -89.6501),
(2, '456 Corporate Blvd', 'Chicago', 'IL', '60601', 41.8781, -87.6298);

-- Sample data insertion for team member assignments
INSERT INTO ProjectTeamMembers (ProjectID, MemberID) VALUES
(1, 1), -- Alice Johnson assigned to Backyard Landscaping
(2, 2); -- Bob Smith assigned to Office Park Development
```
