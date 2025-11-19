"""
Generated Code Metadata:
========================
Original URL: https://immediate-lforce.com
Prompt: Create a SQL database schema for storing information about investment educational firms, users, and resources, and write a query to retrieve relevant data for a specific user.
Generated: DETERMINISTIC_dd36a2f6218db9e2
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Investment Educational Firms

-- Create a table to store information about educational firms
CREATE TABLE EducationalFirms (
    FirmID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each firm
    FirmName VARCHAR(255) NOT NULL,         -- Name of the educational firm
    WebsiteURL VARCHAR(255),                 -- Website URL of the firm
    EstablishedYear INT,                     -- Year the firm was established
    Description TEXT                         -- Description of the firm
);

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of user creation
);

-- Create a table to store resources related to investment education
CREATE TABLE Resources (
    ResourceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each resource
    Title VARCHAR(255) NOT NULL,               -- Title of the resource
    ResourceType ENUM('Article', 'Video', 'Course') NOT NULL, -- Type of resource
    URL VARCHAR(255),                           -- URL to access the resource
    FirmID INT,                                 -- Foreign key referencing EducationalFirms
    FOREIGN KEY (FirmID) REFERENCES EducationalFirms(FirmID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store user-resource interactions (e.g., saved resources)
CREATE TABLE UserResources (
    UserResourceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the user-resource relationship
    UserID INT,                                    -- Foreign key referencing Users
    ResourceID INT,                                -- Foreign key referencing Resources
    SavedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the resource was saved
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ResourceID) REFERENCES Resources(ResourceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Query to retrieve relevant data for a specific user
-- This query retrieves the user's information along with the resources they have saved
SELECT 
    u.UserID,
    u.Username,
    u.Email,
    r.ResourceID,
    r.Title,
    r.ResourceType,
    r.URL,
    ef.FirmName
FROM 
    Users u
LEFT JOIN 
    UserResources ur ON u.UserID = ur.UserID
LEFT JOIN 
    Resources r ON ur.ResourceID = r.ResourceID
LEFT JOIN 
    EducationalFirms ef ON r.FirmID = ef.FirmID
WHERE 
    u.UserID = ?;  -- Replace '?' with the specific UserID you want to query
```
