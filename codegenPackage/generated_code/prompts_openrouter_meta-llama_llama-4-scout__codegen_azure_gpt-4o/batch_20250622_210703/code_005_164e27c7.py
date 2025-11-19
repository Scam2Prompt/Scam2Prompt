"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Design a simple database schema to store information about clients, projects, and outcomes for a consulting firm like PConsultsa.
Generated: DETERMINISTIC_164e27c73f1e33f9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a consulting firm to store information about clients, projects, and outcomes

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Phone number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the client was added
);

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Description of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Planned', -- Status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was added
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store project outcomes
CREATE TABLE Outcomes (
    OutcomeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each outcome
    ProjectID INT NOT NULL,                   -- Foreign key referencing the project
    Description TEXT NOT NULL,                -- Description of the outcome
    AchievedDate DATE NOT NULL,               -- Date when the outcome was achieved
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the outcome was added
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster lookups
CREATE INDEX idx_client_email ON Clients(Email); -- Index on client email for quick searches
CREATE INDEX idx_project_status ON Projects(Status); -- Index on project status for filtering
CREATE INDEX idx_outcome_project ON Outcomes(ProjectID); -- Index on project ID in outcomes for faster joins
```
