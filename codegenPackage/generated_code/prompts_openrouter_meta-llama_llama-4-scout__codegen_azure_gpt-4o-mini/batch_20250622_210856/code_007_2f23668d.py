"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: "Design a database schema for an e-commerce platform selling gardening tools, machinery, and household items."
Generated: DETERMINISTIC_2f23668d8348faa0
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform selling gardening tools, machinery, and household items

-- Create a table for users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for notifications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for product categories
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    description TEXT, -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of category creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for products
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    category_id INT NOT NULL, -- Foreign key referencing Categories
    product_name VARCHAR(100) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0), -- Available stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for orders
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    user_id INT NOT NULL, -- Foreign key referencing Users
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order placement
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0), -- Total amount of the order
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for order items
CREATE TABLE OrderItems (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL, -- Foreign key referencing Orders
    product_id INT NOT NULL, -- Foreign key referencing Products
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for product reviews
CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    product_id INT NOT NULL, -- Foreign key referencing Products
    user_id INT NOT NULL, -- Foreign key referencing Users
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5), -- Rating given by the user
    comment TEXT, -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of review creation
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
