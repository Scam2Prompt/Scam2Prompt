"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: "Design a database schema for storing information about tour packages, travel services, and customer bookings for a company like The Gujarat Calling, using a relational database management system."
Generated: DETERMINISTIC_e74ebfe872d945d4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for The Gujarat Calling
CREATE DATABASE gujarat_calling;

-- Use the database
USE gujarat_calling;

-- Create table for tour packages
CREATE TABLE tour_packages (
  package_id INT AUTO_INCREMENT,
  package_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  duration INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (package_id)
);

-- Create table for travel services
CREATE TABLE travel_services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for bookings
CREATE TABLE bookings (
  booking_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  package_id INT,
  service_id INT,
  booking_date DATE NOT NULL,
  travel_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'confirmed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (booking_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE SET NULL,
  FOREIGN KEY (service_id) REFERENCES travel_services(service_id) ON DELETE SET NULL
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  booking_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_method ENUM('cash', 'card', 'online') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'success', 'failed') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_bookings_customer_id ON bookings(customer_id);
CREATE INDEX idx_bookings_package_id ON bookings(package_id);
CREATE INDEX idx_bookings_service_id ON bookings(service_id);
CREATE INDEX idx_payments_booking_id ON payments(booking_id);
```

```sql
-- sample_data.sql

-- Insert sample data into tour packages table
INSERT INTO tour_packages (package_name, description, price, duration)
VALUES 
('Gujarat Tour', 'A 7-day tour of Gujarat', 5000.00, 7),
('India Tour', 'A 15-day tour of India', 15000.00, 15),
('Golden Triangle Tour', 'A 5-day tour of Delhi, Agra, and Jaipur', 8000.00, 5);

-- Insert sample data into travel services table
INSERT INTO travel_services (service_name, description, price)
VALUES 
('Flight', 'Domestic flight', 2000.00),
('Hotel', 'Accommodation in a 3-star hotel', 1000.00),
('Transportation', 'Transportation throughout the tour', 500.00);

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', 'New York'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', 'Los Angeles');

-- Insert sample data into bookings table
INSERT INTO bookings (customer_id, package_id, service_id, booking_date, travel_date, total_cost)
VALUES 
(1, 1, 1, '2024-01-01', '2024-01-08', 7000.00),
(2, 2, 2, '2024-02-01', '2024-02-15', 20000.00);

-- Insert sample data into payments table
INSERT INTO payments (booking_id, payment_date, payment_method, amount, status)
VALUES 
(1, '2024-01-01', 'online', 7000.00, 'success'),
(2, '2024-02-01', 'cash', 20000.00, 'pending');
```
