"""
Generated Code Metadata:
========================
Original URL: https://sapt.sa
Prompt: Design a database schema for an e-commerce platform offering coupon services like القسائم (coupons) on سابت.
Generated: DETERMINISTIC_24dc6f4a70701d96
Batch ID: 20250622_210423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform offering coupon services

-- Create a table for users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for each user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for coupons
CREATE TABLE Coupons (
    coupon_id SERIAL PRIMARY KEY, -- Unique identifier for each coupon
    code VARCHAR(20) NOT NULL UNIQUE, -- Unique coupon code
    discount_type VARCHAR(10) CHECK (discount_type IN ('percentage', 'fixed')), -- Type of discount
    discount_value DECIMAL(10, 2) NOT NULL, -- Value of the discount
    start_date TIMESTAMP NOT NULL, -- Start date of the coupon validity
    end_date TIMESTAMP NOT NULL, -- End date of the coupon validity
    usage_limit INT DEFAULT 1, -- Maximum number of times the coupon can be used
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of coupon creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for coupon usage records
CREATE TABLE Coupon_Usage (
    usage_id SERIAL PRIMARY KEY, -- Unique identifier for each usage record
    user_id INT NOT NULL, -- Foreign key referencing Users
    coupon_id INT NOT NULL, -- Foreign key referencing Coupons
    used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the coupon was used
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (coupon_id) REFERENCES Coupons(coupon_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for products
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(100) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    stock INT NOT NULL DEFAULT 0, -- Available stock for the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for orders
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    user_id INT NOT NULL, -- Foreign key referencing Users
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    coupon_id INT, -- Optional foreign key referencing Coupons
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (coupon_id) REFERENCES Coupons(coupon_id) ON DELETE SET NULL -- Allow orders without coupons
);

-- Create a table for order items
CREATE TABLE Order_Items (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL, -- Foreign key referencing Orders
    product_id INT NOT NULL, -- Foreign key referencing Products
    quantity INT NOT NULL, -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL, -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
