"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-folks.icu
Prompt: Create a database schema in SQL for storing client details, project specifications, and design preferences for a custom home design company like Odos Designs.
Generated: DETERMINISTIC_f18047435391fcdf
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Odos Designs, a custom home design company

-- Create a table for storing client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,         -- First name of the client
    LastName VARCHAR(100) NOT NULL,          -- Last name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client (unique)
    PhoneNumber VARCHAR(15),                 -- Phone number of the client
    Address TEXT,                            -- Address of the client
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the client was added
);

-- Create a table for storing project specifications
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Reference to the Clients table
    ProjectName VARCHAR(150) NOT NULL,        -- Name of the project
    StartDate DATE,                           -- Project start date
    EndDate DATE,                             -- Project end date
    Budget DECIMAL(15, 2),                    -- Budget for the project
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending', -- Project status
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the project was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) -- Establish foreign key relationship
);

-- Create a table for storing design preferences
CREATE TABLE DesignPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for design preferences
    ProjectID INT NOT NULL,                      -- Reference to the Projects table
    Style VARCHAR(100),                          -- Preferred design style (e.g., Modern, Rustic, etc.)
    ColorPalette VARCHAR(255),                  -- Preferred color palette (comma-separated values)
    Features TEXT,                               -- Custom design features (e.g., "Open floor plan, skylights")
    Notes TEXT,                                  -- Additional notes or comments
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the preference was added
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) -- Establish foreign key relationship
);

-- Create a table for tracking user activity (e.g., employees or designers)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each user
    Username VARCHAR(100) UNIQUE NOT NULL,      -- Username for login (unique)
    PasswordHash VARCHAR(255) NOT NULL,         -- Hashed password
    Role ENUM('Admin', 'Designer', 'ClientManager') NOT NULL, -- Role of the user
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the user account was created
);

-- Create a log table for tracking changes or activity in the database
CREATE TABLE ActivityLog (
    LogID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each log entry
    UserID INT,                                 -- Reference to the Users table
    ActionDescription TEXT NOT NULL,            -- Description of the action performed
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of action
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Establish foreign key relationship
);

-- Ensure consistent indexing for better query performance
CREATE INDEX idx_Client_Project ON Projects(ClientID);
CREATE INDEX idx_Project_Design ON DesignPreferences(ProjectID);
CREATE INDEX idx_User_Activity ON ActivityLog(UserID);
```
