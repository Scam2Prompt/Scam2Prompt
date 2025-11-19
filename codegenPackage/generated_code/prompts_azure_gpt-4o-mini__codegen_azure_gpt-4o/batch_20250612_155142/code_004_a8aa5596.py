"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Design a database schema for an NDIS provider that tracks client goals, support services, and community engagement, reflecting the tailored services provided by Shareth Homecare.
Generated: DETERMINISTIC_a8aa5596c86a478d
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an NDIS provider to track client goals, support services, and community engagement

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,               -- Client's date of birth
    ContactNumber VARCHAR(15),               -- Client's contact number
    Email VARCHAR(100),                      -- Client's email address
    Address TEXT,                            -- Client's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store client goals
CREATE TABLE ClientGoals (
    GoalID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each goal
    ClientID INT NOT NULL,                   -- Foreign key referencing Clients table
    GoalDescription TEXT NOT NULL,           -- Description of the client's goal
    StartDate DATE NOT NULL,                 -- Start date of the goal
    EndDate DATE,                            -- End date of the goal (optional)
    Status ENUM('Active', 'Completed', 'On Hold') DEFAULT 'Active', -- Status of the goal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store support services provided to clients
CREATE TABLE SupportServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the support service
    ServiceDescription TEXT,                  -- Description of the service
    ServiceDate DATE NOT NULL,                -- Date the service was provided
    ProviderName VARCHAR(100),                -- Name of the service provider
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store community engagement activities
CREATE TABLE CommunityEngagement (
    EngagementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each engagement activity
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients table
    ActivityName VARCHAR(100) NOT NULL,          -- Name of the community engagement activity
    ActivityDescription TEXT,                    -- Description of the activity
    ActivityDate DATE NOT NULL,                  -- Date the activity took place
    Location VARCHAR(100),                       -- Location of the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store notes or updates related to clients
CREATE TABLE ClientNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each note
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    NoteContent TEXT NOT NULL,                  -- Content of the note
    CreatedBy VARCHAR(100) NOT NULL,            -- Name of the person who created the note
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_goals_clientid ON ClientGoals(ClientID);
CREATE INDEX idx_support_services_clientid ON SupportServices(ClientID);
CREATE INDEX idx_community_engagement_clientid ON CommunityEngagement(ClientID);
CREATE INDEX idx_client_notes_clientid ON ClientNotes(ClientID);
```
