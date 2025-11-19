"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: Design a database schema in SQL to store information about tour packages, taxi services, and customer bookings based on the offerings listed on the "Best Holidays All India" website.
Generated: DETERMINISTIC_2908caa1111a71ab
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Best Holidays All India
CREATE DATABASE best_holidays_all_india;

-- Use the database
USE best_holidays_all_india;

-- Create table for tour packages
CREATE TABLE tour_packages (
    package_id INT AUTO_INCREMENT,
    package_name VARCHAR(255) NOT NULL,
    package_description TEXT,
    package_duration INT,
    package_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (package_id)
);

-- Create table for taxi services
CREATE TABLE taxi_services (
    service_id INT AUTO_INCREMENT,
    service_name VARCHAR(255) NOT NULL,
    service_description TEXT,
    service_vehicle_type VARCHAR(50),
    service_rate DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (service_id)
);

-- Create table for customers
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (customer_id)
);

-- Create table for bookings
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT,
    customer_id INT,
    package_id INT,
    service_id INT,
    booking_date DATE,
    pickup_location VARCHAR(100),
    drop_location VARCHAR(100),
    booking_status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (booking_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id),
    FOREIGN KEY (service_id) REFERENCES taxi_services(service_id)
);

-- Create table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    booking_id INT,
    payment_method VARCHAR(50),
    payment_date DATE,
    payment_amount DECIMAL(10, 2),
    payment_status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- Create indexes for faster queries
CREATE INDEX idx_bookings_customer_id ON bookings(customer_id);
CREATE INDEX idx_bookings_package_id ON bookings(package_id);
CREATE INDEX idx_bookings_service_id ON bookings(service_id);
CREATE INDEX idx_payments_booking_id ON payments(booking_id);

-- Insert sample data
INSERT INTO tour_packages (package_name, package_description, package_duration, package_price)
VALUES 
('Golden Triangle', 'Visit Delhi, Agra, and Jaipur', 7, 25000.00),
('Kerala Backwaters', 'Explore the backwaters of Kerala', 5, 18000.00);

INSERT INTO taxi_services (service_name, service_description, service_vehicle_type, service_rate)
VALUES 
('Sedan', 'Toyota Innova or similar', 'Sedan', 1500.00),
('SUV', 'Toyota Innova Crysta or similar', 'SUV', 2500.00);

INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', 'New York'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', 'Los Angeles');

INSERT INTO bookings (customer_id, package_id, service_id, booking_date, pickup_location, drop_location)
VALUES 
(1, 1, 1, '2024-09-16', 'New Delhi', 'Agra'),
(2, 2, 2, '2024-09-20', 'Kochi', 'Alleppey');

INSERT INTO payments (booking_id, payment_method, payment_date, payment_amount)
VALUES 
(1, 'Credit Card', '2024-09-16', 25000.00),
(2, 'Bank Transfer', '2024-09-20', 18000.00);
```
