"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Design a database schema for a web application using MySQL on a Megh iTech Linux web hosting plan.
Generated: DETERMINISTIC_fb7d47c7916d67a3
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a web application using MySQL

-- Create a database for the web application
CREATE DATABASE IF NOT EXISTS WebAppDB;

-- Use the created database
USE WebAppDB;

-- Table for storing user information
CREATE TABLE IF NOT EXISTS Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username must be unique
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email must be unique
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing user roles (e.g., admin, user, etc.)
CREATE TABLE IF NOT EXISTS Roles (
    RoleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each role
    RoleName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the role
    Description TEXT                       -- Description of the role
);

-- Table for associating users with roles (many-to-many relationship)
CREATE TABLE IF NOT EXISTS UserRoles (
    UserRoleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user-role association
    UserID INT NOT NULL,                       -- Foreign key to Users table
    RoleID INT NOT NULL,                       -- Foreign key to Roles table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the role was assigned
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID) ON DELETE CASCADE  -- Cascade delete if role is deleted
);

-- Table for storing application settings
CREATE TABLE IF NOT EXISTS Settings (
    SettingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each setting
    SettingKey VARCHAR(100) NOT NULL UNIQUE,  -- Key for the setting
    SettingValue TEXT NOT NULL,               -- Value of the setting
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for logging application events
CREATE TABLE IF NOT EXISTS Logs (
    LogID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    LogLevel ENUM('INFO', 'WARNING', 'ERROR') NOT NULL, -- Severity level of the log
    Message TEXT NOT NULL,                 -- Log message
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the log was created
);

-- Table for storing user sessions
CREATE TABLE IF NOT EXISTS Sessions (
    SessionID VARCHAR(255) PRIMARY KEY,   -- Unique identifier for the session
    UserID INT NOT NULL,                  -- Foreign key to Users table
    ExpiresAt TIMESTAMP NOT NULL,         -- Expiration timestamp for the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the session was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table for storing user activity logs
CREATE TABLE IF NOT EXISTS UserActivity (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity
    UserID INT NOT NULL,                       -- Foreign key to Users table
    ActivityType VARCHAR(100) NOT NULL,        -- Type of activity (e.g., login, logout, etc.)
    ActivityDetails TEXT,                      -- Additional details about the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the activity occurred
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table for storing content (e.g., blog posts, articles, etc.)
CREATE TABLE IF NOT EXISTS Content (
    ContentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each content item
    Title VARCHAR(255) NOT NULL,              -- Title of the content
    Body TEXT NOT NULL,                       -- Body of the content
    AuthorID INT NOT NULL,                    -- Foreign key to Users table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the content was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID) ON DELETE SET NULL -- Set author to NULL if user is deleted
);

-- Table for storing comments on content
CREATE TABLE IF NOT EXISTS Comments (
    CommentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comment
    ContentID INT NOT NULL,                   -- Foreign key to Content table
    UserID INT NOT NULL,                      -- Foreign key to Users table
    CommentText TEXT NOT NULL,                -- Text of the comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the comment was created
    FOREIGN KEY (ContentID) REFERENCES Content(ContentID) ON DELETE CASCADE, -- Cascade delete if content is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table for storing tags for content
CREATE TABLE IF NOT EXISTS Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    TagName VARCHAR(50) NOT NULL UNIQUE   -- Name of the tag
);

-- Table for associating tags with content (many-to-many relationship)
CREATE TABLE IF NOT EXISTS ContentTags (
    ContentTagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each content-tag association
    ContentID INT NOT NULL,                      -- Foreign key to Content table
    TagID INT NOT NULL,                          -- Foreign key to Tags table
    FOREIGN KEY (ContentID) REFERENCES Content(ContentID) ON DELETE CASCADE, -- Cascade delete if content is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Cascade delete if tag is deleted
);
```
