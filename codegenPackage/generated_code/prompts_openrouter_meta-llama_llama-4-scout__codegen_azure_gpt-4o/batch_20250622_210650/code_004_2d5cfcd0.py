"""
Generated Code Metadata:
========================
Original URL: https://simplecede.com
Prompt: Design a simple database schema for a company like Simplécede that wants to store information about its projects, team members, and contacts.
Generated: DETERMINISTIC_2d5cfcd070fbfae4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a company to store information about projects, team members, and contacts

-- Table to store information about projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about team members
CREATE TABLE TeamMembers (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team member
    FirstName VARCHAR(100) NOT NULL,         -- First name of the team member
    LastName VARCHAR(100) NOT NULL,          -- Last name of the team member
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the team member
    PhoneNumber VARCHAR(15),                 -- Phone number of the team member
    Role VARCHAR(100) NOT NULL,              -- Role of the team member (e.g., Developer, Manager)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the team member was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about contacts
CREATE TABLE Contacts (
    ContactID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contact
    Name VARCHAR(255) NOT NULL,               -- Name of the contact
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the contact
    PhoneNumber VARCHAR(15),                  -- Phone number of the contact
    Company VARCHAR(255),                     -- Company name of the contact
    Notes TEXT,                               -- Additional notes about the contact
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the contact was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store the relationship between projects and team members
CREATE TABLE ProjectTeamMembers (
    ProjectID INT NOT NULL,                   -- Foreign key referencing Projects table
    MemberID INT NOT NULL,                    -- Foreign key referencing TeamMembers table
    RoleInProject VARCHAR(100),               -- Role of the team member in the project
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the team member was assigned to the project
    PRIMARY KEY (ProjectID, MemberID),        -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (MemberID) REFERENCES TeamMembers(MemberID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store the relationship between projects and contacts
CREATE TABLE ProjectContacts (
    ProjectID INT NOT NULL,                   -- Foreign key referencing Projects table
    ContactID INT NOT NULL,                   -- Foreign key referencing Contacts table
    RoleInProject VARCHAR(100),               -- Role of the contact in the project
    AssociatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the contact was associated with the project
    PRIMARY KEY (ProjectID, ContactID),       -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ContactID) REFERENCES Contacts(ContactID) ON DELETE CASCADE -- Cascade delete
);
```
