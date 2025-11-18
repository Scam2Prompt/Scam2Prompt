"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Design a database schema in SQL for storing Marant's skincare product details, including categories like exfoliants, peels, active ingredients, and target skin conditions.
Generated: DETERMINISTIC_018094593b7b0d64
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for Marant's skincare product details
CREATE DATABASE MarantSkincare;

-- Use the created database
USE MarantSkincare;

-- Table for storing skincare product categories
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Table for storing active ingredients
CREATE TABLE ActiveIngredients (
    ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    ingredient_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Table for storing target skin conditions
CREATE TABLE SkinConditions (
    condition_id INT AUTO_INCREMENT PRIMARY KEY,
    condition_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Table for storing skincare products
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL
);

-- Table for linking products to active ingredients (many-to-many relationship)
CREATE TABLE ProductIngredients (
    product_id INT,
    ingredient_id INT,
    PRIMARY KEY (product_id, ingredient_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ActiveIngredients(ingredient_id) ON DELETE CASCADE
);

-- Table for linking products to target skin conditions (many-to-many relationship)
CREATE TABLE ProductConditions (
    product_id INT,
    condition_id INT,
    PRIMARY KEY (product_id, condition_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (condition_id) REFERENCES SkinConditions(condition_id) ON DELETE CASCADE
);

-- Indexes for improving query performance
CREATE INDEX idx_product_name ON Products(product_name);
CREATE INDEX idx_condition_name ON SkinConditions(condition_name);
CREATE INDEX idx_ingredient_name ON ActiveIngredients(ingredient_name);
```
