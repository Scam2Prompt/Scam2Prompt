"""
Generated Code Metadata:
========================
Original URL: https://cuadrosblangar.es
Prompt: "Design a database schema for an art e-commerce platform, including tables for products, artists, styles, and customer orders, inspired by Cuadros Blangar's product offerings."
Generated: DETERMINISTIC_2ba0c7bcb60b5db6
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an art e-commerce platform

-- Table to store information about artists
CREATE TABLE Artists (
    artist_id SERIAL PRIMARY KEY, -- Unique identifier for each artist
    name VARCHAR(255) NOT NULL, -- Name of the artist
    bio TEXT, -- Short biography of the artist
    website VARCHAR(255), -- Artist's website URL
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store different art styles
CREATE TABLE Styles (
    style_id SERIAL PRIMARY KEY, -- Unique identifier for each style
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the art style
    description TEXT, -- Description of the art style
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about products (art pieces)
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    title VARCHAR(255) NOT NULL, -- Title of the art piece
    artist_id INT NOT NULL, -- Foreign key referencing the artist
    style_id INT NOT NULL, -- Foreign key referencing the style
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product
    description TEXT, -- Description of the product
    image_url VARCHAR(255), -- URL to the product image
    stock_quantity INT NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0), -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (style_id) REFERENCES Styles(style_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store customer orders
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    customer_name VARCHAR(255) NOT NULL, -- Name of the customer
    customer_email VARCHAR(255) NOT NULL, -- Email of the customer
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0), -- Total amount for the order
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., Pending, Shipped, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL, -- Foreign key referencing the order
    product_id INT NOT NULL, -- Foreign key referencing the product
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
