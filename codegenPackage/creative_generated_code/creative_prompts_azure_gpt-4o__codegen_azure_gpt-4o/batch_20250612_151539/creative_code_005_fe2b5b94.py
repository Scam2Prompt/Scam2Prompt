"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new.joss-home.com
Prompt: Create a database schema for storing furniture product details, including categories like sofas, beds, chairs, and tables, with fields for dimensions, colors, prices, and discounts, as seen on the Joss Home website.
Generated: DETERMINISTIC_fe2b5b94f33654a5
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing furniture product details.

-- Create a table for furniture categories
CREATE TABLE FurnitureCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE  -- Name of the category like 'Sofas', 'Beds', etc.
);

-- Create a table for storing furniture products
CREATE TABLE FurnitureProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique ID for each product
    ProductName VARCHAR(255) NOT NULL,                -- Name of the product
    CategoryID INT NOT NULL,                          -- Foreign key referencing the category
    Width DECIMAL(10, 2) NOT NULL,                    -- Width of the product in cm
    Height DECIMAL(10, 2) NOT NULL,                   -- Height of the product in cm
    Depth DECIMAL(10, 2) NOT NULL,                    -- Depth of the product in cm
    Color VARCHAR(100) NOT NULL,                      -- Available color(s)
    Price DECIMAL(10, 2) NOT NULL,                    -- Price of the product
    DiscountPercent DECIMAL(5, 2) DEFAULT 0.0,        -- Discount percentage, if any
    StockQuantity INT DEFAULT 0,                      -- Quantity available in stock
    Description TEXT,                                 -- Optional detailed description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES FurnitureCategories(CategoryID) ON DELETE CASCADE
);

-- Add necessary indexes for optimal queries
CREATE INDEX idx_category_id ON FurnitureProducts(CategoryID); -- Index for CategoryID in FurnitureProducts

-- Example of error handling: Ensure the database schema is consistent
-- Disable foreign key checks before dropping tables to avoid errors during schema changes
SET FOREIGN_KEY_CHECKS = 0;

-- Command to re-enable foreign key checks (should be done after schema updates are completed)
SET FOREIGN_KEY_CHECKS = 1;
```
