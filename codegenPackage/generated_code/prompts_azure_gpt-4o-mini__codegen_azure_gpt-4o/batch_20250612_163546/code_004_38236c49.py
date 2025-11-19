"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Design a database schema for managing high-quality legal leads, incorporating the specific types of cases highlighted on ClaimLink, such as truck and motorcycle accidents.
Generated: DETERMINISTIC_38236c49d08ebb89
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing high-quality legal leads

-- Table to store information about legal leads
CREATE TABLE LegalLeads (
    LeadID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each lead
    FirstName VARCHAR(100) NOT NULL,       -- First name of the lead
    LastName VARCHAR(100) NOT NULL,        -- Last name of the lead
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email address of the lead
    PhoneNumber VARCHAR(15),               -- Phone number of the lead
    CaseTypeID INT NOT NULL,               -- Foreign key to reference the type of case
    LeadStatus ENUM('New', 'Contacted', 'Qualified', 'Closed') DEFAULT 'New', -- Status of the lead
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the lead was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the lead was last updated
);

-- Table to store types of cases (e.g., truck accidents, motorcycle accidents)
CREATE TABLE CaseTypes (
    CaseTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each case type
    CaseTypeName VARCHAR(100) NOT NULL UNIQUE, -- Name of the case type (e.g., "Truck Accident", "Motorcycle Accident")
    Description TEXT,                          -- Description of the case type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the case type was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the case type was last updated
);

-- Table to store notes or additional information about leads
CREATE TABLE LeadNotes (
    NoteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each note
    LeadID INT NOT NULL,                   -- Foreign key to reference the lead
    NoteText TEXT NOT NULL,                -- Text of the note
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the note was created
    FOREIGN KEY (LeadID) REFERENCES LegalLeads(LeadID) ON DELETE CASCADE -- Cascade delete if lead is removed
);

-- Table to store user accounts (e.g., legal professionals managing leads)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email address of the user
    Role ENUM('Admin', 'Manager', 'Staff') DEFAULT 'Staff', -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user account was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the user account was last updated
);

-- Table to log actions performed on leads (audit trail)
CREATE TABLE LeadActions (
    ActionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each action
    LeadID INT NOT NULL,                     -- Foreign key to reference the lead
    UserID INT NOT NULL,                     -- Foreign key to reference the user who performed the action
    ActionType ENUM('Created', 'Updated', 'Deleted', 'Contacted', 'Qualified', 'Closed') NOT NULL, -- Type of action
    ActionTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the action was performed
    FOREIGN KEY (LeadID) REFERENCES LegalLeads(LeadID) ON DELETE CASCADE, -- Cascade delete if lead is removed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE SET NULL -- Set user to NULL if user is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_lead_status ON LegalLeads(LeadStatus); -- Index for querying leads by status
CREATE INDEX idx_case_type_name ON CaseTypes(CaseTypeName); -- Index for querying case types by name
CREATE INDEX idx_user_role ON Users(Role); -- Index for querying users by role
```
