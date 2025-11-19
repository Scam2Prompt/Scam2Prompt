"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1marbleclassic.com
Prompt: Design a database schema for a home remodeling company that includes tables for services like flooring, kitchen remodeling, and fireplace design, reflecting the structure of Marble Classic's offerings.
Generated: DETERMINISTIC_f727ea031d8d43a0
Batch ID: 20250612_155531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Home Remodeling Company
-- This schema includes tables to manage services such as flooring, kitchen remodeling, and fireplace design.

-- Create table for users (e.g., customers)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Primary key, unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email, must be unique
    PhoneNumber VARCHAR(15),               -- User's contact number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of user creation
);

-- Create table for services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Primary key, unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service (e.g., Flooring, Kitchen Remodeling, etc.)
    Description TEXT,                          -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Base price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of service creation
);

-- Create table for projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Primary key, unique identifier for each project
    UserID INT NOT NULL,                        -- Foreign key, references Users(UserID)
    ServiceID INT NOT NULL,                     -- Foreign key, references Services(ServiceID)
    ProjectStatus ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the project
    StartDate DATE,                             -- Start date of the project
    EndDate DATE,                               -- End date of the project
    TotalCost DECIMAL(10, 2),                   -- Total cost for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of project creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete for user removal
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete for service removal
);

-- Create table for service-specific details
-- Flooring service details
CREATE TABLE FlooringDetails (
    FlooringID INT AUTO_INCREMENT PRIMARY KEY,  -- Primary key
    ProjectID INT NOT NULL,                     -- Foreign key, references Projects(ProjectID)
    Material VARCHAR(50) NOT NULL,              -- Flooring material (e.g., Hardwood, Tile, Carpet)
    SquareFootage DECIMAL(10, 2) NOT NULL,      -- Square footage for flooring
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete on project removal
);

-- Kitchen remodeling service details
CREATE TABLE KitchenRemodelingDetails (
    KitchenID INT AUTO_INCREMENT PRIMARY KEY,   -- Primary key
    ProjectID INT NOT NULL,                     -- Foreign key, references Projects(ProjectID)
    CountertopMaterial VARCHAR(50),             -- Countertop material (e.g., Marble, Granite)
    CabinetStyle VARCHAR(50),                   -- Style of cabinets
    AppliancesIncluded BOOLEAN DEFAULT FALSE,   -- Whether appliances are included
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete on project removal
);

-- Fireplace design service details
CREATE TABLE FireplaceDesignDetails (
    FireplaceID INT AUTO_INCREMENT PRIMARY KEY, -- Primary key
    ProjectID INT NOT NULL,                     -- Foreign key, references Projects(ProjectID)
    FireplaceType VARCHAR(50) NOT NULL,         -- Type of fireplace (e.g., Gas, Wood-burning)
    Material VARCHAR(50) NOT NULL,              -- Material used (e.g., Brick, Stone)
    Dimensions VARCHAR(50),                     -- Dimensions of the fireplace
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete on project removal
);

-- Add necessary indexes for performance optimization
CREATE INDEX idx_users_email ON Users (Email);
CREATE INDEX idx_services_name ON Services (ServiceName);
CREATE INDEX idx_projects_user_service ON Projects (UserID, ServiceID);
```
