"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microrentacar.biz
Prompt: Create a database schema for managing car rental services, including categories like luxury cars, wedding cars, and trip vehicles, based on the offerings of Micro Rent a Car.
Generated: DETERMINISTIC_f448ae1321f8c406
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing car rental services
-- This schema includes tables for cars, categories, rentals, and customers.

-- Create the database
CREATE DATABASE CarRentalService;

-- Use the created database
USE CarRentalService;

-- Table to store car categories (e.g., Luxury, Wedding, Trip)
CREATE TABLE CarCategories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,        -- Name of the category
    description TEXT                             -- Description of the category
);

-- Table to store car details
CREATE TABLE Cars (
    car_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each car
    make VARCHAR(50) NOT NULL,                  -- Manufacturer of the car
    model VARCHAR(50) NOT NULL,                 -- Model of the car
    year INT NOT NULL,                           -- Year of manufacture
    category_id INT,                            -- Foreign key referencing CarCategories
    price_per_day DECIMAL(10, 2) NOT NULL,     -- Rental price per day
    availability BOOLEAN DEFAULT TRUE,           -- Availability status of the car
    FOREIGN KEY (category_id) REFERENCES CarCategories(category_id) -- Foreign key constraint
);

-- Table to store customer information
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,             -- Customer's first name
    last_name VARCHAR(50) NOT NULL,              -- Customer's last name
    email VARCHAR(100) NOT NULL UNIQUE,          -- Customer's email address (unique)
    phone_number VARCHAR(15),                     -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when customer was registered
);

-- Table to manage car rentals
CREATE TABLE Rentals (
    rental_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each rental
    car_id INT NOT NULL,                          -- Foreign key referencing Cars
    customer_id INT NOT NULL,                     -- Foreign key referencing Customers
    rental_start DATE NOT NULL,                   -- Start date of the rental
    rental_end DATE NOT NULL,                     -- End date of the rental
    total_amount DECIMAL(10, 2) NOT NULL,        -- Total amount for the rental
    FOREIGN KEY (car_id) REFERENCES Cars(car_id), -- Foreign key constraint
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) -- Foreign key constraint
);

-- Index for optimizing queries on rentals
CREATE INDEX idx_rental_dates ON Rentals (rental_start, rental_end);

-- Sample data insertion for CarCategories
INSERT INTO CarCategories (category_name, description) VALUES
('Luxury', 'High-end luxury cars for special occasions.'),
('Wedding', 'Special cars for wedding rentals.'),
('Trip', 'Vehicles suitable for long trips and vacations.');

-- Sample data insertion for Cars
INSERT INTO Cars (make, model, year, category_id, price_per_day) VALUES
('Mercedes-Benz', 'S-Class', 2022, 1, 250.00),
('BMW', '7 Series', 2021, 1, 240.00),
('Toyota', 'Camry', 2020, 3, 50.00),
('Ford', 'Explorer', 2019, 3, 75.00);

-- Sample data insertion for Customers
INSERT INTO Customers (first_name, last_name, email, phone_number) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321');

-- Sample data insertion for Rentals
INSERT INTO Rentals (car_id, customer_id, rental_start, rental_end, total_amount) VALUES
(1, 1, '2023-10-01', '2023-10-05', 1000.00),
(3, 2, '2023-10-10', '2023-10-15', 250.00);
```
