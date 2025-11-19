"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Design a database schema to store information about electronic components, including categories, pricing, and inventory levels.
Generated: DETERMINISTIC_630cd2329bddb719
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about electronic components

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Components;

-- Table to store categories of electronic components
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category
    description TEXT,  -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store electronic components
CREATE TABLE Components (
    component_id SERIAL PRIMARY KEY,  -- Unique identifier for each component
    component_name VARCHAR(100) NOT NULL,  -- Name of the component
    category_id INT NOT NULL,  -- Foreign key referencing Categories
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the component, must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the component was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store inventory levels for components
CREATE TABLE Inventory (
    inventory_id SERIAL PRIMARY KEY,  -- Unique identifier for each inventory record
    component_id INT NOT NULL,  -- Foreign key referencing Components
    quantity INT NOT NULL CHECK (quantity >= 0),  -- Quantity in stock, must be non-negative
    restock_date TIMESTAMP,  -- Optional date for when the component is expected to be restocked
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the inventory record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (component_id) REFERENCES Components(component_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_component_name ON Components(component_name);
CREATE INDEX idx_category_name ON Categories(category_name);
CREATE INDEX idx_component_id ON Inventory(component_id);
```
