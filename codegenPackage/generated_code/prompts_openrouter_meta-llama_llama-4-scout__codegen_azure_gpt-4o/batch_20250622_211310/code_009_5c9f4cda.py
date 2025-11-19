"""
Generated Code Metadata:
========================
Original URL: https://immediate-xzen.com
Prompt: Design a database schema using SQL that stores user information, educational resources, and investment education firm data for Immediate ZenX, ensuring data security and scalability.
Generated: DETERMINISTIC_5c9f4cda48787e0d
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Immediate ZenX

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store educational resources
CREATE TABLE EducationalResources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resource
    Title VARCHAR(255) NOT NULL,               -- Title of the resource
    Description TEXT,                          -- Description of the resource
    URL VARCHAR(2083) NOT NULL,                -- URL to access the resource
    ResourceType ENUM('Article', 'Video', 'E-Book', 'Webinar') NOT NULL, -- Type of resource
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of resource creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store investment education firm data
CREATE TABLE InvestmentFirms (
    FirmID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each firm
    FirmName VARCHAR(100) NOT NULL,        -- Name of the firm
    WebsiteURL VARCHAR(2083),              -- Website URL of the firm
    ContactEmail VARCHAR(100),             -- Contact email for the firm
    PhoneNumber VARCHAR(15),               -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of firm record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to track which users have accessed which resources
CREATE TABLE UserResourceAccess (
    AccessID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each access record
    UserID INT NOT NULL,                     -- Foreign key to Users table
    ResourceID INT NOT NULL,                 -- Foreign key to EducationalResources table
    AccessedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of access
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (ResourceID) REFERENCES EducationalResources(ResourceID) ON DELETE CASCADE -- Cascade delete if resource is deleted
);

-- Create a table to track which firms provide which resources
CREATE TABLE FirmResources (
    FirmResourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each firm-resource relationship
    FirmID INT NOT NULL,                           -- Foreign key to InvestmentFirms table
    ResourceID INT NOT NULL,                       -- Foreign key to EducationalResources table
    FOREIGN KEY (FirmID) REFERENCES InvestmentFirms(FirmID) ON DELETE CASCADE, -- Cascade delete if firm is deleted
    FOREIGN KEY (ResourceID) REFERENCES EducationalResources(ResourceID) ON DELETE CASCADE -- Cascade delete if resource is deleted
);

-- Add an index to optimize queries on frequently searched columns
CREATE INDEX idx_users_email ON Users (Email);
CREATE INDEX idx_resources_type ON EducationalResources (ResourceType);
CREATE INDEX idx_firms_name ON InvestmentFirms (FirmName);
```
