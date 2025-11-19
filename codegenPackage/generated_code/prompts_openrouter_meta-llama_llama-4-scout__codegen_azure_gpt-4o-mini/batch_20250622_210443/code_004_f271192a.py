"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: "Design a database schema for storing information about clients, talent profiles, and recruitment processes for a consulting firm that offers international talent selection services."
Generated: DETERMINISTIC_f271192a4acb8ed8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a consulting firm offering international talent selection services

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactEmail VARCHAR(255) UNIQUE NOT NULL, -- Email address for client contact
    PhoneNumber VARCHAR(20),                   -- Phone number for client contact
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store talent profiles
CREATE TABLE TalentProfiles (
    TalentID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each talent profile
    FirstName VARCHAR(100) NOT NULL,           -- First name of the talent
    LastName VARCHAR(100) NOT NULL,            -- Last name of the talent
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the talent
    PhoneNumber VARCHAR(20),                    -- Phone number of the talent
    Skills TEXT,                                -- Skills of the talent (comma-separated)
    ExperienceYears INT CHECK (ExperienceYears >= 0), -- Years of experience
    Availability BOOLEAN DEFAULT TRUE,          -- Availability status of the talent
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the profile was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store recruitment processes
CREATE TABLE RecruitmentProcesses (
    ProcessID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each recruitment process
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    TalentID INT NOT NULL,                      -- Foreign key referencing TalentProfiles
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Status of the recruitment process
    StartDate DATE NOT NULL,                    -- Start date of the recruitment process
    EndDate DATE,                               -- End date of the recruitment process (nullable)
    Feedback TEXT,                              -- Feedback from the client (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the process was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TalentID) REFERENCES TalentProfiles(TalentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(ContactEmail);
CREATE INDEX idx_talent_email ON TalentProfiles(Email);
CREATE INDEX idx_recruitment_status ON RecruitmentProcesses(Status);
```
