"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Provide an example of a database schema for managing product categories (e.g., residential systems, commercial systems, accessories) and promotions, as seen on Frigoterm.ro.
Generated: DETERMINISTIC_8f5e41b2e40e0af8
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing product categories and promotions

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Promotions;
DROP TABLE IF EXISTS ProductCategories;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the category (e.g., Residential Systems)
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store promotions
CREATE TABLE Promotions (
    PromotionID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each promotion
    PromotionName VARCHAR(255) NOT NULL,        -- Name of the promotion
    DiscountPercentage DECIMAL(5, 2) NOT NULL,  -- Discount percentage for the promotion
    StartDate DATE NOT NULL,                     -- Start date of the promotion
    EndDate DATE NOT NULL,                       -- End date of the promotion
    CategoryID INT,                              -- Foreign key referencing ProductCategories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the promotion was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the promotion was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Establishing foreign key relationship
);

-- Sample data insertion for ProductCategories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Residential Systems', 'Systems designed for residential use.'),
('Commercial Systems', 'Systems designed for commercial use.'),
('Accessories', 'Additional accessories for systems.');

-- Sample data insertion for Promotions
INSERT INTO Promotions (PromotionName, DiscountPercentage, StartDate, EndDate, CategoryID) VALUES
('Winter Sale', 15.00, '2023-12-01', '2023-12-31', 1),  -- Promotion for Residential Systems
('Summer Clearance', 20.00, '2023-06-01', '2023-06-30', 2), -- Promotion for Commercial Systems
('Accessory Discount', 10.00, '2023-11-01', '2023-11-30', 3); -- Promotion for Accessories
```
