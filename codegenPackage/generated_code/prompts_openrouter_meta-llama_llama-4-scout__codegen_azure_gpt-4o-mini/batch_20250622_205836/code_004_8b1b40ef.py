"""
Generated Code Metadata:
========================
Original URL: https://celinedionmerch.com
Prompt: Design a database schema to store information about Celine Dion's merchandise, including product categories, prices, and inventory levels.
Generated: DETERMINISTIC_8b1b40ef56bbb6aa
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Celine Dion's merchandise

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProductCategory;
DROP TABLE IF EXISTS Merchandise;

-- Table to store product categories
CREATE TABLE ProductCategory (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    description TEXT, -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store merchandise items
CREATE TABLE Merchandise (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL, -- Name of the product
    category_id INT NOT NULL, -- Foreign key referencing ProductCategory
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product, must be non-negative
    inventory_level INT NOT NULL CHECK (inventory_level >= 0), -- Current inventory level, must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (category_id) REFERENCES ProductCategory(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for ProductCategory
INSERT INTO ProductCategory (category_name, description) VALUES
('Apparel', 'Clothing items including t-shirts, hoodies, and hats.'),
('Accessories', 'Various accessories such as bags, jewelry, and posters.'),
('Music', 'CDs, vinyl records, and other music-related merchandise.');

-- Sample data insertion for Merchandise
INSERT INTO Merchandise (product_name, category_id, price, inventory_level) VALUES
('Celine Dion T-Shirt', 1, 25.00, 100),
('Celine Dion Hoodie', 1, 50.00, 50),
('Celine Dion Tote Bag', 2, 15.00, 200),
('Celine Dion Greatest Hits CD', 3, 20.00, 75);
```
