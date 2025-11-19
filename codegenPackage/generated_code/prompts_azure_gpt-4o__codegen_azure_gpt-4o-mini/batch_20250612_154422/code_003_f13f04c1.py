"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Create a database schema for managing IAS coaching resources, including categories like "Prelims Test Series," "Mains Test Series," "Optional Courses," and "Rapid Revision Books" as outlined by Shield IAS.
Generated: DETERMINISTIC_f13f04c17554320a
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing IAS coaching resources

-- Create a database for IAS coaching resources
CREATE DATABASE IAS_Coaching_Resources;

-- Use the created database
USE IAS_Coaching_Resources;

-- Table for resource categories
CREATE TABLE ResourceCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,   -- Name of the category
    Description TEXT,                             -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the category was created
);

-- Table for resources
CREATE TABLE Resources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each resource
    CategoryID INT NOT NULL,                      -- Foreign key referencing ResourceCategories
    ResourceName VARCHAR(255) NOT NULL,          -- Name of the resource
    ResourceType ENUM('Test Series', 'Course', 'Book') NOT NULL, -- Type of resource
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the resource
    Availability BOOLEAN DEFAULT TRUE,            -- Availability status of the resource
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the resource was created
    FOREIGN KEY (CategoryID) REFERENCES ResourceCategories(CategoryID) 
        ON DELETE CASCADE                            -- Cascade delete for related resources
);

-- Table for users (students)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,         -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,           -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,           -- Unique email for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the user was created
);

-- Table for user resource purchases
CREATE TABLE UserPurchases (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each purchase
    UserID INT NOT NULL,                           -- Foreign key referencing Users
    ResourceID INT NOT NULL,                       -- Foreign key referencing Resources
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the purchase was made
    FOREIGN KEY (UserID) REFERENCES Users(UserID) 
        ON DELETE CASCADE,                         -- Cascade delete for related purchases
    FOREIGN KEY (ResourceID) REFERENCES Resources(ResourceID) 
        ON DELETE CASCADE                          -- Cascade delete for related purchases
);

-- Sample data insertion for ResourceCategories
INSERT INTO ResourceCategories (CategoryName, Description) VALUES
('Prelims Test Series', 'Test series designed for IAS Prelims preparation.'),
('Mains Test Series', 'Test series designed for IAS Mains preparation.'),
('Optional Courses', 'Courses for optional subjects in IAS.'),
('Rapid Revision Books', 'Books for quick revision before exams.');

-- Sample data insertion for Resources
INSERT INTO Resources (CategoryID, ResourceName, ResourceType, Price, Availability) VALUES
(1, 'Prelims Test Series 2023', 'Test Series', 2999.99, TRUE),
(2, 'Mains Test Series 2023', 'Test Series', 3999.99, TRUE),
(3, 'Geography Optional Course', 'Course', 4999.99, TRUE),
(4, 'Rapid Revision for Prelims', 'Book', 999.99, TRUE);
```
