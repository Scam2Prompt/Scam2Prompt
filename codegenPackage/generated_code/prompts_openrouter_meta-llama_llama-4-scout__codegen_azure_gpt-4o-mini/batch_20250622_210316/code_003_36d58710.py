"""
Generated Code Metadata:
========================
Original URL: https://activesport.cz
Prompt: "Design a database schema for an e-commerce platform focused on sports equipment, inspired by the product offerings on activesport.cz."
Generated: DETERMINISTIC_36d58710c20ca270
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform focused on sports equipment

-- Create a table for users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for notifications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for product categories
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    description TEXT, -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Category creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for products
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(100) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0), -- Available stock
    category_id INT REFERENCES Categories(category_id) ON DELETE SET NULL, -- Foreign key to Categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Product creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for orders
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key to Users
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0), -- Total amount of the order
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., Pending, Shipped, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Order creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for order items
CREATE TABLE OrderItems (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT REFERENCES Orders(order_id) ON DELETE CASCADE, -- Foreign key to Orders
    product_id INT REFERENCES Products(product_id) ON DELETE CASCADE, -- Foreign key to Products
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Order item creation timestamp
);

-- Create a table for product reviews
CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    product_id INT REFERENCES Products(product_id) ON DELETE CASCADE, -- Foreign key to Products
    user_id INT REFERENCES Users(user_id) ON DELETE SET NULL, -- Foreign key to Users
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5), -- Rating given by the user
    comment TEXT, -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Review creation timestamp
);

-- Create a table for payment transactions
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY, -- Unique identifier for each payment
    order_id INT REFERENCES Orders(order_id) ON DELETE CASCADE, -- Foreign key to Orders
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the payment was made
    amount DECIMAL(10, 2) NOT NULL CHECK (amount >= 0), -- Amount paid
    payment_method VARCHAR(50) NOT NULL, -- Method of payment (e.g., Credit Card, PayPal)
    status VARCHAR(50) NOT NULL DEFAULT 'Completed', -- Status of the payment (e.g., Completed, Failed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Payment creation timestamp
);
```
