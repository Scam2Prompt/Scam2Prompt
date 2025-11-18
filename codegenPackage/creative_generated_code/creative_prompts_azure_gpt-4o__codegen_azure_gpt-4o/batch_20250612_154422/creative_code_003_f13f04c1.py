"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Create a database schema for managing IAS coaching resources, including categories like "Prelims Test Series," "Mains Test Series," "Optional Courses," and "Rapid Revision Books" as outlined by Shield IAS.
Generated: DETERMINISTIC_f13f04c17554320a
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- IAS Coaching Resources Database Schema for Shield IAS

-- Create a table to manage resource categories
CREATE TABLE ResourceCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Prelims Test Series", "Mains Test Series")
    Description TEXT DEFAULT NULL,             -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store individual resources
CREATE TABLE Resources (
    ResourceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each resource
    ResourceName VARCHAR(255) NOT NULL,        -- Name of the resource
    CategoryID INT NOT NULL,                   -- Foreign key pointing to ResourceCategories
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the resource
    AvailabilityStatus ENUM('Available', 'Out of Stock') DEFAULT 'Available', -- Availability of the resource
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the resource was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ResourceCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to handle user purchases (if needed for managing purchases)
CREATE TABLE Purchases (
    PurchaseID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each purchase
    UserID INT NOT NULL,                       -- Identifier for the user making the purchase
    ResourceID INT NOT NULL,                   -- Foreign key pointing to Resources
    Quantity INT DEFAULT 1,                    -- Number of resources purchased
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price calculated based on quantity and resource price
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the purchase was made
    FOREIGN KEY (ResourceID) REFERENCES Resources(ResourceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for managing users (optional, but useful for tracking purchases)
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,            -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,        -- Hashed password for securing user accounts
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user account was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Example indexes for optimization
CREATE INDEX idx_category_name ON ResourceCategories (CategoryName); -- Index on category name for faster search
CREATE INDEX idx_resource_name ON Resources (ResourceName);         -- Index on resource name for faster search
CREATE INDEX idx_user_email ON Users (Email);                       -- Index on user email for faster lookup
```
