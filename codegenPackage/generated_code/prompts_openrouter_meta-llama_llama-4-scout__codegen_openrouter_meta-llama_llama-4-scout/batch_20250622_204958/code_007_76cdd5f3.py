"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Design a database schema for storing information about Tanzania's national parks, safari packages, and customer bookings.
Generated: DETERMINISTIC_76cdd5f3906582ee
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Tanzania's national parks and safari packages
CREATE DATABASE tanzania_national_parks;

-- Use the database
USE tanzania_national_parks;

-- Create table for national parks
CREATE TABLE national_parks (
    park_id INT AUTO_INCREMENT,
    park_name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (park_id)
);

-- Create table for safari packages
CREATE TABLE safari_packages (
    package_id INT AUTO_INCREMENT,
    package_name VARCHAR(255) NOT NULL,
    park_id INT,
    package_description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    duration INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (package_id),
    FOREIGN KEY (park_id) REFERENCES national_parks(park_id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (customer_id)
);

-- Create table for bookings
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT,
    customer_id INT,
    package_id INT,
    booking_date DATE NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (booking_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES safari_packages(package_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    booking_id INT,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Insert sample data into national parks table
INSERT INTO national_parks (park_name, location, description)
VALUES 
('Serengeti National Park', 'Arusha Region', 'The Serengeti is one of the most famous wildlife reserves in Africa'),
('Ngorongoro Conservation Area', 'Arusha Region', 'The Ngorongoro Conservation Area is a UNESCO World Heritage Site'),
('Tarangire National Park', 'Dodoma Region', 'Tarangire National Park is known for its large elephant population');

-- Insert sample data into safari packages table
INSERT INTO safari_packages (package_name, park_id, package_description, price, duration)
VALUES 
('Serengeti Safari', 1, 'A 3-day safari adventure in the Serengeti', 1500.00, 3),
('Ngorongoro Crater Tour', 2, 'A 2-day tour of the Ngorongoro Crater', 800.00, 2),
('Tarangire Elephant Expedition', 3, 'A 4-day expedition to see elephants in Tarangire', 2000.00, 4);

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '+255 712 345 678'),
('Jane', 'Doe', 'jane.doe@example.com', '+255 765 432 109');

-- Insert sample data into bookings table
INSERT INTO bookings (customer_id, package_id, booking_date, start_date, end_date, total_cost)
VALUES 
(1, 1, '2024-09-01', '2024-09-05', '2024-09-08', 1500.00),
(2, 2, '2024-09-15', '2024-09-17', '2024-09-19', 800.00);

-- Insert sample data into payments table
INSERT INTO payments (booking_id, payment_date, payment_amount, payment_method)
VALUES 
(1, '2024-09-01', 1500.00, 'Credit Card'),
(2, '2024-09-15', 800.00, 'Bank Transfer');
```
