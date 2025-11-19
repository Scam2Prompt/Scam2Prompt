"""
Generated Code Metadata:
========================
Original URL: https://www.lecarolee.it
Prompt: Create a sample database schema for an agriturismo management system, including tables for products, accommodations, and customer information, inspired by the Le Carolee website.
Generated: DETERMINISTIC_738c19faf4e396d2
Batch ID: 20250622_204907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Agriturismo Management System Database Schema

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Accommodations;
DROP TABLE IF EXISTS Customers;

-- Table for storing product information
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(100) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0, -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing accommodation information
CREATE TABLE Accommodations (
    accommodation_id SERIAL PRIMARY KEY, -- Unique identifier for each accommodation
    name VARCHAR(100) NOT NULL, -- Name of the accommodation
    description TEXT, -- Description of the accommodation
    price_per_night DECIMAL(10, 2) NOT NULL, -- Price per night for the accommodation
    max_guests INT NOT NULL, -- Maximum number of guests allowed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of accommodation creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing customer information
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL, -- Customer's first name
    last_name VARCHAR(50) NOT NULL, -- Customer's last name
    email VARCHAR(100) NOT NULL UNIQUE, -- Customer's email address (must be unique)
    phone VARCHAR(15), -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of customer creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing bookings, linking customers to accommodations
CREATE TABLE Bookings (
    booking_id SERIAL PRIMARY KEY, -- Unique identifier for each booking
    customer_id INT NOT NULL, -- Foreign key referencing Customers
    accommodation_id INT NOT NULL, -- Foreign key referencing Accommodations
    check_in_date DATE NOT NULL, -- Check-in date for the booking
    check_out_date DATE NOT NULL, -- Check-out date for the booking
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of booking creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (accommodation_id) REFERENCES Accommodations(accommodation_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for storing product orders, linking customers to products
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    customer_id INT NOT NULL, -- Foreign key referencing Customers
    product_id INT NOT NULL, -- Foreign key referencing Products
    quantity INT NOT NULL, -- Quantity of the product ordered
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(name);
CREATE INDEX idx_accommodation_name ON Accommodations(name);
CREATE INDEX idx_customer_email ON Customers(email);
```
