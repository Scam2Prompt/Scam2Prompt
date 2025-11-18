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
-- Create a database schema for storing furniture product details

CREATE DATABASE FurnitureStore;

USE FurnitureStore;

-- Table to store categories of furniture
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each category
    category_name VARCHAR(255) NOT NULL UNIQUE, -- Name of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store furniture products
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each product
    category_id INT NOT NULL, -- Foreign key referencing Categories
    product_name VARCHAR(255) NOT NULL, -- Name of the product
    dimensions VARCHAR(100) NOT NULL, -- Dimensions of the product (e.g. "80x30x40 cm")
    colors VARCHAR(255) NOT NULL, -- Available colors for the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    discount DECIMAL(5, 2) DEFAULT 0.00, -- Discount on the product (if applicable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Optional: Table to store product reviews (for future expansion)
CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each review
    product_id INT NOT NULL, -- Foreign key referencing Products
    user_name VARCHAR(255) NOT NULL, -- Name of the user who submitted the review
    rating TINYINT CHECK (rating BETWEEN 1 AND 5), -- Rating out of 5
    comments TEXT, -- User comments
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was added
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Optional: Indexes for optimized searching
CREATE INDEX idx_product_name ON Products(product_name);
CREATE INDEX idx_category_name ON Categories(category_name);
```
