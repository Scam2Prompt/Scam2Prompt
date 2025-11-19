"""
Generated Code Metadata:
========================
Original URL: https://immediatecode-360.com
Prompt: Design a basic database schema to store user information and investment education resources, similar to those offered by Immediate Code 360, and provide a sample query to retrieve relevant data.
Generated: DETERMINISTIC_949ce905954b3071
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user information and investment education resources

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store investment education resources
CREATE TABLE Resources (
    ResourceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each resource
    Title VARCHAR(100) NOT NULL,                -- Title of the resource
    Description TEXT,                            -- Description of the resource
    URL VARCHAR(255) NOT NULL,                  -- URL link to the resource
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the resource was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to link users to resources they are interested in
CREATE TABLE UserResources (
    UserResourceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for the user-resource link
    UserID INT NOT NULL,                             -- Foreign key referencing Users
    ResourceID INT NOT NULL,                         -- Foreign key referencing Resources
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (ResourceID) REFERENCES Resources(ResourceID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample query to retrieve user information along with their interested resources
SELECT 
    u.UserID,
    u.Username,
    u.Email,
    r.ResourceID,
    r.Title,
    r.Description,
    r.URL
FROM 
    Users u
LEFT JOIN 
    UserResources ur ON u.UserID = ur.UserID
LEFT JOIN 
    Resources r ON ur.ResourceID = r.ResourceID
WHERE 
    u.UserID = ?;  -- Replace ? with the specific UserID to retrieve data for that user
```
