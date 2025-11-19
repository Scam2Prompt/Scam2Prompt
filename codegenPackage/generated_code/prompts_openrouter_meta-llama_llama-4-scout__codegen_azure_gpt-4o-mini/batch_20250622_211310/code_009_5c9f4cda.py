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
-- Database schema for Immediate ZenX

-- Create a database for Immediate ZenX
CREATE DATABASE ImmediateZenX;

-- Use the created database
USE ImmediateZenX;

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for each user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store educational resources
CREATE TABLE EducationalResources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resource
    Title VARCHAR(255) NOT NULL, -- Title of the educational resource
    Description TEXT, -- Description of the resource
    ResourceType ENUM('Article', 'Video', 'Course', 'Webinar') NOT NULL, -- Type of resource
    URL VARCHAR(255) NOT NULL, -- URL to access the resource
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of resource creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store investment education firm data
CREATE TABLE InvestmentFirms (
    FirmID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each firm
    FirmName VARCHAR(255) NOT NULL UNIQUE, -- Unique name of the investment firm
    ContactEmail VARCHAR(100) NOT NULL, -- Contact email for the firm
    PhoneNumber VARCHAR(15), -- Phone number for the firm
    Website VARCHAR(255), -- Website URL for the firm
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of firm creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to link users with educational resources (many-to-many relationship)
CREATE TABLE UserResources (
    UserID INT NOT NULL, -- Foreign key referencing Users
    ResourceID INT NOT NULL, -- Foreign key referencing EducationalResources
    PRIMARY KEY (UserID, ResourceID), -- Composite primary key
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ResourceID) REFERENCES EducationalResources(ResourceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to link users with investment firms (many-to-many relationship)
CREATE TABLE UserFirms (
    UserID INT NOT NULL, -- Foreign key referencing Users
    FirmID INT NOT NULL, -- Foreign key referencing InvestmentFirms
    PRIMARY KEY (UserID, FirmID), -- Composite primary key
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (FirmID) REFERENCES InvestmentFirms(FirmID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(Username);
CREATE INDEX idx_email ON Users(Email);
CREATE INDEX idx_resource_type ON EducationalResources(ResourceType);
CREATE INDEX idx_firm_name ON InvestmentFirms(FirmName);
```
