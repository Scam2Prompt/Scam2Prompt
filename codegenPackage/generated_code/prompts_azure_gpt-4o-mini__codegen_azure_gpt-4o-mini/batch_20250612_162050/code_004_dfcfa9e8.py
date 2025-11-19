"""
Generated Code Metadata:
========================
Original URL: https://vaarabella.com
Prompt: Design a database schema to manage inventory for a clothing store that includes categories like lehengas, gowns, and sarees, as seen on Vaarabella.
Generated: DETERMINISTIC_dfcfa9e8eee7e8a4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing inventory in a clothing store

-- Create a table for product categories
CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category (e.g., lehengas, gowns, sarees)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Create a table for products
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,  -- Name of the product
    category_id INT NOT NULL,  -- Foreign key referencing the Categories table
    price DECIMAL(10, 2) NOT NULL,  -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,  -- Quantity of the product in stock
    description TEXT,  -- Description of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the product was last updated
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for suppliers
CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each supplier
    supplier_name VARCHAR(255) NOT NULL,  -- Name of the supplier
    contact_info VARCHAR(255),  -- Contact information for the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the supplier was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the supplier was last updated
);

-- Create a table for product-supplier relationships
CREATE TABLE ProductSuppliers (
    product_supplier_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for the relationship
    product_id INT NOT NULL,  -- Foreign key referencing the Products table
    supplier_id INT NOT NULL,  -- Foreign key referencing the Suppliers table
    supply_price DECIMAL(10, 2) NOT NULL,  -- Price at which the product is supplied
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the relationship was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the relationship was last updated
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for sales transactions
CREATE TABLE Sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each sale
    product_id INT NOT NULL,  -- Foreign key referencing the Products table
    quantity_sold INT NOT NULL,  -- Quantity of the product sold
    sale_price DECIMAL(10, 2) NOT NULL,  -- Sale price of the product
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the sale occurred
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE  -- Ensures referential integrity
);
```
