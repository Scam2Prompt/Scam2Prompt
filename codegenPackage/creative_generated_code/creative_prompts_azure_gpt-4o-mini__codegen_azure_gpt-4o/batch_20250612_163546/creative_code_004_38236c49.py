"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Design a database schema for managing high-quality legal leads, incorporating the specific types of cases highlighted on ClaimLink, such as truck and motorcycle accidents.
Generated: DETERMINISTIC_38236c49d08ebb89
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to manage high-quality legal leads

-- Create a table to store information about the types of cases
CREATE TABLE CaseTypes (
    CaseTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each case type
    CaseTypeName VARCHAR(255) NOT NULL,        -- Name of the case type (e.g., 'Truck Accident', 'Motorcycle Accident')
    Description TEXT                           -- Detailed description of the case type
);

-- Create a table to store lead information
CREATE TABLE LegalLeads (
    LeadID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique ID for each lead
    FullName VARCHAR(255) NOT NULL,             -- Full name of the lead
    Email VARCHAR(255) NOT NULL,                -- Email address of the lead
    PhoneNumber VARCHAR(15) NOT NULL,           -- Phone number of the lead
    CaseTypeID INT NOT NULL,                    -- Foreign key linking to CaseTypes
    LeadDetails TEXT,                           -- Additional details about the lead's case
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the lead was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    CONSTRAINT FK_CaseType FOREIGN KEY (CaseTypeID) REFERENCES CaseTypes(CaseTypeID) ON DELETE CASCADE
);

-- Create a table to track the status of each lead
CREATE TABLE LeadStatus (
    StatusID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each status
    StatusName VARCHAR(255) NOT NULL         -- Name of the status (e.g., 'New', 'Under Review', 'Closed')
);

-- Create a table to manage the status history of each lead
CREATE TABLE LeadStatusHistory (
    HistoryID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique ID for each history entry
    LeadID INT NOT NULL,                          -- Foreign key referencing LegalLeads
    StatusID INT NOT NULL,                        -- Foreign key referencing LeadStatus
    ChangedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the status was changed
    Notes TEXT,                                   -- Optional notes about the status change
    CONSTRAINT FK_Lead FOREIGN KEY (LeadID) REFERENCES LegalLeads(LeadID) ON DELETE CASCADE,
    CONSTRAINT FK_Status FOREIGN KEY (StatusID) REFERENCES LeadStatus(StatusID) ON DELETE CASCADE
);

-- Create a table to store user information for those managing leads
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique ID for each user
    FullName VARCHAR(255) NOT NULL,            -- Full name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the user (unique for login purposes)
    PasswordHash VARCHAR(255) NOT NULL,        -- Securely hashed password
    Role ENUM('Admin', 'Manager', 'Reviewer') NOT NULL, -- Role of the user in the system
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user account was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table to track user actions for auditing purposes
CREATE TABLE AuditLog (
    AuditID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique ID for each audit record
    UserID INT NOT NULL,                        -- Foreign key referencing Users
    Action VARCHAR(255) NOT NULL,               -- Description of the action performed
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the action occurred
    CONSTRAINT FK_User FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);
```
