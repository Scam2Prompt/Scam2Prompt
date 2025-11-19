"""
Generated Code Metadata:
========================
Original URL: https://reg-thentwr.pages.dev
Prompt: Create a database schema for managing collectible items, including categories like designer toys, trading cards, and accessories, as described on NTWRK.
Generated: DETERMINISTIC_7419cfe877b68178
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing collectible items

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CollectibleItems;
DROP TABLE IF EXISTS Categories;

-- Create a table for Categories to classify collectible items
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category, must be unique
    Description TEXT,                            -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Create a table for Collectible Items
CREATE TABLE CollectibleItems (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each collectible item
    ItemName VARCHAR(255) NOT NULL,              -- Name of the collectible item
    Description TEXT,                             -- Description of the collectible item
    CategoryID INT,                               -- Foreign key referencing Categories
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the item, must be non-negative
    Quantity INT NOT NULL CHECK (Quantity >= 0), -- Quantity available, must be non-negative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the item was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion for Categories
INSERT INTO Categories (CategoryName, Description) VALUES
('Designer Toys', 'Collectible designer toys from various artists and brands.'),
('Trading Cards', 'Collectible trading cards from various games and series.'),
('Accessories', 'Various accessories related to collectibles.');

-- Sample data insertion for Collectible Items
INSERT INTO CollectibleItems (ItemName, Description, CategoryID, Price, Quantity) VALUES
('Limited Edition Toy', 'A rare designer toy from a famous artist.', 1, 150.00, 10),
('Rare Trading Card', 'A limited edition trading card from a popular series.', 2, 50.00, 5),
('Collector’s Case', 'A protective case for storing collectible items.', 3, 25.00, 20);
```
