"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lulumalls.in
Prompt: Create a database schema for managing user accounts, including login credentials, for a website like Lulu Malls.
Generated: DETERMINISTIC_40e3afebbaadda92
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, including login credentials

-- Create a table for storing user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,          -- User's first name
    LastName VARCHAR(50) NOT NULL,           -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- User's email address (unique for each user)
    PhoneNumber VARCHAR(15),                 -- Optional phone number for the user
    DateOfBirth DATE,                        -- Optional date of birth for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last account update
);

-- Create a table for storing login credentials
CREATE TABLE UserCredentials (
    CredentialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each credential record
    UserID INT NOT NULL,                         -- Foreign key linking to Users table
    Username VARCHAR(50) NOT NULL UNIQUE,        -- Username for login (unique across the system)
    PasswordHash VARCHAR(256) NOT NULL,          -- Hashed password (never store plain-text passwords)
    PasswordSalt VARCHAR(256) NOT NULL,          -- Salt used for password hashing
    LastLogin TIMESTAMP,                         -- Timestamp of the user's last successful login
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete credentials if the user is deleted
);

-- Create a table for storing user roles and permissions
CREATE TABLE UserRoles (
    RoleID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each role
    RoleName VARCHAR(50) NOT NULL UNIQUE,       -- Name of the role (e.g., 'Admin', 'Customer')
    Description VARCHAR(255)                    -- Optional description of the role
);

-- Create a table for associating users with roles
CREATE TABLE UserRoleMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each record
    UserID INT NOT NULL,                         -- Foreign key linking to Users table
    RoleID INT NOT NULL,                         -- Foreign key linking to UserRoles table
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,    -- Cascade delete mappings if the user is deleted
    FOREIGN KEY (RoleID) REFERENCES UserRoles(RoleID) ON DELETE CASCADE -- Cascade delete mappings if the role is deleted
);

-- Indexes for improving query performance
CREATE INDEX IDX_User_Email ON Users(Email);          -- Index for fast lookup of users by email
CREATE INDEX IDX_Credentials_Username ON UserCredentials(Username); -- Index for fast lookup of credentials by username
CREATE INDEX IDX_UserRoleMapping_UserID ON UserRoleMapping(UserID); -- Index for fast lookup of role mappings by user ID

-- Ensure the database is case-insensitive for usernames and emails (optional, for MySQL)
ALTER TABLE Users MODIFY Email VARCHAR(100) COLLATE utf8_general_ci;
ALTER TABLE UserCredentials MODIFY Username VARCHAR(50) COLLATE utf8_general_ci;

-- Ensure security best practices for password storage
-- PasswordHash and PasswordSalt should be properly hashed and salted using a secure algorithm (e.g., bcrypt, Argon2).
```
