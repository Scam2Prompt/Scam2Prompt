"""
Generated Code Metadata:
========================
Original URL: https://immediate-affinity.com
Prompt: Design a database schema for storing user information, investment education resources, and firm details for a platform like Switch ePrex 0.3.
Generated: DETERMINISTIC_05ba4fb111003df6
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user information, investment education resources, and firm details

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store investment education resources
CREATE TABLE InvestmentResources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resource
    Title VARCHAR(100) NOT NULL,               -- Title of the resource
    Description TEXT,                          -- Detailed description of the resource
    URL VARCHAR(255) NOT NULL,                 -- Link to the resource
    Category VARCHAR(50),                      -- Category of the resource (e.g., stocks, bonds, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the resource was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store firm details
CREATE TABLE Firms (
    FirmID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each firm
    Name VARCHAR(100) NOT NULL,            -- Name of the firm
    Website VARCHAR(255),                  -- Firm's website URL
    ContactEmail VARCHAR(100),             -- Contact email for the firm
    PhoneNumber VARCHAR(20),               -- Contact phone number for the firm
    Address TEXT,                          -- Physical address of the firm
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the firm was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to track user interactions with investment resources
CREATE TABLE UserResourceInteractions (
    InteractionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each interaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    ResourceID INT NOT NULL,                      -- Foreign key referencing InvestmentResources table
    InteractionType ENUM('viewed', 'liked', 'shared') NOT NULL, -- Type of interaction
    InteractionTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of the interaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (ResourceID) REFERENCES InvestmentResources(ResourceID) ON DELETE CASCADE -- Cascade delete if resource is removed
);

-- Table to track user-firm relationships (e.g., users following firms)
CREATE TABLE UserFirmRelationships (
    RelationshipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each relationship
    UserID INT NOT NULL,                           -- Foreign key referencing Users table
    FirmID INT NOT NULL,                           -- Foreign key referencing Firms table
    RelationshipType ENUM('following', 'client') NOT NULL, -- Type of relationship
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the relationship was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (FirmID) REFERENCES Firms(FirmID) ON DELETE CASCADE -- Cascade delete if firm is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_users_email ON Users(Email); -- Index for quick lookup by email
CREATE INDEX idx_resources_category ON InvestmentResources(Category); -- Index for filtering by category
CREATE INDEX idx_firms_name ON Firms(Name); -- Index for quick lookup by firm name
```
