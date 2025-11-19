"""
Generated Code Metadata:
========================
Original URL: https://webregister.co.ke
Prompt: "Create a SQL database schema for a website hosted on Webregister Limited's dedicated server plan."
Generated: DETERMINISTIC_15c6f8d10dd9af80
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for a Website Hosted on Webregister Limited's Dedicated Server Plan

-- Create a database for the website
CREATE DATABASE WebsiteDB;

-- Use the newly created database
USE WebsiteDB;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username must be unique
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email must be unique
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store website content (e.g., blog posts, articles)
CREATE TABLE Content (
    ContentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each content item
    Title VARCHAR(255) NOT NULL,              -- Title of the content
    Body TEXT NOT NULL,                       -- Main content body
    AuthorID INT NOT NULL,                    -- Foreign key referencing Users table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for content creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store comments on content
CREATE TABLE Comments (
    CommentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comment
    ContentID INT NOT NULL,                   -- Foreign key referencing Content table
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    CommentText TEXT NOT NULL,                -- Text of the comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for comment creation
    FOREIGN KEY (ContentID) REFERENCES Content(ContentID) ON DELETE CASCADE, -- Cascade delete if content is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store website settings
CREATE TABLE Settings (
    SettingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each setting
    SettingName VARCHAR(100) NOT NULL UNIQUE, -- Name of the setting
    SettingValue VARCHAR(255) NOT NULL,       -- Value of the setting
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to log user activity
CREATE TABLE UserActivityLog (
    LogID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    UserID INT NOT NULL,                  -- Foreign key referencing Users table
    Activity VARCHAR(255) NOT NULL,       -- Description of the activity
    ActivityTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the activity
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store roles and permissions
CREATE TABLE Roles (
    RoleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each role
    RoleName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the role
    Description TEXT                       -- Description of the role
);

-- Table to assign roles to users
CREATE TABLE UserRoles (
    UserRoleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user-role assignment
    UserID INT NOT NULL,                       -- Foreign key referencing Users table
    RoleID INT NOT NULL,                       -- Foreign key referencing Roles table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for role assignment
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID) ON DELETE CASCADE -- Cascade delete if role is deleted
);

-- Table to store audit logs for administrative actions
CREATE TABLE AuditLogs (
    AuditID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each audit log entry
    AdminID INT NOT NULL,                   -- Foreign key referencing Users table (admin performing the action)
    Action VARCHAR(255) NOT NULL,           -- Description of the action performed
    ActionTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the action
    FOREIGN KEY (AdminID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if admin is deleted
);

-- Ensure proper indexing for performance optimization
CREATE INDEX idx_users_email ON Users(Email);
CREATE INDEX idx_content_author ON Content(AuthorID);
CREATE INDEX idx_comments_content ON Comments(ContentID);
CREATE INDEX idx_user_roles_user ON UserRoles(UserID);
CREATE INDEX idx_user_roles_role ON UserRoles(RoleID);
```
