"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Design a database schema for an NDIS provider that tracks client goals, support services, and community engagement, reflecting the tailored services provided by Shareth Homecare.
Generated: DETERMINISTIC_a8aa5596c86a478d
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking client goals, support services, and community engagement
-- for Shareth Homecare as an NDIS provider.

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,                  -- Client's first name
    LastName VARCHAR(100) NOT NULL,                   -- Client's last name
    DateOfBirth DATE NOT NULL,                        -- Client's date of birth
    ContactNumber VARCHAR(15) NOT NULL,               -- Client's contact number
    EmailAddress VARCHAR(100),                        -- Optional email address
    Address TEXT NOT NULL,                            -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store client goals
CREATE TABLE ClientGoals (
    GoalID INT PRIMARY KEY AUTO_INCREMENT,            -- Unique identifier for each goal
    ClientID INT NOT NULL,                            -- Foreign key referencing Clients
    GoalDescription TEXT NOT NULL,                   -- Description of the goal
    StartDate DATE NOT NULL,                          -- Start date for the goal
    EndDate DATE,                                     -- Optional end date for the goal
    ProgressStatus ENUM('Not Started', 'In Progress', 'Completed') DEFAULT 'Not Started', -- Progress status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE   -- Cascade delete for referenced client
);

-- Table to store support services offered to clients
CREATE TABLE SupportServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,                -- Name of the service
    ServiceDescription TEXT,                          -- Detailed description of the service
    ServiceCost DECIMAL(10, 2) NOT NULL,              -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to track services availed by clients
CREATE TABLE ClientServices (
    ClientServiceID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each record
    ClientID INT NOT NULL,                            -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                           -- Foreign key referencing SupportServices
    StartDate DATE NOT NULL,                          -- Start date of the service
    EndDate DATE,                                     -- Optional end date of the service
    Notes TEXT,                                       -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,   -- Cascade delete for referenced client
    FOREIGN KEY (ServiceID) REFERENCES SupportServices(ServiceID) ON DELETE CASCADE -- Cascade delete for referenced service
);

-- Table to store community engagement activities
CREATE TABLE CommunityEngagement (
    EngagementID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each activity
    ClientID INT NOT NULL,                            -- Foreign key referencing Clients
    ActivityName VARCHAR(100) NOT NULL,               -- Name of the community activity
    ActivityDescription TEXT,                         -- Detailed description of the activity
    EngagementDate DATE NOT NULL,                     -- Date of the engagement
    Feedback TEXT,                                    -- Feedback from the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE    -- Cascade delete for referenced client
);

-- Ensure proper indexing for optimized queries
CREATE INDEX idx_ClientGoals_ClientID ON ClientGoals(ClientID);
CREATE INDEX idx_ClientServices_ClientID ON ClientServices(ClientID);
CREATE INDEX idx_ClientServices_ServiceID ON ClientServices(ServiceID);
CREATE INDEX idx_CommunityEngagement_ClientID ON CommunityEngagement(ClientID);
```
