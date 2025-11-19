"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: "Design a database schema to store information about construction tools and equipment for an e-commerce platform."
Generated: DETERMINISTIC_9bfab1ee5a03d2c6
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about construction tools and equipment

CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(100) NOT NULL,      -- Name of the category
    description TEXT,                 -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE Tools (
    tool_id SERIAL PRIMARY KEY,       -- Unique identifier for each tool
    name VARCHAR(100) NOT NULL,       -- Name of the tool
    description TEXT,                 -- Description of the tool
    price DECIMAL(10, 2) NOT NULL,    -- Price of the tool
    stock_quantity INT NOT NULL,      -- Quantity available in stock
    category_id INT,                  -- Foreign key referencing Categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL -- Handle category deletion
);

CREATE TABLE Suppliers (
    supplier_id SERIAL PRIMARY KEY,    -- Unique identifier for each supplier
    name VARCHAR(100) NOT NULL,         -- Name of the supplier
    contact_email VARCHAR(100),         -- Contact email of the supplier
    phone_number VARCHAR(15),           -- Phone number of the supplier
    address TEXT,                       -- Address of the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE Tool_Supplier (
    tool_id INT,                        -- Foreign key referencing Tools
    supplier_id INT,                    -- Foreign key referencing Suppliers
    PRIMARY KEY (tool_id, supplier_id), -- Composite primary key
    FOREIGN KEY (tool_id) REFERENCES Tools(tool_id) ON DELETE CASCADE, -- Handle tool deletion
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id) ON DELETE CASCADE -- Handle supplier deletion
);

CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,        -- Unique identifier for each order
    customer_id INT NOT NULL,           -- ID of the customer placing the order
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    status VARCHAR(50) NOT NULL,        -- Status of the order (e.g., pending, completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE Order_Items (
    order_item_id SERIAL PRIMARY KEY,   -- Unique identifier for each order item
    order_id INT NOT NULL,               -- Foreign key referencing Orders
    tool_id INT NOT NULL,                -- Foreign key referencing Tools
    quantity INT NOT NULL,               -- Quantity of the tool ordered
    price DECIMAL(10, 2) NOT NULL,       -- Price of the tool at the time of order
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE, -- Handle order deletion
    FOREIGN KEY (tool_id) REFERENCES Tools(tool_id) ON DELETE CASCADE -- Handle tool deletion
);
```
