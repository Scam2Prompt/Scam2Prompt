"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.org
Prompt: Create a database schema to store user preferences and match them with investment education firms, following Immediate Migna's tailored connection process.
Generated: DETERMINISTIC_000e06f2aa2d740a
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to store user preferences and match them with investment education firms

-- Create a table for storing user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user record was created
);

-- Create a table for storing user preferences
CREATE TABLE UserPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the preference record
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    PreferenceKey VARCHAR(100) NOT NULL,         -- Key name of the preference (e.g., "RiskTolerance", "InvestmentType")
    PreferenceValue VARCHAR(255) NOT NULL,       -- Value of the preference
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the preference record was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Maintain referential integrity
);

-- Create a table for storing investment education firms
CREATE TABLE InvestmentFirms (
    FirmID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the firm
    FirmName VARCHAR(100) NOT NULL,             -- Name of the investment education firm
    Description TEXT,                           -- Description of the firm and its services
    Location VARCHAR(100),                      -- Location of the firm
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the firm record was created
);

-- Create a table to match users with investment education firms based on preferences
CREATE TABLE UserFirmMatches (
    MatchID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the match record
    UserID INT NOT NULL,                        -- Foreign key referencing Users table
    FirmID INT NOT NULL,                        -- Foreign key referencing InvestmentFirms table
    MatchDetails TEXT,                          -- Details of how the match was made
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the match record was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID), -- Maintain referential integrity for UserID
    FOREIGN KEY (FirmID) REFERENCES InvestmentFirms(FirmID) -- Maintain referential integrity for FirmID
);

-- Create a table for logging errors and issues that may arise in the matching process
CREATE TABLE ErrorLogs (
    ErrorID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the error log
    ErrorMessage TEXT NOT NULL,                 -- Description of the error
    ErrorTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the error occurred
    UserID INT,                                 -- Optional reference to the UserID (if applicable)
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Maintain referential integrity for UserID
);
```
