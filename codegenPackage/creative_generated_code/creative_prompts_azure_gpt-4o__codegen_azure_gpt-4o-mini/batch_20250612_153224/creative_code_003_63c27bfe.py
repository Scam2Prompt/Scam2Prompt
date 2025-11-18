"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Create a database schema for managing timber products, including categories like softwood, hardwood, and sawn timber, as described by Askar Trading International.
Generated: DETERMINISTIC_63c27bfee277f6b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing timber products

-- Create a database for timber management
CREATE DATABASE timber_management;

-- Use the newly created database
USE timber_management;

-- Table to store timber categories
CREATE TABLE timber_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each category
    name VARCHAR(50) NOT NULL,                 -- Name of the timber category (e.g., Softwood, Hardwood)
    description TEXT,                           -- Description of the timber category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Table to store timber products
CREATE TABLE timber_products (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each timber product
    category_id INT NOT NULL,                   -- Foreign key referencing the timber category
    name VARCHAR(100) NOT NULL,                 -- Name of the timber product
    dimensions VARCHAR(50),                     -- Dimensions of the timber product (e.g., "2x4", "1x8")
    quantity INT NOT NULL,                       -- Available quantity of the timber product
    price DECIMAL(10, 2) NOT NULL,              -- Price of the timber product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for last update
    FOREIGN KEY (category_id) REFERENCES timber_categories(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store timber suppliers
CREATE TABLE timber_suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each supplier
    name VARCHAR(100) NOT NULL,                -- Name of the supplier
    contact_person VARCHAR(100),               -- Contact person at the supplier
    phone VARCHAR(15),                         -- Phone number of the supplier
    email VARCHAR(100),                        -- Email address of the supplier
    address TEXT,                              -- Address of the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the supplier was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to manage timber product purchases
CREATE TABLE timber_purchases (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each purchase
    product_id INT NOT NULL,                   -- Foreign key referencing purchased timber product
    supplier_id INT NOT NULL,                  -- Foreign key referencing supplier
    purchase_date DATE NOT NULL,               -- Date of purchase
    quantity INT NOT NULL,                     -- Quantity purchased
    total_price DECIMAL(10, 2) NOT NULL,      -- Total price for the purchase
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the purchase was recorded
    FOREIGN KEY (product_id) REFERENCES timber_products(id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (supplier_id) REFERENCES timber_suppliers(id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Ensure to handle any potential errors during execution
-- Example: Use try-catch (if applicable in your SQL environment) or check for errors post-execution
```
