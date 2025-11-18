"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Provide an example of a database schema for managing product categories (e.g., residential systems, commercial systems, accessories) and promotions, as seen on Frigoterm.ro.
Generated: DETERMINISTIC_8f5e41b2e40e0af8
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing product categories and promotions

-- Table for storing product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                 -- Name of the category
    Description TEXT,                           -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing promotions
CREATE TABLE Promotions (
    PromotionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each promotion
    Title VARCHAR(255) NOT NULL,                -- Title of the promotion
    Description TEXT,                           -- Optional description of the promotion
    DiscountPercentage DECIMAL(5, 2),           -- Discount percentage (e.g., 10.00 for 10%)
    StartDate DATE NOT NULL,                    -- Start date of the promotion
    EndDate DATE NOT NULL,                      -- End date of the promotion
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the promotion was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for mapping promotions to product categories (many-to-many relationship)
CREATE TABLE CategoryPromotions (
    CategoryPromotionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    CategoryID INT NOT NULL,                            -- Foreign key referencing ProductCategories
    PromotionID INT NOT NULL,                           -- Foreign key referencing Promotions
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (PromotionID) REFERENCES Promotions(PromotionID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_category_name ON ProductCategories(Name);
CREATE INDEX idx_promotion_title ON Promotions(Title);

-- Sample constraints and validations
ALTER TABLE Promotions
ADD CONSTRAINT chk_discount_percentage CHECK (DiscountPercentage >= 0 AND DiscountPercentage <= 100);

-- End of schema
```
