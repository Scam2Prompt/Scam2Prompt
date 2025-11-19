"""
Generated Code Metadata:
========================
Original URL: https://bonaeac.com
Prompt: Design a database schema to store user information, membership levels, and earning percentages for a platform like bonaeac.com.
Generated: DETERMINISTIC_8edb7ed45a307af9
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user information, membership levels, and earning percentages

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store membership levels
CREATE TABLE MembershipLevels (
    MembershipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each membership level
    LevelName VARCHAR(50) NOT NULL UNIQUE,       -- Name of the membership level (e.g., Bronze, Silver, Gold)
    EarningPercentage DECIMAL(5, 2) NOT NULL,    -- Earning percentage associated with the membership level
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the membership level was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to associate users with membership levels
CREATE TABLE UserMemberships (
    UserMembershipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user-membership association
    UserID INT NOT NULL,                             -- Foreign key referencing Users table
    MembershipID INT NOT NULL,                       -- Foreign key referencing MembershipLevels table
    StartDate DATE NOT NULL,                         -- Date when the membership started
    EndDate DATE DEFAULT NULL,                       -- Date when the membership ends (NULL if active)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the association was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (MembershipID) REFERENCES MembershipLevels(MembershipID) ON DELETE CASCADE -- Cascade delete if membership level is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_users_email ON Users (Email); -- Index for quick lookup by email
CREATE INDEX idx_user_memberships_userid ON UserMemberships (UserID); -- Index for quick lookup by user ID
CREATE INDEX idx_user_memberships_membershipid ON UserMemberships (MembershipID); -- Index for quick lookup by membership ID
```
