"""
Generated Code Metadata:
========================
Original URL: https://kocaeli.com
Prompt: Provide recommendations for a database schema to store information about Kocaeli.COM's categories, such as "Gezilecek Yerler," "Yemek Yerleri," and "Oto Galerileri," and write SQL code to create the database.
Generated: DETERMINISTIC_2b96e5f7cff65fda
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Kocaeli.COM
CREATE DATABASE KocaeliDB;

-- Use the newly created database
USE KocaeliDB;

-- Create a table to store categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Gezilecek Yerler")
    Description TEXT,                           -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table to store items within each category
CREATE TABLE Items (
    ItemID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each item
    CategoryID INT NOT NULL,                    -- Foreign key referencing Categories
    ItemName VARCHAR(255) NOT NULL,             -- Name of the item (e.g., specific place or restaurant)
    Address VARCHAR(255),                        -- Address of the item
    PhoneNumber VARCHAR(20),                     -- Contact number for the item
    Website VARCHAR(255),                        -- Website link for the item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the item was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store user reviews for items
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each review
    ItemID INT NOT NULL,                         -- Foreign key referencing Items
    UserName VARCHAR(100) NOT NULL,             -- Name of the user who wrote the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the user (1 to 5)
    Comment TEXT,                                -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store tags for items
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each tag
    TagName VARCHAR(100) NOT NULL UNIQUE,       -- Name of the tag
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the tag was created
);

-- Create a junction table to associate items with tags (many-to-many relationship)
CREATE TABLE ItemTags (
    ItemID INT NOT NULL,                         -- Foreign key referencing Items
    TagID INT NOT NULL,                          -- Foreign key referencing Tags
    PRIMARY KEY (ItemID, TagID),                -- Composite primary key
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Ensures referential integrity
);
```
