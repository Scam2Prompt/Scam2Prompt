"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harinderfarms.com
Prompt: Design a database schema for managing orders and deliveries of agricultural products like corn silage bales and potato seeds from Harinder Farms.
Generated: DETERMINISTIC_df8ccbea3241cac1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing orders and deliveries of agricultural products from Harinder Farms

-- Create a table for storing information about agricultural products
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,       -- Unique identifier for each product
    product_name VARCHAR(100) NOT NULL,  -- Name of the product (e.g., corn silage bales, potato seeds)
    product_type VARCHAR(50) NOT NULL,   -- Type of product (e.g., silage, seeds)
    price DECIMAL(10, 2) NOT NULL,       -- Price of the product
    in_stock INT NOT NULL DEFAULT 0,     -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for customers
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,           -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,         -- Customer's first name
    last_name VARCHAR(50) NOT NULL,          -- Customer's last name
    email VARCHAR(100) UNIQUE NOT NULL,      -- Customer's email address (unique)
    phone VARCHAR(15),                        -- Customer's phone number
    address TEXT NOT NULL,                    -- Customer's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for storing orders
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,              -- Unique identifier for each order
    customer_id INT NOT NULL,                 -- Reference to the customer placing the order
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL,     -- Total amount for the order
    status VARCHAR(50) DEFAULT 'Pending',      -- Order status (e.g., Pending, Completed, Cancelled)
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Foreign key constraint
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for order items (products included in each order)
CREATE TABLE OrderItems (
    order_item_id SERIAL PRIMARY KEY,          -- Unique identifier for each order item
    order_id INT NOT NULL,                     -- Reference to the associated order
    product_id INT NOT NULL,                   -- Reference to the product being ordered
    quantity INT NOT NULL,                     -- Quantity of the product ordered
    item_price DECIMAL(10, 2) NOT NULL,       -- Price of the item at the time of order
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE,  -- Foreign key constraint
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for deliveries
CREATE TABLE Deliveries (
    delivery_id SERIAL PRIMARY KEY,            -- Unique identifier for each delivery
    order_id INT NOT NULL,                     -- Reference to the order being delivered
    delivery_date TIMESTAMP,                   -- Date and time of delivery
    status VARCHAR(50) DEFAULT 'Pending',      -- Delivery status (e.g., Pending, Delivered, Cancelled)
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE, -- Foreign key constraint
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);
```
