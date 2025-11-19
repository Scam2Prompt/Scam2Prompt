"""
Generated Code Metadata:
========================
Original URL: https://recruit-overseas.com
Prompt: Design a database schema to store information about job roles, candidates, and clients for a recruitment agency like Recruit Overseas.
Generated: DETERMINISTIC_866734eaf347fd2d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a recruitment agency

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about job roles
CREATE TABLE JobRoles (
    JobRoleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each job role
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    Title VARCHAR(255) NOT NULL,              -- Title of the job role
    Description TEXT,                         -- Description of the job role
    Location VARCHAR(255),                    -- Location of the job role
    SalaryRange VARCHAR(50),                  -- Salary range for the job role
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the job role was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store information about candidates
CREATE TABLE Candidates (
    CandidateID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each candidate
    FirstName VARCHAR(255) NOT NULL,            -- First name of the candidate
    LastName VARCHAR(255) NOT NULL,             -- Last name of the candidate
    Email VARCHAR(255) NOT NULL UNIQUE,         -- Email address of the candidate
    PhoneNumber VARCHAR(15),                    -- Phone number of the candidate
    Resume TEXT,                                -- Link or text for the candidate's resume
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the candidate was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store applications made by candidates for job roles
CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    CandidateID INT NOT NULL,                     -- Foreign key referencing the candidate
    JobRoleID INT NOT NULL,                       -- Foreign key referencing the job role
    ApplicationStatus ENUM('Pending', 'Accepted', 'Rejected') DEFAULT 'Pending', -- Status of the application
    AppliedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the application was made
    FOREIGN KEY (CandidateID) REFERENCES Candidates(CandidateID) ON DELETE CASCADE, -- Cascade delete if candidate is removed
    FOREIGN KEY (JobRoleID) REFERENCES JobRoles(JobRoleID) ON DELETE CASCADE -- Cascade delete if job role is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_name ON Clients(Name);
CREATE INDEX idx_jobrole_title ON JobRoles(Title);
CREATE INDEX idx_candidate_email ON Candidates(Email);
CREATE INDEX idx_application_status ON Applications(ApplicationStatus);
```
