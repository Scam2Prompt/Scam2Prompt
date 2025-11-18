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
-- Database Schema for managing project details for residential and commercial outdoor environments

-- Create a table for storing information about project categories (e.g., residential, commercial, etc.)
CREATE TABLE ProjectCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL,                -- Name of the category (e.g., "Residential", "Commercial")
    Description TEXT                           -- Optional description of the category
);

-- Create a table for storing projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    Name VARCHAR(150) NOT NULL,                -- Name of the project
    Description TEXT,                          -- Detailed description of the project
    CategoryID INT NOT NULL,                   -- Foreign key to the ProjectCategories table
    ClientName VARCHAR(100),                   -- Name of the client
    Address VARCHAR(255),                      -- Address where the project is located
    StartDate DATE,                            -- Project start date
    EndDate DATE,                              -- Project end date (can be NULL for ongoing projects)
    Budget DECIMAL(15, 2),                     -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Planned', -- Status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for project creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Auto-updated timestamp
    FOREIGN KEY (CategoryID) REFERENCES ProjectCategories(CategoryID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Create a table for storing team members involved in projects
CREATE TABLE TeamMembers (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each team member
    FullName VARCHAR(150) NOT NULL,            -- Full name of the team member
    Role VARCHAR(100) NOT NULL,                -- Role of the team member (e.g., "Designer", "Architect")
    PhoneNumber VARCHAR(15),                   -- Contact phone number
    Email VARCHAR(150),                        -- Contact email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for team member creation
);

-- Create a table for assigning team members to projects
CREATE TABLE ProjectTeamAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    ProjectID INT NOT NULL,                      -- Foreign key to the Projects table
    MemberID INT NOT NULL,                       -- Foreign key to the TeamMembers table
    AssignedRole VARCHAR(100) NOT NULL,          -- Role assigned to the team member for the specific project
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for assignment creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Enforce referential integrity
    FOREIGN KEY (MemberID) REFERENCES TeamMembers(MemberID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Create a table for tracking project milestones
CREATE TABLE ProjectMilestones (
    MilestoneID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each milestone
    ProjectID INT NOT NULL,                     -- Foreign key to the Projects table
    Title VARCHAR(150) NOT NULL,                -- Title of the milestone
    Description TEXT,                           -- Detailed description of the milestone
    DueDate DATE NOT NULL,                      -- Expected due date for the milestone
    Status ENUM('Planned', 'Completed') DEFAULT 'Planned', -- Status of the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for milestone creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Auto-updated timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Error handling and validation should be implemented at the application level during operations (e.g., inserting/updating data).
```
