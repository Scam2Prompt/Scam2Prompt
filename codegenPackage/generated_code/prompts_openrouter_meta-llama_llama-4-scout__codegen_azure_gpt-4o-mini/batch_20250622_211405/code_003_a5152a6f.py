"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Design a database schema for an e-commerce platform specializing in books, manga, and literary supplies, ensuring efficient storage and retrieval of product information and customer orders.
Generated: DETERMINISTIC_a5152a6fbd545af7
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform specializing in books, manga, and literary supplies

-- Create a table for storing product categories
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    description TEXT, -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for storing products
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    title VARCHAR(255) NOT NULL, -- Title of the product
    author VARCHAR(255), -- Author of the book or manga
    category_id INT REFERENCES Categories(category_id) ON DELETE SET NULL, -- Foreign key referencing Categories
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0), -- Quantity available in stock
    description TEXT, -- Description of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- Create a table for storing customer information
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL, -- Customer's first name
    last_name VARCHAR(100) NOT NULL, -- Customer's last name
    email VARCHAR(255) NOT NULL UNIQUE, -- Customer's email address
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);

-- Create a table for storing customer orders
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    customer_id INT REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Foreign key referencing Customers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0), -- Total amount for the order
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., Pending, Shipped, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the order was last updated
);

-- Create a table for storing order items
CREATE TABLE OrderItems (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT REFERENCES Orders(order_id) ON DELETE CASCADE, -- Foreign key referencing Orders
    product_id INT REFERENCES Products(product_id) ON DELETE CASCADE, -- Foreign key referencing Products
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order item was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the order item was last updated
);

-- Create a table for storing reviews
CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    product_id INT REFERENCES Products(product_id) ON DELETE CASCADE, -- Foreign key referencing Products
    customer_id INT REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Foreign key referencing Customers
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5), -- Rating given by the customer (1 to 5)
    comment TEXT, -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the review was last updated
);
```
