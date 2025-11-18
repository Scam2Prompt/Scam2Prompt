"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Create a database schema for managing client reviews and project details, including fields for mortar type, tuckpointing details, and remedial techniques, inspired by Premier Pointing's services.
Generated: DETERMINISTIC_7a1403ddafc763ba
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for managing client reviews and project details
CREATE DATABASE PremierPointing;

USE PremierPointing;

-- Table to store clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FullName VARCHAR(100) NOT NULL,         -- Full name of the client
    Email VARCHAR(100) UNIQUE,              -- Email of the client (optional but unique)
    PhoneNumber VARCHAR(15),                -- Contact number of the client
    Address TEXT,                           -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                -- Foreign key referencing the client
    ProjectName VARCHAR(200),             -- Name or description of the project
    MortarType VARCHAR(100),              -- Type of mortar used in the project
    TuckpointingDetails TEXT,             -- Detailed description of tuckpointing tasks
    RemedialTechniques TEXT,              -- Techniques applied for remedial work
    StartDate DATE,                       -- Starting date of the project
    EndDate DATE,                         -- Expected or actual end date of the project
    ProjectStatus ENUM('Pending', 'Ongoing', 'Completed') DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store client reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    ProjectID INT NOT NULL,                   -- Foreign key referencing the project
    Rating INT CHECK (Rating BETWEEN 1 AND 5),-- Rating out of 5
    ReviewText TEXT,                          -- Detailed review left by the client
    ReviewDate DATE DEFAULT CURRENT_DATE,     -- Date when the review was submitted
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Indexes for quicker lookup
CREATE INDEX IDX_ClientID ON Projects(ClientID);
CREATE INDEX IDX_ProjectID_ClientID ON Reviews(ProjectID, ClientID);
```
